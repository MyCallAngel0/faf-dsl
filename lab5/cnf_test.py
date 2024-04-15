import unittest
import cnf, variants


class TestChomskyNormalForm(unittest.TestCase):
    def test_chomsky_for_variant1(self):
        grammar_to_cnf_test = cnf.Grammar(variants.Vn1, variants.Vt1, variants.P1).to_cnf()
        dict_to_verify = {'S': ['AC', 'EC', 'BC', 'AS', 'a', 'FB', 'FD'], 'A': ['GS', 'EC', 'b', 'AS', 'BC', 'a', 'FD'],
                          'B': ['b', 'GS'], 'C': ['BA'], 'D': ['HC', 'FG'], 'E': ['AS'], 'F': ['a'],
                          'G': ['b'], 'H': ['FG']}
        for key in grammar_to_cnf_test.keys():
            grammar_to_cnf_test[key] = set(grammar_to_cnf_test[key])
            dict_to_verify[key] = set(dict_to_verify[key])
        self.assertDictEqual(grammar_to_cnf_test, dict_to_verify)

    def test_chomsky_for_variant2(self):
        grammar_to_cnf_test = cnf.Grammar(variants.Vn2, variants.Vt2, variants.P2).to_cnf()
        dict_to_verify = {'S': ['CB', 'EA', 'b'], 'A': ['GB', 'CB', 'EB', 'AS', 'CD', 'ES', 'b', 'FB', 'EA'],
                          'B': ['b', 'ES'], 'D': ['BB'], 'C': ['a'], 'E': ['b'], 'F': ['EA'], 'G': ['FA']}
        for key in grammar_to_cnf_test.keys():
            grammar_to_cnf_test[key] = set(grammar_to_cnf_test[key])
            dict_to_verify[key] = set(dict_to_verify[key])
        self.assertDictEqual(grammar_to_cnf_test, dict_to_verify)

    def test_chomsky_for_variant3(self):
        grammar_to_cnf_test = cnf.Grammar(variants.Vn3, variants.Vt3, variants.P3).to_cnf()
        dict_to_verify = {'S': ['GB', 'DS', 'd', 'DB'], 'A': ['d', 'DS', 'GB'], 'B': ['CS', 'DS', 'GB', 'a', 'd'],
                          'C': ['a'], 'D': ['d'], 'E': ['CA'], 'F': ['ED'], 'G': ['FA']}
        for key in grammar_to_cnf_test.keys():
            grammar_to_cnf_test[key] = set(grammar_to_cnf_test[key])
            dict_to_verify[key] = set(dict_to_verify[key])
        self.assertDictEqual(grammar_to_cnf_test, dict_to_verify)

    def test_chomsky_for_variant13(self):
        grammar_to_cnf_test = cnf.Grammar(variants.Vn13, variants.Vt13, variants.P13).to_cnf()
        dict_to_verify = {'S': ['BD', 'DA', 'a', 'EB', 'GB'], 'A': ['BA', 'BD', 'a', 'b', 'EB', 'GB'], 'B': ['BA', 'b'],
                          'D': ['BA'], 'C': ['b'], 'E': ['CA'], 'F': ['CD'], 'G': ['FA']}
        for key in grammar_to_cnf_test.keys():
            grammar_to_cnf_test[key] = set(grammar_to_cnf_test[key])
            dict_to_verify[key] = set(dict_to_verify[key])
        self.assertDictEqual(grammar_to_cnf_test, dict_to_verify)

    def test_chomsky_for_variant19(self):
        grammar_to_cnf_test = cnf.Grammar(variants.Vn19, variants.Vt19, variants.P19).to_cnf()
        dict_to_verify = {'S': ['a', 'CA', 'DB'], 'A': ['a', 'GB', 'CA', 'd', 'DB'], 'B': ['a', 'GB', 'CA', 'd', 'DB'],
                          'C': ['b'], 'D': ['d'], 'E': ['a'], 'F': ['EA'], 'G': ['FD']}
        for key in grammar_to_cnf_test.keys():
            grammar_to_cnf_test[key] = set(grammar_to_cnf_test[key])
            dict_to_verify[key] = set(dict_to_verify[key])
        self.assertDictEqual(grammar_to_cnf_test, dict_to_verify)


if __name__ == "__main__":
    unittest.main()
