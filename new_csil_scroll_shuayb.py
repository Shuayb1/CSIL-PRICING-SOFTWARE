from tkinter import *
# from stringvariables import *
# from functionalties import *
from tkinter import messagebox, StringVar
import tkinter as tk

bg_orange = bg='#FF7F50'
root=Tk()
sizex = 1200
sizey = 800
posx  = 0
posy  = 0
root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
root.configure(bg='#000')
myframe=Frame(root,width=50,height=100,bd=0)
myframe.place(x=10,y=10)

canvas=Canvas(myframe)
canvas.configure(bg=bg_orange)
frame=Frame(canvas)
frame.configure(bg=bg_orange)
myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

calculate_button, replacement_charge_label,generate_button,more_row_entry,replacement_charge_value,current_end_row,end = '','','','','',6,0



# page.configure(bg='#FF7F50')
dana_list, open_list, foreign_list = [], [], []
space_one, error_label, total_dana_price_label, total_dana_price_entry, tw_percent_total_dana_label, tw_percent_total_dana_entry = '','','','','',''
total_open_price_label,total_open_price_entry, total_open_price_plus_label,total_open_price_plus_entry, fiv_percent_total_plus_open_label, fiv_percent_total_plus_open_entry, sev_percent_total_plus_open_plus_label, sev_percent_total_plus_open_plus_entry='','','','','','','',''
vat_total_dana_price_label,vat_total_dana_price_entry,vat_total_open_price_in_two_label,vat_total_open_price_in_two_entry,vat_fifty_perc_total_open_price_label,vat_fifty_perc_total_open_price_entry,vat_seventy_five_perc_total_open_price_label,vat_seventy_five_perc_total_open_price_entry= '','','','','','','',''
final_total_of_total_dana_price_label,final_total_of_total_dana_price_entry,final_total_of_total_open_price_label,final_total_of_total_open_price_entry,final_total_of_total_fifty_perc_open_price_label,final_total_of_total_fifty_perc_open_price_entry,final_total_of_total_seventy_five_perc_open_price_label,final_total_of_total_seventy_five_perc_open_price_entry = '','','','', '','','',''


name_0_value,name_1_value,name_2_value,name_3_value,name_4_value = StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
more_row_value,replacement_charge_value = StringVar(),StringVar()
dana_0_value,dana_1_value,dana_2_value,dana_3_value,dana_4_value = StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
foreign_0_value,foreign_1_value,foreign_2_value,foreign_3_value,foreign_4_value, = StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
open_0_value,open_1_value,open_2_value,open_3_value,open_4_value = StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
error_message = StringVar()

total_dana_price,tw_percent_total_dana,total_open_price,total_open_price_plus_l,sev_percent_total_plus_open_plus_l,fiv_percent_total_plus_open_l = IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),

a_one,a_two,a_three,a_four = IntVar(),IntVar(),IntVar(),IntVar(),

vat_total_dana_price = IntVar()
vat_total_open_price_in_two = IntVar()
vat_fifty_perc_total_open_price = IntVar()
vat_seventy_five_perc_total_open_price = IntVar()
final_total_of_total_dana_price = IntVar()
final_total_of_total_open_price = IntVar()
final_total_of_total_fifty_perc_open_price = IntVar()
final_total_of_total_seventy_five_perc_open_price = IntVar()
page = frame


