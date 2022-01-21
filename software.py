from data_class import Player, Weapon
import tkinter as tk

line = "_____________________________________________________________________________________________________"

window = tk.Tk()
window.geometry("800x500")
window.title("Weapon Simulator")
window.resizable(False, False)

p1_shown = False
p2_shown = False

def p1_show():
    global p1_shown

    if p1_shown:
        Damage1Button.place_forget()
        p1_shown = False
    else:
        Damage1Button.place(x=150, y=175)
        p1_shown = True

def p2_show(player="p2"):
    global p2_shown

    if p2_shown:
        Damage2Button.place_forget()
        p2_shown = False
    else:
        Damage2Button.place(x=550, y=175)
        p2_shown = True

p1 = Player()
p2 = Player()

gun = Weapon(dmg=50)

def change_slider(slider, value):
    slider.configure(state='normal')
    slider.set(value)
    slider.configure(state='disabled')

def p1_takedamage():
    p1.take_damage(gun)

    change_slider(Hp1Slider, p1.get_hp())
    change_slider(Shield1Slider, p1.get_shield())

ProgName = tk.Label(window, font=('Comic Sans MS',30,'bold'),text="Weapon Simulator", fg="yellow")
ProgName.place(x=400,y=470,anchor="center")

LineLabel = tk.Label(window, font=('Comic Sans MS',50,'bold'),text=line)
LineLabel.place(x=400,y=400, anchor="center")

P1Button = tk.Button(window,text="P1",height=1, width=7,font=('Comic Sans MS',15,'bold'), command=p1_show)
P1Button.place(x=50,y=100)

Hp1Slider = tk.Scale(window, from_=0,to=100,orient='horizontal',width=15)
Hp1Slider.configure(state='disabled')
Hp1Slider.place(x=45,y=150)

HpLabel = tk.Label(window, font=('Comic Sans MS',15,'bold'),text="Hp:")
HpLabel.place(x=20,y=175, anchor="center")

Damage1Button = tk.Button(window,text="Damage", width=7,font=('Comic Sans MS',15,'bold'))

Shield1Slider = tk.Scale(window, from_=0,to=100,orient='horizontal',width=15)
Shield1Slider.configure(state='disabled')
Shield1Slider.place(x=45,y=200)

ShieldLabel = tk.Label(window, font=('Comic Sans MS',9,'bold'),text="Shield:")
ShieldLabel.place(x=23,y=228, anchor="center")

P2Button = tk.Button(window,text="P2",height=1, width=7,font=('Comic Sans MS',15,'bold'), command=p2_show)
P2Button.place(x=650,y=100)

Hp2Slider = tk.Scale(window, from_=0,to=100,orient='horizontal',width=15)
Hp2Slider.configure(state='disabled')
Hp2Slider.place(x=645,y=150)

Shield2Slider = tk.Scale(window, from_=0,to=100,orient='horizontal',width=15)
Shield2Slider.configure(state='disabled')
Shield2Slider.place(x=645,y=200)

Damage2Button = tk.Button(window,text="Damage", width=7,font=('Comic Sans MS',15,'bold'), command=p1_takedamage)

window.mainloop()
