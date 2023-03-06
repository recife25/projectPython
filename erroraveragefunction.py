erroraveragefunction
test_average (test_average.TestAverageAndShowWork) ... FAIL
test_average_and_show_work (test_average.TestAverageAndShowWork) ... FAIL

======================================================================
FAIL: test_average (test_average.TestAverageAndShowWork)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/codio/workspace/.guides/secure/test_average.py", line 49, in test_average
    self.assertEqual(outputs[i], result, msg='testing average_and_show_work(' + str(inputs[i]) + ') prints the string:\n' + outputs[i] + '\nInstead saw the string:\n' + result)
AssertionError: '(2 + 2 + 2) / 3 = 6 / 3 = 2.0' != ''
- (2 + 2 + 2) / 3 = 6 / 3 = 2.0
+ 
 : testing average_and_show_work((2, 2, 2)) prints the string:
(2 + 2 + 2) / 3 = 6 / 3 = 2.0
Instead saw the string:


======================================================================
FAIL: test_average_and_show_work (test_average.TestAverageAndShowWork)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/codio/workspace/.guides/secure/test_average.py", line 52, in test_average_and_show_work
    assert(average_and_show_work(2, 2, 2) == None) # (2 + 2 + 2) / 3 = 6 / 3 = 2.0
AssertionError

----------------------------------------------------------------------
Ran 2 tests in 0.044s