def generate_initial_interface():
    colspan = 4
    dana_0_value.set(0),more_row_value.set(1),dana_1_value.set(0),dana_2_value.set(0),dana_3_value.set(0),dana_4_value.set(0)
    open_0_value.set(0),open_1_value.set(0),open_2_value.set(0),open_3_value.set(0),open_4_value.set(0),replacement_charge_value.set(0)
    foreign_0_value.set(0),foreign_1_value.set(0),foreign_2_value.set(0),foreign_3_value.set(0),foreign_4_value.set(0)
    global dana_list,open_list,foreign_list
    dana_list = [dana_0_value, dana_1_value, dana_2_value, dana_3_value, dana_4_value]
    open_list = [open_0_value, open_1_value, open_2_value, open_3_value, open_4_value]
    foreign_list = [foreign_0_value, foreign_1_value, foreign_2_value, foreign_3_value, foreign_4_value]

    # headers and spaces
    csil_title = tk.Label(page, bg=bg_orange, font=(18),text='Combined System International Limited (CSIL) Pricing Software', pady=10).grid(row=1, column=3,columnspan=4)
    product_name_label = tk.Label(page, bg=bg_orange, text='Product Name').grid(row=2, column=2)
    dana_price_label = tk.Label(page, bg=bg_orange, text='Dana Price').grid(row=2, column=4)
    froreign_price_label = tk.Label(page, bg=bg_orange, text='Foreign Price').grid(row=2, column=6)
    open_market_price_label = tk.Label(page, bg=bg_orange, text='Open Market Price').grid(row=2, column=8)

    # input fields
    item_number = tk.Label(page, bg=bg_orange, text='Item 1').grid(row=3, column=1)
    product_name = tk.Entry(page,textvariable=name_0_value).grid(row=3, column=2)
    dana_price = tk.Entry(page,textvariable=dana_0_value).grid(row=3, column=4)
    open_price = tk.Entry(page,textvariable=foreign_0_value).grid(row=3, column=6)
    open_market_price = tk.Entry(page,textvariable=open_0_value).grid(row=3, column=8, pady=5)

    item_number = tk.Label(page, bg=bg_orange, text='Item 2').grid(row=4, column=1)
    product_name = tk.Entry(page, textvariable=name_1_value).grid(row=4, column=2)
    dana_price = tk.Entry(page,textvariable=dana_1_value).grid(row=4, column=4)
    foreign_price = tk.Entry(page,textvariable=foreign_1_value).grid(row=4, column=6)
    open_market_price = tk.Entry(page,textvariable=open_1_value).grid(row=4, column=8, pady=5)

    item_number = tk.Label(page, bg=bg_orange, text='Item 3').grid(row=5, column=1)
    product_name = tk.Entry(page, textvariable=name_2_value).grid(row=5, column=2)
    dana_price = tk.Entry(page, textvariable=dana_2_value).grid(row=5, column=4)
    foreign_price = tk.Entry(page, textvariable=foreign_2_value).grid(row=5, column=6)
    open_market_price = tk.Entry(page, textvariable=open_2_value).grid(row=5, column=8, pady=5)

    item_number = tk.Label(page, bg=bg_orange, text='Item 4').grid(row=6, column=1)
    product_name = tk.Entry(page, textvariable=name_3_value).grid(row=6, column=2)
    dana_price = tk.Entry(page,textvariable=dana_3_value).grid(row=6, column=4)
    foreign_price = tk.Entry(page,textvariable=foreign_3_value).grid(row=6, column=6)
    open_market_price = tk.Entry(page,textvariable=open_3_value).grid(row=6, column=8, pady=5)

    item_number = tk.Label(page, bg=bg_orange, text='Item 5').grid(row=7, column=1)
    product_name = tk.Entry(page, textvariable=name_4_value).grid(row=7, column=2)
    dana_price = tk.Entry(page,textvariable=dana_4_value).grid(row=7, column=4)
    foreign_price = tk.Entry(page,textvariable=foreign_4_value).grid(row=7, column=6)
    open_market_price = tk.Entry(page,textvariable=open_4_value).grid(row=7, column=8, pady=5)



    global replacement_charge_button
    global replacement_charge_label
    global calculate_button
    global generate_button
    global more_row_entry

    global space_one
    global error_label
    global total_dana_price_label
    global total_dana_price_entry
    global tw_percent_total_dana_label
    global tw_percent_total_dana_entry
    global total_open_price_label
    global total_open_price_entry
    global total_open_price_plus_label
    global total_open_price_plus_entry
    global fiv_percent_total_plus_open_label
    global fiv_percent_total_plus_open_entry
    global sev_percent_total_plus_open_plus_label
    global sev_percent_total_plus_open_plus_entry
    global vat_total_dana_price_label
    global vat_total_dana_price_entry
    global vat_total_open_price_in_two_label
    global vat_total_open_price_in_two_entry
    global vat_fifty_perc_total_open_price_label
    global vat_fifty_perc_total_open_price_entry
    global vat_seventy_five_perc_total_open_price_label
    global vat_seventy_five_perc_total_open_price_entry
    global final_total_of_total_dana_price_label
    global final_total_of_total_dana_price_entry
    global final_total_of_total_open_price_label
    global final_total_of_total_open_price_entry
    global final_total_of_total_fifty_perc_open_price_label
    global final_total_of_total_fifty_perc_open_price_entry
    global final_total_of_total_seventy_five_perc_open_price_label
    global final_total_of_total_seventy_five_perc_open_price_entry

    f = Frame(page, height=1, width=50, bg="black")
    f.grid(row=8, column=4, pady=2)

    replacement_charge_label = tk.Label(page, bg=bg_orange, pady=8, text='Replacement Charge')
    replacement_charge_label.grid(row=8, column=1,pady=8,)
    replacement_charge_button = tk.Entry(page, textvariable=replacement_charge_value)
    replacement_charge_button.grid(row=8, column=2)



    calculate_button = tk.Button(page, text="    Calculate    ", command=generate_result_interface)
    calculate_button.grid(row=9, column=2)
    more_row_entry = tk.Entry(page, width=3,  textvariable=more_row_value)
    more_row_entry.grid(row=9, column=4,padx=7, sticky=W)
    generate_button = tk.Button(page, text="More rows", command=add_some_more_rows)
    generate_button.grid(row=9, column=4, padx=7, pady=4, sticky=E)

    space_one = tk.Label(page, font=(16), bg=bg_orange, text='RESULTS')
    error_label = tk.Label(page, bg=bg_orange, fg='red', textvariable=error_message)

    total_dana_price_label = tk.Label(page, justify='left',bg=bg_orange, text='Total Dana Price is: ')
    total_dana_price_entry = tk.Entry(page, justify='left', bg='white', textvariable=total_dana_price)

    tw_percent_total_dana_label = tk.Label(page, justify='left',bg=bg_orange, text="22.5% of Total Dana Price is: ")
    tw_percent_total_dana_entry = tk.Entry(page, justify='left', textvariable=tw_percent_total_dana)

    total_open_price_label = tk.Label(page, justify='left',bg=bg_orange, text='Total Open Market Price is: ')
    total_open_price_entry = tk.Entry(page, bg='white', justify='left', textvariable=total_open_price)

    total_open_price_plus_label = tk.Label(page, bg=bg_orange,justify='left', text='Total OP + Total OP  + 22.5% of Total Dana Price is : ')
    total_open_price_plus_entry = tk.Entry(page, bg='white', justify='left', textvariable=total_open_price_plus_l)

    fiv_percent_total_plus_open_label = tk.Label(page, bg=bg_orange, justify='left',text='50% of Total OP + Total OP  + 22.5% of Total Dana Price is : ')
    fiv_percent_total_plus_open_entry = tk.Entry(page, bg='white', justify='left',textvariable=fiv_percent_total_plus_open_l)

    sev_percent_total_plus_open_plus_label = tk.Label(page, bg=bg_orange,justify='left',text='75% of Total OP + Total OP  + 22.5% of Total Dana Price is : ')
    sev_percent_total_plus_open_plus_entry = tk.Entry(page,  justify='left',textvariable=sev_percent_total_plus_open_plus_l)

    #a_one is the summation of the Replacement Charge(RC) and the Total Dana Price(TDP)
    vat_total_dana_price_label = tk.Label(page, bg=bg_orange, justify='left',text='VAT(5%) of Total Dana Price  : ')
    vat_total_dana_price_entry = tk.Entry(page, justify='left',textvariable=vat_total_dana_price)

    # a_two is the summation of the Replacement Charge(RC) and (the Total Open Market Price(TOP) + the Total Open Market Price(TOP) + 25%TDP)
    vat_total_open_price_in_two_label = tk.Label(page, bg=bg_orange, justify='left', text='VAT(5%) of Total Open Price: ')
    vat_total_open_price_in_two_entry = tk.Entry(page, justify='left', textvariable=vat_total_open_price_in_two)

    # a_three is the summation of the Replacement Charge(RC) and the 50% Total Open Price(TOP)
    vat_fifty_perc_total_open_price_label = tk.Label(page, bg=bg_orange, justify='left', text='VAT(5%) of 50%(Total Open Price) : ')
    vat_fifty_perc_total_open_price_entry = tk.Entry(page, justify='left', textvariable=vat_fifty_perc_total_open_price)

    # a_four is the summation of the Replacement Charge(RC) and the 75% Total Open Price(TOP)
    vat_seventy_five_perc_total_open_price_label = tk.Label(page, bg=bg_orange, justify='left', text='VAT(5%) of 75%(Total Open Price) : ')
    vat_seventy_five_perc_total_open_price_entry = tk.Entry(page, justify='left', textvariable=vat_seventy_five_perc_total_open_price)

    final_total_of_total_dana_price_label = tk.Label(page, bg=bg_orange, justify='left',text='TOTAL OF DANA PRICE : ')
    final_total_of_total_dana_price_entry = tk.Entry(page, justify='left', textvariable=final_total_of_total_dana_price)

    final_total_of_total_open_price_label = tk.Label(page, bg=bg_orange, justify='left', text='TOTAL OF OPEN MARKET PRICE : ')
    final_total_of_total_open_price_entry = tk.Entry(page, justify='left', textvariable=final_total_of_total_open_price)

    final_total_of_total_fifty_perc_open_price_label = tk.Label(page, bg=bg_orange, justify='left', text='TOTAL OF 50% OPEN MARKET PRICE : ')
    final_total_of_total_fifty_perc_open_price_entry = tk.Entry(page, justify='left', textvariable=final_total_of_total_fifty_perc_open_price)

    final_total_of_total_seventy_five_perc_open_price_label = tk.Label(page, bg=bg_orange, justify='left',text='TOTAL OF 75% OPEN MARKET PRICE : ')
    final_total_of_total_seventy_five_perc_open_price_entry = tk.Entry(page, justify='left',textvariable=final_total_of_total_seventy_five_perc_open_price)

    error_message.set('')
    space_one.grid(row=current_end_row + 3, column=2,sticky=W)
    error_label.grid(row=current_end_row + 3,column=2, sticky=E, columnspan=colspan,pady=2)
    total_dana_price_label.grid(row=current_end_row + 4, column=2, sticky=W)
    total_dana_price_entry.grid(row=current_end_row + 4, column=2, sticky=E, columnspan=colspan ,pady=2)
    tw_percent_total_dana_label.grid(row=current_end_row + 5, column=2, sticky=W)
    tw_percent_total_dana_entry.grid(row=current_end_row + 5, column=2, sticky=E, columnspan=colspan,pady=2)
    total_open_price_label.grid(row=current_end_row + 6, column=2, sticky=W)
    total_open_price_entry.grid(row=current_end_row + 6, column=2, sticky=E, columnspan=colspan,pady=2)
    total_open_price_plus_label.grid(row=current_end_row + 7, column=2, sticky=W)
    total_open_price_plus_entry.grid(row=current_end_row + 7, column=2, sticky=E, columnspan=colspan,pady=2)
    fiv_percent_total_plus_open_label.grid(row=current_end_row + 8,column=2, sticky=W)
    fiv_percent_total_plus_open_entry.grid(row=current_end_row + 8,column=2, sticky=E, columnspan=colspan,pady=2)
    sev_percent_total_plus_open_plus_label.grid(row=current_end_row + 9, column=2, sticky=W)
    sev_percent_total_plus_open_plus_entry.grid(row=current_end_row + 9, column=2, sticky=E, columnspan=colspan,pady=2)
    vat_total_dana_price_label.grid(row=current_end_row + 11, column=2, sticky=W)
    vat_total_dana_price_entry.grid(row=current_end_row + 11, column=2, sticky=E, columnspan=colspan, pady=2)
    vat_total_open_price_in_two_label.grid(row=current_end_row + 12, column=2, sticky=W)
    vat_total_open_price_in_two_entry.grid(row=current_end_row + 12, column=2, sticky=E, columnspan=colspan, pady=2)
    vat_fifty_perc_total_open_price_label.grid(row=current_end_row + 13, column=2, sticky=W)
    vat_fifty_perc_total_open_price_entry.grid(row=current_end_row + 13, column=2, sticky=E, columnspan=colspan, pady=2)
    vat_seventy_five_perc_total_open_price_label.grid(row=current_end_row + 14, column=2, sticky=W)
    vat_seventy_five_perc_total_open_price_entry.grid(row=current_end_row + 14, column=2, sticky=E, columnspan=colspan, pady=2)
    final_total_of_total_dana_price_label.grid(row=current_end_row + 16, column=2, sticky=W)
    final_total_of_total_dana_price_entry.grid(row=current_end_row + 16, column=2, sticky=E, columnspan=colspan,pady=2)
    final_total_of_total_open_price_label.grid(row=current_end_row + 17, column=2, sticky=W)
    final_total_of_total_open_price_entry.grid(row=current_end_row + 17, column=2, sticky=E, columnspan=colspan, pady=2)
    final_total_of_total_fifty_perc_open_price_label.grid(row=current_end_row + 18, column=2, sticky=W)
    final_total_of_total_fifty_perc_open_price_entry.grid(row=current_end_row + 18, column=2, sticky=E, columnspan=colspan, pady=2)
    final_total_of_total_seventy_five_perc_open_price_label.grid(row=current_end_row + 19, column=2, sticky=W)
    final_total_of_total_seventy_five_perc_open_price_entry.grid(row=current_end_row + 19, column=2, sticky=E, columnspan=colspan, pady=2)


