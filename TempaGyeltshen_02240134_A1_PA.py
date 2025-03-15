
def primenumberchecker(x):
    
    if x <= 1:
        return False  
    for i in range(2, x): 
        if x % i == 0: 
            return False
    return True  

def prime_sum_calculator():
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the end number: "))

    prime_sum = 0

    for n in range(start, end + 1):
        if primenumberchecker(n):  
            prime_sum += n  

    print("Sum of prime numbers between",start, "and" ,end, "is: ", prime_sum)

def length_unit_converter():
    
    value = float(input("Enter the length value: "))
    user_coice = input("Enter 'M' for meters to feet or 'F' for feet to meters: ").upper()

    if user_coice == 'M':
        converted_value = value * 3.28084 
        print(value, "meters = ",round(converted_value, 2), "feets")
    elif user_coice == 'F':
        converted_value = value / 3.28084 
        print(f"{value} feet = {round(converted_value, 2)} meters")
    else:
        print("Invalid. Please enter 'M' or 'F' .")


def consonant_counter():
    
    user_text = input("Enter a string: ")
    consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    count = 0

    for char in user_text:
        if char in consonants:
            count += 1
    print("Number of consonants in",user_text, "is :",count)
         


def minimum_maximum_finder():
    numbers = []
    number_list = int(input("How many numbers do you want to enter? "))

    for i in range(number_list):
        entered_number = float(input(f"Enter number {i + 1}: "))
        numbers.append(entered_number)

    smallest = min(numbers)
    largest = max(numbers)

    print("Smallest number is : ",smallest," and ", "Largest number is: ",largest)

def palindrome_checker():
    text = input("Enter a string to check for Palindrome: ")
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())  
    check_palindrome = cleaned_text == cleaned_text[::-1] 

    print("Is ",text, "a palindrome?",check_palindrome)
    

def word_counter():
    words_to_count = ["the", "was", "and"]
    file_path = input("Enter the path to the text file: ")

    try:
        with open(file_path, 'r') as file:
            text = file.read().lower()  
        word_counts = {}
        for word in words_to_count:
            word_counts[word] = 0 

        words_in_text = text.split()

        for word in words_in_text:
            if word in word_counts:  
                word_counts[word] += 1   
        for word, count in word_counts.items():
            print(f"'{word}' appears {count} times.")
    except FileNotFoundError:
        print("File not found. Please check the file path.")


def main_menu():
    while True:
        print("Select a function (1-6):")
        print("1. Calculate the sum of prime numbers")
        print("2. Convert length units")
        print("3. Count consonants in string")
        print("4. Find min and max numbers")
        print("5. Check for palindrome")
        print("6. Word Counter")
        print("7. Exit program")

        choice = input("Enter your choice: ")

        if choice == '1':
            prime_sum_calculator()
        elif choice == '2':
            length_unit_converter()
        elif choice == '3':
            consonant_counter()
        elif choice == '4':
            minimum_maximum_finder()
        elif choice == '5':
            palindrome_checker()
        elif choice == '6':
            word_counter()
        elif choice == '7':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

        if choice != '7':
            again = input("Would you like to try another function? (y/n): ").lower()
            if again != 'y':
                print("Exiting program. Goodbye!")
                break

main_menu()