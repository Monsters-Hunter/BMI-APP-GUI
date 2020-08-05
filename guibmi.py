import tkinter as tk

win = tk.Tk()
win.title("BMI APP")
win.geometry('300x200')
win.configure(background = "white")

def calcul():
    hei = float(hei_entry.get())
    wei = float(wei_entry.get())
    print(wei/(hei**2))

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

calcul_btn = tk.Button(win,text="計算",command = calcul)
calcul_btn.pack()

win.mainloop()