def add_x_more_entry(x):
    item_number = tk.Label(page, bg=bg_orange, text='Item '+str(x)).grid(row=x+2, column=1)
    product_name = tk.Entry(page, textvariable = 'name_'+str(x)+'value').grid(row=x+2, column=2)
    dana_price = tk.Entry(page, textvariable=current_dana_list[x])
    dana_price.grid(row=x+2, column=4)
    foreign_price = tk.Entry(page, textvariable=current_foreign_list[x])
    foreign_price.grid(row=x+2, column=6)
    open_market_price = tk.Entry(page, textvariable=current_open_list[x])
    open_market_price.grid(row=x+2, column=8, pady=5)
    dana_list.append(dana_price)
    open_list.append(open_market_price)
    foreign_list.append(foreign_price)

current_dana_list,current_foreign_list,current_open_list =[1,2,3,4,5,5,5],[1,2,3,4,5,5,5],[1,2,3,4,5,5,5]
def add_some_more_rows():
    if float(more_row_value.get())-float(more_row_value.get())==0:
        global current_dana_list, current_foreign_list,current_end_row, end
        end = int(more_row_value.get())+current_end_row
        if end<300:
            for x in range(current_end_row, end):
                current_dana_list.append('dana_' + str(x) + 'value')
                current_open_list.append('open_' + str(x) + 'value')
                current_foreign_list.append('foreign_' + str(x) + 'value')
            for x in range(current_end_row, end):
                current_dana_list[x]  = IntVar()
                current_open_list[x]  = IntVar()
                current_foreign_list[x]  = IntVar()
                add_x_more_entry(x)

        replacement_charge_label.grid(row=end +2, column=1)
        replacement_charge_button.grid(row=end +2, column=2)
        calculate_button.grid(row=end+3,column=3)
        more_row_entry.grid(row=end+3,column=4)
        generate_button.grid(row=end+3,column=5)

        space_one.grid(row=end+4, column=2,sticky=W)
        error_label.grid(row=end + 5,column=2, sticky=W)

        total_dana_price_label.grid(row=end + 6, column=2, sticky=W)
        total_dana_price_entry.grid(row=end + 6, column=3, sticky=W)
        tw_percent_total_dana_label.grid(row=end + 7, column=2, sticky=W)
        tw_percent_total_dana_entry.grid(row=end + 7, column=3, sticky=W)
        total_open_price_label.grid(row=end + 8, column=2, sticky=W)
        total_open_price_entry.grid(row=end + 8, column=3, sticky=W)
        total_open_price_plus_label.grid(row=end + 9, column=2, sticky=W)
        total_open_price_plus_entry.grid(row=end + 9, column=3, sticky=W)
        fiv_percent_total_plus_open_label.grid(row=end + 10,column=2, sticky=W)
        fiv_percent_total_plus_open_entry.grid(row=end + 10,column=3, sticky=W)
        sev_percent_total_plus_open_plus_label.grid(row=end + 11, column=2, sticky=W)
        sev_percent_total_plus_open_plus_entry.grid(row=end + 11, column=3, sticky=W)
        vat_total_dana_price_label.grid(row=end + 12, column=2, sticky=W)
        vat_total_dana_price_entry.grid(row=end + 12, column=3, sticky=W)
        vat_total_open_price_in_two_label.grid(row=end + 13, column=2, sticky=W)
        vat_total_open_price_in_two_entry.grid(row=end + 13, column=3, sticky=W)
        vat_fifty_perc_total_open_price_label.grid(row=end + 14, column=2, sticky=W)
        vat_fifty_perc_total_open_price_entry.grid(row=end + 14, column=3, sticky=W)
        vat_seventy_five_perc_total_open_price_label.grid(row=end + 15, column=2, sticky=W)
        vat_seventy_five_perc_total_open_price_entry.grid(row=end + 15, column=3, sticky=W)
        final_total_of_total_dana_price_label.grid(row=end + 16, column=2, sticky=W)
        final_total_of_total_dana_price_entry.grid(row=end + 16, column=3, sticky=W)
        final_total_of_total_open_price_label.grid(row=end + 17, column=2, sticky=W)
        final_total_of_total_open_price_entry.grid(row=end + 17, column=3, sticky=W)
        final_total_of_total_fifty_perc_open_price_label.grid(row=end + 18, column=2, sticky=W)
        final_total_of_total_fifty_perc_open_price_entry.grid(row=end + 18, column=3, sticky=W)
        final_total_of_total_seventy_five_perc_open_price_label.grid(row=end + 19, column=2, sticky=W)
        final_total_of_total_seventy_five_perc_open_price_entry.grid(row=end + 19, column=3, sticky=W)
        current_end_row = end
    else:
        messagebox.showinfo('Error', 'Invalid value "' + str(more_row_value.get()) + '"')



