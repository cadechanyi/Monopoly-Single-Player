from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk

gui = Tk()
gui.geometry("950x750")
gui.title('Monkopoly')

frame = Frame(gui, width=2000, height=2000)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)
#boardimg0 = ImageTk.PhotoImage(Image.open('monboard14.jpg'))
boardimg = Image.open('Images//finalboard.png')
image2 = boardimg.resize((737, 738),Image.BICUBIC)
boardimg2=ImageTk.PhotoImage(image2)
tradeboard = boardimg.resize((600, 600),Image.BICUBIC)
tradeboard2 = ImageTk.PhotoImage(tradeboard)
boardlabel = Label(frame, image = boardimg2)
boardlabel.pack()
bluemoney = tk.PhotoImage(file='Images//monkeymoneycokeb.png')
bluemoneylb = tk.Label(gui, image=bluemoney)
bluemoneylb.place(x=1, y=1)
bimg = Image.open('Images//monkeyfaceblue4.png')
bimg2 = bimg.resize((65, 60),Image.BICUBIC)
bbut = PhotoImage(file='Images//monkeyfaceblue4.png')
bimg3=ImageTk.PhotoImage(bimg2)
blabel = Label(gui, image = bimg3)
blabel.place(x=18, y=20)
redmoney = tk.PhotoImage(file='Images//monkeymoneyr4.png')
redmoneylb = tk.Label(gui, image=redmoney)
redmoneylb.place(x=1, y=626)
rimg = Image.open('Images//newmonred.png')
rimg2 = rimg.resize((65, 60),Image.BICUBIC)
rimg3=ImageTk.PhotoImage(rimg2)
rlabel = Label(gui, image = rimg3)
rlabel.place(x=18, y=646)
greenmoney = tk.PhotoImage(file='Images//monkeymoneyg4.png')
greenmoneylb = tk.Label(gui, image=greenmoney)
greenmoneylb.place(x=845, y=1)
gimg = Image.open('Images//newmongreen.png')
gimg2 = gimg.resize((65, 60),Image.BICUBIC)
gimg3=ImageTk.PhotoImage(gimg2)
glabel = Label(gui, image = gimg3)
glabel.place(x=863, y=20)
pinkmoney = tk.PhotoImage(file='Images//monkeymoneyp4.png')
pinkmoneylb = tk.Label(gui, image=pinkmoney)
pinkmoneylb.place(x=845, y=626)
pimg = Image.open('Images//newmonpink.png')
pimg2 = pimg.resize((65, 60),Image.BICUBIC)
pimg3=ImageTk.PhotoImage(pimg2)
plabel = Label(gui, image = pimg3)
plabel.place(x=863, y=646)

monblueimg = tk.PhotoImage(file='Images//monkeyfaceblue4.png')
mongreenimg = tk.PhotoImage(file='Images//newmongreen.png')
monredimg = tk.PhotoImage(file='Images//newmonred.png')
monpinkimg = tk.PhotoImage(file='Images//newmonpink.png')
monbluelabel = tk.Label(frame, image = monblueimg)
monbluelabel.place(x = '640', y = '715')
mongreenlabel = Label(frame, image=mongreenimg)
mongreenlabel.place(x = '640', y = '690')
monredlabel = Label(frame, image=monredimg)
monredlabel.place(x = '640', y = '665')
monpinklabel = Label(frame, image=monpinkimg)
monpinklabel.place(x = '640', y = '640')

bmoneyvallb = Label(gui, height = 1, width=4, text='1500', font=('Cooper Std Black', 24), bg='blue', fg='white')
bmoneyvallb.place(x=22, y=84)
rmoneyvallb = Label(gui, height = 1, width=4, text='1500', font=('Cooper Std Black', 24), bg='red', fg='white')
rmoneyvallb.place(x=22, y=710)
gmoneyvallb = Label(gui, height = 1, width=4, text='1500', font=('Cooper Std Black', 24), bg='#28DC28', fg='white')
gmoneyvallb.place(x=868, y=84)
pmoneyvallb = Label(gui, height = 1, width=4, text='1500', font=('Cooper Std Black', 24), bg='#C525E2', fg='white')
pmoneyvallb.place(x=868, y=710)

