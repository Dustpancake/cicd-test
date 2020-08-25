import sys
import calc

res = calc.addn(*sys.argv[1:])
print(f"Your sum is:\n{res}")
