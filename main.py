import random

class EnglishPracticeTool:
    
    def __init__(self):
        # self.input_english_sentence = input("輸入要練習的英文句子: ")
        self.input_english_sentence = "As you know, our school is having its annual dinner dance on that day."
        self.default_input_english_sentence = ''
        self.special_symbol_removal_list = [',', '?', '.']
        self.remove_special_symbol_word_list = []
        self.hide_word_number = 2
        self.hide_english_sectence = []
        
    def removeSpecialSymobol(self):
        
        self.default_input_english_sentence = self.input_english_sentence
        # 特殊符號加上特殊符號 作為分辨使用
        for remove_special_symbol in self.special_symbol_removal_list:
            self.input_english_sentence = self.input_english_sentence.replace(remove_special_symbol, remove_special_symbol + '@@')
    def strToList(self):
        # 字串轉列表
        str_to_list = self.input_english_sentence.split(' ')
        return str_to_list

    def main(self):
        self.removeSpecialSymobol()
        input_english_sentence_to_list = self.strToList()
                
        get_hide_englist_sentence = self.randomHideWordNumber(hide_englist_sentece=input_english_sentence_to_list)
        
        self.getHideEnglishSentence(input_english_sentence=input_english_sentence_to_list, get_hide_englist_sentence=get_hide_englist_sentence)
        print('隱藏單字列表:', get_hide_englist_sentence)
        print('隱藏單字列表:', self.remove_special_symbol_word_list)

        self.dividerFunction()
        print('完整移除特殊符號句子列表:  ', input_english_sentence_to_list)
        # print('完整未移除特殊符號句子列表:', self.default_input_english_sentence)
        # self.dividerFunction()
        print('完整句子列表:    ', self.default_input_english_sentence)
        print('完整隱藏句子列表:', ' '.join(self.hide_english_sectence).replace('@@', ''))

        print('完整句子列表:    ', self.default_input_english_sentence.split(' '))
        print('完整隱藏句子列表:', ' '.join(self.hide_english_sectence).replace('@@', '').split(' '))        
        get_hid_english_sectence = ' '.join(self.hide_english_sectence).replace('@@', '')
        input_hide_english_word = input('請輸入缺少的單字，並後面空格作為分隔，如：you me，輸入完後請按下Enter \n')
        check_input_number = input('你輸入的空格上的單字為: %s \n確定請按1, 重新輸入請按2\n' % input_hide_english_word)
        if check_input_number == '1':
            print("開始驗證")
            print(get_hid_english_sectence)
            
            # print(type(input_hide_english_word))
            print(input_hide_english_word.split(' '))
            
            # for j in input_hide_english_word.split(' '):
            #     print(j)
            get_hid_english_sectence = get_hid_english_sectence.replace('___', 'ddd')
            #     print(j)
            #     for i in get_hid_english_sectence_list:
            #         if '___' in str(i):
            #             print('@@@@@')
            #             i = j
            #             break
            print(get_hid_english_sectence)
            
        if check_input_number == '2':
            pass
        
        
    def dividerFunction(self):
        print("=" * 10)
        
    def getHideEnglishSentence(self, input_english_sentence, get_hide_englist_sentence):
        for x in input_english_sentence:
            if x in str(get_hide_englist_sentence):
                if '@@' in x:
                    self.hide_english_sectence.append('___' + x[-3])
                else:
                    self.hide_english_sectence.append('___')
            else:
                self.hide_english_sectence.append(x)
        
    def randomHideWordNumber(self, hide_englist_sentece):
        # 取得要隱藏的的單字
        get_random_hide_sentect = random.sample(hide_englist_sentece, self.hide_word_number)
        
        for i in get_random_hide_sentect:
            if '@@' in str(i):
                self.remove_special_symbol_word_list.append(i[:-3])
            else:
                self.remove_special_symbol_word_list.append(i)
        return get_random_hide_sentect

        
      
        
        
if __name__ == '__main__':
    
    run = EnglishPracticeTool()
    run.main()