# 第一題
'''
number = int(input())
resultlist = []

if number == 6174:
    print(6174)
else:
    while number != 6174:
        if number < 10:
            number = number * 1000
        elif 9 < number < 100:
            number = number * 100
        elif 99 < number < 1000:
            number = number * 10

        a = number // 1000
        number -= a * 1000
        b = number // 100
        number -= b * 100
        c = number // 10
        number -= c * 10
        d = number

        list = []
        list.append(a)
        list.append(b)
        list.append(c)
        list.append(d)
        list.sort()

        small = list[0] * 1000 + list[1] * 100 + list[2] * 10 + list[3]
        list.reverse()
        big = list[0] * 1000 + list[1] * 100 + list[2] * 10 + list[3]

        number = big - small
        resultlist.append(number)

    for i in range(len(resultlist)):
        if i == len(resultlist)-1:
            print(resultlist[i], end="")
        else:
            print(resultlist[i], end=',')
'''
# 用while true

   
'''
number = int(input())
result = ""

for i in range(3):
    if number < 10:
        number = number * 100
    elif 9 < number < 100:
        number = number *10

    a = number // 100
    number -= a * 100
    b = number // 10
    number -= b * 10
    c = number

    maximum = a
    if b > a:
        if b > c:
            maximum = b
        else:
            maximum = c
    else:
        if c > a:
            maximum = c

    mediem = a
    if a > b >= c or c > b >= a: 
        mediem = b
    if a > c >= b or b > c >= a:
        mediem = c

    minimum = a
    if b < a:
        if b < c:
            minimum = b
        else:
            minimum = c
    else:
        if c < a:
            minimum = c

    big = maximum * 100 + mediem * 10 + minimum
    small = minimum * 100 + mediem * 10 + maximum

    number = big - small
    
    if i == 2:
        result += str(number)
    else:
        result += (str(number) + ",")
        
print(result)
'''

# 第二題
'''
intervalamount_demand = input().split(',')
interval_rate = input().split(',')
intervalamount = []
demand = []
interval = []
rate = []
sum = 0

for i in range(len(intervalamount_demand)):
    if i == 0:
        intervalamount.append(int(intervalamount_demand[i]))
    else:
        demand.append(int(intervalamount_demand[i]))

for i in range(len(interval_rate)):
    if i < intervalamount[0]:
        interval.append(int(interval_rate[i]))
    else:
        rate.append(int(interval_rate[i]))

interval.insert(0,0)

for i in range(intervalamount[0]):
    if interval[i+1] <= demand[0]:
        sum += (interval[i+1]-interval[i]) * rate[i]
    else:
        if demand[0] < interval[i]:
            pass
        else:
            sum += (demand[0] - interval[i]) * rate[i]

print(sum)
'''
# 第三題

intervalamount_demand = input().split(',')
interval_rate = input().split(',')
intervalamount = []
demand = []
interval = []
rate = []
sum_ = 0
incremental = 0  # 超越需求量後的級距乘單價
lowpoint = 0
# 把資料存入各個清單
for i in range(len(intervalamount_demand)):
    if i == 0:
        intervalamount.append(int(intervalamount_demand[i]))
    else:
        demand.append(int(intervalamount_demand[i]))

for i in range(len(interval_rate)):
    if i < intervalamount[0]:
        interval.append(int(interval_rate[i]))
    else:
        rate.append(int(interval_rate[i]))
# 補0為第一個級距的起點(因為後面計算需要用到級距間的差額)
interval.insert(0,0)

for i in range(intervalamount[0]):
    if demand[0] > interval[i+1]:  # 若需求大於該級距，則加總該段的金額
        sum_ += rate[i] * (interval[i+1] - interval[i])
    else:
        if demand[0] <= interval[i]:  # 當需求未大於該級距，且在需求也未大於上一個級距
            if (interval[i+1] - interval[i])*rate[i] + incremental <= 0:  # 若本級距的斜率是負的
                sum_ += (interval[i+1] - interval[i])*rate[i] + incremental  # 加上負值
                incremental = 0
                lowpoint = interval[i+1]
            else:
                incremental += (interval[i+1] - interval[i])*rate[i] # 若本級距的斜率是正的，先存著
        else:  # 當需求未大於該級距，但有高於上一個級距
            if (interval[i+1] - interval[i])*rate[i] <= (demand[0] - interval[i])*rate[i]:  # 若本級距斜率是負的
                sum_ += (interval[i+1] - interval[i])*rate[i] # 加上負值
                lowpoint = interval[i+1]
            else:
                incremental += (interval[i+1] - interval[i])*rate[i] - (demand[0] - interval[i])*rate[i]
                sum_ += (demand[0] - interval[i])*rate[i]
                lowpoint = demand[0]
print(str(lowpoint)+','+str(sum_))

'''
for i in range(intervalamount[0]):
    if interval[i+1] <= demand[0]:
        sum_ += (interval[i+1]-interval[i]) * rate[i]
    else:
        if demand[0] < interval[i]:
            pass
        else:
            sum_ += (demand[0] - interval[i]) * rate[i]

minisum_ = 0
minisum_list = []
for i in range(intervalamount[0]):
    minisum_ += (interval[i+1] - interval[i]) * rate[i]
    minisum_list.append(minisum_)

min_index = minisum_list.index(min(minisum_list))


if min(minisum_list) < sum_ and interval[min_index+1] > demand[0]:
    print(str(interval[min_index+1])+','+str(min(minisum_list)))
else:
    print(str(demand[0])+','+str(sum_))
'''
# 大於需求量的才來比較


# 第四題
catagory = int(input())  # 產品的種類數，是正整數
aset = input().split(',')  # 成組的那些產品編號
itemprice = input().split(',')  # 四種產品分別的售價
demand = input().split(',')  # 四種產品分別的購買量
aset_int = []  # 將產品編號轉成數字型態
itemprice_int = []  # 將售價轉成數字型態
demand_int = []  # 將購買量轉成數字型態
setamount = []  # 成組販售商品分別的需求量

# 先將成組商品、產品售價、購買量清單內的資料改成數字型態
for i in aset:
    aset_int.append(int(i))

for i in itemprice:
    itemprice_int.append(int(i))

for i in demand:
    demand_int.append(int(i))
# 求未考慮折扣前的總價，利用迴圈將購買量列表和產品價格列表兩者依序相乘加總
totalprice = 0
for i in range(1, catagory+1):
    totalprice += demand_int[i-1] * itemprice_int[i-1]  # 需求量乘單位價格
# 把可以湊成組販售的商品需求量另外拉到一張表
for i in aset_int:
    setamount.append(demand_int[i-1])
# 用迴圈找可以湊成的最大組數(也就是setamount中需求量最小的那個數字)
minimum = setamount[0]  # minimum為可以湊成的組數

for i in setamount:
    if i < minimum:
        minimum = i
# 計算折扣
discount = 0
for i in aset_int:
    discount += (itemprice_int[i-1] * minimum) * 0.1  # 成組的商品每一單價可折10%
# 計算超過五組的部分，每一單價可以再折10%
morediscount = minimum // 5
for i in aset_int:
    discount += (itemprice_int[i-1] * morediscount*5) * 0.1

result = int(totalprice - discount)  # 最終總價為原始價減折扣
newcrew = int(discount // 1000)  # 節省超過一千元多招募一名新球員的計算

if newcrew >= 1:  # 超過一人則印省下的錢及新球員人數
    print(str(result)+','+str(newcrew))
else:  # 成效不彰則印道歉文字
    print("So sad. I messed up.")
