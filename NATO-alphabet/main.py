import pandas

data = pandas.read_csv("C:/Users/nguye/projects/python-mini-projects/NATO-alphabet/phonetic_alphabet.csv")
# print(data)

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

def generate_phonetic(): 
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("sorry, only alphabet. ")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()