def count_words(content):
    l = content.split()
    return len(l)

def count_characters(content):
    d = dict()
    for i in content:
        d[i.lower()] = d.get(i.lower(), 0) + 1
    return d

def write_report(all_words, all_characters):
    print(f"--- Begin report of books/frankenstein.txt ---\n{all_words} words found in the document\n")
    for i in all_characters:
        print(f"The '{i}' character was found {all_characters[i]} times")
    
    
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    write_report(count_words(file_contents), count_characters(file_contents))


main()
