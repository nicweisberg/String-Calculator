# Nick Weisberg
# 7shifts programming question
# January 27 2020


def Add(numbers):
    """
    Add:    adds up all the numbers in a string
    param:  String numbers - a string of delimitted numbers
            Assumes: start of string formatted as: "//DELIMITER\n" 
    return: int value equal to sum of numbers in input string 
    """
    # get index of first new line char to tell where end of delimitter ends
    newLine_index = numbers.index("\n")
    # delimitted is equal to the string after "//" and before the new line char
    delim = numbers[2:newLine_index]
    # the remaining section of the string is our numbers to be summed 
    numbers = numbers[newLine_index:]
    # check if multiple delimiters
    if "," in delim and len(delim) > 1:
        delimiters = delim.split(",")
        # replace all instances of unique delimiters with a comma
        for delimiter in delimiters:
            numbers = numbers.replace(delimiter, ",")
        # set the delimiter to a comma
        delim = ","
    # case of empty string
    if numbers == "\n": return 0
    # converting our remaining numbers to an array
    number_array = numbers.split(delim)
    # removing any new line chars and converting numbers of array to integers 
    number_array = [int(number.strip()) for number in number_array if int(number) <= 1000]
    # raising a value error if any number in array is negative
    for number in number_array:
        if number < 0:
            raise ValueError("Negatives not allowed: {}".format(number))
    # returning sum of array elements
    return sum(number_array)
    
    
    

##################################################################################
# TEST CASES FOR FUNCTION ADD

tests = {

# simple
"//,\n1,3,4" : 8,
"//,\n17,56,33,1" : 107,
"//,\n10,21,2,45,19,34,67" : 198,

# edges
"//,\n0,3,4" : 7,
"//,\n1000,3,4" : 1007,
"//,\n0" : 0,
"//,\n0,0,0,0,0,0" : 0,
"//,\n1000,0,1000,0,7, 1000" : 3007,

# special cases
"//,\n" : 0,
"//,\n1001" : 0,
"//,\n3,1001,21" : 24,
"//,\n29765, 2349, 4459, 2394" : 0,

# delimiters
"//;\n1;3;4" : 8,
"//$\n1$2$3" : 6,
"//@\n2@3@8" : 13,
"//***\n1***2***3" : 6,
"//$,@\n1$2@3" : 6

}

for test in tests:
    assert Add(test) == tests[test], "Test case: {} Result: {} Answer: {}".format(test,Add(test),tests[test])
