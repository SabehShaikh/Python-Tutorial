words = {
    "kese ho": "how are you?",
    "theek hun": "i am fine",
    "apka name kya ha": "what is your name",
    "mera name sabeh": "my name is sabeh",
}

word = input("Enter a word: ")
print(words.get(word, "word not found"))

# explanation:
# get(key, default_value) Parameters:
# key – The key you are looking for in the dictionary.
# default_value (optional) – 
# The value to return if the key 
# is not found. If not provided,  it returns None.
