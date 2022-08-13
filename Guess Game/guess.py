import tkinter as tk
import random

### Guess game setting
def set_game():
    key.set(random.randint(0,100))
    l.set(0)
    h.set(100)
    flag.set(0)
    show_text.insert('insert', "Set the game, key is changed\n")

def guess_compute():
    try:
        guess = int(entry.get())
        if key.get() == -1:
            show_text.insert('insert', "Please press the [Set Game] button\n")
        else:
            if flag.get() == 0:
                global low
                global high
                low = l.get()
                high = h.get()
                flag.set(1)
            random_number = key.get()
            if guess >= 0 and guess <= 100:
                #show_text.insert('insert', "Your Guess Number is : " + str(guess) + '\n')
                if random_number == guess:
                    show_text.insert('insert', "Win\n")
                    key.set(-1)
                elif guess > random_number :
                    if guess < high:
                        high = guess
                    show_text.insert('insert', "Key range is : " + str(low) + " - " + str(high) + '\n')
                elif guess < random_number :
                    if guess > low:
                        low = guess
                    show_text.insert('insert', "Key range is : " + str(low) + " - " + str(high) + '\n')
            else:
                show_text.insert('insert', "Error, please input a 0~100 number\n")
    except:
        show_text.insert('insert', "Please input a number\n") 

def clean():
    show_text.delete("1.0",tk.END)

### Window
window = tk.Tk()
window.title('Guess Game')
window.geometry("285x250")

### Variable
key = tk.IntVar()
key.set(-1)
l = tk.IntVar()
h = tk.IntVar()
flag = tk.IntVar()
flag.set(-1)

### Entry
entry = tk.Entry(window,     # 輸入欄位所在視窗
                 width = 7) # 輸入欄位的寬度
entry.place(x = 10, y = 10)

### Button 1
button1 = tk.Button(window,          # 按鈕所在視窗
                   text = 'Guess',  # 顯示文字
                   command = guess_compute) # 按下按鈕所執行的函數
button1.place(x = 100, y = 9)

### Button 2
button2 = tk.Button(window,          # 按鈕所在視窗
                   text = 'Set Game',  # 顯示文字
                   command = set_game) # 按下按鈕所執行的函數
button2.place(x = 180, y = 9)

### Button 3
button3 = tk.Button(window,          # 按鈕所在視窗
                   text = 'Clean',  # 顯示文字
                   command = clean) # 按下按鈕所執行的函數
button3.place(x = 10, y = 210)

### label
mylabel = tk.Label(window, text='This game is made by Steven-YiTseWu', font=("Times", 12, "italic"))
mylabel.pack()
mylabel.place(x = 87, y = 214)

### Frame
show_text = tk.Text(window, height = 11, width = 37)
show_text.place(x = 10, y = 50)

window.mainloop()