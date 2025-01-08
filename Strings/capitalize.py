#capitalize() is a Python method that returns a copy of the original string with the first character in uppercase and the rest of the characters in lowercase
def Capitalize (stri):
    stri = list(stri) #In python, strings are immutable so we need to transform "stri" into a list
    for i in range(len(stri)):
        if i == 0 and stri[i].isalpha(): # isalpha() is a Python method that checks if the string contains only alphabetic characters
            stri[i] = stri[i].upper() # upper() transforms the letter into his uppercase form, in case in it has none or its a number, it remains unchanged
        elif i != 0 and stri[i].isalpha():
            stri[i] = stri[i].lower() # lower() transforms the letter into his lowercase form, in case in it has none or its a number, it remains unchanged
        else:
            pass
    return ''.join(stri)
## join() is a Python method that joins elements of an iterable (like a list or tuple) into a single string
## The string calling join() acts as a separator between elements.
## If the iterable contains non-string elements, join() will raise an error.
#  In this case '' acts as a separator, is the string who will separate the elements that are separated in the list
saludo = "hello WORLD12"
print(Capitalize(saludo))
                        
    