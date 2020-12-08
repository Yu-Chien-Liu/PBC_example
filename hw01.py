# hw_1
full = int(input())  # 購買全票的張數，為整數
fullprice = int(input())  # 全票之票價，為整數
student = int(input())  # 購買學生票的張數，為整數
studentprice = int(input())  # 學生票之票價，為整數
payment = int(input())  # 買方付現數，為整數

total = full*fullprice + student*studentprice  # 總票價合計
change = payment - total  # 應找回之金額
#判斷輸出的結果
if change < 0:  # 若付現數不夠支應總票價，則顯示-1
    print("-1")
else:
    print("$"+str(change))  # 若付現數足支應總票價，則顯示應找回之金額

# hw_2

full = int(input())  # 購買全票的張數，為整數
fullprice = int(input())  # 全票之票價，為整數
student = int(input())  # 購買學生票的張數，為整數
studentprice = int(input())  # 學生票之票價，為整數
payment = int(input())  # 買方付現數，為整數
limit = int(input())  # 購票上限數

totalpiece = full + student  # 購票張數合計

totalprice = full*fullprice + student*studentprice  # 總票價合計
change = payment - totalprice  # 應找回之金額

if totalpiece > limit:
    if change < 0:
        print("-1"+","+"-2")  # 當購票數超限，付現數不夠支應總票價，則顯示為-1,-2
    else:
        print("-1"+","+"$"+str(change))  # 當購票數超限，付現數足支應總票價，則顯示-1及應找回之金額
else:
    more = limit - totalpiece  # 當購票數未超限，則計算尚可購買之數量
    if change < 0:
        print(str(more)+","+"-2")  # 若付現數不夠支應總票價，則顯示尚可購買之數量及-2
    else:
        print(str(more)+","+"$"+str(change))  # 若付現數足夠支應總票價，則顯示顯示尚可購買之數量及應找回之金額

# 另
full = int(input())  # 購買全票的張數，為整數
fullprice = int(input())  # 全票之票價，為整數
student = int(input())  # 購買學生票的張數，為整數
studentprice = int(input())  # 學生票之票價，為整數
payment = int(input())  # 買方付現數，為整數
limit = int(input())  # 購票上限數

totalpiece = full + student  # 購票張數合計

totalprice = full*fullprice + student*studentprice  # 總票價合計
change = payment - totalprice  # 應找回之金額
# 判斷購票數是否超限
if totalpiece > limit:
    print("-1", end=',')  # 當購票數超限，則顯示-1
else:
    more = limit - totalpiece  # 尚可購買的票數
    print(str(more), end=',')  # 當購票數未超限，則顯示可購張數
# 判斷付現數是否足夠支應票價
if change < 0:
    print("-2")  # 若付現數不夠支應總票價，則顯示-2
else:
    print("$"+str(change))  # 若付現數足夠支應總票價，則顯示應找回之金額

# hw_3

full = int(input())  # 購買全票的張數，為整數
fullprice = int(input())  # 全票之票價，為整數
student = int(input())  # 購買學生票的張數，為整數
studentprice = int(input())  # 學生票之票價，為整數
payment = int(input())  # 買方付現數，為整數
limit = int(input())  # 購票上限數

totalpiece = full + student  # 購票張數合計

totalprice = full*fullprice + student*studentprice  # 總票價合計
change = payment - totalprice  # 應找回之金額

if totalpiece <= limit:
    if change >= 0:  # 若購票數未超限且付現數足夠支應總票價，則計算尚可購買之數量，並顯示兩者數值
        more = limit - totalpiece  # 尚可購買的票數
        print(str(more)+","+"$"+str(change))
    else:  # 若購票數未超限但付現數不夠支應總票價，則只顯示尚可購買之數量
        more = limit - totalpiece
        print(str(more)+",")
else:
    if change >= 0:  # 若購票數超限然付現數足夠支應總票價，則顯示應找回之金額，否則都不顯示
        print("$"+str(change))

# 另
full = int(input())  # 購買全票的張數，為整數
fullprice = int(input())  # 全票之票價，為整數
student = int(input())  # 購買學生票的張數，為整數
studentprice = int(input())  # 學生票之票價，為整數
payment = int(input())  # 買方付現數，為整數
limit = int(input())  # 購票上限數

totalpiece = full + student  # 購票張數合計

totalprice = full*fullprice + student*studentprice  # 總票價合計
more = limit - totalpiece  # 尚可購買的票數
change = payment - totalprice  # 應找回之金額
# 判斷購票數是否超限
if totalpiece <= limit:
    print(str(more), end=',')  # 若購票數未超限，則顯示尚可購買之數量，若超限則不處理
# 判斷付現數是否足夠支應票價
if change >= 0:
    print("$"+str(change))  # 若付現數足夠支應總票價，則顯示應找回之金額，否則都不顯示


# hw_4

particulate_matter = int(input())  # 非負整數的濃度系數
temperature = int(input())  # 非負整數的氣溫系數
dewpoint = int(input())  # 非負整數的露點溫度系數
criticalpoint = float(input())  # 臨界值為介於0與1之間的浮點數

willing_airpolution = 0.5  # 考慮空汙前赴約的意願系數
willing_humidity = 0.5  # 考路濕度前赴約的意願系數

if particulate_matter <= 35:  # 依粉塵濃度區分計算空汙影響的計算公式
    willing_airpolution += (100 - particulate_matter)*0.005
else:
    willing_airpolution += (45 - particulate_matter)*0.02  # 得出考慮空汙後的意願系數

if willing_airpolution <= 0:  # 意願上下限為0及1，因此係數不及0則調為0
    willing_airpolution = 0
elif willing_airpolution >= 1:  # 係數超過1則調為1
    willing_airpolution = 1

humidity = 100 - 5*(temperature - dewpoint)  # 將氣溫與露點溫度帶入求濕度

if humidity <= 30:  # 依上計算之濕度計算影響係數的結果
    willing_humidity = willing_humidity/60 * (110 - humidity)
else:
    willing_humidity = willing_humidity/45 * (90 - humidity)  # 得出考慮濕度後的意願系數

if willing_humidity <= 0:  # 意願上下限為0及1，因此係數不及0則調為0
    willing_humidity = 0
elif willing_humidity >= 1:  # 係數超過1則調為1
    willing_humidity = 1

determine = min(willing_airpolution, willing_humidity)  # 空汙和濕度影響下較小者為最後決定是否赴約的係數
print('{:.2f}'.format(determine))  # 將浮點數取至小數後兩位

if determine >= criticalpoint:  # 最終意願系數不小於臨界值則赴約，小於則拒絕
    print("Let's go together.")
else:
    print("I wouldn't go out with you.")