def give_total_dana_price():
    total_dana_price_value = 0
    for y in range(current_end_row - 1):
        if float(dana_list[y].get())-float(dana_list[y].get())==0:
            total_dana_price_value += float(dana_list[y].get())
        else:
            messagebox.showinfo('Error', 'Invalid value "'+str(dana_list[y].get())+'"')
            break

    return total_dana_price_value


def give_total_open_price():
    total_open_price_value = 0
    for y in range(current_end_row - 1):
        if float(open_list[y].get())-float(open_list[y].get())==0:
            total_open_price_value += float(open_list[y].get())
        else:
            messagebox.showinfo('Error', 'Invalid value "'+str(open_list[y].get())+'"')
            break
    return total_open_price_value


def give_total_foreign_price():
    total_foreign_price_value = 0
    for y in range(current_end_row - 1):
        if float(foreign_list[y].get())-float(foreign_list[y].get())==0:
            total_foreign_price_value += float(foreign_list[y].get())
        else:
            messagebox.showinfo('Error', 'Invalid value "'+str(foreign_list[y].get())+'"')
            break

    return total_foreign_price_value


def replacement_charge_add_a_one():
    if float(replacement_charge_value.get())-float(replacement_charge_value.get())==0:
        a_one = float(replacement_charge_value.get()) + give_total_dana_price()
        return a_one
    else:
        messagebox.showinfo('Error', 'Invalid value, input it must be a number"' + str(replacement_charge_value.get()) + '"')


