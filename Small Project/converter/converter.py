one_digit_words=["zero","one","two","three","four","five","six","seven","eight","nine"]

two_digit_words=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","thirty","forty","fifty","sixty","seventy",
                 "eighty","ninety"]



large_sum_words = ["hundred","thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion", "octillion", "nonillion"]

def detect_ten(number):
    a=abs(int((number)))
    length=len(str(number))
    word=""
    mod = a % 10
    quotient = a // 10
    if quotient == 0:
        word = word + " " + one_digit_words[a]
    if quotient == 1:
        word = word + " " + two_digit_words[mod]
    if quotient > 1 and quotient < 10:
        order = 10 + quotient - 1
        index = order - 1
        if mod == 0:
            word = word + " " + two_digit_words[index]
        else:
            word = word + " " + two_digit_words[index] + " " + one_digit_words[mod]
    return word

def detect_hundred(number):
    if str(number).endswith("00"):
        hundred=one_digit_words[int(str(number)[0])]+" "+large_sum_words[0]
    else:
        remain=number-100*int(str(number)[0])
        hundred = one_digit_words[int(str(number)[0])] + " " + large_sum_words[0]+" "+"and"+detect_ten(remain)
    return hundred

def number_lst(number):
    str_n=str(number)
    word=""
    if len(str_n)==3:
        word=word+" "+detect_hundred(number)
    elif len(str_n)==2:
        word=word+" "+detect_ten(number)
    elif len(str_n)==1:
        word=word+" "+one_digit_words[number]
    return word
Continue=True
while Continue:
    number=input("Enter a number to convert:")
    length=len((number))
    a=abs(int(number))
    word=""
    if number.startswith("-"):
        # 如果为负数，转换后的字符串开头先加“negative",同时符号“-”不能算进位数里面
        word=word+"negative"
        length=length-1
    if a>10 and a<100:
        word=word+" "+detect_ten(a)

    elif a>=100 and a<=999:
        word=word+" "+detect_hundred(a)
    elif a>=1000:
        # 检查除去输入数字中第一位后面的位数
            str_a=str(a)
            a='{:,}'.format(a).split(",")
            len_a=len(a[1:])
            if int(a[0])>0 and int(a[0])<10:
                word=word+" "+one_digit_words[int(a[0])]+" "+large_sum_words[len_a]
                a = int(str_a) - int(a[0]) * pow(1000, len_a)
                while True:
                    str_a=str(a)
                    if a<1000:
                        if a>=100 and a<=999:
                            word=word+" "+" "+detect_hundred(a)
                        elif a>=10 and a<=999:
                            word=word+" "+"and"+" "+detect_ten(a)
                        else:
                            if a > 0:
                                word = word + " " + "and" + " " + one_digit_words[a]
                            else:
                                word = word
                        break
                    else:
                        b='{:,}'.format(int(str_a)).split(",")
                        len_b=len(b[1:])
                        word = word + " " +number_lst(int(b[0]))+" " + large_sum_words[len_b]
                        a = int(str_a) - int(b[0]) * pow(1000, len_b)

            elif int(a[0]) >=10 and int(a[0]) < 100:
                word = word + " " + detect_ten(int(a[0])) + " " + large_sum_words[len_a]
                a = int(str_a) - int(a[0]) * pow(1000, len_a)
                while True:
                    str_a = str(a)
                    if a < 1000:
                        if a >= 100 and a <= 999:
                            word = word + " " + " " + detect_hundred(a)
                        elif a >= 10 and a <= 999:
                            word = word + " " + "and" + " " + detect_ten(a)
                        else:
                            if a>0:
                              word = word + " " + "and" + " " + one_digit_words[a]
                            else:
                              word=word
                        break
                    else:
                        b = '{:,}'.format(int(str_a)).split(",")
                        len_b = len(b[1:])
                        word = word + " " + number_lst(int(b[0])) + " " + large_sum_words[len_b]
                        a = int(str_a) - int(b[0]) * pow(1000, len_b)
            elif int(a[0]) >=100 and int(a[0]) < 999:
                word = word + " " + detect_hundred(int(a[0])) + " " + large_sum_words[len_a]
                a = int(str_a) - int(a[0]) * pow(1000, len_a)
                while True:
                    str_a = str(a)
                    if a < 1000:
                        if a >= 100 and a <= 999:
                            word = word + " " + " " + detect_hundred(a)
                        elif a >= 10 and a <= 999:
                            word = word + " " + "and" + " " + detect_ten(a)
                        else:
                            if a>0:
                              word = word + " " + "and" + " " + one_digit_words[a]
                            else:
                              word=word
                        break
                    else:
                        b = '{:,}'.format(int(str_a)).split(",")
                        len_b = len(b[1:])
                        word = word + " " + number_lst(int(b[0])) + " " + large_sum_words[len_b]
                        a = int(str_a) - int(b[0]) * pow(1000, len_b)

    print(number+"----->"+word)
    play=input("Do you still want to play(Y/N):")
    if play.upper()=="Y":
        Continue=True
    elif play.upper()=="N":
        Continue=False
    else:
        Continue=False



