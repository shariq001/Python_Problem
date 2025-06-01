# Problem 2: Count Vowels in a String
# Write a function that counts the number of vowels (a, e, i, o, u) in a string (case-insensitive).



def check_vowels( user_input ):
    
    vowel_count = 0
    
    vowels = ["a", "A", "E", "e", "I", "i", "O", "o", "U", "u"]
    
    for char in user_input:
        
        if char in vowels:
            vowel_count += 1
            
    print(vowel_count)
        
    
    
check_vowels("A is a vowel in alphabets in English. Let's Check how much vowels this sentence contains.")