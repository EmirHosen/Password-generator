#passwd Generator with python
import random

lower_case = "abcdefghijklmnopqrsyz"
upper_case = "ABCDEFGHIJKLMNOPQRSYZ"
number = "0123456789"
sumbols = "@#$%*/?"

Use_for = lower_case + upper_case + number + sumbols
length_for_pass = 18

passwd = "".join(random.sample(Use_for, length_for_pass))

print("your Generated Password : ",passwd )