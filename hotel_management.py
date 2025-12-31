from tkinter import * 
import mysql.connector 
from tkinter import ttk 
from tkinter import messagebox 
from PIL import Image,ImageTk 
from tkcalendar import Calendar 
import PIL.Image 
import datetime 
root= Tk() 
root.geometry("400x400") 
 
#ADMIN 
def admin(): 
    top=Toplevel() 
    top.geometry("300x150") 
    top.configure(background="black") 
    def show(): 
        p=password.get() 
        passw="1234" 
        if passw==str(p): 
            global checkin 
            top=Toplevel() 
            top.geometry("600x650") 
            top.configure(background="black") 
            img = 
Image.open(r"C:\Users\NANDHIKA\AppData\Local\Programs\Python\Python3
7\admin.png")  
            # resize the image and apply a high-quality down sampling filter  
            img = img.resize((200,200), Image.LANCZOS)  
            # PhotoImage class is used to add image to widgets, icons etc  
            img = ImageTk.PhotoImage(img)  
            # create a label  
            panel = Label(top, image = img)  
            # set the image as img   
            panel.image = img  
            panel.grid(row = 10, column=100) 
            def details(): 
                top=Toplevel() 
16 
 
                top.geometry("300x150") 
                top.configure(bg="black") 
                def roombooked(): 
                    top=Toplevel() 
                    top.geometry("600x600") 
                    top.configure(bg="black") 
                    def show2(): 
                        myc1=mysql.connector.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
                        c1=myc1.cursor() 
                        c1.execute("SELECT 
ROOMNO,ROOMTYPEID,NAME,PHNO,EMAILID,CHECKIN,CHECKOUT,SC
OST from RBOOKING ") 
                        r1=c1.fetchall() 
                        for 
j,(ROOMNO,ROOMTYPEID,NAME,PHNO,EMAILID,CHECKIN,CHECKOUT,S
COST) in enumerate(r1,start=1): 
                            
listBox1.insert("","end",values=(ROOMNO,ROOMTYPEID,NAME,PHNO,EMAI
LID,CHECKIN,CHECKOUT,SCOST)) 
                            myc1.close() 
                    
cols1=("ROOMNO","ROOMTYPEID","NAME","PHNO","EMAILID","CHECKIN",
"CHECKOUT","SCOST" ) 
                    listBox1=ttk.Treeview(top,columns=cols1,show="headings") 
                    for col1 in cols1: 
                        listBox1.heading(col1,text=col1) 
                        listBox1.grid(row=1,column=0,columnspan=2) 
                    show2() 
                 
                def tables(): 
                    top=Toplevel() 
                    top.geometry("600x600") 
                    top.configure(bg="black") 
                    def show2(): 
                        
myc1=mysql.connector.connect(host="localhost",user="root",password="root",
database="hotel_management") 
                        c1=myc1.cursor() 
17 
 
                        c1.execute("SELECT DISTINCT 
NAME,PH_NO,GMAIL,BOOKING_DATE,TIMESLOT,NO_OF_PEOPLE from 
TABLE_BOOKING;  ") 
                        r1=c1.fetchall() 
                        for 
j,(NAME,PH_NO,GMAIL,BOOKING_DATE,TIMESLOT,NO_OF_PEOPLE) in 
enumerate(r1,start=1): 
                            
listBox1.insert("","end",values=(NAME,PH_NO,GMAIL,BOOKING_DATE,TIME
SLOT,NO_OF_PEOPLE)) 
                            myc1.close() 
                    
cols1=("NAME","PH_NO","GMAIL","BOOKING_DATE","TIMESLOT","NO_OF_
PEOPLE") 
                    listBox1=ttk.Treeview(top,columns=cols1,show="headings") 
                    for col1 in cols1: 
                        listBox1.heading(col1,text=col1) 
                        listBox1.grid(row=1,column=0,columnspan=2) 
                    show2() 
 
                P1=Button(top,text="ROOM 
BOOKED",command=roombooked,bg="white") 
                P1.grid(row=0,column=0) 
                 
                P3=Button(top,text="TABLES",command=tables,bg="white") 
                P3.grid(row=2,column=0) 
            def availability(): 
                top=Toplevel() 
                top.geometry("300x300") 
                top.configure(bg="black") 
                 
                def rooms(): 
                    top=Toplevel() 
                    top.geometry("800x600") 
                    top.configure(bg="black") 
                    def show2(): 
                        myc1=mysql.connector.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
                        c1=myc1.cursor() 
18 
 
                        c1.execute("SELECT DISTINCT 
ROOMNO,ROOMTYPEID,ROOMSTATUS,RDATE from ROOMS WHERE 
ROOMSTATUS= 'NOT OCCUPIED';  ") 
                        r1=c1.fetchall() 
                        for j,(ROOMNO,ROOMTYPEID,ROOMSTATUS,RDATE) in 
enumerate(r1,start=1): 
                            
listBox1.insert("","end",values=(ROOMNO,ROOMTYPEID,ROOMSTATUS,RD
ATE)) 
                            myc1.close() 
                    cols1=("ROOMNO","ROOMTYPEID","ROOM STATUS","RDATE") 
                    listBox1=ttk.Treeview(top,columns=cols1,show="headings") 
                    for col1 in cols1: 
                        listBox1.heading(col1,text=col1) 
                        listBox1.grid(row=1,column=0,columnspan=2) 
                    show2() 
                P4=Button(top,text="ROOMS",command=rooms,bg="white") 
                P4.grid(row=0,column=0) 
            def info(): 
                top=Toplevel() 
                top.geometry("800x300") 
                top.configure(bg="black") 
                def view(): 
                    top=Toplevel() 
                    top.geometry("800x350") 
                    top.configure(bg="green") 
                    def show1(): 
                        myc=mysql.connector.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
                        c=myc.cursor() 
                        c.execute("SELECT DISTINCT CODE,NAME,SALARY,PHNO 
from EMP ") 
                        r=c.fetchall() 
                        for i,(CODE,NAME,SALARY,PHNO) in enumerate(r,start=1): 
                            
listBox.insert("","end",values=(CODE,NAME,SALARY,PHNO)) 
                            myc.close() 
                    cols=('code','name','salary','phno') 
                    listBox=ttk.Treeview(top,columns=cols,show='headings') 
                    for col in cols: 
19 
 
                        listBox.heading(col,text=col) 
                        listBox.grid(row=1,column=0,columnspan=2) 
                    show1() 
                def edit(): 
                    top=Toplevel() 
                    top.geometry("350x350") 
                    top.configure(bg="teal") 
                    a=StringVar() 
                    b=StringVar() 
                    a1=Entry(top,width=25) 
                    b1=Entry(top,width=25) 
                    a21=Label(top,text="PHNO",fg="white",bg="teal") 
                    b21=Label(top,text="SALARY",fg="white",bg="teal") 
                    a21.grid(row=0,column=1) 
                    b21.grid(row=2,column=1) 
                     
                    a1.grid(row=0,column=10) 
                    b1.grid(row=2,column=10) 
                    def enter1(): 
                        top=Toplevel() 
                        a2=a1.get() 
                        b2=int(b1.get()) 
                         
                         
                        myc=mysql.connector.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
                        c=myc.cursor() 
                        sql="UPDATE  EMP  SET SALARY={} WHERE 
PHNO='{}'".format(b2,a2) 
                         
                        c.execute(sql) 
                        myc.commit() 
                        messagebox.showinfo("EDIT PERSONAL INFO","UPDATED") 
         
             
                    pi=Button(top,text="ENTER",command=enter1,bg="white") 
                    pi.grid(row=5,column=5) 
                pj=Button(top,text="EDIT",command=edit,bg="white") 
                pj.grid(row=2,column=0) 
                ph=Button(top,text="VIEW",command=view,bg="white") 
20 
 
                ph.grid(row=3,column=0) 
                def add(): 
                    top=Toplevel() 
                    top.geometry("400x400") 
                    top.configure(bg="black") 
                               
                    a1=Entry(top,width=25) 
                    b1=Entry(top,width=25) 
                    c1=Entry(top,width=25) 
                    d1=Entry(top,width=25) 
                     
              
                    a1.grid(row=0,column=27)  
                    b1.grid(row=3,column=27)  
                    c1.grid(row=5,column=27)  
                    d1.grid(row=7,column=27) 
                    
 
                    
a12=Label(top,text="CODE",fg="white",padx=59,pady=10,bg="black") 
                    
a22=Label(top,text="NAME",fg="white",padx=71.5,pady=10,bg="black") 
                    
a32=Label(top,text="SALARY",fg="white",padx=56.5,pady=10,bg="black") 
                    
a42=Label(top,text="PHNO",fg="white",padx=65,pady=10,bg="black") 
                     
 
                    a12.grid(row=0,column=0)  
                    a22.grid(row=3,column=0)  
                    a32.grid(row=5,column=0)  
                    a42.grid(row=7,column=0)  
 
                    def enter1(): 
                        top=Toplevel() 
                        a2=a1.get() 
                        b2=b1.get() 
                         
                        c2=c1.get() 
                        d2=d1.get()   
21 
 
                        myc=mysql.connector.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
                        c=myc.cursor() 
                        sql="INSERT INTO 
EMP(CODE,NAME,SALARY,PHNO)VALUES(%s,%s,%s,%s)" 
                        val=(a2,b2,c2,d2)        
                        c.execute(sql,val) 
                        myc.commit() 
                    pi=Button(top,text="ENTER",command=enter1,bg="white") 
                    pi.grid(row=15,column=7) 
                pz=Button(top,text="ADD",command=add,bg="white") 
                pz.grid(row=5,column=0) 
                def remove(): 
                    top=Toplevel() 
                    top.geometry("350x350") 
                    top.configure(bg="teal") 
                    a=StringVar() 
                    a1=Entry(top,width=25) 
                    a21=Label(top,text="PHNO",fg="white",bg="teal") 
                    a21.grid(row=0,column=1) 
                    a1.grid(row=0,column=10) 
                    def enter1(): 
                        top=Toplevel() 
                        a2=a1.get() 
                        myc=mysql.connector.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
                        c=myc.cursor() 
                        sql="DELETE FROM EMP WHERE PHNO='{}'".format(a2) 
                        c.execute(sql) 
                        myc.commit() 
                        messagebox.showinfo("EMP","UPDATED") 
                    pi=Button(top,text="ENTER",command=enter1,bg="white") 
                    pi.grid(row=5,column=5) 
                py=Button(top,text="REMOVE",command=remove,bg="white") 
                py.grid(row=7,column=0) 
         
            def foodmenu(): 
                top=Toplevel() 
                top.geometry("200x200") 
                top.configure(bg="teal") 
22 
 
                def view(): 
                        top=Toplevel() 
                        top.geometry("800x350") 
                        top.configure(bg="green") 
                        def show1(): 
                            myc=mysql.connector.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
                            c=myc.cursor() 
                            c.execute("SELECT DISTINCT ITEM_ID,ITEM,COST from 
MENU ") 
                            r=c.fetchall() 
                            for i,(ITEM_ID,ITEM,COST) in enumerate(r,start=1): 
                                listBox.insert("","end",values=(ITEM_ID,ITEM,COST)) 
                                myc.close() 
                        cols=('ITEM_ID','ITEM','COST') 
                        listBox=ttk.Treeview(top,columns=cols,show='headings') 
                        for col in cols: 
                            listBox.heading(col,text=col) 
                            listBox.grid(row=1,column=0,columnspan=2) 
                        show1() 
                def edit(): 
                        top=Toplevel() 
                        top.geometry("350x350") 
                        top.configure(bg="teal") 
                        a=StringVar() 
                        b=StringVar() 
                        a1=Entry(top,width=25) 
                        b1=Entry(top,width=25) 
                        a21=Label(top,text="FOOD TYPE",fg="white",bg="teal") 
                        b21=Label(top,text="CHANGE",fg="white",bg="teal") 
                        a21.grid(row=0,column=1) 
                        b21.grid(row=2,column=1) 
                        a1.grid(row=0,column=10) 
                        b1.grid(row=2,column=10) 
                        def enter1(): 
                            top=Toplevel() 
                            a2=a1.get() 
                            b2=int(b1.get()) 
                             
23 
 
                            myc=mysql.connector.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
                            c=myc.cursor() 
                            sql="UPDATE  MENU SET COST={} WHERE 
ITEM_ID='{}'".format(b2,a2) 
                            c.execute(sql) 
                            myc.commit() 
                            messagebox.showinfo("MENU","UPDATED") 
                        pi=Button(top,text="ENTER",command=enter1,bg="white") 
                        pi.grid(row=5,column=5) 
                pj=Button(top,text="EDIT",command=edit,bg="white") 
                pj.grid(row=2,column=0) 
                ph=Button(top,text="VIEW",command=view,bg="white") 
                ph.grid(row=3,column=0) 
            def checkinnow(): 
                top=Toplevel() 
                top.geometry("400x400") 
                top.configure(bg="black") 
                a1=Entry(top,width=25) 
                b1=Entry(top,width=25) 
                c1=Entry(top,width=25) 
                d1=Entry(top,width=25) 
                e1=Entry(top,width=25) 
                f1=Entry(top,width=25) 
                a1.grid(row=0,column=27)  
                b1.grid(row=3,column=27)  
                c1.grid(row=5,column=27)  
                d1.grid(row=7,column=27) 
                e1.grid(row=9,column=27) 
                f1.grid(row=11,column=27) 
                a12=Label(top,text="ROOM 
NO.",fg="white",padx=59,pady=10,bg="black") 
                
a22=Label(top,text="NAME",fg="white",padx=71.5,pady=10,bg="black") 
                a32=Label(top,text="PHONE 
NO.",fg="white",padx=56.5,pady=10,bg="black") 
                a42=Label(top,text="EMAIL 
ID",fg="white",padx=65,pady=10,bg="black") 
                a52=Label(top,text="CHECK IN ",fg="white",bg="black",pady=10) 
                a62=Label(top,text="CHECK OUT",fg="white",bg="black",pady=10) 
24 
 
                a12.grid(row=0,column=0)  
                a22.grid(row=3,column=0)  
                a32.grid(row=5,column=0)  
                a42.grid(row=7,column=0) 
                a52.grid(row=9,column=0) 
                a62.grid(row=11,column=0) 
 
                def enter1(): 
                            top=Toplevel() 
                            a2=a1.get() 
                            b2=b1.get() 
                             
                            c2=c1.get() 
                            d2=d1.get() 
                            e2=e1.get() 
                            f2=f1.get() 
                            A=int(a2) 
                            L1=e2.split("-") 
                            L2=f2.split("-") 
                             
                            if int(L2[1])==int(L1[1]): 
                                d=int(L2[2])-int(L1[2]) +1 
                            elif int(L2[1])-int(L1[1])==1: 
                                if int(L1[1])  in (1,3,5,7,8,9,10,12): 
                                    d=31 - int(L1[2]) +1 + int(L2[2]) 
                                elif int(L1[1])==2: 
                                    d=28 - int(L1[2]) +1 + int(L2[2]) 
                                else: 
                                    d=30 - int(L1[2]) +1 + int(L2[2]) 
                            else: 
                                d=60 
                            if d<59: 
                                a=mysql.connector.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
                                b=a.cursor() 
                                e="OCCUPIED" 
                                A2=int(a2) 
                                x=("SELECT COUNT(ROOMNO) FROM ROOMS WHERE 
ROOMSTATUS='NOT OCCUPIED' AND ROOMNO=%s AND  (RDATE >=%s) 
AND  (RDATE <=%s) ") 
25 
 
                                b.execute(x,(A2,e2,f2)) 
                                rraw=(b.fetchall()[0]) 
                                 
                                if int(rraw[0])==d: 
                                     
                                    if A in (1,2,3,4,5): 
                                        
a=mysql.connector.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
                                        b=a.cursor() 
                                        scost=float(d*25000) 
                                        sql="INSERT INTO 
RBOOKING(ROOMNO,ROOMTYPEID,NAME,PHNO,EMAILID,CHECKIN,CH
ECKOUT,SCOST)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)" 
                                        val=(a2,'P',b2,c2,d2,e2,f2,scost) 
                                        b.execute(sql,val) 
                                        sql="UPDATE ROOMS SET 
ROOMSTATUS=%s,PHNO=%s WHERE ROOMNO=%s AND RDATE 
BETWEEN %s AND %s" 
                                        v=(e,c2,a2,e2,f2) 
                                        b.execute(sql,v) 
                                        a.commit() 
                                        sql="INSERT INTO 
RBILL(ROOMNO,SCOST,CHECKOUT) VALUES(%s,%s,%s)" 
                                        val=(a2,scost,f2) 
                                        b.execute(sql,val) 
                                        messagebox.showinfo("BOOKING","UPDATED") 
                                    elif A in (6,7,8,9,10,11,12,13,14,15): 
                                        
a=mysql.connector.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
                                        b=a.cursor() 
                                        scost=float(d*7000) 
                                        sql="INSERT INTO 
RBOOKING(ROOMNO,ROOMTYPEID,NAME,PHNO,EMAILID,CHECKIN,CH
ECKOUT,SCOST)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)" 
                                        val=(a2,'K',b2,c2,d2,e2,f2,scost) 
                                        b.execute(sql,val) 
                                        sql="INSERT INTO 
RBILL(ROOMNO,SCOST,CHECKOUT) VALUES(%s,%s,%s)" 
26 
 
                                        val=(a2,scost,f2) 
                                        b.execute(sql,val) 
                                        sql="UPDATE ROOMS SET 
ROOMSTATUS=%s,PHNO=%s WHERE ROOMNO=%s AND RDATE 
BETWEEN %s AND %s" 
                                        v=(e,c2,a2,e2,f2) 
                                        b.execute(sql,v) 
                                        a.commit() 
                                        messagebox.showinfo("BOOKING","UPDATED") 
 
                                else: 
                                      messagebox.showinfo("OOPS!","Dates unavailable") 
             
                pi=Button(top,text="ENTER",command=enter1,bg="white") 
                pi.grid(row=15,column=7) 
            def payment(): 
                top=Toplevel() 
                top.geometry("500x500") 
                top.configure(bg="blue") 
                def roompay(): 
                    top=Toplevel() 
                    top.geometry("500x500") 
                    top.configure(bg="blue") 
                    v11=StringVar()  
                    v21=Entry(top,width=25,textvariable=v11) 
                    v21.grid(row=0,column=27) 
                    a21=Label(top,text="ROOM 
NO",fg="white",bg="blue",padx=71.5,pady=10) 
                    a22=Label(top,text="CHECKOUT 
DATE",fg="white",bg="blue",padx=71.5,pady=10) 
                    v22=Entry(top,width=25) 
                    v22.grid(row=5,column=27) 
                    a21.grid(row=0,column=0) 
                    a22.grid(row=5,column=0) 
                    def enter(): 
                        v1=v21.get() 
 
                        v2=v22.get() 
 
                        top=Toplevel() 
27 
 
                        top.geometry("200x200") 
                        top.configure(bg="blue") 
                        myc1=mysql.connector.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
                        c1=myc1.cursor() 
                        c=("SELECT * FROM RBILL WHERE ROOMNO=%s AND 
CHECKOUT=%s") 
                        v=(v1,v2) 
                        c1.execute(c,v) 
                        a=0 
                        r1=c1.fetchone() 
                        a=a+(r1[1]+r1[2]) 
                        ttcoststr=str(a) 
                        label32=Label(top,text="TOTAL COST TO BE PAID =" + 
ttcoststr,font=15) 
                        label32.grid(row=0,column=0) 
                        def pay(): 
                            v1=v21.get() 
                            myc1=mysql.connector.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
                            c1=myc1.cursor() 
                            sql="SELECT PHNO FROM RBOOKING WHERE 
ROOMNO=%s AND CHECKOUT=%s" 
                            val=(v1,v2) 
                            c1.execute(sql,val) 
                            ph=(c1.fetchone()[0]) 
                            e="NOT OCCUPIED"  
                            sql="DELETE FROM RBILL WHERE ROOMNO=%s AND 
CHECKOUT=%s" 
                            va=(v1,v2) 
                            c1.execute(sql,val) 
                            myc1.commit() 
                            sql="UPDATE ROOMS SET 
ROOMSTATUS=%s,PHNO=NULL WHERE ROOMNO=%s AND PHNO=%s 
AND RDATE<=%s" 
                            v=(e,v1,ph,v2) 
                            c1.execute(sql,v) 
                            sql="DELETE FROM RBOOKING WHERE ROOMNO=%s 
AND CHECKOUT=%s" 
                            val=(v1,v2) 
28 
 
                            c1.execute(sql,val) 
                            myc1.commit() 
                            myc1.commit() 
                        s11=Button(top,text="PAY",command=pay) 
                        s11.grid(row=4,column=1)       
                    s10=Button(top,text="ENTER",command=enter) 
                    s10.grid(row=7,column=27) 
                pq=Button(top,text="ROOM BILL",command=roompay,fg="black") 
                pq.grid(row=5,column=5) 
                 
                def roomtable(): 
                    top=Toplevel() 
                    top.geometry("500x500") 
                    top.configure(bg="blue") 
                    v10=StringVar()  
                    v12=StringVar()  
                    v20=Entry(top,width=25,textvariable=v10) 
                    v21=Entry(top,width=25) 
                    v22=Entry(top,width=25,textvariable=v12) 
                    v23=Entry(top,width=25) 
                    v24=Entry(top,width=25) 
                    v21.grid(row=3,column=27) 
                    v22.grid(row=5,column=27) 
                    v23.grid(row=7,column=27) 
                    v24.grid(row=9,column=27) 
                    a21=Label(top,text="ITEM 
ID",fg="white",bg="blue",padx=71.5,pady=10) 
                    
a22=Label(top,text="QTY",fg="white",bg="blue",padx=71.5,pady=10) 
                    a23=Label(top,text="CHECKOUT 
DATE",fg="white",bg="blue",padx=71.5,pady=10) 
                    a24=Label(top,text="ROOM 
NO",fg="white",bg="blue",padx=71.5,pady=10) 
                    a21.grid(row=3,column=0) 
                    a22.grid(row=5,column=0) 
                    a23.grid(row=7,column=0) 
                    a24.grid(row=9,column=0) 
                            
                    def add(): 
                        a2=v21.get() 
29 
 
                        b2=int(v24.get()) 
                         
                        c2=v22.get() 
                        d2=v23.get() 
                        myc=mysql.connector.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
                        c=myc.cursor() 
                        sql="INSERT INTO TTABLE 
(ITEM_ID,NUMBER)VALUES(%s,%s)" 
                        val=(a2,c2)      
                        c.execute(sql,val)        
                        myc.commit() 
                        messagebox.showinfo("ITEM ADDED","UPDATED") 
                    def bill(): 
                        top=Toplevel() 
                        top.geometry("800x600") 
                        top.configure(bg="white") 
                        def show2(): 
                            b2=int(v24.get()) 
                            d2=v23.get() 
                            myc1=mysql.connector.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
                            c1=myc1.cursor() 
                            c1.execute("SELECT 
ITEM_ID,ITEM,NUMBER,COST,NUMBER*COST AS PRICE FROM TTABLE 
NATURAL JOIN MENU;  ") 
                            r1=c1.fetchall()   
                            for j,(ITEM_ID,ITEM,NUMBER,COST,PRICE) in 
enumerate(r1,start=1): 
                                
listBox1.insert("","end",values=(ITEM_ID,ITEM,NUMBER,COST,PRICE)) 
                                myc1.close() 
                            myc1=mysql.connector.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
                            c1=myc1.cursor() 
                            c1.execute("SELECT 
ITEM_ID,ITEM,NUMBER,COST,NUMBER*COST AS PRICE FROM TTABLE 
NATURAL JOIN MENU;  ") 
                            r1=c1.fetchall() 
                            a=0 
30 
 
                            for i in range(len(r1)): 
                                a=a+(r1[i][4]) 
                            ttcoststr=str(a) 
                            x=float(a) 
                            label32=Label(top,text="TOTAL COST TO BE PAID =" + 
ttcoststr,font=15) 
                            label32.grid(row=12,column=0)           
                            myc1.close() 
                            myc1=mysql.connector.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
                            c1=myc1.cursor() 
                            sql="UPDATE RBILL SET TCOST=TCOST + %s WHERE 
ROOMNO=%s AND CHECKOUT=%s" 
                            val=(x,b2,d2)     
                            c1.execute(sql,val)   
                            myc1.commit() 
                            myc=mysql.connector.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
                            c=myc.cursor() 
                            c.execute("DELETE FROM TTABLE")    
                            myc.commit() 
                        cols1=("ITEM_ID","ITEM","NUMBER","COST","PRICE") 
                        listBox1=ttk.Treeview(top,columns=cols1,show="headings") 
                        for col1 in cols1: 
                            listBox1.heading(col1,text=col1) 
                            listBox1.grid(row=1,column=0,columnspan=2)  
                        show2() 
                    su=Button(top,text="BILL",command=bill,bg="white") 
                    su.grid(row=17,column=7) 
                    pi=Button(top,text="ADD",command=add,bg="white") 
                    pi.grid(row=15,column=7)     
                si=Button(top,text="STAY TABLE 
BILL",command=roomtable,bg="white") 
                si.grid(row=7,column=5) 
                 
            def tablebook(): 
                    top=Toplevel() 
                    top.geometry("500x500") 
                    top.configure(bg="blue") 
                    v10=StringVar()  
31 
 
                    v11=StringVar()  
                    v12=StringVar()  
                    v20=Entry(top,width=25,textvariable=v10) 
                    v22=Entry(top,width=25,textvariable=v12) 
                    v20.grid(row=0,column=27) 
                    v22.grid(row=5,column=27) 
                    a21=Label(top,text="ITEM 
ID",fg="white",bg="blue",padx=71.5,pady=10) 
                    
a22=Label(top,text="QTY",fg="white",bg="blue",padx=71.5,pady=10) 
                    a21.grid(row=0,column=0) 
                    a22.grid(row=5,column=0) 
 
                    def add(): 
                        a2=v20.get() 
                         
                        c2=v22.get() 
                         
                        myc=mysql.connector.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
                        c=myc.cursor() 
                        sql="INSERT INTO TTABLE 
(ITEM_ID,NUMBER)VALUES(%s,%s)" 
                        val=(a2,c2)     
                        c.execute(sql,val)   
                        myc.commit() 
                        messagebox.showinfo("ITEM ADDED","UPDATED") 
                    def bill(): 
                        top=Toplevel() 
                        top.geometry("1000x600") 
                        top.configure(bg="white") 
                        def show2(): 
                            myc1=mysql.connector.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
                            c1=myc1.cursor() 
                            c1.execute("SELECT 
ITEM_ID,ITEM,NUMBER,COST,NUMBER*COST AS PRICE FROM TTABLE 
NATURAL JOIN MENU;  ") 
                            r1=c1.fetchall() 
32 
 
                            for j,(ITEM_ID,ITEM,NUMBER,COST,PRICE) in 
enumerate(r1,start=1): 
                                
listBox1.insert("","end",values=(ITEM_ID,ITEM,NUMBER,COST,PRICE)) 
                                myc1.close() 
                            myc1=mysql.connector.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
                            c1=myc1.cursor() 
                            c1.execute("SELECT 
ITEM_ID,ITEM,NUMBER,COST,NUMBER*COST AS PRICE FROM TTABLE
NATURAL JOIN MENU;  ") 
                            r1=c1.fetchall() 
                            a=0 
                            for i in range(len(r1)): 
                                a=a+(r1[i][4]) 
                             
                            ttcoststr=str(a) 
                            label32=Label(top,text="TOTAL COST TO BE PAID =" + 
ttcoststr,font=15) 
                            label32.grid(row=12,column=0)     
                            myc1.close() 
                        cols1=("ITEM_ID","ITEM","NUMBER","COST","PRICE") 
                        listBox1=ttk.Treeview(top,columns=cols1,show="headings") 
                        for col1 in cols1: 
                            listBox1.heading(col1,text=col1) 
                            listBox1.grid(row=1,column=0,columnspan=2) 
                         
                        show2() 
                        def pay(): 
                            myc=mysql.connector.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
                            c=myc.cursor() 
                            c.execute("DELETE FROM TTABLE")  
                            myc.commit() 
                        sh=Button(top,text="PAY",command=pay,bg="white") 
                        sh.grid(row=20,column=5)    
                    su=Button(top,text="BILL",command=bill,bg="white") 
                    su.grid(row=17,column=7) 
                    pi=Button(top,text="ADD",command=add,bg="white") 
                    pi.grid(row=15,column=7) 
33 
 
             
            def book_table(): 
                table=Toplevel() 
                #page background 
                
ft=PIL.Image.open(r"C:\Users\NANDHIKA\AppData\Local\Programs\Python\Py
thon37\table booking.png") 
                bg=ImageTk.PhotoImage(ft,master=table) 
                bgt = Label(table,image=bg) 
                bgt.place(x=0, y=0, relwidth=1,relheight=1)                     
 
                #table config 
                table.title('BOOK TABLE') 
                table.geometry("1700x1000") 
                table.configure(bg="black") 
 
                #labels  
                l2=Label(table,text="Room no",font=("Lora", 
15),fg="#02baf2",bg='black') 
                r_no=Entry(table,width=20) 
                l4=Label(table,text="From Date",font=("Lora", 
15),fg="#02baf2",bg="black") 
                Label(table, text = "Pick timeslot", 
                                  font = ("Lora", 
15),fg="#02baf2",bg="black").place(relx=0.56,rely=0.52) 
                def tslot1(): 
                 global ts 
                 ts="8:00-11:00 am" 
                 return ts 
                def tslot2(): 
                 global ts 
                 ts="1:00-4:00 pm" 
                 return ts 
                def tslot3(): 
                 global ts 
                 ts="6:00-9:00 pm" 
                 return ts 
                ts1=Button(table,text="8:00-11:00 
am",bg="#02baf2",fg="black",command=tslot1) 
34 
 
                ts2=Button(table,text="1:00-4:00 
pm",bg="#02baf2",fg="black",command=tslot2) 
                ts3=Button(table,text="6:00-9:00 
pm",bg="#02baf2",fg="black",command=tslot3) 
                Label(table, text = "Party of(max: 80)", 
                font = ("Lora", 
15),fg="#02baf2",bg="black").place(relx=0.51,rely=0.635) 
                no_people=Entry(table,width=18) 
 
                #calendar 
                t_cal= Calendar(table, selectmode = 'day',year = 2024, month = 
2,day = 1) 
                def t_choose_date(): 
                    t_date.config(text=t_cal.get_date()) 
                b1=Button(table,text="choose 
date",bg="#02baf2",fg="black",command=t_choose_date) 
                t_date=Label(table,fg="#02baf2",bg="black",font=("Lora", 15)) 
 
                #sql- connection and bill page 
                def tbook(): 
                     import mysql.connector as m 
                     a=m.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
                     b=a.cursor() 
                     rno=r_no.get() 
                     td_raw=format(t_cal.get_date()) 
                     L=td_raw.split("/") 
                     if len(L[0])==1: 
                              L[0]="0"+L[0] 
                     if len(L[1])==1: 
                              L[1]="0"+L[1] 
                     td="20"+L[2]+"-"+L[0]+"-"+L[1] 
                     try: 
                       tno=int(no_people.get()) 
 
                     except Exception as e: 
                         messagebox.showinfo("OOPS!","Enter no of people") 
                     if tno==0: 
                        messagebox.showinfo("OOPS","enter no of people")  
                     else: 
35 
 
                        if tno%4==0: 
                          ntab=(tno)//4 
                        else: 
                         ntab=((tno)//4) + 1 
                         x=("SELECT COUNT(*) FROM RESTABLES WHERE 
TABLE_STATUS='NOT OCCUPIED' AND TDATE = %s AND TIMESLOT = 
%s") 
                         b.execute(x, (td,ts)) 
                         r=int(str(b.fetchone()[0])) 
                          
                         if ntab<=r: 
                             for i in range(0,ntab): 
                                  
                                 x=("SELECT MIN(TABLE_NO) FROM restables WHERE 
TABLE_STATUS='NOT OCCUPIED' AND TDATE = %s AND TIMESLOT = 
%s ") 
                                 b.execute(x,(td,ts)) 
                                 tano=int(str(b.fetchone()[0])) 
                                  
                                 x=("UPDATE restables SET 
TABLE_STATUS='OCCUPIED',PH_NO=%s WHERE TABLE_NO=%s AND 
TDATE=%s AND TIMESLOT = %s") 
                                 b.execute(x,(rno,tano,td,ts)) 
                                 a.commit() 
                             sql="INSERT INTO 
ORDER_STAY(ROOMNO,DATE,NO_OF_PEOPLE,TIMESLOT) 
VALUES(%s,%s,%s,%s)" 
                             val=(rno,td,tno,ts) 
                             b.execute(sql,val) 
                             a.commit() 
                             messagebox.showinfo("BOOKING","TABLE BOOKED") 
                b1.place(relx=0.34,rely=0.80) 
                ts1.place(relx=0.51,rely=0.58) 
                ts2.place(relx=0.58,rely=0.58) 
                ts3.place(relx=0.65,rely=0.58) 
                l2.place(relx=0.40,rely=0.40) 
                l4.place(relx=0.24,rely=0.50) 
                no_people.place(relx=0.63,rely=0.65) 
                t_date.place(relx=0.33,rely=0.50) 
                t_cal.place(relx=0.28,rely=0.57) 
36 
 
                b1.place(relx=0.34,rely=0.80) 
                r_no.place(relx=0.47,rely=0.42) 
 
                
book=Button(table,text="BOOK",command=tbook,bg="#02baf2",fg="black",hei
ght= 2, width=8) 
                book.place(relx=0.5,rely=0.87) 
                 
                table.mainloop() 
             
            def log(): 
                import mysql.connector as m 
                import datetime 
                top=Toplevel() 
                top.geometry("550x500") 
                top.configure(bg="black") 
                def get1(): 
                    #SQL 
                    #Insert and delete restables rows 
                    import mysql.connector as m 
                    import datetime 
                    a=m.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
                    b=a.cursor() 
                    rno=1 
                    #Enter a date in YYYY-MM-DD format' 
                    D1=(str(a1.get())) 
                    y, m, d = map(int, D1.split('-')) 
                    d1 = datetime.date(y, m, d) 
                    D2= str(b1.get()) 
                    y, m, d = map(int, D2.split('-')) 
                    d2 = datetime.date(y, m, d) 
                    startdate = d1 
                    enddate = d2 
                    #enter tslot in same format as in user code 
                    ts=c1.get() 
                    while rno<21: 
                        curdate = startdate 
                        while curdate <= enddate: 
                            formatted_date = str(curdate.strftime('%Y-%m-%d')) 
37 
 
                            query = f"INSERT INTO restables 
(TABLE_NO,TABLE_STATUS,TIMESLOT,TDATE) VALUES (%s,%s,%s,%s)" 
                            b.execute(query,(rno,'NOT OCCUPIED',ts,formatted_date)) 
                            curdate += datetime.timedelta(days=1) 
                            a.commit() 
                        rno+=1 
                def get2(): 
                    #delete logs 
                    #d1 format 2023-02-5  yyyy-mm-dd enter 1 date more than the 
month u wanted deleted 
                    a=m.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
                    b=a.cursor() 
                    de1=str(d1.get()) 
                    x=f"DELETE FROM restables WHERE TDATE<%s" 
                    b.execute(x,(de1,)) 
                    a.commit() 
                def get3(): 
                    #Insert and delta rooms rows 
                    #insert logs 
                    import mysql.connector as m 
                    import datetime 
                    a=mysql.connector.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
                    b=a.cursor() 
 
                    #Enter a date in YYYY-MM-DD format' 
                    D1= (str(e1.get())) 
                    y, m, d = map(int, D1.split('-')) 
                    d1 = datetime.date(y, m, d) 
                    D2=str(f1.get()) 
                    y, m, d = map(int, D2.split('-')) 
                    d2 = datetime.date(y, m, d) 
                    startdate = d1 
                    enddate = d2 
                    rty=(g1.get()) 
                    if rty=='P': 
                         
                        k=6 
                        rno=1 
38 
 
                        while rno<k: 
                            curdate = startdate 
                            while curdate <= enddate: 
                                formatted_date = str(curdate.strftime('%Y-%m-%d')) 
                                query = f"INSERT INTO ROOMS 
(ROOMTYPEID,ROOMNO,ROOMSTATUS,RDATE) VALUES 
(%s,%s,%s,%s)" 
                                b.execute(query,(rty,rno,'NOT 
OCCUPIED',formatted_date)) 
                                curdate += datetime.timedelta(days=1) 
                            a.commit() 
                            rno+=1 
                    elif rty=='K': 
                        k=16 
                        rno=6 
                        while rno<k: 
                            curdate = startdate 
                            while curdate <= enddate: 
                                formatted_date = str(curdate.strftime('%Y-%m-%d')) 
                                query = f"INSERT INTO ROOMS 
(ROOMTYPEID,ROOMNO,ROOMSTATUS,RDATE) VALUES 
(%s,%s,%s,%s)" 
                                b.execute(query,(rty,rno,'NOT 
OCCUPIED',formatted_date)) 
                                curdate += datetime.timedelta(days=1) 
                            a.commit() 
                            rno+=1 
 
                def get4(): 
                    #delete logs 
                    #d1 format 2023-02-5  yyyy-mm-dd enter 1 date more than the 
month u wanted deleted 
                    a=mysql.connector.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
                    b=a.cursor() 
                    de1=str(h1.get()) 
                    x=f"DELETE FROM ROOMS WHERE RDATE<%s" 
                    b.execute(x,(de1,)) 
                    a.commit() 
 
39 
 
                def get5(): 
                    #table booking delete rows 
                    a=mysql.connector.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
                    b=a.cursor() 
                    #enter date in YYYY-MM-DD in a  
                    tbd=str(i1.get()) 
                    x="DELETE FROM TABLE_BOOKING WHERE 
BOOKING_DATE<%s" 
                    b.execute(x,(tbd,)) 
                    x="DELETE FROM ORDER_STAY WHERE DATE<%s" 
                    b.execute(x,(tbd,)) 
                    x="DELETE FROM RBILL WHERE CHECKOUT<%s" 
                    b.execute(x,(tbd,)) 
                    a.commit() 
                but1=Button(top,text="create",command=get1) 
                but2=Button(top,text="del",command=get2) 
                but3=Button(top,text="create",command=get3) 
                but4=Button(top,text="del",command=get4) 
                but5=Button(top,text="del",command=get5) 
                a1=Entry(top,width=25) 
                b1=Entry(top,width=25) 
                c1=Entry(top,width=25) 
                d1=Entry(top,width=25) 
                e1=Entry(top,width=25) 
                f1=Entry(top,width=25) 
                g1=Entry(top,width=25) 
                h1=Entry(top,width=25) 
                i1=Entry(top,width=25) 
                a1.grid(row=0,column=27)  
                b1.grid(row=3,column=27)  
                c1.grid(row=5,column=27)  
                d1.grid(row=7,column=27) 
                e1.grid(row=9,column=27)  
                f1.grid(row=11,column=27) 
                g1.grid(row=15,column=27)  
                h1.grid(row=19,column=27) 
                i1.grid(row=21,column=27) 
                but1.grid(row=6,column=20) 
                but2.grid(row=8,column=20) 
40 
 
                but3.grid(row=16,column=20) 
                but4.grid(row=20,column=20) 
                but5.grid(row=22,column=20) 
                a12=Label(top,text="RESTABLES START 
DATE",fg="white",padx=59,pady=10,bg="black") 
                a22=Label(top,text="END 
DATE",fg="white",padx=71.5,pady=10,bg="black") 
                
a32=Label(top,text="TIMESLOT",fg="white",padx=56.5,pady=10,bg="black") 
                a42=Label(top,text="DEL BEFORE 
DATE",fg="white",padx=65,pady=10,bg="black") 
                a52=Label(top,text="ROOMS START 
DATE",fg="white",padx=59,pady=10,bg="black") 
                a62=Label(top,text="END 
DATE",fg="white",padx=71.5,pady=10,bg="black") 
                a72=Label(top,text="ROOM 
TYPE",fg="white",padx=56.5,pady=10,bg="black") 
                a82=Label(top,text="DEL BEFORE 
DATE",fg="white",padx=65,pady=10,bg="black") 
                a92=Label(top,text="RBILL,TBOOK,ORDER DEL BEFORE 
DATE",fg="white",padx=65,pady=10,bg="black") 
                a12.grid(row=0,column=0)  
                a22.grid(row=3,column=0)  
                a32.grid(row=5,column=0)  
                a42.grid(row=7,column=0) 
                a52.grid(row=9,column=0)  
                a62.grid(row=11,column=0)  
                a72.grid(row=15,column=0)  
                a82.grid(row=19,column=0) 
                a92.grid(row=21,column=0) 
                top.mainloop() 
 
            def cancellation(): 
                cancel=Toplevel() 
                #table config 
                cancel.title('CANCELLATION') 
                cancel.geometry("1700x1000") 
                cancel.configure(bg="black") 
41 
 
                
f=PIL.Image.open(r"C:\Users\NANDHIKA\AppData\Local\Programs\Python\Pyt
hon37\cancellation.png") 
                cancel.bg=ImageTk.PhotoImage(f,master=cancel) 
                bgc = Label(cancel,image=cancel.bg) 
                bgc.place(x=0, y=0, relwidth=1,relheight=1) 
                #labels_room 
                lrc=Label(cancel,text="ROOM CANCELLATION",font=("Lora", 
20),fg="#02baf2",bg="black") 
                ltc=Label(cancel,text="TABLE CANCELLATION",font=("Lora", 
20),fg="#02baf2",bg="black") 
                l2=Label(cancel,text="Phone no",font=("Lora", 
15),fg="#02baf2",bg='black') 
                name=Entry(cancel,width=15) 
                ph_no=Entry(cancel,width=20) 
                gmail=Entry(cancel,width=15) 
                l4=Label(cancel,text="From",font=("Lora", 
15),fg="#02baf2",bg="black") 
                l5=Label(cancel,text="To ",font=("Lora", 
15),fg="#02baf2",bg="black") 
                 
                #calendar 
                calfrom= Calendar(cancel, selectmode = 'day',year = 2024, month = 
2,day = 1) 
                def r_from_date(): 
                    from_date.config(text=calfrom.get_date()) 
                b1=Button(cancel,text="Choose 
date",bg="#02baf2",fg="black",command=r_from_date) 
                from_date=Label(cancel,fg="#02baf2",bg="black",font=("Lora", 15)) 
 
                calto = Calendar(cancel, selectmode = 'day',year = 2024, month = 
2,day = 1) 
                def choose_to_date(): 
                    To_date.config(text=calto.get_date()) 
                b2=Button(cancel,text="Choose 
date",command=choose_to_date,bg="#02baf2",fg="black") 
                To_date=Label(cancel,fg="#02baf2",bg="black",font=("Lora", 15)) 
                def cancel1(): 
                    import mysql.connector as m 
42 
 
                    a=m.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
                    b=a.cursor() 
                    rp=str(ph_no.get()) 
                    rdf_raw=format(calfrom.get_date()) 
                    rdt_raw=format(calto.get_date()) 
                    L1=rdf_raw.split("/") 
                    if len(L1[0])==1: 
                             L1[0]="0"+L1[0] 
                    if len(L1[1])==1: 
                             L1[1]="0"+L1[1] 
                    rdf="20"+L1[2]+"-"+L1[0]+"-"+L1[1] 
                    L2=rdt_raw.split("/") 
                    if len(L2[0])==1: 
                             L2[0]="0"+L2[0] 
                    if len(L2[1])==1: 
                             L2[1]="0"+L2[1] 
                    rdt="20"+L2[2]+"-"+L2[0]+"-"+L2[1] 
                    x=("DELETE FROM RBOOKING WHERE PHNO=%s AND 
(CHECKOUT = %s) AND (CHECKIN = %s)") 
                    b.execute(x,(rp,rdt,rdf)) 
                    x=("UPDATE ROOMS SET ROOMSTATUS='NOT 
OCCUPIED',PHNO=NULL WHERE PHNO=%s AND (RDATE >= %s ) AND 
(RDATE <= %s)" ) 
                    b.execute(x,(rp,rdf,rdt)) 
                    a.commit() 
                    messagebox.showinfo("CANCELLATION SUCCESS","Your room 
reservation is cancelled succesfully.") 
                
cancel1=Button(cancel,text="CANCEL",command=cancel1,bg="#02baf2",fg="
black",height= 2, width=8) 
                #place_room 
                lrc.place(relx=0.28,rely=0.28) 
                ltc.place(relx=0.66,rely=0.28) 
                l2.place(relx=0.30,rely=0.355) 
                l4.place(relx=0.16,rely=0.5) 
                l5.place(relx=0.40,rely=0.5) 
                ph_no.place(relx=0.39,rely=0.37) 
                from_date.place(relx=0.25,rely=0.50) 
                calfrom.place(relx=0.20,rely=0.57) 
43 
 
                b1.place(relx=0.25,rely=0.80) 
                To_date.place(relx=0.50,rely=0.50) 
                calto.place(relx=0.44,rely=0.57) 
                b2.place(relx=0.50,rely=0.80) 
                cancel1.place(relx=0.4,rely=0.87) 
 
                #labels_table 
                l1=Label(cancel,text="Room no",font=("Lora", 
15),fg="#02baf2",bg="black") 
                l2=Label(cancel,text="Chosen slot",font=("Lora", 
15),fg="#02baf2",bg="black") 
                l3=Label(cancel,text="Date",font=("Lora", 
15),fg="#02baf2",bg="black") 
                phno=Entry(cancel,width=20) 
                def tslot1(): 
                     global ts 
                     ts="8:00-11:00 am" 
                     return ts 
                def tslot2(): 
                     global ts 
                     ts="1:00-4:00 pm" 
                     return ts 
                def tslot3(): 
                     global ts 
                     ts="6:00-9:00 pm" 
                     return ts 
                ts1=Button(cancel,text="8:00-11:00 
am",bg="#02baf2",fg="black",command=tslot1) 
                ts2=Button(cancel,text="1:00-4:00 
pm",bg="#02baf2",fg="black",command=tslot2) 
                ts3=Button(cancel,text="6:00-9:00 
pm",bg="#02baf2",fg="black",command=tslot3) 
                #calendar 
                ct_cal= Calendar(cancel, selectmode = 'day',year = 2024, month = 
2,day = 1) 
                def ct_choose_date(): 
                    ct_date.config(text=ct_cal.get_date()) 
                bc=Button(cancel,text="choose 
date",bg="#02baf2",fg="black",command=ct_choose_date) 
                ct_date=Label(cancel,fg="#02baf2",bg="black",font=("Lora", 15)) 
44 
 
                def cancel2(): 
                    import mysql.connector as m 
                    a=m.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
                    b=a.cursor() 
                    tp=str(phno.get()) 
                    td_raw=format(ct_cal.get_date()) 
                    L=td_raw.split("/") 
                    if len(L[0])==1: 
                             L[0]="0"+L[0] 
                    if len(L[1])==1: 
                             L[1]="0"+L[1] 
                    td="20"+L[2]+"-"+L[0]+"-"+L[1] 
                    x=("SELECT NO_OF_PEOPLE FROM ORDER_STAY WHERE 
ROOMNO=%s AND DATE = %s AND TIMESLOT = %s") 
                    b.execute(x, (tp,td,ts)) 
                    rraw=(b.fetchone()) 
                     
                    r=int(str(rraw[0])) 
                    if r%4==0: 
                       ntab=(r)//4 
                    else: 
                       ntab=((r)//4) + 1 
                    x=("UPDATE restables SET TABLE_STATUS='NOT 
OCCUPIED',PH_NO=NULL WHERE TDATE=%s AND PH_NO=%s AND 
TIMESLOT = %s") 
                    b.execute(x,(td,tp,ts)) 
                    x=("DELETE FROM ORDER_STAY WHERE ROOMNO=%s AND 
DATE = %s AND TIMESLOT = %s") 
                    b.execute(x, (tp,td,ts)) 
                    a.commit() 
                    messagebox.showinfo("CANCELLATION SUCCESS","Your table 
reservation is cancelled succesfully.") 
                
cancel2=Button(cancel,text="CANCEL",command=cancel2,bg="#02baf2",fg="
black",height= 2, width=8) 
 
                #place_table 
                l1.place(relx=0.68,rely=0.355) 
                l2.place(relx=0.72,rely=0.41) 
45 
 
                l3.place(relx=0.66,rely=0.50) 
                phno.place(relx=0.75,rely=0.37) 
                ct_date.place(relx=0.73,rely=0.50) 
                ct_cal.place(relx=0.68,rely=0.57) 
                bc.place(relx=0.74,rely=0.80) 
                ts1.place(relx=0.66,rely=0.46) 
                ts2.place(relx=0.73,rely=0.46) 
                ts3.place(relx=0.80,rely=0.46) 
                cancel2.place(relx=0.74,rely=0.87) 
            
sq=Button(top,text="CANCELLATION",command=cancellation,bg="white",pad
y=10,padx=30) 
            sq.grid(row=310,column=100) 
            st=Button(top,text="LOG",command=log,bg="white",pady=10,padx=30) 
            st.grid(row=300,column=100) 
            sv=Button(top,text="TABLE 
BOOK",command=book_table,bg="white",pady=10,padx=30) 
            sv.grid(row=290,column=100) 
            sb=Button(top,text="TABLE 
BILL",command=tablebook,bg="white",pady=10,padx=30) 
            sb.grid(row=280,column=100) 
            
pt=Button(top,text="PAYMENT",command=payment,bg="white",pady=10,padx
=30) 
            pt.grid(row=270,column=100) 
            pk=Button(top,text="CHECK 
IN",command=checkinnow,bg="white",pady=10,padx=30) 
            pk.grid(row=220,column=100) 
            pf=Button(top,text="FOOD 
MENU",command=foodmenu,bg="white",pady=10,padx=22) 
            pf.grid(row=230,column=100) 
            pd=Button(top,text="PERSONAL 
INFO",command=info,bg="white",pady=10,padx=14) 
            pd.grid(row=240,column=100) 
            pc=Button(top,text="AVAILABLE 
ROOMS",command=availability,bg="white",pady=10,padx=7) 
            pc.grid(row=250,column=100)  
            pb=Button(top,text="CUSTOMER 
DETAILS",command=details,bg="white",pady=10,padx=7) 
            pb.grid(row=260,column=100) 
46 
 
    password=StringVar() 
    entry=Entry(top,width=50,textvariable=password,show="*") 
    entry.grid(row=0,column=0,columnspan=1) 
    
pa=Button(top,text="ENTER",command=show,padx=50,pady=10,bg="white") 
    pa.grid(row=1,column=0,columnspan=1) 
 
#USER 
def user(): 
    main=Tk() 
    mainframe = Frame(main,bg="black") 
    mainframe.pack() 
     
    #main config 
    sw=main.winfo_screenwidth() 
    sh=main.winfo_screenheight() 
    str1=str(sw)+"x"+str(sh) 
    main.geometry(str1) 
    frame1=Frame(main,bg="black") 
    frame1.pack(fill="both",expand=True) 
    framebar=Frame(frame1,bg="black") 
    framebar.place(relx=0,rely=0,relwidth=1,relheight=0.1,anchor=NW) 
    
f=PIL.Image.open(r"C:\Users\NANDHIKA\AppData\Local\Programs\Python\Pyt
hon37\frontpage.png") 
    fu=f.resize((1580,710),Image.LANCZOS) 
    bg=ImageTk.PhotoImage(fu,master=main) 
    bgt = Label(main,image=bg) 
    bgt.place(relx=0.0, rely=0.1) 
    #logo 
    
logoimg_=PIL.Image.open(r"C:\Users\NANDHIKA\AppData\Local\Programs\P
ython\Python37\logo.png") 
    logoimg__=logoimg_.resize((190,162),Image.LANCZOS) 
    lg=ImageTk.PhotoImage(logoimg__,master=framebar) 
    lgu = Label(framebar,image=lg) 
    lgu.place(x=0.5, y=0.8, relwidth=0.09,relheight=0.9) 
 
    #book now button 
47 
 
    booknowbutton=Menubutton(framebar,text="BOOK 
NOW",bg="#5ce1e6",fg="black",font=("Times New 
Roman",16),relief=SOLID,borderwidth=0) 
    
booknowbutton.place(relx=0.9,rely=0.5,relwidth=0.1,relheight=0.8,anchor=CE
NTER) 
    booknowbutton.menu=Menu(booknowbutton, tearoff=0, fg="#5ce1e6", 
bg="black", font=("Times New Roman", 14), relief="flat", borderwidth=0) 
    booknowbutton["menu"] = booknowbutton.menu 
 
    #contact button 
    
contactbutton=Menubutton(framebar,text="CONTACT",bg="#5ce1e6",fg="blac
k",font=("Times New Roman",16),relief=SOLID,borderwidth=0) 
    
contactbutton.place(relx=0.78,rely=0.5,relwidth=0.1,relheight=0.8,anchor=CEN
TER) 
    
contactbutton.menu=Menu(contactbutton,tearoff=0,fg="#5ce1e6",bg="black",fo
nt=("Times New Roman",14),relief="flat",borderwidth=0) 
    contactbutton["menu"]=contactbutton.menu 
    contactbutton.menu.add_checkbutton(label="+91 98409 90018") 
    contactbutton.menu.add_checkbutton(label="info.bluewaves@gmail.com") 
     
    def room_booking(): 
 
        #room config 
        room=Toplevel(main) 
        room.title('BLUE WAVES HOTEL') 
        room.geometry("1700x1000") 
        room.configure(bg="black") 
        
fr=PIL.Image.open(r"C:\Users\NANDHIKA\AppData\Local\Programs\Python\Py
thon37\room booking.png") 
        bg=ImageTk.PhotoImage(fr,master=room) 
        bgr = Label(room,image=bg) 
        bgr.place(x=0, y=0, relwidth=1,relheight=1) 
        #labels 
        l1=Label(room,text="Name",font=("Lora", 15),fg="#02baf2",bg="black") 
        l2=Label(room,text="Phone no",font=("Lora", 15),fg="#02baf2",bg='black') 
48 
 
        l3=Label(room,text="Gmail",font=("Lora", 15),fg="#02baf2",bg="black") 
        name=Entry(room,width=20) 
        ph_no=Entry(room,width=20) 
        gmail=Entry(room,width=20) 
        l4=Label(room,text="From",font=("Lora", 15),fg="#02baf2",bg="black") 
        l5=Label(room,text="To ",font=("Lora", 15),fg="#02baf2",bg="black") 
        l6=Label(room,text="KING SUITE",font=("Lora", 
15),fg="#02baf2",bg="black") 
        l7=Label(room,text="PREMIUM SUITE",font=("Lora", 
15),fg="#02baf2",bg="black") 
        l8=Label(room,text="Size:45-47 square metres\n  Occupancy: 2 adults +1 
\n Bedding: 2 king bed\n Amenities: Balcony, TV,Wi-Fi,\n Iron, Hair Dryer, 24
Hours Room Service",font=("Lora", 13),fg="#02baf2",bg="black") 
        l9=Label(room,text="Size: 101 square metres \n Occupancy:3 adults + 2, 
Bedding: 2 King beds \n Amenities: Balcony,TV, Breakfast,space,walk-in 
closet,\n billiards board, Sitting Area, Internet Access Wi-Fi,\n  Iron, Hair Dryer, 
24-Hours Room Service",font=("Lora", 13),fg="#02baf2",bg="black") 
        Label(room, text = "Choose no of rooms (Max:10)", 
                  font = ("Lora", 
15),fg="#02baf2",bg="black").place(relx=0.67,rely=0.54) 
        no_r1=Entry(room,width=20) 
        Label(room, text = "Choose no of rooms (Max:5)",  
                  font = ("Lora", 15),fg="#02baf2",bg="black").place( 
relx=0.67,rely=0.82) 
        no_r2=Entry(room,width=20) 
 
        #calendar 
        calfrom= Calendar(room, selectmode = 'day',year = 2024, month = 2,day 
= 1) 
        def r_from_date(): 
            from_date.config(text=calfrom.get_date()) 
        b1=Button(room,text="Choose 
date",bg="#02baf2",fg="black",command=r_from_date) 
        from_date=Label(room,fg="#02baf2",bg="black",font=("Lora", 15)) 
 
        calto = Calendar(room, selectmode = 'day',year = 2024, month = 2,day = 
1) 
        def choose_to_date(): 
            To_date.config(text=calto.get_date()) 
49 
 
        b2=Button(room,text="Choose 
date",command=choose_to_date,bg="#02baf2",fg="black") 
        To_date=Label(room,fg="#02baf2",bg="black",font=("Lora", 15)) 
        #sql- connection and bill page 
        def rbook(): 
            import mysql.connector as m 
            a=m.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
            b=a.cursor() 
            rn=name.get() 
            rp=ph_no.get() 
            rg=gmail.get() 
            rdf_raw=format(calfrom.get_date()) 
            rdt_raw=format(calto.get_date()) 
            L1=rdf_raw.split("/") 
            if len(L1[0])==1: 
                     L1[0]="0"+L1[0] 
            if len(L1[1])==1: 
                     L1[1]="0"+L1[1] 
            rdf="20"+L1[2]+"-"+L1[0]+"-"+L1[1] 
            L2=rdt_raw.split("/") 
            if len(L2[0])==1: 
                     L2[0]="0"+L2[0] 
            if len(L2[1])==1: 
                     L2[1]="0"+L2[1] 
            rdt="20"+L2[2]+"-"+L2[0]+"-"+L2[1] 
             
            try: 
               rt1=int(no_r1.get()) 
 
            except Exception as e: 
                 messagebox.showinfo("OOPS!","Enter room no") 
            try: 
               rt2=int(no_r2.get()) 
 
            except Exception as e: 
                 messagebox.showinfo("OOPS!","Enter no of rooms") 
            if rt1==0 and rt2==0: 
                messagebox.showinfo("OOPS!","0 rooms not valid \n enter number 
in atleast 1 suite") 
50 
 
            else: 
                    if int(L2[0])==int(L1[0]): 
                        d=int(L2[1])-int(L1[1]) +1 
                    elif int(L2[0])-int(L1[0])==1: 
                        if int(L1[0])  in (1,3,5,7,8,9,10,12): 
                            d=31 - int(L1[1]) +1 + int(L2[1]) 
                        elif int(L1[0])==2 and int(L1[2])%4!=0: 
                            d=28 - int(L1[1]) +1 + int(L2[1]) 
                        elif int(L1[0])==2 and int(L1[2])%4==0: 
                            d=29 - int(L1[1]) +1 + int(L2[1]) 
                        else: 
                            d=30 - int(L1[1]) +1 + int(L2[1]) 
                    else: 
                        d=60 
                    if d<59: 
                         
                        x=("SELECT ROOMNO FROM ROOMS WHERE 
ROOMTYPEID='K' AND ROOMSTATUS='NOT OCCUPIED' AND RDATE 
BETWEEN %s AND %s") 
                        b.execute(x,(rdf,rdt)) 
                        rraw=(b.fetchall()) 
                         
                        LKA=[] 
                        for i in rraw: 
                            if rraw.count(i)==d: 
                                if i not in LKA: 
                                  LKA.append(i) 
                        check1=len(LKA) 
                        
                        x=("SELECT ROOMNO FROM ROOMS WHERE 
ROOMTYPEID='P' AND ROOMSTATUS='NOT OCCUPIED' AND RDATE 
BETWEEN %s AND %s") 
                        b.execute(x,(rdf,rdt)) 
                        rraw=(b.fetchall()) 
                         
                        LPA=[] 
                        for i in rraw: 
                            if rraw.count(i)==d: 
                                if i not in LPA: 
                                  LPA.append(i) 
51 
 
                        check2=len(LPA) 
                         
                        if int(rt1) <=check1 and int(rt2) <=check2: 
                            b.execute("SELECT RATE FROM 
ROOMS_MASTER_TABLE WHERE ROOMTYPEID='K'") 
                            rt1co=float(str(b.fetchone()[0])) 
                            b.execute("SELECT RATE FROM 
ROOMS_MASTER_TABLE WHERE ROOMTYPEID='P'") 
                            rt2co=float(str(b.fetchone()[0])) 
                            sco1=d*rt1co 
                            sco2=d*rt2co 
                            sco=d*(rt1*rt1co+rt2*rt2co) 
                            L=[6,7,8,9,10,11,12,13,14,15] 
                            Lk=[] 
                            x=("SELECT ROOMNO FROM ROOMS WHERE 
ROOMSTATUS='NOT OCCUPIED' AND ROOMTYPEID='K' AND  (RDATE 
>=%s) AND  (RDATE <=%s) ") 
                            b.execute(x,(rdf,rdt)) 
                            rraw=(b.fetchall()) 
                            for i in rraw: 
                                if i[0] in L: 
                                    if i[0] not in Lk: 
                                        Lk.append(i[0]) 
                             
                            for i in Lk[0:rt1]: 
                                    rno1=int(i) 
                                    x=("UPDATE ROOMS SET PHNO=%s WHERE 
ROOMNO=%s AND ROOMTYPEID='K' AND  ((RDATE >= %s ) AND (RDATE 
<= %s))" ) 
                                    b.execute(x,(rp,rno1,rdf,rdt)) 
                                    sql="INSERT INTO 
RBOOKING(ROOMNO,ROOMTYPEID,NAME,PHNO,EMAILID,CHECKIN,CH
ECKOUT,SCOST) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)" 
                                    val=(rno1,'K',rn,rp,rg,rdf,rdt,sco1) 
                                    b.execute(sql,val) 
                                    sql="INSERT INTO 
RBILL(ROOMNO,SCOST,CHECKOUT) VALUES(%s,%s,%s)" 
                                    val=(rno1,sco1,rdt) 
                                    b.execute(sql,val) 
                                    a.commit() 
52 
 
                            x=("UPDATE ROOMS SET ROOMSTATUS='OCCUPIED' 
WHERE ROOMSTATUS='NOT OCCUPIED'  AND ROOMTYPEID='K' AND 
PHNO=%s AND (RDATE > %s ) AND (RDATE < %s)" ) 
                            b.execute(x,(rp,rdf,rdt)) 
                            x=("UPDATE ROOMS SET ROOMSTATUS='OCCUPIED' 
WHERE ROOMSTATUS='NOT OCCUPIED'  AND ROOMTYPEID='K' AND 
PHNO=%s AND (RDATE = %s ) " ) 
                            b.execute(x,(rp,rdf)) 
                            x=("UPDATE ROOMS SET ROOMSTATUS='OCCUPIED' 
WHERE ROOMSTATUS='NOT OCCUPIED'  AND ROOMTYPEID='K' AND 
PHNO=%s AND (RDATE = %s ) " ) 
                            b.execute(x,(rp,rdt)) 
                            a.commit() 
                            L=[1,2,3,4,5] 
                            Lp=[] 
                            x=("SELECT ROOMNO FROM ROOMS WHERE 
ROOMSTATUS='NOT OCCUPIED' AND ROOMTYPEID='P' AND  (RDATE 
>=%s) AND  (RDATE <=%s) ") 
                            b.execute(x,(rdf,rdt)) 
                            rraw=(b.fetchall()) 
                            for i in rraw: 
                                if i[0] in L: 
                                    if i[0] not in Lp: 
                                        Lp.append(i[0]) 
                             
                            for i in Lp[0:rt2]: 
                                    rno2=int(i) 
                                    x=("UPDATE ROOMS SET PHNO=%s WHERE 
ROOMNO=%s AND ROOMTYPEID='P' AND  (RDATE >= %s ) AND (RDATE 
<= %s)" ) 
                                    b.execute(x,(rp,rno2,rdf,rdt)) 
                                    sql="INSERT INTO 
RBOOKING(ROOMNO,ROOMTYPEID,NAME,PHNO,EMAILID,CHECKIN,CH
ECKOUT,SCOST) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)" 
                                    val=(rno2,'P',rn,rp,rg,rdf,rdt,sco2) 
                                    b.execute(sql,val) 
                                    sql="INSERT INTO 
RBILL(ROOMNO,SCOST,CHECKOUT) VALUES(%s,%s,%s)" 
                                    val=(rno2,sco2,rdt) 
                                    b.execute(sql,val) 
53 
 
                                    a.commit() 
                            x=("UPDATE ROOMS SET ROOMSTATUS='OCCUPIED' 
WHERE ROOMSTATUS='NOT OCCUPIED'  AND ROOMTYPEID='P' AND 
PHNO=%s AND (RDATE > %s ) AND (RDATE < %s)" ) 
                            b.execute(x,(rp,rdf,rdt)) 
                            a.commit() 
                            x=("UPDATE ROOMS SET ROOMSTATUS='OCCUPIED' 
WHERE ROOMSTATUS='NOT OCCUPIED'  AND ROOMTYPEID='P' AND 
PHNO=%s AND (RDATE = %s ) " ) 
                            b.execute(x,(rp,rdf)) 
                            a.commit() 
                            x=("UPDATE ROOMS SET ROOMSTATUS='OCCUPIED' 
WHERE ROOMSTATUS='NOT OCCUPIED'  AND ROOMTYPEID='P' AND 
PHNO=%s AND (RDATE = %s ) " ) 
                            b.execute(x,(rp,rdt)) 
                            a.commit() 
                             
                            rbill = Toplevel(room) 
                            rbill.title("STAY TABLE BILL") 
                            rbill.geometry("200x200") 
                            rbill.configure(bg="black") 
                            Label(rbill, text ="BILL",fg="#02baf2",bg="black",font=("Lora", 
20)).place(relx=0.4,rely=0.1) 
                            l1=Label(rbill,text="Name",font=("Lora", 
15),fg="#02baf2",bg="black").place(relx=0.2,rely=0.2) 
                            l2=Label(rbill,text="Phone no",font=("Lora", 
15),fg="#02baf2",bg='black').place(relx=0.2,rely=0.3) 
                            l3=Label(rbill,text="Gmail",font=("Lora", 
15),fg="#02baf2",bg="black").place(relx=0.2,rely=0.4) 
                            l4=Label(rbill,text="From",font=("Lora", 
15),fg="#02baf2",bg="black").place(relx=0.2,rely=0.5) 
                            l5=Label(rbill,text="To",font=("Lora", 
15),fg="#02baf2",bg="black").place(relx=0.2,rely=0.6) 
                            l6=Label(rbill,text="King suite",font=("Lora", 
15),fg="#02baf2",bg="black").place(relx=0.2,rely=0.7) 
                            l7=Label(rbill,text="Premium suite",font=("Lora", 
15),fg="#02baf2",bg="black").place(relx=0.2,rely=0.8) 
                            l8=Label(rbill,text="Total Cost(Pay after stay)",font=("Lora", 
15),fg="#02baf2",bg="black").place(relx=0.2,rely=0.9) 
54 
 
                            a1=Label(rbill,text=rn,font=("Lora", 
15),fg="#02baf2",bg="black").place(relx=0.5,rely=0.2) 
                            a2=Label(rbill,text=rp,font=("Lora", 
15),fg="#02baf2",bg='black').place(relx=0.5,rely=0.3) 
                            a3=Label(rbill,text=rg,font=("Lora", 
15),fg="#02baf2",bg="black").place(relx=0.5,rely=0.4) 
                            a4=Label(rbill,text=rdf,font=("Lora", 
15),fg="#02baf2",bg="black").place(relx=0.5,rely=0.5) 
                            a5=Label(rbill,text=rdt,font=("Lora", 
15),fg="#02baf2",bg="black").place(relx=0.5,rely=0.6) 
                            a6=Label(rbill,text=rt1,font=("Lora", 
15),fg="#02baf2",bg="black").place(relx=0.5,rely=0.7) 
                            a7=Label(rbill,text=rt2,font=("Lora", 
15),fg="#02baf2",bg="black").place(relx=0.5,rely=0.8) 
                            a8=Label(rbill,text=sco,font=("Lora", 
15),fg="#02baf2",bg="black").place(relx=0.5,rely=0.9) 
                        else: 
                            messagebox.showinfo("OOPS","rooms unavailable \n 
choose other dates") 
                    else: 
                        messagebox.showinfo("OOPS!","maximum stay limit= 59 
days")                 
                          
                 
             
        
book=Button(room,text="BOOK",command=rbook,bg="#02baf2",fg="black",hei
ght= 2, width=8) 
 
        #place 
        l1.place(anchor=NW,relx=0.01,rely=0.355) 
        l2.place(relx=0.25,rely=0.355) 
        l3.place(relx=0.01,rely=0.425) 
        l4.place(relx=0.01,rely=0.5) 
        l5.place(relx=0.25,rely=0.5) 
        l6.place(anchor=NW,relx=0.5,rely=0.355) 
        l7.place(relx=0.5,rely=0.58) 
        l8.place(relx=0.68,rely=0.38) 
        l9.place(relx=0.67,rely=0.64) 
        name.place(relx=0.08,rely=0.37) 
55 
 
        ph_no.place(relx=0.34,rely=0.37) 
        gmail.place(relx=0.08,rely=0.43) 
        from_date.place(relx=0.10,rely=0.50) 
        calfrom.place(relx=0.05,rely=0.57) 
        b1.place(relx=0.10,rely=0.80) 
        To_date.place(relx=0.35,rely=0.50) 
        calto.place(relx=0.29,rely=0.57) 
        b2.place(relx=0.35,rely=0.80) 
        no_r1.place(relx=0.86,rely=0.56) 
        no_r2.place(relx=0.86,rely=0.84) 
        book.place(relx=0.5,rely=0.87) 
        room.mainloop() 
    
booknowbutton.menu.add_checkbutton(label="ROOM",command=room_booki
ng) 
    def table_booking(): 
        table=Toplevel(main) 
        #table config 
        table.title('TABLE RESERVATION') 
        table.geometry("1700x1000") 
        table.configure(bg="black") 
        #page background 
        
ft=PIL.Image.open(r"C:\Users\NANDHIKA\AppData\Local\Programs\Python\Py
thon37\table booking.png") 
        bg=ImageTk.PhotoImage(ft,master=table) 
        bgt = Label(table,image=bg) 
        bgt.place(x=0, y=0, relwidth=1,relheight=1) 
         
 
        #labels 
        l1=Label(table,text="Name",font=("Lora", 15),fg="#02baf2",bg="black") 
        l2=Label(table,text="Phone no",font=("Lora", 15),fg="#02baf2",bg='black') 
        l3=Label(table,text="Gmail",font=("Lora", 15),fg="#02baf2",bg="black") 
        name=Entry(table,width=20) 
        ph_no=Entry(table,width=20) 
        gmail=Entry(table,width=20) 
        l4=Label(table,text="Pick Date",font=("Lora", 15),fg="#02baf2",bg="black") 
        Label(table, text = "Pick timeslot", 
        font = ("Lora", 15),fg="#02baf2",bg="black").place(relx=0.56,rely=0.52) 
56 
 
        def tslot1(): 
            global ts 
            ts="8:00-11:00 am" 
            return ts 
        def tslot2(): 
            global ts 
            ts="1:00-4:00 pm" 
            return ts 
        def tslot3(): 
            global ts 
            ts="6:00-9:00 pm" 
            return ts 
        ts1=Button(table,text="8:00-11:00 
am",bg="#02baf2",fg="black",command=tslot1) 
        ts2=Button(table,text="1:00-4:00 
pm",bg="#02baf2",fg="black",command=tslot2) 
        ts3=Button(table,text="6:00-9:00 
pm",bg="#02baf2",fg="black",command=tslot3) 
        Label(table, text = "No of people (max: 80)", 
        font = ("Lora", 15),fg="#02baf2",bg="black").place(relx=0.51,rely=0.635) 
        no_people=Entry(table,width=17) 
 
        #calendar 
        t_cal= Calendar(table, selectmode = 'day',year = 2024, month = 2,day = 
1) 
        def t_choose_date(): 
            t_date.config(text=t_cal.get_date()) 
        b1=Button(table,text="choose 
date",bg="#02baf2",fg="black",command=t_choose_date) 
        t_date=Label(table,fg="#02baf2",bg="black",font=("Lora", 15)) 
        #sql- connection and bill page 
        def tbook(): 
            import mysql.connector as m 
            a=m.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
            b=a.cursor() 
            tn=name.get() 
            tp=ph_no.get() 
            tg=gmail.get() 
            td_raw=format(t_cal.get_date()) 
57 
 
            L=td_raw.split("/") 
            if len(L[0])==1: 
                  L[0]="0"+L[0] 
            if len(L[1])==1: 
                  L[1]="0"+L[1] 
            td="20"+L[2]+"-"+L[0]+"-"+L[1] 
            try: 
               tno=int(no_people.get()) 
               print(tno) 
               if tno==0: 
                  messagebox.showinfo("OOPS","Enter no of people")  
 
            except Exception as e: 
                 messagebox.showinfo("OOPS!","Enter no of people") 
             
            else: 
             if tno%4==0: 
                 ntab=(tno)//4 
             else: 
                 ntab=((tno)//4) + 1 
                 print(ntab) 
             x=("SELECT COUNT(*) FROM restables WHERE 
TABLE_STATUS='NOT OCCUPIED' AND TDATE = %s AND TIMESLOT = 
%s") 
             b.execute(x, (td,ts)) 
             print(ts) 
             r=int(str(b.fetchone()[0])) 
             print(r) 
             if ntab<=r: 
                 for i in range(0,ntab): 
                     x=("SELECT MIN(TABLE_NO) FROM restables WHERE 
TABLE_STATUS='NOT OCCUPIED' AND TDATE = %s AND TIMESLOT = 
%s ") 
                     b.execute(x,(td,ts)) 
                     rno=int(str(b.fetchone()[0])) 
                     x=("UPDATE restables SET 
TABLE_STATUS='OCCUPIED',PH_NO=%s WHERE TABLE_NO=%s AND 
TDATE=%s AND TIMESLOT = %s") 
                     b.execute(x,(tp,rno,td,ts)) 
58 
 
                 sql="INSERT INTO 
TABLE_BOOKING(NAME,PH_NO,GMAIL,BOOKING_DATE,NO_OF_PEOPL
E,TIMESLOT) VALUES(%s,%s,%s,%s,%s,%s)" 
                 val=(tn,tp,tg,td,tno,ts) 
                 b.execute(sql,val) 
                 a.commit() 
                 tbill = Toplevel(table) 
                 tbill.title("TABLE BILL") 
                 tbill.geometry("200x200") 
                 tbill.configure(bg="black") 
                 Label(tbill, text ="TABLE 
RESERVATION",fg="#02baf2",bg="black",font=("Lora", 
20)).place(relx=0.4,rely=0.1) 
                 l1=Label(tbill,text="Name",font=("Lora", 
15),fg="#02baf2",bg="black").place(relx=0.2,rely=0.3) 
                 l2=Label(tbill,text="Phone no",font=("Lora", 
15),fg="#02baf2",bg='black').place(relx=0.2,rely=0.4) 
                 l3=Label(tbill,text="Gmail",font=("Lora", 
15),fg="#02baf2",bg="black").place(relx=0.2,rely=0.5) 
                 l4=Label(tbill,text="Date",font=("Lora", 
15),fg="#02baf2",bg="black").place(relx=0.2,rely=0.6) 
                 l5=Label(tbill,text="Timeslot",font=("Lora", 
15),fg="#02baf2",bg="black").place(relx=0.2,rely=0.7) 
                 l6=Label(tbill,text="No of people",font=("Lora", 
15),fg="#02baf2",bg="black").place(relx=0.2,rely=0.8) 
                 a1=Label(tbill,text=tn,font=("Lora", 
15),fg="#02baf2",bg="black").place(relx=0.5,rely=0.3) 
                 a2=Label(tbill,text=tp,font=("Lora", 
15),fg="#02baf2",bg='black').place(relx=0.5,rely=0.4) 
                 a3=Label(tbill,text=tg,font=("Lora", 
15),fg="#02baf2",bg="black").place(relx=0.5,rely=0.5) 
                 a4=Label(tbill,text=td,font=("Lora", 
15),fg="#02baf2",bg="black").place(relx=0.5,rely=0.6) 
                 a5=Label(tbill,text=ts,font=("Lora", 
15),fg="#02baf2",bg="black").place(relx=0.5,rely=0.7) 
                 a6=Label(tbill,text=tno,font=("Lora", 
15),fg="#02baf2",bg="black").place(relx=0.5,rely=0.8) 
             else: 
                 messagebox.showinfo("OOPS","Not enough tables! \n choose 
different date or timeslot")  
59 
 
        
book=Button(table,text="BOOK",command=tbook,bg="#02baf2",fg="black",hei
ght= 2, width=8) 
                
        def menu(): 
            menu = Toplevel(table) 
            menu.title("MENU") 
            menu.geometry("590x990") 
            menu.configure(bg="black") 
            
fm=PIL.Image.open(r"C:\Users\NANDHIKA\AppData\Local\Programs\Python\P
ython37\menu.png") 
            bg=ImageTk.PhotoImage(fm,master=menu) 
            bgm = Label(menu,image=bg) 
            bgm.place(x=0, y=0, relwidth=1,relheight=1) 
            menubg.place(relx=0,rely=0,anchor=NW,relheight=1,relwidth=1) 
        menu=Button(table,text="view 
menu",command=menu,fg="black",bg="#02baf2",height= 1, width=8) 
 
        #place 
        l1.place(anchor=NW,relx=0.2,rely=0.39) 
        l2.place(relx=0.38,rely=0.39) 
        l3.place(relx=0.6,rely=0.39) 
        l4.place(relx=0.20,rely=0.5) 
        name.place(relx=0.25,rely=0.4) 
        ph_no.place(relx=0.47,rely=0.4) 
        gmail.place(relx=0.68,rely=0.4) 
        t_date.place(relx=0.33,rely=0.50) 
        t_cal.place(relx=0.28,rely=0.57) 
        b1.place(relx=0.34,rely=0.80) 
        ts1.place(relx=0.51,rely=0.58) 
        ts2.place(relx=0.58,rely=0.58) 
        ts3.place(relx=0.65,rely=0.58) 
        no_people.place(relx=0.66,rely=0.65) 
        book.place(relx=0.5,rely=0.87) 
        menu.place(relx=0.59,rely=0.72) 
        table.mainloop() 
 
                
60 
 
    
booknowbutton.menu.add_checkbutton(label="TABLE",command=table_booki
ng) 
    def cancel(): 
        cancel=Toplevel(main) 
        #table config 
        cancel.title('CANCELLATION') 
        cancel.geometry("1700x1000") 
        cancel.configure(bg="black") 
        
f=PIL.Image.open(r"C:\Users\NANDHIKA\AppData\Local\Programs\Python\Pyt
hon37\cancellation.png") 
        cancel.bg=ImageTk.PhotoImage(f,master=cancel) 
        bgc = Label(cancel,image=cancel.bg) 
        bgc.place(x=0, y=0, relwidth=1,relheight=1) 
        #labels_room 
        lrc=Label(cancel,text="ROOM CANCELLATION",font=("Lora", 
20),fg="#02baf2",bg="black") 
        ltc=Label(cancel,text="TABLE CANCELLATION",font=("Lora", 
20),fg="#02baf2",bg="black") 
         
        l2=Label(cancel,text="Phone no",font=("Lora", 
15),fg="#02baf2",bg='black') 
         
        name=Entry(cancel,width=15) 
        ph_no=Entry(cancel,width=20) 
        gmail=Entry(cancel,width=15) 
        l4=Label(cancel,text="From",font=("Lora", 15),fg="#02baf2",bg="black") 
        l5=Label(cancel,text="To ",font=("Lora", 15),fg="#02baf2",bg="black") 
         
        #calendar 
        calfrom= Calendar(cancel, selectmode = 'day',year = 2024, month = 
2,day = 1) 
        def r_from_date(): 
            from_date.config(text=calfrom.get_date()) 
        b1=Button(cancel,text="Choose 
date",bg="#02baf2",fg="black",command=r_from_date) 
        from_date=Label(cancel,fg="#02baf2",bg="black",font=("Lora", 15)) 
 
61 
 
        calto = Calendar(cancel, selectmode = 'day',year = 2024, month = 2,day = 
1) 
        def choose_to_date(): 
            To_date.config(text=calto.get_date()) 
        b2=Button(cancel,text="Choose 
date",command=choose_to_date,bg="#02baf2",fg="black") 
        To_date=Label(cancel,fg="#02baf2",bg="black",font=("Lora", 15)) 
        def cancel1(): 
            import mysql.connector as m 
            a=m.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
            b=a.cursor() 
            rp=str(ph_no.get()) 
            rdf_raw=format(calfrom.get_date()) 
            rdt_raw=format(calto.get_date()) 
            L1=rdf_raw.split("/") 
            if len(L1[0])==1: 
                     L1[0]="0"+L1[0] 
            if len(L1[1])==1: 
                     L1[1]="0"+L1[1] 
            rdf="20"+L1[2]+"-"+L1[0]+"-"+L1[1] 
            L2=rdt_raw.split("/") 
            if len(L2[0])==1: 
                     L2[0]="0"+L2[0] 
            if len(L2[1])==1: 
                     L2[1]="0"+L2[1] 
            rdt="20"+L2[2]+"-"+L2[0]+"-"+L2[1] 
            x=("DELETE FROM RBOOKING WHERE PHNO=%s AND (CHECKIN 
= %s) AND (CHECKOUT = %s)") 
            b.execute(x,(rp,rdf,rdt)) 
            x=("UPDATE ROOMS SET ROOMSTATUS='NOT 
OCCUPIED',PHNO=NULL WHERE PHNO=%s AND (RDATE >= %s ) AND 
(RDATE <= %s)" ) 
            b.execute(x,(rp,rdf,rdt)) 
            a.commit() 
            messagebox.showinfo("CANCELLATION SUCCESS","Your room 
reservation is cancelled succesfully.") 
        
cancel1=Button(cancel,text="CANCEL",command=cancel1,bg="#02baf2",fg="
black",height= 2, width=8) 
62 
 
        #place_room 
        lrc.place(relx=0.28,rely=0.28) 
        ltc.place(relx=0.66,rely=0.28) 
        l2.place(relx=0.30,rely=0.355) 
        l4.place(relx=0.16,rely=0.5) 
        l5.place(relx=0.40,rely=0.5) 
        ph_no.place(relx=0.39,rely=0.37) 
        from_date.place(relx=0.25,rely=0.50) 
        calfrom.place(relx=0.20,rely=0.57) 
        b1.place(relx=0.25,rely=0.80) 
        To_date.place(relx=0.50,rely=0.50) 
        calto.place(relx=0.44,rely=0.57) 
        b2.place(relx=0.50,rely=0.80) 
        cancel1.place(relx=0.4,rely=0.87) 
 
        #labels_table 
        l1=Label(cancel,text="Phone no",font=("Lora", 
15),fg="#02baf2",bg="black") 
        l2=Label(cancel,text="Chosen slot",font=("Lora", 
15),fg="#02baf2",bg="black") 
        l3=Label(cancel,text="Date",font=("Lora", 15),fg="#02baf2",bg="black") 
        phno=Entry(cancel,width=20) 
        def tslot1(): 
             global ts 
             ts="8:00-11:00 am" 
             return ts 
        def tslot2(): 
             global ts 
             ts="1:00-4:00 pm" 
             return ts 
        def tslot3(): 
             global ts 
             ts="6:00-9:00 pm" 
             return ts 
        ts1=Button(cancel,text="8:00-11:00 
am",bg="#02baf2",fg="black",command=tslot1) 
        ts2=Button(cancel,text="1:00-4:00 
pm",bg="#02baf2",fg="black",command=tslot2) 
        ts3=Button(cancel,text="6:00-9:00 
pm",bg="#02baf2",fg="black",command=tslot3) 
63 
 
        #calendar 
        ct_cal= Calendar(cancel, selectmode = 'day',year = 2024, month = 2,day 
= 1) 
        def ct_choose_date(): 
            ct_date.config(text=ct_cal.get_date()) 
        bc=Button(cancel,text="choose 
date",bg="#02baf2",fg="black",command=ct_choose_date) 
        ct_date=Label(cancel,fg="#02baf2",bg="black",font=("Lora", 15)) 
        def cancel2(): 
            import mysql.connector as m 
            a=m.connect(host="localhost",user="root", 
password="root",database="hotel_management") 
            b=a.cursor() 
            tp=str(phno.get()) 
            td_raw=format(ct_cal.get_date()) 
            L=td_raw.split("/") 
            if len(L[0])==1: 
                     L[0]="0"+L[0] 
            if len(L[1])==1: 
                     L[1]="0"+L[1] 
            td="20"+L[2]+"-"+L[0]+"-"+L[1] 
            x=("SELECT NO_OF_PEOPLE FROM TABLE_BOOKING WHERE 
PH_NO=%s AND BOOKING_DATE = %s AND TIMESLOT = %s") 
            b.execute(x, (tp,td,ts)) 
            rraw=(b.fetchall()) 
            for i in rraw: 
                r1=int(i[0]) 
            r=int(str(r1)) 
            if r%4==0: 
               ntab=(r)//4 
            else: 
               ntab=((r)//4) + 1 
            x=("UPDATE restables SET TABLE_STATUS='NOT 
OCCUPIED',PH_NO=NULL WHERE TDATE=%s AND PH_NO=%s AND 
TIMESLOT = %s") 
            b.execute(x,(td,tp,ts)) 
            x=("DELETE FROM TABLE_BOOKING WHERE PH_NO=%s AND 
BOOKING_DATE = %s AND TIMESLOT = %s") 
            b.execute(x, (tp,td,ts)) 
            a.commit() 
64 
 
            messagebox.showinfo("CANCELLATION SUCCESS","Your table 
reservation is cancelled succesfully.") 
        
cancel2=Button(cancel,text="CANCEL",command=cancel2,bg="#02baf2",fg="
black",height= 2, width=8) 
 
        #place_table 
        l1.place(relx=0.68,rely=0.355) 
        l2.place(relx=0.72,rely=0.41) 
        l3.place(relx=0.66,rely=0.50) 
        phno.place(relx=0.75,rely=0.37) 
        ct_date.place(relx=0.73,rely=0.50) 
        ct_cal.place(relx=0.68,rely=0.57) 
        bc.place(relx=0.74,rely=0.80) 
        ts1.place(relx=0.66,rely=0.46) 
        ts2.place(relx=0.73,rely=0.46) 
        ts3.place(relx=0.80,rely=0.46) 
        cancel2.place(relx=0.74,rely=0.87) 
    
booknowbutton.menu.add_checkbutton(label="CANCELLATION",command=c
ancel) 
    main.mainloop() 
 
b=Button(root,text="USER",command=user,font=(12)) 
b.place(relx=0.1,rely=0.1) 
a=Button(root,text="ADMIN",command=admin,font=(12)) 
a.place(relx=0.3,rely=0.1) 
root.mainloop()
