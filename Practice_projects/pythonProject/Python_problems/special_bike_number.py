"""
Question:- Write a program to get a 4-digit bike number where number ranging from 0001 to 9999 with following condition.
     Condition 1 :- The number must be in increasing order. (Ex. 1239)
     Condition 2 :- The last digit must be 9.
     Condition 3 :- When we add the 4-digit number, it sum must be 8. (Ex. 0269 = 0+2+6+9 = 17 => 1+7 => 8)
     Condition 4 :- Repeatation not allowed, only 3rd-digit and 4th-digit can repeat.
     Condition 5 :- Output must be stored in list.
"""

special = """
                 ===========    =============    ||       ++      ++========== 
                    ||     ||         ||         ||     ++        ++
                    ||     ||         ||         ||   ++          ++ 
                    ||=====           ||         || ++            ++
                    ||     ||         ||         ||++             ++========
                    ||     ||         ||         ||  ++           ++
                    ||     ||         ||         ||    ++         ++
                  ==========    ==============   ||      ++       ++=========== 

"""
print(special)

# Empty list to store bike number
bike_number = []

# First for loop to iterate from 0 to 9
for i in range(0, 10):

    # Second for loop to iterate from 0 to 9
    for j in range(0, 10):

        # To move further i must be less than j
        if i < j:

            # Third loop to iterate from 1 to 9
            for k in range(0, 10):

                # To move further j must be small than k
                if j < k:

                    # Fourth loop to iterate only 9 because of question condition
                    for n in range(9, 10):

                        # Summing i, j, k and n
                        sum = i + j + k + n

                        # After sum value is not equal 8, then move forward
                        if sum != 8:

                            # Because sum is in 2-digit integer , to further add it we will convert it to string
                            make = str(sum)

                            # After conversion, we will fetch using index and covert to int and sum it
                            sum1 = int(make[0]) + int(make[1])

                            # After summing if it is equal to 8, then move forward else discard it.
                            if sum1 == 8:

                                # To store number convert i,j,k,n to string respectively
                                bike = str(i) + str(j) + str(k) + str(n)

                                # After conversion, append in list
                                bike_number.append(bike)

                        # In case it is equal to 8, then append to list
                        else:
                            d = str(i) + str(j) + str(k) + str(n)
                            bike_number.append(d)


print(bike_number)





