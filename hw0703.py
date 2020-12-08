# 第三題


def find(keyword_list, sentence_list):
    '''存取句子中出現關鍵字的結果'''
    # 從每一句第一個字開始找，以關鍵字的長度為準，看起始字及後面數位字元的組成是否為所求的關鍵字
    # 符合則存取結果，從找到關鍵字的下一位開始找
    # 若不符合則往下一位字元開始找
    # 格式[[第幾句,[關鍵字,關鍵字...]],[]...]
    result = []
    for i in range(len(sentence_list)):
        result.append([i])  # 紀錄是第幾句的結果
        index = 0  # 從每句的第一個字開始找
        while index < len(sentence_list):  # 若還沒檢查過句中的每一個字，就繼續找
            for j in range(len(keyword_list)):
                check = sentence_list[i][index:index+len(keyword_list[j][0])]
                if check != keyword_list[j][0]:
                    continue  # 起始值為首的詞與本輪關鍵字不同，則繼續比對下一組關鍵字
                else:
                    result[i].append(keyword_list[j][0])
                    index += len(keyword_list[j][0]) - 1  # 若找到相應的關鍵詞組，則從詞語後一位字元開始新查詢
                    break
            index += 1  # 若起始值為首的詞與本輪所有關鍵字都不同，則以下一位字元開始新查詢
    result.sort()
    return result


def weight(weight_dict, list_):
    '''加總每句關鍵字的權重'''
    # 找出字典中關鍵字權重
    # 並依各句累加
    # 輸出的結果存在字典內
    # weight_dict是關鍵字權重字典
    # list_是已找出的關鍵字清單
    # 格式[[第幾句,權重],[],[].....]
    sentence_weight_dict = dict()
    for i in range(len(list_)):
        effect = 0
        for j in range(1, len(list_[i])):
            effect += weight_dict[list_[i][j]]
        sentence_weight_dict[i] = effect
    return sentence_weight_dict


def count(company, list_, dict_):
    '''特定公司有關的新聞標題權重加總'''
    # 若該句中有出現特定公司名，則累加該句的權重至該公司的分數上
    # company是本輪的指定公司
    # list_是已找出公司名的清單
    # dict_是每句新聞標題的分數結果
    grade = 0
    for i in range(len(list_)):
        for j in range(1, len(list_[i])):
            if list_[i][j] == company:
                grade += dict_[list_[i][0]]
                break
    return grade


title_file_input = input()
dict_file_input = input()
category_file_input = input()
instruction = input().split(',')

industry = instruction[0]
totalquantity = int(instruction[1])
rowquantity = instruction[2].split(':')
for i in range(len(rowquantity)):
    rowquantity[i] = int(rowquantity[i])

# 處理標題檔
title_list = []
title_file = open(title_file_input, "r", encoding="utf-8")
for i in title_file:
    i = i.strip('\n')
    title_list.append(i)
title_file.close()

# 處理關鍵字權重檔
keyword_weight_dict = dict()
keyword_weight_list = []
dict_file = open(dict_file_input, "r", encoding="utf-8")
for i in dict_file:
    i = i.strip('\n')
    i = i.split(' ')
    i[1] = int(i[1])
    keyword_weight_dict[i[0]] = i[1]
    keyword_weight_list.append(i)
dict_file.close()
keyword_weight_list.sort(key=lambda k: len(k[0]), reverse=True)  # 按照關鍵字長短排序

# 處理公司名檔
company_category_dict = dict()
company_category_list = []
category_file = open(category_file_input, "r", encoding="utf-8")
for i in category_file:
    i = i.strip('\n')
    i = i.split(' ')
    company_category_dict[i[0]] = i[1]
    company_category_list.append(i)
category_file.close()

keyword_result = find(keyword_list=keyword_weight_list, sentence_list=title_list)
company_result = find(keyword_list=company_category_list, sentence_list=title_list)
weight_of_each_title = weight(weight_dict=keyword_weight_dict, list_=keyword_result)

# 找出符合所求產業下的所有公司
belong_industry = []  # 格式[[公司,分數加總,要買的張數]...]
for i in range(len(company_category_list)):
    if company_category_list[i][1] == industry:
        belong_industry.append([company_category_list[i][0]])

if len(belong_industry) == 0:  # 若沒有公司符合所求的產業
    print("NO_MATCH")
else:
    for i in range(len(belong_industry)):
        grade = count(company=belong_industry[i][0], list_=company_result, dict_=weight_of_each_title)  # 特定產業下各公司的分數合計
        belong_industry[i].append(grade)  # 第一位存分數
        belong_industry[i].append(0)  # 第二位存購買張數
    belong_industry.sort(key=lambda k: k[1], reverse=True)

    bal = totalquantity - 0  # 還可購買的張數
    while bal > 0:
        if len(belong_industry) >= len(rowquantity):  # 若可購公司數量大於預購公司數量，則預購公司數量做為分配依據
            for i in range(len(rowquantity)):
                if bal < rowquantity[i]:  # 若剩於購買張數不及本輪預購張數，則以小值全部購完，結束分配
                    belong_industry[i][2] += bal
                    bal = 0
                    break
                else:  # 若仍夠下一輪分配，則繼續
                    belong_industry[i][2] += rowquantity[i]
                    bal -= rowquantity[i]
        else:  # 若可購公司數量小於預購公司數量，則以可購公司數量做為分配依據
            for i in range(len(belong_industry)):
                if bal < rowquantity[i]:  # 若剩於購買張數不及本輪預購張數，則以小值全部購完，結束分配
                    belong_industry[i][2] += bal
                    bal = 0
                    break
                else:  # 若仍夠下一輪分配，則繼續
                    belong_industry[i][2] += rowquantity[i]
                    bal -= rowquantity[i]
    for i in range(len(belong_industry)):
        if belong_industry[i][2] > 0:  # 若該公司有應購張數，則輸出結果
            print('{}購買{}張'.format(belong_industry[i][0], belong_industry[i][2]))
