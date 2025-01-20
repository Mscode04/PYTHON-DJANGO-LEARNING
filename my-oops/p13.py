import time

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  
        result = func(*args, **kwargs)  
        end_time = time.time() 
        print(f"Execution time of {func.__name__}: {end_time - start_time:.4f} seconds")
        return result
    return wrapper


class MyClass:
    @log_execution_time 
    def slow_method(self):
        time.sleep(2)  
        return "Method Finished"



obj = MyClass()
print(obj.slow_method())  

