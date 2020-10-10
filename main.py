import calculator as calc

#Problem 1.2, p. 16 = Solved
def problem_1_2(r):
    #Calculate the volume of a sphere with the radius r=3.14159 as the parameter.
    #Return the volume as a float

    pi = float(3.14159)
    volume = (4/3) * pi * (r**3)
    return volume

#Problem 1.3, p. 18 = Solved
def problem_1_3(a, b, c, d, e):
    #The goal is to use sep and end to isolate the three first parameters with five spaces between them.
    sep = " "
    new_a = str(a)+sep*5
    new_b = str(b)+sep*5
    print(new_a,new_b,c,d,e)

#Problem 1.4, p. 20 = Solved (a and b)
def problem_1_4_a(s):
    #Accept parameter and return the first half of it, excluding the middle character if the length is odd
    length = len(s)

    if length%2 == 0: #The length is even
        new_string = s[0:length//2]
        return new_string

    else: #The length is odd
        new_string = s[0:length // 2]
        return new_string

def problem_1_4_b(s):
    #Accept parameter and reverse the order before returning a reversed string

    reversed_string = s[::-1]
    return reversed_string

#Problem 1.5, p. 21 = Solved
def problem_1_5():

    animals = ["bear", "ant", "cat", "dog"]
    print("This is the initial list: ",animals, "\n")
    #1 - Append "eagle"
    animals.append("eagle")
    print("This is the list after step 1: ", animals, "\n")
    #2 - Replace at 2 with "fox
    animals.insert(2, "fox")
    #3 - Remove entry at index 1
    animals.pop(1)
    print("This is the list after step 3: ",animals, "\n")
    #4 - Sort reverse alphabetically
    animals.sort(reverse=True)
    print("This is the list after step 4: ", animals, "\n")
    #5 - Replace "eagle" with "hawk"
    position = animals.index("eagle")
    animals.pop(position)
    animals.insert(position, "hawk")
    print("This is the list after step 5: ", animals, "\n")
    #6 - Add the string "hunter" to the last entry on the list
    last_entry = len(animals)-1
    new_string = animals[last_entry] + " hunter"
    animals.pop(last_entry)
    animals.insert(last_entry, new_string)
    print("This is the list after step 6: ", animals, "\n")

#Problem 1.7, p. 27 = Solved
def problem_1_7():
    #Find the largest paldindrome from the product of two 3-digit numbers
    #Lowest = 100, Highest = 999
    lowest_three_digit = 100
    largest_palindrome = int(0)
    x = []
    y = []

    while lowest_three_digit < 999: #Fills the arrays from 100-999
        x.append(lowest_three_digit)
        y.append(lowest_three_digit)
        lowest_three_digit += 1

    for i in x: #For every number in the list X, we multiply it by every value in y
        for t in y:
            product = i*t
            product_string = str(product) #Convert to string
            reversed_string = product_string[::-1] #Check if reversed string is the same as original
            if product_string == reversed_string and product > largest_palindrome:
                #If they're identical and the int number is larger than the previous recorded palindrome,
                #we update the variable
                largest_palindrome = product


    print(largest_palindrome)

#Problem 1.8, p. 28 = Solved
def problem_1_8(n):
    #Alterating harmonic series. Computer the first 500 000 terms using list comprehension
    #Formula: x = ((-1)**(n+1))/n

    #Import lesson learned for using list comprehension:
    #You must put the operation/formula for it to work. You can not predefine it somewhere else and then
    #inserr it into the bracket. square = x**2 ==> [square for i in range(10)] will not work.
    list_hs = [float((((-1)**(n+1))/n)) for n in range(1,n)]
    sum()
    print(sum(list_hs))

#Problem 2.1, p. 33 = Solved
def problem_2_1(list):
    #Return: min, max, average
    #Bonus: can you do it as a single line
    low = min(list)
    high = max(list)
    average = float((sum(list)/len(list)))
    dir()
    return (print(min(list), max(list), float(sum(list)/len(list)), sep=","))

#Problem 2.2, p. 35 = Solved
def problem_2_2():
    #This is to test out which data types are mutable and which are not
    #_o = original
    int_o = int(1)
    str_o = "Original text"
    list_o = ["Robert", "Kaja", "Iver"]
    tuple_o = (4.0, 3.0)
    set_o = {"Heidi", "Reidar", "Kurt-Leo", "Svein Ronny"}

    #_a = altered
    int_a = int_o
    str_a = str_o
    list_a = list_o
    tuple_a = tuple_o
    set_a = set_o

    #Here we alter them and then print to see which were affected
    int_a += 1
    print("Integer case:",int_o, int_a, "\n", sep=" | ")
    str_a += ", and then some"
    print("String case:", str_o, str_a, "\n", sep=" | ")
    list_a.append("Trond")
    print("List case:", list_o, list_a, "\n", sep=" | ")
    tuple_a += (1,2)
    print("Tuple case:", tuple_o, tuple_a, "\n", sep=" | ")
    set_a.add("Marlene")
    print("Set case:", set_o, set_a, "\n", sep=" | ")

    print("The following data types are mutable (we can change them): list, set \n"
          "The following data types are umutable: int, string, tuples")

#Problem 2.3, p.28 = Solved
def problem_2_3(x,y):
    #Call on a method in calculator.py, which imports the math library
    sum = calc.sum(x,y)
    product = calc.product(x,y)
    return print("The sum is {}, and the product is {}".format(sum, product))




if __name__ == '__main__':
    #Problem 1.2
    #print(problem_1_2(2))

    #Problem 1.3
    #problem_1_3(1,2,3,4,5)

    #Problem 1.4
    #print(problem_1_4_a("I am angry at everyone."), problem_4_b("Even"))

    #Problem 1.5
    #problem_1_5()

    #Problem 1.7
    #problem_1_7()

    #Problem 1.8
    #problem_1_8(500000)

    #Problem 2.1
    #list = [9, 4, 7, 2, 10, 11, 12, 19, 18, 15]
    #problem_2_1(list)

    #Problem 2.2
    #problem_2_2()

    #Problem 2.3
    #problem_2_3(5,10)