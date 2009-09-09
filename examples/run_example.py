import yeti.tokenizer
import unittest
import runner
from example import BowlingSpec, FooSpec

suite = unittest.TestSuite()
suite.addTest(runner.makeSuite(BowlingSpec, prefix='should'))
suite.addTest(runner.makeSuite(FooSpec, prefix='should'))
unittest.TextTestRunner().run(suite)
