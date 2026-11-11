class Solution:
    def isHappy(self, n: int) -> bool:
        numbers = set()
        while(True):
            n = self.get_new(n)
            if n ==1:
                return True
            elif n in numbers:
                return False
            else :
                numbers.add(n)


    def get_digits(self,n:int)->list[int]:
        res=[]
        while(n!=0):
            a= n%10
            res.append(a)
            n=int((n-a)/10)
        return res
    def get_new(self,n:int)->int:
        a=0
        l = self.get_digits(n)
        for i in l:
            a+=i*i
        return a


s= Solution()
print(s.isHappy(123))
