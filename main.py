# Read the file

file_path = "books/frankenstein.txt"
with open(file_path, "r") as file:
    data = file.read()
# count the number of words in the file 
    word_count = len(data.split())

# categorise characters and return unique counts
    alpha_num = {}
      
    for char in data:
        if char.isalpha():
            lower_char = char.lower()
            if lower_char not in alpha_num:
                alpha_num[lower_char] = 1
            else:
                alpha_num[lower_char] += 1
        else:
            try:
                raise ValueError("Invalid character")
            except ValueError:
                continue
# covert dictionary to list of tuples and sort in alphabetical order
    alpha_num_sorted = sorted(list(alpha_num.items()), key=lambda x: (x[0], x[1]))

    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} found in the document\n")

# Loop through list of sorted list of tuples and print characters with character counts.
    for tp in alpha_num_sorted:
        char_element = tp[0]
        count_element = tp[1]
        output = "The '{}' character was found {} times".format(char_element, count_element)
       
        print(output)

    print("--- End report ---")

   


