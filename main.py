#Problem 2, p. 16
def problem_2(r):
    #Calculate the volume of a sphere with the radius r=3.14159 as the parameter.
    #Return the volume as a float

    pi = float(3.14159)
    volume = (4/3) * pi * (r**3)
    return volume

if __name__ == '__main__':
    #Problem 2
    print(problem_2(2))
