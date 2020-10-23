

import HTMLTestRunner
import unittest

import fp as fp

from Tests.Test_1 import Test_1
from Tests.Test_10 import Test_10
from Tests.Test_11 import Test_11
from Tests.Test_12 import Test_12
from Tests.Test_13 import Test_13
from Tests.Test_14 import Test_14
from Tests.Test_15 import Test_15
from Tests.Test_2 import Test_2
from Tests.Test_3 import Test_3
from Tests.Test_4 import Test_4
from Tests.Test_5 import Test_5
from Tests.Test_6 import Test_6
from Tests.Test_7 import Test_7
from Tests.Test_8 import Test_8
from Tests.Test_9 import Test_9


suite1 = unittest.TestLoader().loadTestsFromTestCase(Test_1)
suite2 = unittest.TestLoader().loadTestsFromTestCase(Test_2)
suite3 = unittest.TestLoader().loadTestsFromTestCase(Test_3)
suite4 = unittest.TestLoader().loadTestsFromTestCase(Test_4)
suite5 = unittest.TestLoader().loadTestsFromTestCase(Test_5)
suite6 = unittest.TestLoader().loadTestsFromTestCase(Test_6)
suite7 = unittest.TestLoader().loadTestsFromTestCase(Test_7)
suite8 = unittest.TestLoader().loadTestsFromTestCase(Test_8)
suite9 = unittest.TestLoader().loadTestsFromTestCase(Test_9)
suite10 = unittest.TestLoader().loadTestsFromTestCase(Test_10)
suite11 = unittest.TestLoader().loadTestsFromTestCase(Test_11)
suite12 = unittest.TestLoader().loadTestsFromTestCase(Test_12)
suite13 = unittest.TestLoader().loadTestsFromTestCase(Test_13)
suite14 = unittest.TestLoader().loadTestsFromTestCase(Test_14)
suite15 = unittest.TestLoader().loadTestsFromTestCase(Test_15)


all_tests = unittest.TestSuite([suite1, suite2,suite3, suite4, suite5, suite6, suite7, suite8, suite9, suite10, suite11, suite12, suite13, suite14, suite15])

html_report_dir = './html_report'
unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output=html_report_dir,combine_reports=True))

