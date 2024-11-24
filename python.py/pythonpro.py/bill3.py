from tkinter import *
import random

class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.maxsize(width = 1280,height = 700)
        self.root.minsize(width = 1280,height = 700)
        self.root.title(" Billing System")

        #====================Variables========================#
        self.cus_name = StringVar()
        self.c_phone = StringVar()
        #For Generating Random Bill Numbers
        x = random.randint(1000,9999)
        self.c_bill_no = StringVar()
        #Seting Value to variable
        self.c_bill_no.set(str(x))

        self.bread = IntVar()
        self.candy = IntVar()
        self.hamburger = IntVar()
        self.hotdog = IntVar()
        self.sandwich = IntVar()
        self.rice = IntVar()
        self.salt = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.gatorade = IntVar()
        self.coke = IntVar()
        self.juice = IntVar()
        self.waffer = IntVar()
        self.biscuits = IntVar()
        self.total_food = StringVar()
        self.total_grocery = StringVar()
        self.total_other = StringVar()
        self.tax_cos = StringVar()
        self.tax_groc = StringVar()
        self.tax_other = StringVar()

        bg_color = "green"
        bg_color = "black"
        fg_color = "white"
        lbl_color = 'white'
        #Title of App
        title = Label(self.root,text = "BILLING SOFTWARE",bd = 12,relief = GROOVE,fg = fg_color,bg = bg_color,font=("times new roman",30,"bold"),pady = 3).pack(fill = X)

        #==========Customers Frame==========#
        F1 = LabelFrame(text = "Customer Details",font = ("time new roman",12,"bold"),fg = "gold",bg = bg_color,relief = GROOVE,bd = 10)
        F1.place(x = 0,y = 80,relwidth = 1)

        #===============Customer Name===========#
        cname_lbl = Label(F1,text="Customer Name",bg = bg_color,fg = fg_color,font=("times new roman",15,"bold")).grid(row = 0,column = 0,padx = 10,pady = 5)
        cname_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.cus_name)
        cname_en.grid(row = 0,column = 1,ipady = 4,ipadx = 30,pady = 5)

        #=================Customer Phone==============#
        cphon_lbl = Label(F1,text = "Phone No",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold")).grid(row = 0,column = 2,padx = 20)
        cphon_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.c_phone)
        cphon_en.grid(row = 0,column = 3,ipady = 4,ipadx = 30,pady = 5)

        #====================Customer Bill No==================#
        cbill_lbl = Label(F1,text = "Bill No.",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold"))
        cbill_lbl.grid(row = 0,column = 4,padx = 20)
        cbill_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.c_bill_no)
        cbill_en.grid(row = 0,column = 5,ipadx = 30,ipady = 4,pady = 5)

        #==================Food Frame=====================#
        F2 = LabelFrame(self.root,text = 'Food',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 5,y = 180,width = 325,height = 380)

        #===========Frame Content
        bath_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Bread")
        bath_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        bath_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.bread)
        bath_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======Candy
        face_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Candy")
        face_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        face_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.candy)
        face_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #========Hamburger
        wash_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Hamburger")
        wash_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        wash_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.hamburger)
        wash_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========Hotdog
        hair_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Hotdog")
        hair_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        hair_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.hotdog)
        hair_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============Sandwich
        lot_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Sandwich")
        lot_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        lot_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.sandwich)
        lot_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #==================Grocery Frame=====================#
        F2 = LabelFrame(self.root,text = 'Grocery',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 330,y = 180,width = 325,height = 380)

        #===========Frame Content
        rice_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Rice")
        rice_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        rice_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.rice)
        rice_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======
        oil_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Food Oil")
        oil_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        oil_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.food_oil)
        oil_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #=======
        daal_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Salt")
        daal_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        daal_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.salt)
        daal_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========
        wheat_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Wheat")
        wheat_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        wheat_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.wheat)
        wheat_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============
        sugar_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Sugar")
        sugar_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        sugar_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.sugar)
        sugar_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #==================Other Stuff=====================#

        F2 = LabelFrame(self.root,text = 'Others',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 655,y = 180,width = 325,height = 380)

        #===========Frame Content
        maza_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Gatorade")
        maza_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        maza_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.gatorade)
        maza_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======
        cock_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Coke")
        cock_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        cock_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.coke)
        cock_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #=======
        frooti_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Juice")
        frooti_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        frooti_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.juice)
        frooti_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========
        cold_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Waffer")
        cold_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        cold_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.waffer)
        cold_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============
        bis_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Biscuits")
        bis_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        bis_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.biscuits)
        bis_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #===================Bill Aera================#
        F3 = Label(self.root,bd = 10,relief = GROOVE)
        F3.place(x = 960,y = 180,width = 325,height = 380)
        #===========
        bill_title = Label(F3,text = "Bill List",font = ("Lucida",13,"bold"),bd= 7,relief = GROOVE)
        bill_title.pack(fill = X)

        #============
        scroll_y = Scrollbar(F3,orient = VERTICAL)
        self.txt = Text(F3,yscrollcommand = scroll_y.set)
        scroll_y.pack(side = RIGHT,fill = Y)
        scroll_y.config(command = self.txt.yview)
        self.txt.pack(fill = BOTH,expand = 1)

        #===========Buttons Frame=============#
        F4 = LabelFrame(self.root,text = 'Bill Menu',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F4.place(x = 0,y = 560,relwidth = 1,height = 145)

        #===================
        cosm_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Food")
        cosm_lbl.grid(row = 0,column = 0,padx = 10,pady = 0)
        cosm_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_food)
        cosm_en.grid(row = 0,column = 1,ipady = 2,ipadx = 5)

        #===================
        gro_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Grocery")
        gro_lbl.grid(row = 1,column = 0,padx = 10,pady = 5)
        gro_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_grocery)
        gro_en.grid(row = 1,column = 1,ipady = 2,ipadx = 5)

        #================
        oth_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Others Total")
        oth_lbl.grid(row = 2,column = 0,padx = 10,pady = 5)
        oth_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_other)
        oth_en.grid(row = 2,column = 1,ipady = 2,ipadx = 5)

        #================
        cosmt_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Food Tax")
        cosmt_lbl.grid(row = 0,column = 2,padx = 30,pady = 0)
        cosmt_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_cos)
        cosmt_en.grid(row = 0,column = 3,ipady = 2,ipadx = 5)

        #=================
        grot_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Grocery Tax")
        grot_lbl.grid(row = 1,column = 2,padx = 30,pady = 5)
        grot_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_groc)
        grot_en.grid(row = 1,column = 3,ipady = 2,ipadx = 5)

        #==================
        otht_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Others Tax")
        otht_lbl.grid(row = 2,column = 2,padx = 10,pady = 5)
        otht_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_other)
        otht_en.grid(row = 2,column = 3,ipady = 2,ipadx = 5)

        #====================
        total_btn = Button(F4,text = "Total",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.total)
        total_btn.grid(row = 1,column = 4,ipadx = 20,padx = 30)

        #========================
        genbill_btn = Button(F4,text = "Generate Bill",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.bill_area)
        genbill_btn.grid(row = 1,column = 5,ipadx = 20)

        #====================
        clear_btn = Button(F4,text = "Clear",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.clear)
        clear_btn.grid(row = 1,column = 6,ipadx = 20,padx = 30)

        #======================
        exit_btn = Button(F4,text = "Exit",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.exit)
        exit_btn.grid(row = 1,column = 7,ipadx = 20)

