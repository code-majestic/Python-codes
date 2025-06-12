text = "Python Loop"
vowels = "aeiouAEIOU"
for ch in text:
    if ch.isalpha() and ch not in vowels:
        print(ch, end=" ")