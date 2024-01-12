import calc_add
import calc.calc_sub as calc_sub
from calc.calc_sub import sub
from calc.calc import Calculator
import os
import sys

print(sys.path)
print(os.path.abspath(os.path.dirname(__file__)))

# if __name__ == '__main__':
#     print(calc_add.add(1,2))
#     print(calc_sub.sub(1,2))
#     print(sub(1,2))
#     c = Calculator()
#     print(c.add())
#     print(c.sub())