dice1img = tk.PhotoImage(file='Images//dice1.png')
dice1lb = tk.Label(gui, image=dice1img)
dice1lb2 = tk.Label(gui, image=dice1img)
dice2img = tk.PhotoImage(file='Images//dice2.png')
dice2lb = tk.Label(gui, image=dice2img)
dice2lb2 = tk.Label(gui, image=dice2img)
dice3img = tk.PhotoImage(file='Images//dice3.png')
dice3lb = tk.Label(gui, image=dice3img)
dice3lb2 = tk.Label(gui, image=dice3img)
dice4img = tk.PhotoImage(file='Images//dice4.png')
dice4lb = tk.Label(gui, image=dice4img)
dice4lb2 = tk.Label(gui, image=dice4img)
dice5img = tk.PhotoImage(file='Images//dice5.png')
dice5lb = tk.Label(gui, image=dice5img)
dice5lb2 = tk.Label(gui, image=dice5img)
dice6img = tk.PhotoImage(file='Images//dice6.png')
dice6lb = tk.Label(gui, image=dice6img)
dice6lb2 = tk.Label(gui, image=dice6img)

dice1lblist = [dice1lb, dice2lb, dice3lb, dice4lb, dice5lb, dice6lb]
dice2lblist = [dice1lb2, dice2lb2, dice3lb2, dice4lb2, dice5lb2, dice6lb2]

doubleslb = Label(gui, text='', height =1, width=16, bg='#D5E8D4', fg='green', font=('Cooper Std Black', 30))
doubleslb.place(x=400, y =142)

cashlb = Label(gui, text='', height =1, width=10, bg='#D5E8D4', fg='red', font=('Cooper Std Black', 30))
cashlb.place(x=472, y =540)



caledonimg = tk.PhotoImage(file='Images//caledon.png')
miltonimg = tk.PhotoImage(file='Images//milton.png')
angolaimg = tk.PhotoImage(file='Images//angola.png')
somaliaimg = tk.PhotoImage(file='Images//somalia.png')
chadimg = tk.PhotoImage(file='Images//chad.png')
scarboroughimg = tk.PhotoImage(file='Images//scarborough.png')
markhamimg = tk.PhotoImage(file='Images//Markham.png')
primarycampusimg = tk.PhotoImage(file='Images//primarycampus.png')
gcpimg = tk.PhotoImage(file='Images//gcp.png')
mentorlobbyimg = tk.PhotoImage(file='Images//mentorlobby.png')
bhavbarnimg = tk.PhotoImage(file='Images//bhavbarn.png')
mentorgymimg = tk.PhotoImage(file='Images//mentorgym.png')
northkoreaimg = tk.PhotoImage(file='Images//northkorea.png')
mentorofficeimg = tk.PhotoImage(file='Images//mentoroffice.png')
yehiapyramidimg = tk.PhotoImage(file='Images//yehiapyramid.png')
egyptimg = tk.PhotoImage(file='Images//egypt.png')
landdownunderimg = tk.PhotoImage(file='Images//landdownunder.png')
evancampimg = tk.PhotoImage(file='Images//evancamp.png')
greenwoodimg = tk.PhotoImage(file='Images//greenwood.png')
oakvilleimg = tk.PhotoImage(file='Images//oakville.png')
crystalcoveimg = tk.PhotoImage(file='Images//crystalcove.png')
jungleofmonkeysimg = tk.PhotoImage(file='Images//jungleofmonkeys.png')
smithbusimg = tk.PhotoImage(file='Images//smithbus.png')
waynebusimg = tk.PhotoImage(file='Images//waynebus.png')
danbusimg = tk.PhotoImage(file='Images//danbus.png')
jeffbusimg = tk.PhotoImage(file='Images//jeffbus.png')
pepsicompanyimg = tk.PhotoImage(file='Images//pepsicompany.png')
cokecompanyimg = tk.PhotoImage(file='Images//cokecompany.png')

#allactivelineslist = []

