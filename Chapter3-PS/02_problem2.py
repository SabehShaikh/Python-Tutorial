letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''

print(letter.replace("<|Name|>", "Sabeh")
      .replace("<|Date|>", "15 February 2025"))