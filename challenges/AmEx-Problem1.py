
'''Save the town (100 Marks)
The town of Wonderland is under attack by an unknown virus. There are twenty six types of people who reside in the town of Wonderland i.e every person in the town belongs to any one of the types from a - z.


Many people have got infected by the virus and are fighting for their lives. Scientists have studied the virus and its impact on different types of people. After their study, they found that the virus is unable to cause damage to any of the people who belong to the type which are maximum in the town.


For example - If in the town, the maximum people belong to the type b, then all b types of people will be safe from the virus.


Scientists want to know the type for which the people are maximum so that they can safeguard them and also develop vaccination as an antidote to the virus which will provide immunity to other people. They are short of time and therefore need your help in determining the type for which the people are maximum in the town. 



Note: If there are more than one type of people with equal maximum then the type with lesser ASCII value will be considered.



Can you help the Scientists in saving the town ?



Input Format
The first line of input consists of number of test cases, T.

The second line of each test case consists of a string representing the type of each individual person in the town.



Constraints
1<= T <=10

1<= |string| <=100000




Output Format
For each test case, print the required output in a separate line.




Sample TestCase 1
Input
2
gqtrawq
heeellloooiiiipppppppppp
Output
q
p
Explanation
Test Case 1: There are 2 q types of people rest all are present alone.

Test Case 2: There are 2 y and 2 z types of people. Since the maximum value is same, the type with lesser Ascii value is considered as output. Therfore, y is the correct type.'''
 

def main():
    # read first line
    no_of_inputs = input()

    # create a mapper with letter as key and letter count as value
    def mapper(k):        
        try:
            tt[k] += 1
        except:
            tt[k] = 0
            tt[k] += 1
        return None

    # read subsequent lines
    for i in range(0,int(no_of_inputs)):
        town = input()
        
        tt = {}

        w = list(map(mapper, town.__iter__()))
        
        sorted_tt = sorted(tt.items(), key=lambda x: x[1], reverse=True)
        sorted_max = sorted_tt[0][1]
        groups = []
        for t in sorted_tt:
            if sorted_max == t[1]:
                groups.append(t[0])
        print(sorted(groups)[0])    


if __name__ == '__main__':
    main()