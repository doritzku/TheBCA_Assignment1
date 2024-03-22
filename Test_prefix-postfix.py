# testing postfix and prefix
from prefix_postfix import find_precedence, postfix, prefix


class TestPrefixPostfix:
    def test_find_precedence(self):
        assert find_precedence("+") == 1
        assert find_precedence("-") == 1
        assert find_precedence("*") == 2
        assert find_precedence("/") == 2
        assert find_precedence("^") == 3

    def test_postfix(self):
        assert postfix("A+B*C") == "ABC*+"
        assert postfix("A+B*C-D") == "ABC*+D-"
        assert postfix("A+B*C-D/E") == "ABC*+DE/-"
        assert postfix("A^B^C") == "AB^C^"
        assert postfix("A+B^C") == "ABC^+"
        assert postfix("A^B+C") == "AB^C+"

    def test_prefix(self):
        assert prefix("A+B*C") == "+A*BC"
        assert prefix("A+B*C-D") == "-+A*BCD"
        assert prefix("A+B*C-D/E") == "-+A*BC/DE"
        assert prefix("A^B^C") == "^^ABC"
        assert prefix("A+B^C") == "+A^BC"
        assert prefix("A^B+C") == "+^ABC"


def main():
    test = TestPrefixPostfix()
    test.test_find_precedence()
    test.test_postfix()
    test.test_prefix()