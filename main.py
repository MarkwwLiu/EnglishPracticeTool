
class EnglishPracticeTool:
    
    def __init__(self):
        # self.input_english_sentence = input("輸入要練習的英文句子: ")
        self.input_english_sentence = "how are you?"
        self.special_symbol_removal_list = [',', '?', '.']
        self.hide_word_number = 1
        
    def main(self):
        # 先移除特殊符號
        for remove_special_symbol in self.special_symbol_removal_list:
            self.input_english_sentence = self.input_english_sentence.replace(remove_special_symbol, '')
        # 轉換為 list 
        input_english_sentence_to_list = self.input_english_sentence.split(' ')
        
        print(input_english_sentence_to_list)
        
        
        
        
        
if __name__ == '__main__':
    
    run = EnglishPracticeTool()
    run.main()