managegui = tk.Toplevel()
managegui.geometry("1240x692")
managegui.title('manage')
managegui.withdraw()

caledonimg2 = Image.open('Images//caledon.png')
caledonimg3 = caledonimg2.resize((150, 172),Image.BICUBIC)
caledonimg4=ImageTk.PhotoImage(caledonimg3)
caledonsmalllb = tk.Label(managegui, image=caledonimg4)

miltonimg2 = Image.open('Images//milton.png')
miltonimg3 = miltonimg2.resize((150, 172),Image.BICUBIC)
miltonimg4=ImageTk.PhotoImage(miltonimg3)
miltonsmalllb = tk.Label(managegui, image=miltonimg4)

angolaimg2 = Image.open('Images//angola.png')
angolaimg3 = angolaimg2.resize((150, 172),Image.BICUBIC)
angolaimg4=ImageTk.PhotoImage(angolaimg3)
angolasmalllb = tk.Label(managegui, image=angolaimg4)

somaliaimg2 = Image.open('Images//somalia.png')
somaliaimg3 = somaliaimg2.resize((150, 172),Image.BICUBIC)
somaliaimg4=ImageTk.PhotoImage(somaliaimg3)
somaliasmalllb = tk.Label(managegui, image=somaliaimg4)

chadimg2 = Image.open('Images//chad.png')
chadimg3 = chadimg2.resize((150, 172),Image.BICUBIC)
chadimg4=ImageTk.PhotoImage(chadimg3)
chadsmalllb = tk.Label(managegui, image=chadimg4)

scarboroughimg2 = Image.open('Images//scarborough.png')
scarboroughimg3 = scarboroughimg2.resize((150, 172),Image.BICUBIC)
scarboroughimg4=ImageTk.PhotoImage(scarboroughimg3)
scarboroughsmalllb = tk.Label(managegui, image=scarboroughimg4)

markhamimg2 = Image.open('Images//Markham.png')
markhamimg3 = markhamimg2.resize((150, 172),Image.BICUBIC)
markhamimg4=ImageTk.PhotoImage(markhamimg3)
markhamsmalllb = tk.Label(managegui, image=markhamimg4)

primarycampusimg2 = Image.open('Images//primarycampus.png')
primarycampusimg3 = primarycampusimg2.resize((150, 172),Image.BICUBIC)
primarycampusimg4=ImageTk.PhotoImage(primarycampusimg3)
primarycampussmalllb = tk.Label(managegui, image=primarycampusimg4)

gcpimg2 = Image.open('Images//gcp.png')
gcpimg3 = gcpimg2.resize((150, 172),Image.BICUBIC)
gcpimg4=ImageTk.PhotoImage(gcpimg3)
gcpsmalllb = tk.Label(managegui, image=gcpimg4)

mentorlobbyimg2 = Image.open('Images//mentorlobby.png')
mentorlobbyimg3 = mentorlobbyimg2.resize((150, 172),Image.BICUBIC)
mentorlobbyimg4=ImageTk.PhotoImage(mentorlobbyimg3)
mentorlobbysmalllb = tk.Label(managegui, image=mentorlobbyimg4)

bhavbarnimg2 = Image.open('Images//bhavbarn.png')
bhavbarnimg3 = bhavbarnimg2.resize((150, 172),Image.BICUBIC)
bhavbarnimg4=ImageTk.PhotoImage(bhavbarnimg3)
bhavbarnsmalllb = tk.Label(managegui, image=bhavbarnimg4)

mentorgymimg2 = Image.open('Images//mentorgym.png')
mentorgymimg3 = mentorgymimg2.resize((150, 172),Image.BICUBIC)
mentorgymimg4=ImageTk.PhotoImage(mentorgymimg3)
mentorgymsmalllb = tk.Label(managegui, image=mentorgymimg4)

northkoreaimg2 = Image.open('Images//northkorea.png')
northkoreaimg3 = northkoreaimg2.resize((150, 172),Image.BICUBIC)
northkoreaimg4=ImageTk.PhotoImage(northkoreaimg3)
northkoreasmalllb = tk.Label(managegui, image=northkoreaimg4)

