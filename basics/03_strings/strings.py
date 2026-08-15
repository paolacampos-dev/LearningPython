## 💻 Exercises - 

# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
first = 'Thirty'
second = 'Days'
third=  'Of'
four = 'Python'
space = ' '
string = first + " " + second +space + third + " " + four
print("1.", string) # 1. Thirty Days Of Python

#2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
#3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
#4. Print the variable company using _print()_.
print(company)
#5. Print the length of the company string using _len()_ method and _print()_.
print(len(company))
#6. Change all the characters to uppercase letters using _upper()_ method.
print(company.upper())
print("7.", company.lower())
#7. Change all the characters to lowercase letters using _lower()_ method.

# 8. Use capitalize(), title(), and swapcase()
print(company.capitalize())
print(company.title())
print(company.swapcase())

#9. Cut(slice) out the first word of _Coding For All_ string.
print(company[7:])

#10. Check if _Coding For All_ string contains a word Coding using the method index, find or other methods.
print(company.find('Coding')) # 0 (Returns the index where the word starts at position 0)
company.find("Coding") != -1 # True (if Python cannot find the word, .find() returns -1.)

#11. Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))
#12. Change "Python for Everyone" to "Python for All" using the replace method or other methods. 

#13. Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(" "))

#14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
print(string.split(", "))

#15. What is the character at index 0 in the string _Coding For All_.
firstLetter = company[0]
print(firstLetter)
print(company[0])

#16. What is the last index of the string _Coding For All_.
last_index = len(company) - 1
last_letter = company[last_index]
print(last_index)
print(len(company) - 1)

#17. What character is at index 10 in "Coding For All" string.
index10 = company[10]
print(index10)
print (company[10])

#18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
sentence = "Python For Everyone"
print(sentence[0] + sentence[7] + sentence[11])

#19. Create an acronym or an abbreviation for the name 'Coding For All'.

#20. Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))
#21. Use index to determine the position of the first occurrence of F in Coding For All.
#22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind('l'))
#23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
#24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

#25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence[31:54])

#26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(company.index('because'))

#28. Does 'Coding For All' start with a substring _Coding_?
print(company.startswith('Coding'))
print(company.index('Coding') == 0)

#29. Does 'Coding For All' end with a substring _coding_?
print(company.endwith('coding'))

#30. '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;, remove the left and right trailing spaces in the given string.
print(company.strip()) # .lstrip() → removes spaces from the left    .rstrip() → removes spaces from the right

'''
31. Which one of the following variables return True when we use the method isidentifier():
    - 30DaysOfPython  --> false
    - thirty_days_of_python  --> true
'''
#32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(libraries))

'''
33. Use the new line escape sequence to separate the following sentences.
    I am enjoying this challenge.
    I just wonder what is next.
'''
print('I am enjoying this challenge.\nI just wonder what is next.')

'''
34. Use a tab escape sequence to write the following lines.
    Name      Age     Country   City
    Paola     250     UK        London
'''
print('Name\tAge\tCountry\tCity\nPaola\t250\tUK\t\tLondon')

'''
35. Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
'''
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square.'.format(radius, area))


'''
36. Make the following using string formatting methods:
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
'''
a = 8
b = 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))