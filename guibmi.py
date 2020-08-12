import tkinter as tk
import math
import base64

win = tk.Tk()
win.title("BMI APP")
win.geometry('300x200')
win.configure(background = "white")

def calcul():
    hei = float(hei_entry.get())
    wei = float(wei_entry.get())
    bmi = round(wei/(hei**2),2)
    result = f"你的BMI指數為 : {bmi}"
    result2 = f"{get_bmi(bmi)}"
    result_label2.configure(text = result2)
    result_label.configure(text = result)

def get_bmi(bmi):
    if bmi < 18.5:
        return "體重過輕，可以多吃點!"
    elif 18.5 < bmi and bmi < 24 :
        return "體重剛剛好!"
    elif bmi > 24:
        return "體重有點過重, 多運動!" 

#建立身高框
hei_frame = tk.Frame(win)
hei_frame.pack(side = tk.TOP)
#身高框內輸入文字
hei_mes = tk.Label(hei_frame,text = "身高")
hei_mes.pack(side = tk.LEFT)
#創造身高輸入欄位
hei_entry = tk.Entry(hei_frame)
hei_entry.pack(side = tk.LEFT)

#建立體重框
wei_frame = tk.Frame(win)
wei_frame.pack(side = tk.TOP)
#身高框內輸入文字
wei_mes = tk.Label(wei_frame,text = "體重")
wei_mes.pack(side = tk.LEFT)
#創造體重輸入欄位
wei_entry = tk.Entry(wei_frame)
wei_entry.pack(side = tk.LEFT)

#創造顯示結果欄位
result_label = tk.Label(win)
result_label.pack()
#創造顯示提示欄位
result_label2 = tk.Label(win)
result_label2.pack()

calcul_btn = tk.Button(win,text="計算",command = calcul)
calcul_btn.pack()



win.mainloop()