mentorofficeimg2 = Image.open('Images//mentoroffice.png')
mentorofficeimg3 = mentorofficeimg2.resize((150, 172),Image.BICUBIC)
mentorofficeimg4=ImageTk.PhotoImage(mentorofficeimg3)
mentorofficesmalllb = tk.Label(managegui, image=mentorofficeimg4)

yehiapyramidimg2 = Image.open('Images//yehiapyramid.png')
yehiapyramidimg3 = yehiapyramidimg2.resize((150, 172),Image.BICUBIC)
yehiapyramidimg4=ImageTk.PhotoImage(yehiapyramidimg3)
yehiapyramidsmalllb = tk.Label(managegui, image=yehiapyramidimg4)

egyptimg2 = Image.open('Images//egypt.png')
egyptimg3 = egyptimg2.resize((150, 172),Image.BICUBIC)
egyptimg4=ImageTk.PhotoImage(egyptimg3)
egyptsmalllb = tk.Label(managegui, image=egyptimg4)

landdownunderimg2 = Image.open('Images//landdownunder.png')
landdownunderimg3 = landdownunderimg2.resize((150, 172),Image.BICUBIC)
landdownunderimg4=ImageTk.PhotoImage(landdownunderimg3)
landdownundersmalllb = tk.Label(managegui, image=landdownunderimg4)

evancampimg2 = Image.open('Images//evancamp.png')
evancampimg3 = evancampimg2.resize((150, 172),Image.BICUBIC)
evancampimg4=ImageTk.PhotoImage(evancampimg3)
evancampsmalllb = tk.Label(managegui, image=evancampimg4)

greenwoodimg2 = Image.open('Images//greenwood.png')
greenwoodimg3 = greenwoodimg2.resize((150, 172),Image.BICUBIC)
greenwoodimg4=ImageTk.PhotoImage(greenwoodimg3)
greenwoodsmalllb = tk.Label(managegui, image=greenwoodimg4)

oakvilleimg2 = Image.open('Images//oakville.png')
oakvilleimg3 = oakvilleimg2.resize((150, 172),Image.BICUBIC)
oakvilleimg4=ImageTk.PhotoImage(oakvilleimg3)
oakvillesmalllb = tk.Label(managegui, image=oakvilleimg4)

crystalcoveimg2 = Image.open('Images//crystalcove.png')
crystalcoveimg3 = crystalcoveimg2.resize((150, 172),Image.BICUBIC)
crystalcoveimg4=ImageTk.PhotoImage(crystalcoveimg3)
crystalcovesmalllb = tk.Label(managegui, image=crystalcoveimg4)

jungleofmonkeysimg2 = Image.open('Images//jungleofmonkeys.png')
jungleofmonkeysimg3 = jungleofmonkeysimg2.resize((150, 172),Image.BICUBIC)
jungleofmonkeysimg4=ImageTk.PhotoImage(jungleofmonkeysimg3)
jungleofmonkeyssmalllb = tk.Label(managegui, image=jungleofmonkeysimg4)

smithbusimg2 = Image.open('Images//smithbus.png')
smithbusimg3 = smithbusimg2.resize((150, 172),Image.BICUBIC)
smithbusimg4=ImageTk.PhotoImage(smithbusimg3)
smithbussmalllb = tk.Label(managegui, image=smithbusimg4)

waynebusimg2 = Image.open('Images//waynebus.png')
waynebusimg3 = waynebusimg2.resize((150, 172),Image.BICUBIC)
waynebusimg4=ImageTk.PhotoImage(waynebusimg3)
waynebussmalllb = tk.Label(managegui, image=waynebusimg4)

danbusimg2 = Image.open('Images//danbus.png')
danbusimg3 = danbusimg2.resize((150, 172),Image.BICUBIC)
danbusimg4=ImageTk.PhotoImage(danbusimg3)
danbussmalllb = tk.Label(managegui, image=danbusimg4)

