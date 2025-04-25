def recursive_function(number):
    if number==0:
        return 1  #base case
    else:
        return number *recursive_function(number-1)

print(recursive_function(5))