#Function to get total prices
    def total(self):
        self.c_s_p=self.bread.get()*10
        self.s_c_p=self.candy.get()*20
        self.ss_c_p=self.hamburger.get()*70
        self.sss_c_p=self.hotdog.get()*60
        self.ssss_c_p=self.sandwich.get()*40
        #=================Total Food Prices
        self.total_food_prices =  (
            self.c_s_p+
            self.s_c_p+
            self.ss_c_p+
            self.sss_c_p+
            self.ssss_c_p
            
        )
        self.total_food.set("Rs="+str(self.total_food_prices))
        self.tax_cos.set("Rs="+str(round(self.total_food_prices*0.05)))
        #====================Total Grocery Prices
        self.wh=self.wheat.get()*1
        self.fo=self.food_oil.get() * 50
        self.Sg=self.salt.get() * 10
        self.rg=self.rice.get() *30
        self.sg=self.sugar.get() * 20

        self.total_grocery_prices = (

            self.wh+
            self.fo+
            self.Sg+
            self.rg+
            self.sg

        )
        self.total_grocery.set("Rs="+str(self.total_grocery_prices))
        self.tax_groc.set("Rs="+str(round(self.total_grocery_prices*0.05)))
        #======================Total Other Prices
        self.gg=self.gatorade.get() * 40
        self.jg=self.juice.get() * 20
        self.cg=self.coke.get() * 20
        self.wg=self.waffer.get() * 20
        self.bg=self.biscuits.get() * 20

        self.total_other_prices = (
            self.gg+
            self.jg+
            self.cg+
            self.wg+
            self.bg
        )
        self.total_other.set("Rs="+str(self.total_other_prices))
        self.tax_other.set("Rs="+str(round(self.total_other_prices*0.05)))

        

