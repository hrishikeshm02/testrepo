from timeit import timeit

# string
def strings():
    x = 'python'
    y = x.replace('n','z')
    z = x + 'programming'
    t = y + 'programming'
    print(f"x= {x}\ny= {y}\nz= {z}\nt= {t}")

# ====================================================================
# list comprehension
# in easy way
def list_comprehension():
    my_list = [[1,2],[3,4]]

    # for i in my_list:
    #     for j in i:
    #         print(j, end=" ")

    another_list = [j for i in my_list for j in i]
    print(another_list)

# ====================================================================
# ZIP Function
def ZIP_Function():
    names = ["Swamini","Aasavari","Hrishikesh"]
    ages = [34,21,26]
    gender = ["female","female","male"]

    all_details = list(zip(names,ages,gender))
    print(all_details)

    for n,a,g in all_details:
        print(f'name: {n}, age: {a}, gender: {g}')

# ====================================================================
# To optimization code and catch execution time
def optimization():
    def implemtation1():
        return [i for i in range(0,5)]
    
    def implemtation2():
        return [0, 1, 2, 3, 4]
    
    timer1: float = timeit(stmt=implemtation1)
    timer2: float = timeit(stmt=implemtation2)

    print(round(timer1, 6))
    print(round(timer2, 6))

# ====================================================================
# unpacking
def unpacking():
    user_inputs = [
        "Hrishikesh",
        26,
        "India",
        "402303",
        9767874165,
        "Male"
    ]
    name, age, * details, gender = user_inputs
    print(name, age, gender)
    print(details)

if __name__=="__main__":
    # strings()
    # list_comprehension()
    # ZIP_Function()
    optimization()
    # unpacking()