def give_replacement_charge():
    if float(replacement_charge_value.get())-float(replacement_charge_value.get())==0:
        return float(replacement_charge_value.get())
    else:
        messagebox.showinfo('Error', 'Invalid value, input it must be a number"' + str(replacement_charge_value.get()) + '"')


def generate_result_interface():
    try:
        error_message.set('')
        td = give_total_dana_price()
        total_dana_price.set(str(td))

        l = 0.225*td
        tw_percent_total_dana.set(str(l))

        # Ototal
        to = give_total_open_price()
        total_open_price.set(str(to))

        tf = give_total_foreign_price()

        # total_open_price_plus_l.set(str((2*to)+l))
        # fiv_percent_total_plus_open_l.set(str((0.5*to)+to+l))
        #
        # sev_percent_total_plus_open_plus_l.set(str((0.75*to)+to+l))
        #
        # rcv = give_replacement_charge()
        # gto = give_total_open_price()
        #
        # vat_total_dana_price.set(0.05*(rcv+gto))
        #
        # vat_total_open_price_in_two.set(0.05*(rcv+(2*gto)))
        #
        # vat_fifty_perc_total_open_price.set(0.05*(rcv + (0.5*gto)))
        #
        # vat_seventy_five_perc_total_open_price.set(0.05 * (rcv + (0.75*gto)))
        #
        # final_total_of_total_dana_price.set(0.05*(rcv+gto) + rcv+gto)
        #
        # final_total_of_total_open_price.set(0.05*(rcv+(2*gto)) + (rcv+(2*gto)))
        #
        # final_total_of_total_fifty_perc_open_price.set(0.05*(rcv+(0.5*gto)) + rcv+(0.5*gto))
        #
        # final_total_of_total_seventy_five_perc_open_price.set(0.05 * (rcv + (0.75*gto)) + (rcv + (0.75*gto)))


        error_message.set('')
        td = give_total_dana_price()
        total_dana_price.set(str('{:.2f}'.format(td)))

        l = 0.225*td
        tw_percent_total_dana.set(str('{:.2f}'.format(l)))

        # Ototal
        to = give_total_open_price()
        total_open_price.set(str('{:.2f}'.format(to)))

        tf = give_total_foreign_price()

        # total_open_price_plus_l.set(str((2*to)+l))
        total_open_price_plus_l.set(str('{:.2f}'.format((2*to)+l)))
        # fiv_percent_total_plus_open_l.set(str((0.5*to)+to+l))
        fiv_percent_total_plus_open_l.set(str('{:.2f}'.format(int(0.5*to)+to+l)))

        sev_percent_total_plus_open_plus_l.set(str('{:.2f}'.format(int(0.75*to)+to+l)))
        # sev_percent_total_plus_open_plus_l.set(str((0.75*to)+to+l))

        rcv = give_replacement_charge()
        gto = give_total_open_price()

        # vat_total_dana_price.set(0.05*(rcv+gto))
        vat_total_dana_price.set('{:.2f}'.format(0.05*(rcv+gto)))

        # vat_total_open_price_in_two.set(0.05*(rcv+(2*gto)))
        vat_total_open_price_in_two.set('{:.2f}'.format(float(0.05*(rcv+(2*gto)))))

        # vat_fifty_perc_total_open_price.set(0.05*(rcv + (0.5*gto)))
        vat_fifty_perc_total_open_price.set('{:.2f}'.format(float(0.05*(rcv + (0.5*gto)))))

        # vat_seventy_five_perc_total_open_price.set(0.05 * (rcv + (0.75*gto)))
        vat_seventy_five_perc_total_open_price.set('{:.2f}'.format(0.05 * (rcv + (0.75*gto))))

        # final_total_of_total_dana_price.set(0.05*(rcv+gto) + rcv+gto)
        final_total_of_total_dana_price.set('{:.2f}'.format(float(0.05*(rcv+gto) + rcv+gto)))

        # final_total_of_total_open_price.set(0.05*(rcv+(2*gto)) + (rcv+(2*gto)))
        final_total_of_total_open_price.set('{:.2f}'.format(float(0.05*(rcv+(2*gto)) + (rcv+(2*gto)))))

        # final_total_of_total_fifty_perc_open_price.set(0.05*(rcv+(0.5*gto)) + rcv+(0.5*gto))
        final_total_of_total_fifty_perc_open_price.set('{:.2f}'.format(float(0.05*(rcv+(0.5*gto)) + rcv+(0.5*gto))))

        # final_total_of_total_seventy_five_perc_open_price.set(0.05 * (rcv + (0.75*gto)) + (rcv + (0.75*gto)))
        final_total_of_total_seventy_five_perc_open_price.set('{:.2f}'.format(float(0.05 * (rcv + (0.75*gto)) + (rcv + (0.75*gto)))))

    except TypeError:
        pass
    except ValueError:
        messagebox.showinfo('Error', 'Invalid value')
        error_message.set("Invalid value")