jeffbusimg2 = Image.open('Images//jeffbus.png')
jeffbusimg3 = jeffbusimg2.resize((150, 172),Image.BICUBIC)
jeffbusimg4=ImageTk.PhotoImage(jeffbusimg3)
jeffbussmalllb = tk.Label(managegui, image=jeffbusimg4)

pepsicompanyimg2 = Image.open('Images//pepsicompany.png')
pepsicompanyimg3 = pepsicompanyimg2.resize((150, 172),Image.BICUBIC)
pepsicompanyimg4=ImageTk.PhotoImage(pepsicompanyimg3)
pepsicompanysmalllb = tk.Label(managegui, image=pepsicompanyimg4)

cokecompanyimg2 = Image.open('Images//cokecompany.png')
cokecompanyimg3 = cokecompanyimg2.resize((150, 172),Image.BICUBIC)
cokecompanyimg4=ImageTk.PhotoImage(cokecompanyimg3)
cokecompanysmalllb = tk.Label(managegui, image=cokecompanyimg4)

trade_gui = tk.Toplevel()
trade_gui.geometry('1240x490')
trade_gui.title('Trade')
#trade_gui.wm_protocol("WM_DELETE_WINDOW", noclose)
#trade_gui.resizable(False, False)
explanation_label = Label(trade_gui, text='Press on a Coloured Rectangle above property to add that property to the trade')
explanation_label2 = Label(trade_gui, text='Dark Colours are in the trade, light colors cannot be in the trade as they belong to players outside the current trade')
tradefromlb = Label(trade_gui, text='Give Properties', font=('Cooper Std Black', 13))
tradetolb = Label(trade_gui, text='Get Properties', font=('Cooper Std Black', 13))
tradeline = Label(trade_gui, bg='black', height=1, width=180)
trade_gui.withdraw()

caledontradelb = tk.Label(trade_gui, image=caledonimg4)
miltontradelb = tk.Label(trade_gui, image=miltonimg4)
angolatradelb = tk.Label(trade_gui, image=angolaimg4)
somaliatradelb = tk.Label(trade_gui, image=somaliaimg4)
chadtradelb = tk.Label(trade_gui, image=chadimg4)
scarboroughtradelb = tk.Label(trade_gui, image=scarboroughimg4)
markhamtradelb = tk.Label(trade_gui, image=markhamimg4)
primarycampustradelb = tk.Label(trade_gui, image=primarycampusimg4)
gcptradelb = tk.Label(trade_gui, image=gcpimg4)
mentorlobbytradelb = tk.Label(trade_gui, image=mentorlobbyimg4)
bhavbarntradelb = tk.Label(trade_gui, image=bhavbarnimg4)
mentorgymtradelb = tk.Label(trade_gui, image=mentorgymimg4)
northkoreatradelb = tk.Label(trade_gui, image=northkoreaimg4)
mentorofficetradelb = tk.Label(trade_gui, image=mentorofficeimg4)
yehiapyramidtradelb = tk.Label(trade_gui, image=yehiapyramidimg4)
egypttradelb = tk.Label(trade_gui, image=egyptimg4)
landdownundertradelb = tk.Label(trade_gui, image=landdownunderimg4)
evancamptradelb = tk.Label(trade_gui, image=evancampimg4)
greenwoodtradelb = tk.Label(trade_gui, image=greenwoodimg4)
oakvilletradelb = tk.Label(trade_gui, image=oakvilleimg4)
crystalcovetradelb = tk.Label(trade_gui, image=crystalcoveimg4)
jungleofmonkeystradelb = tk.Label(trade_gui, image=jungleofmonkeysimg4)
pepsicompanytradelb = tk.Label(trade_gui, image=pepsicompanyimg4)
cokecompanytradelb = tk.Label(trade_gui, image=cokecompanyimg4)
waynebustradelb = tk.Label(trade_gui, image=waynebusimg4)
jeffbustradelb = tk.Label(trade_gui, image=jeffbusimg4)
smithbustradelb = tk.Label(trade_gui, image=smithbusimg4)
danbustradelb = tk.Label(trade_gui, image=danbusimg4)

