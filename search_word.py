# Beta v0.1

file_names = ['file1.txt', 'file2.txt', 'file3.txt']
search_word = str(input("Слово которое вы ищете: "))

for file_name in file_names:
    with open(file_name) as file:
        count_string = 0

        for line in file.readlines():
            line = line.strip().split()
            count_string += 1

            for word in line:
                if word == search_word:
                    print(f"Слово {search_word} находится в файле {file_name} на строке №{count_string}")