#
# class App(object):
#     def __init__(self):
#         generate_initial_interface()
#
# app = App()

def login():
    generaate_login_interface()
    if (username_value.get() == "csil" and password_value.get() == "admin1"):
        generaate_login_interface(destr=1)
        generate_initial_interface()
    else:
        messagebox.showerror('Invalid', 'Invalid details')
username_value, password_value = StringVar(), StringVar()
login_title = tk.Label(page, bg=bg_orange, font=(18),text='Combined System International Limited (CSIL) Pricing Software', pady=10)
login_text = tk.Label(page, bg=bg_orange, text='Login', padx=500)

username_label = tk.Label(page, bg=bg_orange, text='Username')
username_entry = tk.Entry(page, textvariable=username_value)
password_label = tk.Label(page, bg=bg_orange, text='Password')
password_entry = tk.Entry(page, show="*", textvariable=password_value)
login_button = tk.Button(page, width=16, text='Login', command=login)


def generaate_login_interface(destr=0):
    if destr == 0:
        login_title.grid(row=1, column=3, columnspan=4)
        login_text.grid(row=5, column=4, columnspan=2)
        password_entry.grid(row=7, column=4, sticky=E)
        password_label.grid(row=7, column=4, )
        username_entry.grid(row=6, column=4, sticky=E)
        username_label.grid(row=6, column=4, )
        login_button.grid(row=8, column=4, sticky=E, pady=6)
    if destr == 1:
        login_title.destroy()
        login_text.destroy()
        password_entry.destroy()
        password_label.destroy()
        username_entry.destroy()
        username_label.destroy()
        login_button.destroy()


def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=1100,height=650)

root.title('Combined Systems International Limited(CSIL) Pricing Software')
myscrollbar.pack(side="right",fill="y")
canvas.pack(side="left")
canvas.create_window((0,0),window=frame,anchor='nw')
frame.bind("<Configure>",myfunction)
generaate_login_interface()
root.mainloop()