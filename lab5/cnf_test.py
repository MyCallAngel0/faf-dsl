import unittest
import cnf, variants

class TestChomskyNormalForm(unittest.TestCase):

    def test_epsilon(self):
        grammar_epsilon_test = cnf.Grammar(variants.Vn1, variants.Vt1, variants.P1)
        self.assertEqual(grammar_epsilon_test.eliminate_epsilon(),
                         {'S': ['aB', 'AC', 'A'], 'A': ['a', 'ASC', 'BC', 'aD', 'AS', 'B'], 'B': ['b', 'bS'], 'C': ['BA'], 'D': ['abC', 'ab'], 'E': ['aB']})

    def test_unit(self):
        grammar_unit_test = cnf.Grammar(variants.Vn2, variants.Vt2, variants.P2)
        self.assertCountEqual(grammar_unit_test.eliminate_unit(),
                         {'S': ['aB', 'bA'], 'A': ['', 'AS', 'bAAB', 'bS', 'b', 'aD'], 'B': ['b', 'bS'], 'C': ['AB'], 'D': ['BB']})

if __name__ == "__main__":
    unittest.main()