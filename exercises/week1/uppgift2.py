def count_frekvens(text):
    frekvens = {}
    for tecken in text:
        if tecken in frekvens:
            frekvens[tecken] += 1
        else:
            frekvens[tecken] = 1
    return frekvens

input_text = input("Ange valfritt ord: ")
output = count_frekvens(input_text)
print(f'Frekvens av input {input_text}: {output}')