line_dictionary = {
    1: Label(frame, height=1, width=5),
    3: Label(frame, height=1, width=5),
    5: Label(frame, height=1, width=5),
    6: Label(frame, height=1, width=5),
    8: Label(frame, height=1, width=5),
    9: Label(frame, height=1, width=5),
    21: Label(frame, height=1, width=5),
    23: Label(frame, height=1, width=5),
    24: Label(frame, height=1, width=5),
    25: Label(frame, height=1, width=5),
    26: Label(frame, height=1, width=5),
    27: Label(frame, height=1, width=5),
    28: Label(frame, height=1, width=5),
    29: Label(frame, height=1, width=5),
    11: Label(frame, height=3, width=1),
    12: Label(frame, height=3, width=1),
    13: Label(frame, height=3, width=1),
    14: Label(frame, height=3, width=1),
    15: Label(frame, height=3, width=1),
    16: Label(frame, height=3, width=1),
    18: Label(frame, height=3, width=1),
    19: Label(frame, height=3, width=1),
    31: Label(frame, height=3, width=1),
    32: Label(frame, height=3, width=1),
    34: Label(frame, height=3, width=1),
    35: Label(frame, height=3, width=1),
    37: Label(frame, height=3, width=1),
    39: Label(frame, height=3, width=1),
}

mortgaged_line_dictionary = {
    1: Label(frame, text='mortgaged', width=7, font=('Cooper Std Black', 10), bg='red'),
    3: Label(frame, text='mortgaged', width=7, font=('Cooper Std Black', 10), bg='red'),
    5: Label(frame, text='mortgaged', width=7, font=('Cooper Std Black', 10), bg='red'),
    6: Label(frame, text='mortgaged', width=7, font=('Cooper Std Black', 10), bg='red'),
    8: Label(frame, text='mortgaged', width=7, font=('Cooper Std Black', 10), bg='red'),
    9: Label(frame, text='mortgaged', width=7, font=('Cooper Std Black', 10), bg='red'),
    21: Label(frame, text='mortgaged', width=7, font=('Cooper Std Black', 10), bg='red'),
    23: Label(frame, text='mortgaged', width=7, font=('Cooper Std Black', 10), bg='red'),
    24: Label(frame, text='mortgaged', width=7, font=('Cooper Std Black', 10), bg='red'),
    25: Label(frame, text='mortgaged', width=7, font=('Cooper Std Black', 10), bg='red'),
    26: Label(frame, text='mortgaged', width=7, font=('Cooper Std Black', 10), bg='red'),
    27: Label(frame, text='mortgaged', width=7, font=('Cooper Std Black', 10), bg='red'),
    28: Label(frame, text='mortgaged', width=7, font=('Cooper Std Black', 10), bg='red'),
    29: Label(frame, text='mortgaged', width=7, font=('Cooper Std Black', 10), bg='red'),
    11: Label(frame, text='mortgaged', width=10, font=('Cooper Std Black', 12), bg='red'),
    12: Label(frame, text='mortgaged', width=10, font=('Cooper Std Black', 12), bg='red'),
    13: Label(frame, text='mortgaged', width=10, font=('Cooper Std Black', 12), bg='red'),
    14: Label(frame, text='mortgaged', width=10, font=('Cooper Std Black', 12), bg='red'),
    15: Label(frame, text='mortgaged', width=10, font=('Cooper Std Black', 12), bg='red'),
    16: Label(frame, text='mortgaged', width=10, font=('Cooper Std Black', 12), bg='red'),
    18: Label(frame, text='mortgaged', width=10, font=('Cooper Std Black', 12), bg='red'),
    19: Label(frame, text='mortgaged', width=10, font=('Cooper Std Black', 12), bg='red'),
    31: Label(frame, text='mortgaged', width=10, font=('Cooper Std Black', 12), bg='red'),
    32: Label(frame, text='mortgaged', width=10, font=('Cooper Std Black', 12), bg='red'),
    34: Label(frame, text='mortgaged', width=10, font=('Cooper Std Black', 12), bg='red'),
    35: Label(frame, text='mortgaged', width=10, font=('Cooper Std Black', 12), bg='red'),
    37: Label(frame, text='mortgaged', width=10, font=('Cooper Std Black', 12), bg='red'),
    39: Label(frame, text='mortgaged', width=10, font=('Cooper Std Black', 12), bg='red'),
}

