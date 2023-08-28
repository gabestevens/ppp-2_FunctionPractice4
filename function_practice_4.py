def max_num(num_one, num_two, num_three):
    return print(max(num_one, num_two, num_three))#built in max finder

max_num(2 , 5 , 12)

def multi_list(*numbers):
    val = 1
    for number in numbers:
        val = val * number#goes through each number and multiplies them
        
    return print(val)
    

def rev_string(string):
    return print(string [:: -1]) #built i nstring flipper

def num_within(number, begin, end):
    return print(number in range(begin, end+1)) #built in range finder
\
triangle = [[1],[1,1]]
def pascal(n):
    #base case
    if n<1:
        print("not enough rows")
    elif n ==1:
        print(triangle[0])
    else:
        row_number = 2
        #makes the row in triangles
        while len(triangle) < n:
            row=[]
            row_prev = triangle[row_number - 1]
        #makes new row
            length = len(row_prev) +1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length -1:
                    row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1

        for row in triangle:
            print(row)

pascal(2)
pascal(5)