# Python program to print even length words in a string

# Function to print even length words
def print_even_length_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Iterate through each word
    for word in words:
        # Check if the word length is even
        if len(word) % 2 == 0:
            print(word)

# Example input
sentence = "Python is a powerful programming language"
print("Even length words in the sentence:")
print_even_length_words(sentence)