def testfunc():
    pass

Controlgui = Tk()
Controlgui.geometry('350x200+300+300')
Controlgui.title('Player Controls')

smalllbcord_dictionary = {
    1: [0, 0, 26, 175, 10, 80, 202],
    2: [155, 0, 181, 175, 165, 235, 202],
    3: [310, 0, 336, 175, 320, 390, 202],
    4: [465, 0, 491, 175, 475, 545, 202],
    5: [620, 0, 646, 175, 630, 700, 202],
    6: [775, 0, 801, 175, 785, 855, 202],
    7: [930, 0, 956, 175, 940, 1010, 202],
    8: [1085, 0, 1111, 175, 1095, 1165, 202],

    9: [0, 228, 26, 403, 10, 80, 430],
    10: [155, 228, 181, 403, 165, 235, 430],
    11: [310, 228, 336, 403, 320, 390, 430],
    12: [465, 228, 491, 403, 475, 545, 430],
    13: [620, 228, 646, 403, 630, 700, 430],
    14: [775, 228, 801, 403, 785, 855, 430],
    15: [930, 228, 956, 403, 940, 1010, 430],
    16: [1085, 228, 1111, 403, 1095, 1165, 430],

    17: [0, 456, 26, 631, 10, 80, 658],
    18: [155, 456, 181, 631, 165, 235, 658],
    19: [310, 456, 336, 631, 320, 390, 658],
    20: [465, 456, 491, 631, 475, 545, 658],
    21: [620, 456, 646, 631, 630, 700, 658],
    22: [775, 456, 801, 631, 785, 855, 658],
    23: [930, 456, 956, 631, 940, 1010, 658],
    24: [1085, 456, 1111, 631, 1095, 1165, 658]

}

tree1img = tk.PhotoImage(file='Images//1tree.png')
tree190img = tk.PhotoImage(file='Images//1tree90.png')
tree2img = tk.PhotoImage(file='Images//2tree_2.png')
tree290img = tk.PhotoImage(file='Images//2tree90_2.png')
tree3img = tk.PhotoImage(file='Images//3tree_2.png')
tree390img = tk.PhotoImage(file='Images//3tree90_2.png')
tree4img = tk.PhotoImage(file='Images//4tree_2.png')
tree490img = tk.PhotoImage(file='Images//4tree90_2.png')
hotelimg = tk.PhotoImage(file='Images//hotel4.png')
hotel90img = tk.PhotoImage(file='Images//hotel490.png')

