import copy
import json
from pathlib import Path
import tempfile
import unittest
from pipeline import load_corpus,contexts_for,validate_selection,assemble,parse_object,run,HEADERS,FIELDS

class MatrixTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.path=Path(__file__).resolve().parent/'data/literature_10.json'
        cls.records=load_corpus(cls.path)

    def selection(self,record):
        contexts=contexts_for(self.records,record['id'])
        return {'paper_id':record['id'],'selected_evidence':{f:contexts[f][0]['evidence_id'] for f in FIELDS},
                'gap_proyek':'Interpretasi untuk diuji.'},contexts

    def test_exact_schema_and_source_mapping(self):
        self.assertEqual(len(self.records),10)
        for r in self.records:
            obj,ctx=self.selection(r)
            validate_selection(obj,r['id'],ctx)
            row=assemble(r,obj['selected_evidence'],ctx)
            self.assertEqual(list(row),HEADERS)
            for field in FIELDS:self.assertEqual(row[field],ctx[field][0]['text'])

    def test_reject_cross_field_and_cross_article_evidence(self):
        obj,ctx=self.selection(self.records[0])
        for invalid in [ctx['Keterbatasan'][0]['evidence_id'],'R2:method','invented']:
            bad=copy.deepcopy(obj);bad['selected_evidence']['Metode']=invalid
            with self.assertRaises(ValueError):validate_selection(bad,'R1',ctx)

    def test_reject_missing_field_and_nonstring_gap(self):
        obj,ctx=self.selection(self.records[0])
        bad=copy.deepcopy(obj);del bad['selected_evidence']['Dataset']
        with self.assertRaises(ValueError):validate_selection(bad,'R1',ctx)
        bad=copy.deepcopy(obj);bad['gap_proyek']=[]
        with self.assertRaises(ValueError):validate_selection(bad,'R1',ctx)

    def test_reject_invented_corpus_count(self):
        with tempfile.TemporaryDirectory() as folder:
            f=Path(folder)/'corpus.json';f.write_text(json.dumps(self.records[:8]),encoding='utf-8')
            with self.assertRaises(ValueError):load_corpus(f)

    def test_demo_not_marked_as_generation(self):
        with tempfile.TemporaryDirectory() as folder:
            rows,manifest=run(self.path,folder)
            self.assertEqual(len(rows),10)
            self.assertFalse(manifest['llm_called'])
            self.assertEqual(manifest['rows_failed'],0)

    def test_bad_model_is_not_replaced_by_editorial_rows(self):
        with tempfile.TemporaryDirectory() as folder:
            rows,manifest=run(self.path,folder,generate=lambda system,prompt:'{"paper_id":"fake"}')
            self.assertEqual(manifest['rows_failed'],10)
            self.assertEqual(manifest['model_calls'],30)
            self.assertTrue(all(r['Metode'].startswith('GAGAL') for r in rows))

    def test_mocked_selection_contract(self):
        def mock_model(system,prompt):
            request=json.loads(prompt)
            return json.dumps(request['schema_example'])
        with tempfile.TemporaryDirectory() as folder:
            rows,manifest=run(self.path,folder,generate=mock_model,model_info={'mock':True})
            self.assertEqual(len(rows),10)
            self.assertEqual(manifest['rows_failed'],0)
            self.assertTrue(manifest['model_info']['mock'])

    def test_fenced_json(self):
        self.assertEqual(parse_object('```json\n{"a":1}\n```'),{'a':1})
        with self.assertRaises(ValueError):parse_object('invalid')

if __name__=='__main__':unittest.main()
