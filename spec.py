"""
    >>> print untokenize(translate(StringIO('describe Foo').readline))
    import unittest 
    class FooSpec (unittest .TestCase )

    >>> print untokenize(translate(StringIO('''describe Foo:
    ...     pass''').readline))
    import unittest 
    class FooSpec (unittest .TestCase ):
        pass 

    >>> print untokenize(translate(StringIO('''describe Foo:
    ...     it "should do x":
    ...         pass''').readline))
    import unittest 
    class FooSpec (unittest .TestCase ):
        def should_do_x(self ):
            pass 

    >>> print untokenize(translate(StringIO('''describe Foo:
    ...     def before_each:
    ...         self._bar = 'bar'
    ...
    ...     it "should have _bar":
    ...         assert self._bar == 'bar'
    ... ''').readline))
    import unittest 
    class FooSpec (unittest .TestCase ):
        def setUp (self ):
            self ._bar ='bar'
    <BLANKLINE>
        def should_have__bar(self ):
            assert self ._bar =='bar'
    <BLANKLINE>

    >>> print untokenize(translate(StringIO('''describe Foo:
    ...     def after_each: pass''').readline))
    import unittest 
    class FooSpec (unittest .TestCase ):
        def tearDown (self ):pass 

Example of Usage:

    >>> testcase = untokenize(translate(StringIO('''describe Foo:
    ...     it "should 1 be equal to 2":
    ...         assert 1 == 2''').readline))

    >>> tempdir = tempfile.mkdtemp()
    >>> temp_module = os.path.join(tempdir, 'testcase.py')
    >>> testcase_file = open(temp_module, 'w')
    >>> testcase_file.write(testcase)
    >>> testcase_file.close()

    >>> sys.path.append(tempdir)
    >>> from testcase import FooSpec
    >>> suite.addTest(unittest.makeSuite(FooSpec, prefix='should'))
    >>> runner.run(suite)
    <unittest._TextTestResult run=1 errors=0 failures=1>
    >>> os.remove(temp_module)
"""

import unittest
from tokenize import untokenize
from tokenizer import translate
from cStringIO import StringIO
import doctest
import sys
import os
import tempfile

suite = unittest.TestSuite()
runner = unittest.TextTestRunner(stream=StringIO())

if __name__ == '__main__':
    doctest.testmod(optionflags=doctest.ELLIPSIS)
