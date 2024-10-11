class WordsFinder:
    def __init__(self, *files):
        self.file_names = list(files)
        self.words_dict = {}

    def get_all_words(self):
        self.all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = file.read().lower().replace(',', '').replace('.', '').replace('=', '').replace('!', '')\
                    .replace('?', '').replace(';', '').replace(':', '').replace(' - ', '').split()
                self.all_words[file_name] = words
        return self.all_words

    def find(self, word):
        self.result_one = {}
        self.get_all_words()
        for file_name, words in self.all_words.items():
            index = words.index(word.lower())
            self.result_one[file_name] = index
            continue
        return self.result_one

    def count(self, word):
        self.result_two = {}
        self.get_all_words()
        for file_name, words in self.all_words.items():
            count_ = words.count(word.lower())
            if count_ > 0:
                self.result_two[file_name] = count_
        return self.result_two

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))



















































