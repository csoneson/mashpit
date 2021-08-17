#!/usr/bin/env python3

import unittest
import subprocess
from subprocess import PIPE
import sys


class MyTests(unittest.TestCase):
    def test_script(self):
        subprocess.run('mashpit sketch test', shell=True)
        f_expected = open('mashpit/test/test.sig', 'r')
        sig_expected = f_expected.read()
        f_expected.close()
        f_generated = open('test.sig', 'r')
        sig_generated = f_generated.read()
        f_generated.close()
        self.assertEqual(sig_expected, sig_generated)


    def test_script_failure(self):
        if sys.version_info.minor <= 6:
            result_no_args = subprocess.run(['mashpit','sketch'], stdout=PIPE, stderr=PIPE)
        else:
            result_no_args = subprocess.run(['mashpit','sketch'], capture_output=True)
        self.assertEqual(result_no_args.returncode, 2)


if __name__ == '__main__':
    unittest.main()