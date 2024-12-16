         #1.waf that takes number as the paramter and return true if the no is even else return false
def find(number):
    if number%2==0:
        return True#shortcut=return True if n%2==0 else False
    return False#return n%2==0 o/p=always true or false

        # if we want to take input from user
        # no=int(input("enter any no="))
        # find(no)
print(find(7))
print(find(8))  
    #2.waf that takes a string as a parameter and return the length of the string
def length(strings):
    return len(strings)
str=input("enter any letter=")
a=length(str)
print(a)

        #3.waf that takes string as parameter and return the first vowel in the string
def first_vowel(strings):
    for letter in strings.lower():
        if letter in "aeiou":#o/p none becoz we are comparing a single letter to a tuple so donot write letter=("a","e",......)
            return letter
b=first_vowel("hello")
print("found",b)
       #4 waf that takes string as the parameter and return true if the string contains vowels else return false
def vowels(strings):
    for letter in strings.lower():
        # print (letter)
        if letter in ("aeiou"):
            return True
    return False
print(vowels("kuiob"))
print(vowels("rhythm"))
      #5 waf that takes string as parameterand return the first consonent present in the string
def conso_ret(words):
    for letter in words:
        if letter not in "aeiou":
            return letter
value=conso_ret("string")
print("first consonent",value)
   #6 waf that takes string as parameter and return a total no of vowels present in the string
def count_vowels(word):
    count=0
    for letter in word:
        if letter in "aeiou":
            count+=1
    return count
print(count_vowels("aaaerop"))
       #7 waf that takes string as parameter and returns the total no of consonent present in the string
def count_conso(word):
    count=0
    for letter in word:
        if letter not in "aeiou":
            count+=1
    return count
print(count_conso("abcdefgh"))
    #7 waf that takes string as a parameter and return a total no of vowels and consonent present in the string
def total(word):
    count1=0
    count2=0
    for letter in word:
        if letter in "aeiou":
            count1+=1
        if letter not in "aeiou":
            count2+=1
    return count1,count2
a,b=total("abcdefg")
print(f"vowel={a} and consonant={b}")
    #8 waf that takes multiple number as parameter and return the sum of the numbers
def num_total(*numbers):
    sum=0
    for no in numbers:
        sum=sum+no
    return sum
print(num_total(1,2,3,4,5,6)) 
        #9 waf that take string as parameters and returns the first digit present in the string
def ret_digit(words):
    for letter in words:
        if letter.isdigit():#isdigit checks whether ther are any digit in the word
            return letter
print(ret_digit("abcd9fg2"))
         #10 waf that takes string as the parameter and return the first alpahbet present in the string
def first_alp(words):
    for letter in words:
       if letter.isalpha():#isalpha checks whether there are a-z or A-Z
           return letter
print(first_alp("1hello") )
       


