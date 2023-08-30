import unittest
from main.bkool.utils.AST import *
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_1(self):
        """Simple program: class main {} """
        input = '''class Shape {
                                float length,width;
                                float getArea() {}
                                Shape(float length, width){
                                    this.length := length;
                                    this.width := width;

                                }
                            }
                    '''
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 300))