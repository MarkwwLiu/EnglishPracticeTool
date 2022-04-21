from enum import Flag
import random

class EnglishPracticeTool:
    
    def __init__(self):
        # self.input_english_sentence = input("輸入要練習的英文句子: ")
        self.input_english_sentence = "As you, know, input? test."
        self.default_input_english_sentence = ''
        self.special_symbol_removal_list = [',', '?', '.']
        self.remove_special_symbol_word_list = []
        self.hide_word_number = 2
        self.hide_english_sectence = []
        
    def identifySpecialSymobol(self):
        
        self.default_input_english_sentence = self.input_english_sentence
        # 特殊符號加上特殊符號 作為分辨使用
        for remove_special_symbol in self.special_symbol_removal_list:
            self.input_english_sentence = self.input_english_sentence.replace(remove_special_symbol, remove_special_symbol + '@@')
                    
        print('使用者輸出的英文句子:       %s' % self.default_input_english_sentence)
        print('加上識別特殊符號的英文句子: %s' % self.input_english_sentence)

    def inputEnglishSentenceToList(self):
        # 字串轉列表
        
        str_to_list = self.input_english_sentence.split(' ')
        return str_to_list

    def main(self):
        self.default_input_english_sentence = self.input_english_sentence

        # self.identifySpecialSymobol()
        input_english_sentence_to_list = self.inputEnglishSentenceToList()


        get_hide_englist_sentence = self.randomHideWordNumber(
            hide_englist_sentece=input_english_sentence_to_list
            )
        
        print('隨機取得要隱藏的英文單字: %s' % get_hide_englist_sentence)

        self.getHideEnglishSentence(
            input_english_sentence=input_english_sentence_to_list, 
            get_hide_englist_sentence=get_hide_englist_sentence
            )
        self.dividerFunction()

        print('完整句子列表:', input_english_sentence_to_list)
        print('英文句子練習:', ' '.join(self.hide_english_sectence))


        input_hide_english_word = input('請輸入缺少的單字，並後面空格作為分隔，如：you me，輸入完後請按下Enter \n')
        input_hide_english_word_list = input_hide_english_word.split(' ')

        for i in range(len(self.hide_english_sectence)):
            if '___' in str(self.hide_english_sectence[i]):
                if len(self.hide_english_sectence[i]) == 3:
                    self.hide_english_sectence[i] = input_hide_english_word_list[0]
                else:
                    self.hide_english_sectence[i] = input_hide_english_word_list[0] + self.hide_english_sectence[i][-1]
                input_hide_english_word_list.pop(0)

        print('已經填上隱藏單字的句子: %s' % self.hide_english_sectence)
        print('原先正確的句子: %s' % input_english_sentence_to_list)
        

        self.dividerFunction()
        
        list1 = input_english_sentence_to_list
        list2 = self.hide_english_sectence
        
        c = [x for x in list1 if x not in list2]
        d = [y for y in list2 if y not in list1] 
        
        get_diff_errr_word_dict = dict(zip(c, d))  
        for correct_word, error_word in get_diff_errr_word_dict.items():
            print('正確單字為: {0}, 錯誤單字為: {1}'.format(correct_word, error_word))


        self.dividerFunction()

        print('原先正確單字的句子: %s' % self.default_input_english_sentence)
        print('你填寫的單字的句子: %s' % ' '.join(self.hide_english_sectence))
        
    def dividerFunction(self):
        print("=" * 10)
        
    def getHideEnglishSentence(self, input_english_sentence, get_hide_englist_sentence):
        is_add_special = False
        for x in input_english_sentence:
            # 判斷是否有隱藏單字，沒有則照樣加入新的單字
            if x in str(get_hide_englist_sentence):
                # 跑看是否有特殊符號有的話，在___後面加上特殊符號，最後Back離開迴圈
                for i in self.special_symbol_removal_list:
                    if i in str(x):
                        is_add_special = True
                        self.hide_english_sectence.append('___' + x[-1])
                        break
                if is_add_special is False:
                    self.hide_english_sectence.append('___')
            else:
                self.hide_english_sectence.append(x)
        
    def randomHideWordNumber(self, hide_englist_sentece):
        # 取得要隱藏的的單字
        get_random_hide_sentece = random.sample(hide_englist_sentece, self.hide_word_number)
        
        # for word in range(len(get_random_hide_sentece)):
        #     for i in self.special_symbol_removal_list:
        #         get_random_hide_sentece[word] = get_random_hide_sentece[word].replace(i, '')

        

        return get_random_hide_sentece

        
        
        
if __name__ == '__main__':
    
    run = EnglishPracticeTool()
    run.main()