def test_func(function_to_pass):
    function_to_pass(2)
    print("It worked")

def callee_function(x):
    print("whipee")
if __name__ == "__main__":
    test_func(callee_function)
    