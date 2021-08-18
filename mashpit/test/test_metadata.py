#!/usr/bin/env python3

import unittest
import subprocess
from mashpit.create import create_connection
from subprocess import PIPE
import sys


class MyTests(unittest.TestCase):
    def test_script(self):
        subprocess.run('mashpit config tongzhouxu97@gmail.com', shell=True)
        subprocess.run('mashpit metadata test biosample_list --list mashpit/test/test_biosample_list.txt', shell=True)
        conn = create_connection('test.db')
        c = conn.cursor()
        c.execute(''' SELECT COUNT(*) from SRA ''')
        self.assertEqual(c.fetchone()[0], 3)
        c.execute(''' SELECT COUNT(*) from BIOSAMPLE ''')
        self.assertEqual(c.fetchone()[0], 3)

    def test_script_failure(self):
        result = subprocess.run(['mashpit', 'metadata', '--list', 'mashpit/test/test_biosample_list.txt'], capture_output=True)
        result_no_args = subprocess.run(['mashpit','metadata'], capture_output=True)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result_no_args.returncode, 2)


if __name__ == '__main__':
    unittest.main()