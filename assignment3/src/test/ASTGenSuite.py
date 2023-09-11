import unittest
from main.bkool.utils.AST import *
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_1(self):
        """Simple program: class main {} """
        input = """int main() {foo();}"""
        expect = str(Program([ClassDecl(Id("main"), [])]))
        self.assertTrue(TestAST.test(input, expect, 300))