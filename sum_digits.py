number=int(input("Enter a number"))
sum= sum(int(no) for no in str(number)) #no is number
                                        #converting number into a string
print(sum)                                       #converting back to int and then adding