houses_dictionary = {
    1: [tk.Label(gui, image=tree190img), tk.Label(gui, image=tree290img), tk.Label(gui, image=tree390img), tk.Label(gui, image=tree490img), tk.Label(gui, image=hotel90img)],
    3: [tk.Label(gui, image=tree190img), tk.Label(gui, image=tree290img), tk.Label(gui, image=tree390img), tk.Label(gui, image=tree490img), tk.Label(gui, image=hotel90img)],
    6: [tk.Label(gui, image=tree190img), tk.Label(gui, image=tree290img), tk.Label(gui, image=tree390img), tk.Label(gui, image=tree490img), tk.Label(gui, image=hotel90img)],
    8: [tk.Label(gui, image=tree190img), tk.Label(gui, image=tree290img), tk.Label(gui, image=tree390img), tk.Label(gui, image=tree490img), tk.Label(gui, image=hotel90img)],
    9: [tk.Label(gui, image=tree190img), tk.Label(gui, image=tree290img), tk.Label(gui, image=tree390img), tk.Label(gui, image=tree490img), tk.Label(gui, image=hotel90img)],
    21: [tk.Label(gui, image=tree190img), tk.Label(gui, image=tree290img), tk.Label(gui, image=tree390img), tk.Label(gui, image=tree490img), tk.Label(gui, image=hotel90img)],
    23: [tk.Label(gui, image=tree190img), tk.Label(gui, image=tree290img), tk.Label(gui, image=tree390img), tk.Label(gui, image=tree490img), tk.Label(gui, image=hotel90img)],
    24: [tk.Label(gui, image=tree190img), tk.Label(gui, image=tree290img), tk.Label(gui, image=tree390img), tk.Label(gui, image=tree490img), tk.Label(gui, image=hotel90img)],
    26: [tk.Label(gui, image=tree190img), tk.Label(gui, image=tree290img), tk.Label(gui, image=tree390img), tk.Label(gui, image=tree490img), tk.Label(gui, image=hotel90img)],
    27: [tk.Label(gui, image=tree190img), tk.Label(gui, image=tree290img), tk.Label(gui, image=tree390img), tk.Label(gui, image=tree490img), tk.Label(gui, image=hotel90img)],
    29: [tk.Label(gui, image=tree190img), tk.Label(gui, image=tree290img), tk.Label(gui, image=tree390img), tk.Label(gui, image=tree490img), tk.Label(gui, image=hotel90img)],
    11: [tk.Label(gui, image=tree1img), tk.Label(gui, image=tree2img), tk.Label(gui, image=tree3img), tk.Label(gui, image=tree4img), tk.Label(gui, image=hotelimg)],
    13: [tk.Label(gui, image=tree1img), tk.Label(gui, image=tree2img), tk.Label(gui, image=tree3img), tk.Label(gui, image=tree4img), tk.Label(gui, image=hotelimg)],
    14: [tk.Label(gui, image=tree1img), tk.Label(gui, image=tree2img), tk.Label(gui, image=tree3img), tk.Label(gui, image=tree4img), tk.Label(gui, image=hotelimg)],
    16: [tk.Label(gui, image=tree1img), tk.Label(gui, image=tree2img), tk.Label(gui, image=tree3img), tk.Label(gui, image=tree4img), tk.Label(gui, image=hotelimg)],
    18: [tk.Label(gui, image=tree1img), tk.Label(gui, image=tree2img), tk.Label(gui, image=tree3img), tk.Label(gui, image=tree4img), tk.Label(gui, image=hotelimg)],
    19: [tk.Label(gui, image=tree1img), tk.Label(gui, image=tree2img), tk.Label(gui, image=tree3img), tk.Label(gui, image=tree4img), tk.Label(gui, image=hotelimg)],
    31: [tk.Label(gui, image=tree1img), tk.Label(gui, image=tree2img), tk.Label(gui, image=tree3img), tk.Label(gui, image=tree4img), tk.Label(gui, image=hotelimg)],
    32: [tk.Label(gui, image=tree1img), tk.Label(gui, image=tree2img), tk.Label(gui, image=tree3img), tk.Label(gui, image=tree4img), tk.Label(gui, image=hotelimg)],
    34: [tk.Label(gui, image=tree1img), tk.Label(gui, image=tree2img), tk.Label(gui, image=tree3img), tk.Label(gui, image=tree4img), tk.Label(gui, image=hotelimg)],
    37: [tk.Label(gui, image=tree1img), tk.Label(gui, image=tree2img), tk.Label(gui, image=tree3img), tk.Label(gui, image=tree4img), tk.Label(gui, image=hotelimg)],
    39: [tk.Label(gui, image=tree1img), tk.Label(gui, image=tree2img), tk.Label(gui, image=tree3img), tk.Label(gui, image=tree4img), tk.Label(gui, image=hotelimg)],
}

gui.resizable(False, False)
def noclose():
    pass
gui.wm_protocol("WM_DELETE_WINDOW", noclose)

def bind_button(event):
    print('clicked')
    print(' ')
    print(' ')


#houses_dictionary[1][4].place(x=588+92, y=715-80)
#houses_dictionary[11][4].place(x=5+194, y=590-12)
#houses_dictionary[21][4].place(x=136+85, y=5+90)
#houses_dictionary[31][4].place(x=710+28, y=132-15)

#players turn gui with controls

#rollbut['state'] = DISABLED

#Controlgui = Tk()
