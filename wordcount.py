# put your code here.


def get_word_count(filename):
    data = open(filename)
    word_count = {}
    for line in data:
        words = line.rstrip()
        words = line.split(" ")
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        print word_count
        #word_count[word] = word_count.get(word, 0)
    #return word_count
    data.close()


print get_word_count('test.txt')

#poem = "As I was going to St. Ives I met a man with seven wives Every wife had seven sacks"

#def get_word_count(words)
