import random
from fractions import Fraction

def get_factors(n):
    result = []
    for i in range(2, n):
        if n % i == 0:
            result.append(n)
    return result

class Problem:
    def __init__(self, abs_range=200, allow_negatives=True, use_decimals=False, whole_numbers_only=False):
        self._allow_negatives = allow_negatives
        self._use_decimals = use_decimals
        self._whole_numbers_only = whole_numbers_only

        self.left = []
        self.right = []
        num = random.randint(-abs_range if self._allow_negatives else 0, abs_range)
        self._addboth(num)

    def complicate(self, iterations):
        for i in range(iterations):
            func = random.choice([self._complicate_add])
            func()
        self._divide_both(random.randint(1, 30))
        self.finalize()

    def finalize(self):
        variables = ["a", "x", "y", "b", "w", "z"]
        self.answer = random.choice(self.left)
        replace_index = self.left.index(self.answer)
        self.left[replace_index] = random.choice(variables)

    def _get_working_side(self, side):
        return self.left if side == "l" else self.right

    def _assign_working_side(self, side, to_assign):
        if side == "l": self.left = to_assign
        else: self.right = to_assign

    def _complicate_add(self):
        side = random.choice(["l", "r"])
        working_side = self._get_working_side(side)
        item = random.choice(working_side)
        working_side.remove(item)
        self._assign_working_side(side, working_side + self._splitnum(item))

    def _splitnum(self, num, split=None):
        sign = -1 if num < 0 else 1
        num = abs(num)
        if split==None:
            split = random.randint(0, num)
        return sorted([(num-split) * sign, split * sign])
                
    def _addboth(self, num):
        self.left.append(num)
        self.right.append(num)
        
    def _divide(self, numerator, to_divide):
        if numerator % to_divide == 0:
            return int(numerator/to_divide)
        return Fraction(numerator, to_divide)

    def _divide_side(self, side, to_divide):
        working_side = self._get_working_side(side)
        for i in range(len(working_side)):
            working_side[i] = self._divide(working_side[i], to_divide)            
        self._assign_working_side(side, working_side)

    def _divide_both(self, num):
        self._divide_side("l", num)
        self._divide_side("r", num)
    
    def _render(self, l):
        result = ""
        for i in range(len(l)):
            if type(l[i]) == Fraction:
                to_append =("+" if l[i] >= 0 and i!=0  else "-") + "(" + str(abs(l[i])) + ")"
                if l[i] != 0:
                    result += to_append
            if type(l[i]) == int:
                to_append =("+" if l[i] >= 0 and i!=0  else "") + str(l[i])
                if l[i] != 0:
                    result += to_append
            else:
                to_append =("+" if i != 0 else "") + str(l[i])
                if l[i] != 0:
                    result += to_append
        return result

    def __str__(self):
        return self._render(self.left) + " = " + self._render(self.right) + "\t\t\t" + ("ans={}".format(self.answer))

for i in range(10):
    c = Problem()
    c.complicate(5)
    print(str(c))