#Function For Text Area
    def welcome_soft(self):
        self.txt.delete('1.0',END)
        self.txt.insert(END,"       Welcome To Store's Retail\n")
        self.txt.insert(END,f"\nBill No. : {str(self.c_bill_no.get())}")
        self.txt.insert(END,f"\nCustomer Name : {str(self.cus_name.get())}")
        self.txt.insert(END,f"\nPhone No. : {str(self.c_phone.get())}")
        self.txt.insert(END,"\n===================================")
        self.txt.insert(END,"\nProduct          Qty       Price")
        self.txt.insert(END,"\n===================================")

#Function to clear the bill area
    def clear(self):
        self.txt.delete('1.0',END)

#Add Product name , qty and price to bill area
    def bill_area(self):
        self.welcome_soft()
        file=open("bill.txt","w")
        file.write(f"\nBill No: {str(self.c_bill_no.get())}")
        file.write(f"\nName: {str(self.cus_name.get())}")
        file.write(f"\nPhone: {str(self.c_phone.get())}")
        file.write("\n===================================")
        file.write("\nProduct          Qty         Price")
        if self.bread.get() != 0:
            self.txt.insert(END,f"\nBread\t\t{self.bread.get()}\t\t{self.c_s_p}")
        if self.candy.get() != 0:
            self.txt.insert(END,f"\ncandy\t\t{self.candy.get()}\t\t{self.s_c_p}")
        if self.hamburger.get() != 0:
            self.txt.insert(END,f"\nhamburger\t\t{self.hamburger.get()}\t\t{self.ss_c_p}")  
        if self.hotdog.get() != 0:
            self.txt.insert(END,f"\nhotdog\t\t{self.hotdog.get()}\t\t{self.sss_c_p}")      
        if self.sandwich.get() != 0:
            self.txt.insert(END,f"\nsandwich\t\t{self.sandwich.get()}\t\t{self.ssss_c_p}")
        if self.wheat.get() != 0:
            self.txt.insert(END,f"\nwheat\t\t{self.wheat.get()}\t\t{self.wh}")
        if self.food_oil.get() != 0:
            self.txt.insert(END,f"\nfood_oil\t\t{self.food_oil.get()}\t\t{self.fo}")
        if self.salt.get() != 0:
            self.txt.insert(END,f"\nSalt\t\t{self.salt.get()}\t\t{self.Sg}")
        if self.rice.get() != 0:
            self.txt.insert(END,f"\nRice\t\t{self.rice.get()}\t\t{self.rg}")
        if self.sugar.get() != 0:
            self.txt.insert(END,f"\nSugar\t\t{self.sugar.get()}\t\t{self.sg}")
        if self.gatorade.get() != 0:
            self.txt.insert(END,f"\ngatorad\t\t{self.gatorade.get()}\t\t{self.gg}")
        if self.juice.get() != 0:
            self.txt.insert(END,f"\njuice\t\t{self.juice.get()}\t\t{self.jg}")
        if self.coke.get() != 0:
            self.txt.insert(END,f"\ncoke\t\t{self.coke.get()}\t\t{self.cg}")
        if self.waffer.get() != 0:
            self.txt.insert(END,f"\nwaffer\t\t{self.waffer.get()}\t\t{self.wg}")
        if self.biscuits.get() != 0:
            self.txt.insert(END,f"\nbiscuit\t\t{self.biscuits.get()}\t\t{self.bg}")
        
        self.txt.insert(END,"\n===================================")
        self.txt.insert(END,f"\n                 Total : Rs={self.total_food_prices+self.total_grocery_prices+self.total_other_prices+self.total_food_prices * 0.05+self.total_grocery_prices * 0.05+self.total_other_prices * 0.05}")
        file.write(f"\n===================================")
        file.write(f"\n Total : Rs={self.total_food_prices+self.total_grocery_prices+self.total_other_prices+self.total_food_prices * 0.05+self.total_grocery_prices * 0.05+self.total_other_prices * 0.05}")
        

    def exit(self):

        self.root.destroy()


root = Tk()
object = Bill_App(root)
root.mainloop()


          