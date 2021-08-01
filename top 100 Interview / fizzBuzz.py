def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # time complexity o(n) space o(n)
        xda=[]
        for x in range(1,n+1):
            if x %3 ==0 and x%5==0:
                xda.append("FizzBuzz")
            elif x%3 == 0:
                xda.append('Fizz')
            elif x%5==0:
                xda.append("Buzz")
            else:
                xda.append(str(x))
        return xda


            
