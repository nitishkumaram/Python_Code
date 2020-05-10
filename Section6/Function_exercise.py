#Function 1
def myfunc():
    print('Hello World')

#Function 2
def myfunc(name = 'Name'):
    print('Hello ' +name)

#Function 3
def myfunc(value):
    if(value == True):
        return 'Hello'
    else:
        return 'Goodbye'

#Function 4
def myfunc(x,y,z):
    if z == True:
        return x
    else:
        return y

#Function 5
def myfunc(a,b):
    return a+b

#Function 6
def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False

#Function 7
def is_greater(x,y):
    if x>y:
        return True
    else:
        return False

#Function 8
def myfunc(*args):
    return sum(args)

#Function 9
def myfunc(*args):
    output = []
    for num in args:
        if(num%2 == 0):
            output.append(num)
    return output

#Function 10
def myfunc(str):
    out = []
    for i in range(len(str)):
        if i%2 == 0:
            out.append(str[i].lower())
        else:
            out.append(str[i].upper())
    return ''.join(out)

#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers
#  if both numbers are even, but returns the greater if one or both numbers are odd

def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        if a<b:
            result= a
        else:
            result= b
    else:
        if a>b:
            result= a
        else:
            result= b
    return result


#OR You can solve by below program
def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        return max(a,b)


# Check-->
# lesser_of_two_evens(2,4)
# lesser_of_two_evens(2,5)

# ANIMAL CRACKERS: Write a function takes a two-word string and returns 
# True if both words begin with same letter

# def animal_crackers(text):
#    wordlist = text.split()
#     print(wordlist)
    
#    first = wordlist[0]
#    second = wordlist[1]
    
#    return first[0] == second[0]

#OR

def animal_crackers(text):
    wordlist = text.lower().split()
    print(wordlist)
    return wordlist[0][0] == wordlist[1][0]


# Check
animal_crackers('Levelheaded llama')

# Check
animal_crackers('Crazy Kangaroo')

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False

def makes_twenty(n1,n2):
    
    return n1+n2==20 or n1==20 or n2==20

# Check
makes_twenty(20,10)

# Check
makes_twenty(2,3)

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald
# Note: 'macdonald'.capitalize() returns 'Macdonald'

def old_macdonald(name):
    first_letter = name[0]
    inbetween = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]

    return first_letter.upper()+inbetween+fourth_letter.upper()+rest

    # or

    first_half = name[:3]
    second_half = name[3:]

    return first_half.capitalize()+second_half.capitalize()

# MASTER YODA: Given a sentence, return a sentence with the words reversed

    # master_yoda('I am home') --> 'home am I'
    # master_yoda('We are ready') --> 'ready are We'

def master_yoda(text):
    wordlist= text.split()
    reverse_word_list= wordlist[::-1]
    return ' '.join(reverse_word_list)

# Check
master_yoda('I am home')
# Check
master_yoda('We are ready')
