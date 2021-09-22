class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for i in range(len(nums)):
            self.result += nums[i]
        return self
    def subtract(self, num, *nums):
        self.result -= num
        for i in range(len(nums)):
            self.result -= nums[i]
        return self
# your code here
# create an instance:
md = MathDojo()
ex2= MathDojo()
ex3= MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5
x = ex2.add(1).add(3,4,2).subtract(1,2).result
print(x)
x = ex3.add(2).add(7,7,4).subtract(3,2).result
print(x)
# run each of the methods a few more times and check the result!
