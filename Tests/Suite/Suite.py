import unittest
import HtmlTestRunner


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

suite = unittest.TestSuite()
suite.addTests(
    [Test_1(), Test_2(), Test_3(), Test_4(), Test_5(), Test_6(), Test_7(), Test_8(), Test_9(), Test_10(), Test_11(),
     Test_12(), Test_13(), Test_14(), Test_15()])

unittest.TextTestRunner().run(suite)
