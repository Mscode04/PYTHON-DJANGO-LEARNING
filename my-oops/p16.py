class St():
    @staticmethod
    def is_even(x):
        if x % 2 ==0:
            print('Even')
        else:
            print('Odd')    
obj=St()
obj.is_even(2)                        