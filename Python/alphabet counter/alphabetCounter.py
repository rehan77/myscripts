input_string = input("Please enter a string.\n")
string_length = len(input_string)

i = 0
while i < string_length:
    j = 0
    count = 0
    while j < string_length:
        if input_string[j] == input_string[i]:
            count = count + 1
        j = j+1
    print("The count of {} is {}".format(input_string[i],count))
    i = i+1
    