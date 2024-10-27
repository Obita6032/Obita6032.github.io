

# def add_numbers():
#     try:
#         a=float(input("Enter first number"));
#         b=float(input("enter second number"));
#         return a+b;
#     except TypeError:
#         return "only numbers are allowed";
# result=add_numbers();
# print(result);

# result=add_numbers(2,"t");
# print(result)

# list =[1,2,3,4,5,6,7,8,9]
# print(list)
# for numbers in list:
   
#     print(numbers)    

# def add_list(list):
#     sum=0;
#     for numbers in list:
#         sum += numbers;
#     print(sum)  
# add_list(list)  

numbers=[1,2,3,4,5,6,7,8,9]
print(numbers);

for num in numbers:
    print(num);

def add(numbers):
    total=0;
    for num in numbers:
        total +=num;
        print(total);
add(numbers)                   