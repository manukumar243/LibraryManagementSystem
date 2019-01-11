
import sqlite3
import re
from tkinter import *
from tkinter import ttk

obj=Tk()




    
def run():
    
    obj1=Tk()
    
    
    obj1.state('zoomed')
    obj1.config(bg='black')
    obj1.resizable(False,False)
    obj1.title("LIBRARY MANAGEMENT")
    lb22=Label(obj1,text='Your library is your paradise ',font=('arial',30,'bold'),fg='red',bg='black')
    lb22.place(x=400,y=300)

    lb23=Label(obj1,text='Presenting all new Database Aceess management System In ONe GO -- >>',font=('arial',30,'italic'),fg='grey',bg='black')
    lb23.place(x=30,y=360)

    lb24=Label(obj1,text='<< SECURE AND FAST >> ',font=('arial',25,'bold'),fg='blue',bg='black')
    lb24.place(x=900,y=650)


    lb245=Label(obj1,text='~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~',font=('arial',5,'bold'),fg='blue',bg='black')
    lb245.place(x=0,y=200)


    lb246=Label(obj1,text='~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ',font=('arial',5,'bold'),fg='blue',bg='black')
    lb246.place(x=800,y=200)





    lb245=Label(obj1,text='~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~',font=('arial',5,'bold'),fg='blue',bg='black')
    lb245.place(x=0,y=500)


    lb246=Label(obj1,text='~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ',font=('arial',5,'bold'),fg='blue',bg='black')
    lb246.place(x=800,y=500)






    def about():

        def contact():



            def backma():
                objc.destroy()

            objc=Tk()
        
        
            objc.state('zoomed')
            objc.config(bg='black')
            objc.resizable(False,False)
            objc.title(" contact")
            lb71=Label(objc,text='!!>>>>>>>>- WELCOME TO THE ABOUT CORNER OF THIS PYTHON PROJECT --<<<<<<< !! ',font=('arial',20,'bold'),fg='grey',bg='black')
            lb71.place(x=30,y=70)

            lb7=Label(objc,text='1.NAME  ',font=('arial',16,'bold'),fg='blue',bg='black')
            lb7.place(x=30,y=170)
            
            lb71=Label(objc,text='MANU KUMAR ',font=('arial',16,'bold'),fg='grey',bg='black')
            lb71.place(x=30,y=230)

            lb72=Label(objc,text='DESGINATION :-  ',font=('arial',16,'italic'),fg='grey',bg='black')
            lb72.place(x=30,y=290)
            
            lb73=Label(objc,text='BTECH  3RD YEAR , DITU < DEHRADUN ',font=('arial',16,'italic'),fg='grey',bg='black')
            lb73.place(x=30,y=350)
            
            lb74=Label(objc,text='EMAIL ID',font=('arial',16,'bold'),fg='blue',bg='black')
            lb74.place(x=30,y=410)
            
            lb75=Label(objc,text='kumarmk131@gmail.com, facebook id - Manu kumar ',font=('arial',16,'italic'),fg='grey',bg='black')
            lb75.place(x=30,y=470)
                
            lb772=Button(objc,text='back',font=('arial',16,'bold'),fg='cyan',bg='black',command=backma)
            lb772.place(x=30,y=550)



        def backna():
            objp.destroy()






        

        objp=Tk()
    
    
        objp.state('zoomed')
        objp.config(bg='black')
        objp.resizable(False,False)
        objp.title(" ABOUT")
        lb71=Label(objp,text='!!>>>>>>>>- WELCOME TO THE ABOUT CORNER OF THIS PYTHON PROJECT --<<<<<<< !! ',font=('arial',20,'bold'),fg='grey',bg='black')
        lb71.place(x=30,y=70)

        lb7=Label(objp,text='1.What can you do with this application ? ',font=('arial',16,'bold'),fg='blue',bg='black')
        lb7.place(x=30,y=170)
        
        lb71=Label(objp,text='You can view all  ,add  ,delete  ,view specifically  ,sort specifically  ,update i.e (add plus delete),  find the entries  ',font=('arial',16,'bold'),fg='grey',bg='black')
        lb71.place(x=30,y=230)

        lb72=Label(objp,text='NO need to have the knowledge of database working and it\'s maintenance and data corruption  ',font=('arial',16,'italic'),fg='grey',bg='black')
        lb72.place(x=30,y=290)
        
        lb73=Label(objp,text='One can access and update database in one click ',font=('arial',16,'italic'),fg='grey',bg='black')
        lb73.place(x=30,y=350)
        
        lb74=Label(objp,text='What are the modules required in it?',font=('arial',16,'bold'),fg='blue',bg='black')
        lb74.place(x=30,y=410)
        
        lb75=Label(objp,text='tinkter module,re module,sqlite3 module ',font=('arial',16,'italic'),fg='grey',bg='black')
        lb75.place(x=30,y=470)
            

        lb76=Label(objp,text='How much lines of code are there ? ',font=('arial',16,'bold'),fg='blue',bg='black')
        lb76.place(x=30,y=530)

        lb77=Label(objp,text='Contains about 1500 lines( rows) and 200 columns  and 32 tabs',font=('arial',13,'bold'),fg='grey',bg='black')
        lb77.place(x=30,y=590)



        lb77=Label(objp,text='Thank YOU  click below for further details!!!',font=('arial',13,'bold'),fg='blue',bg='black')
        lb77.place(x=30,y=650)


        lb772=Button(objp,text='Contact',font=('arial',16,'bold'),fg='cyan',bg='black',command=contact)
        lb772.place(x=30,y=690)


        lb7721=Button(objp,text='Back',font=('arial',16,'bold'),fg='cyan',bg='black',command=backna)
        lb7721.place(x=1250,y=30)

  










    
    def exit_():

    
        obj.destroy()
        obj1.destroy()


    def errorshow():





        obj6=Tk()
    
    
        obj6.geometry('800x400')
        obj6.config(bg='black')
        obj6.resizable(False,False)
        obj6.title("ERROR MANAGEMENT")
        lb261=Label(obj6,text='ERROR !! ',font=('arial',30,'bold'),fg='red',bg='black')
        lb261.place(x=360,y=50)

        lb26=Label(obj6,text='Oops! it seems like you have typed a wrong input!! TRY AGAIN or see the documentation ',font=('arial',13,'bold'),fg='white',bg='black')
        lb26.place(x=70,y=190)


        





    def entrybooks():


        

        objs=Tk() #constructor
        objs.resizable(False,False)
        objs.geometry('400x400')


        def submit():


            if(re.search(r'^[a-zA-Z]{1,10}\.?\s?[a-zA-Z]*\.?\s?[a-zA-Z]*$',str(entry4.get()))==None):
                 errorshow()


            elif(re.search(r'^[a-zA-Z]{1,10}\.?\s?[a-zA-Z]*\.?\s?[a-zA-Z]*$',str(entry8.get()))==None):
                 errorshow()



            elif(re.search(r'^[A-Z][a-z]{0,19}$',str(entry10.get()))==None):
                 errorshow()



            elif(re.search(r'^20[0-9]{2}-(([0][1-9])|(10|11|12))-(([012][1-9])|(20|30|31|10))$',str(entry6.get()))==None):
                 errorshow()
                 
            elif(re.search(r'^20[0-9]{2}-(([0][1-9])|(10|11|12))-(([012][1-9])|(20|30|31|10))$',str(entry7.get()))==None ):
                 errorshow()

            elif( re.search(r'^[a-zA-Z]{1,10}.?\s?[a-zA-Z]*.?\s?[a-zA-Z]*$',str(entry2.get()))==None):
                 errorshow()

            elif(re.search(r'^\d{4}$',str(entry3.get()))==None):
                 errorshow()
                 
            elif(re.search(r'^\d{1,4}\.\d{2}$',str(entry9.get()))==None ) :
                 errorshow()


            elif(re.search(r'^\d{1,4}\.\d{2}$',str(entry5.get()))==None ):
                 errorshow()



            else:


                
                    
                book_name=str(entry2.get())
                bookid=int(entry3.get())
                author=str(entry4.get())
                price=float(entry5.get())
                rwdate=str(entry6.get())
                redate=str(entry7.get())
                borrower=str(entry8.get())
                dues=float(entry9.get())
                genre=str(entry10.get())


                try:
                
                    dbcon=sqlite3.connect("database3.db")
                    thecursor=dbcon.cursor()
                    thecursor.execute("insert into book_(book_name,book_id,book_author_name,price,date_of_issue,date_of_renewal,borrower,Dues,Genre) values(?,?,?,?,?,?,?,?,?)",[book_name,bookid,author,price,rwdate,redate,borrower,dues,genre])

                    dbcon.commit()
                    dbcon.close()
                        
                    mylab122=Label(objs,text='Entry done',fg='black',font=('arial',20,'italic'))
                    mylab122.place(x=110,y=260)


                except Exception :
                    errorshow()



            
            




        def delete():
        
            

            entry2.delete(0,END)

            entry4.delete(0,END)

            entry3.delete(0,END)

            entry5.delete(0,END)

            entry6.delete(0,END)

            entry7.delete(0,END)

            entry8.delete(0,END)

            entry9.delete(0,END)


            entry10.delete(0,END)
            
        mylab=Label(objs,text='Welcome to entry new book',fg='black',font=('arial',10,'bold'))
        mylab.pack()


        mylab1=Label(objs,text='Book Name',fg='black',font=('arial',10,'italic'))
        mylab1.place(x=20,y=20)

        mylab2=Label(objs,text='Book id',fg='black',font=('arial',10,'italic'))
        mylab2.place(x=40,y=40)

        mylab3=Label(objs,text='Author Name',fg='black',font=('arial',10,'italic'))
        mylab3.place(x=20,y=60)

        mylab4=Label(objs,text='price',fg='black',font=('arial',10,'italic'))
        mylab4.place(x=50,y=82)




        mylab5=Label(objs,text='Issued date',fg='black',font=('arial',10,'italic'))
        mylab5.place(x=20,y=107)
                     
        mylab6=Label(objs,text='Renewal date',fg='black',font=('arial',10,'italic'))
        mylab6.place(x=20,y=130)

        mylab7=Label(objs,text='Borrower',fg='black',font=('arial',10,'italic'))
        mylab7.place(x=40,y=150)

        mylab8=Label(objs,text='Dues',fg='black',font=('arial',10,'italic'))
        mylab8.place(x=60,y=170)

        mylab9=Label(objs,text='Genre',fg='black',font=('arial',10,'italic'))
        mylab9.place(x=40,y=190) 





        entry2=ttk.Entry(objs,width=30)
        entry2.pack()


        
        entry3=ttk.Entry(objs,width=30)
        entry3.pack()
        entry3.insert(0,'digits')


        entry4=ttk.Entry(objs,width=30)
        entry4.pack()

        entry5=ttk.Entry(objs,width=30)
        entry5.pack()
        entry5.insert(0,'digits')


        entry6=ttk.Entry(objs,width=30)
        entry6.pack()
        entry6.insert(0,'yyyy-mm-dd')

        entry7=ttk.Entry(objs,width=30)
        entry7.pack()
        entry7.insert(0,'yyyy-mm-dd')

        entry8=ttk.Entry(objs,width=30)
        entry8.pack()
        

        entry9=ttk.Entry(objs,width=30)
        entry9.pack()
        entry9.insert(0,'digits')

        entry10=ttk.Entry(objs,width=30)
        entry10.pack()
       

        


        myb1=Button(objs,text='Clear',fg='black',font=('arial',10,'bold'),command=delete)
        myb1.place(x=230,y=230)


        myb2=Button(objs,text='Submit',fg='black',font=('arial',10,'bold'),command=submit)
        myb2.place(x=280,y=230)



        
                  
           





    



    def search():
        objse=Tk()
        objse.config(bg='black')
        objse.state('zoomed')
        objse.resizable(False,False)

        
        lb22=Label(objse,text=' GRAPHIC USER INTERFACE makes user easy to interact with systems',font=('arial',30,'italic'),fg='grey',bg='black')
        lb22.place(x=30,y=300)

        lb22=Label(objse,text=' If you want to get laid, go to college. If you want an education, go to the library',font=('arial',20,'bold'),fg='blue',bg='black')
        lb22.place(x=20,y=650)


        
        



        def showbw():

            def deletesew():

                entrybw.delete(0,END)






            def submitsew():

                dbcon=sqlite3.connect("database3.db")
                thecursor=dbcon.cursor()
               
                varname=entrybw.get()
                if(re.search(r'^[a-zA-Z]{1,10}\.?\s?[a-zA-Z]*\.?\s?[a-zA-Z]*$',varname)==None):
                    dbcon.close()
                    errorshow()
                    objsbw.destroy()
                else:
                    
            
                    varname2=thecursor.execute("select * from book_ where borrower= ? ",(varname,))
        
                    dbcon.commit()
                    
                    
                    master = Tk()
                    master.state('zoomed')
                    master.resizable(False,False)


                    frame = Frame(master)
                    frame.pack(fill = BOTH,expand=1)

                    scrollbar = Scrollbar(frame)
                    scrollbar.pack(side = RIGHT,fill=BOTH)

                    listbox = Listbox(frame)
                    listbox.pack(fill=BOTH,expand=1)

                    listbox.config(yscrollcommand = scrollbar.set)
                    scrollbar.config(command = listbox.yview)

                    b='                        BOOKS HAVING BORROWER NAME ' + varname + '\n'+'\n'
                    listbox.insert(END,'{}'.format(b))


                    for row in varname2:

                        b=row[0]
                        listbox.insert(END,' Name of book is :-{}'.format(b))

                        b=str(row[1])
                        listbox.insert(END,' id of the book :- {}'.format(b))

                        b=str(row[2])
                        listbox.insert(END,' Name of author is  :- {}'.format(b))

                        b=str(row[3])
                        listbox.insert(END,' Price of the book :-{}'.format(b))

                        b=str(row[4])
                        listbox.insert(END,' Date of renewal :-  {}'.format(b))

                        b=str(row[5])
                        listbox.insert(END,' Date of issue:- {}'.format(b))

                        b=str(row[6])
                        listbox.insert(END,' Borrower :-{}'.format(b))

                
                        b=str(row[7])
                        listbox.insert(END,' Dues :- {}'.format(b))

                        b=str(row[8])
                        listbox.insert(END,' Genre :- {}'.format(b))




                        b='\n'
                        listbox.insert(END,'{}'.format(b))

                
                    master.mainloop() 
                    dbcon.close()



            objsbw=Tk() 
            objsbw.resizable(False,False)
            objsbw.geometry('400x200')

            entrybw=ttk.Entry(objsbw,width=20)
            entrybw.place(x=40,y=70)
            

            mylabsew=Label(objsbw,text='Enter Name of borrower',fg='black',font=('arial',10,'italic'))
            mylabsew.place(x=40,y=40)
        
            myb1=Button(objsbw,text='Clear',fg='black',font=('arial',10,'bold'),command=deletesew)
            myb1.place(x=250,y=10)


            mybb=Button(objsbw,text='Submit',fg='black',font=('arial',10,'bold'),command=submitsew)
            mybb.place(x=320,y=10)




        def showan():

            def deletesan():

                entryan.delete(0,END)






            def submitsan():

                dbcon=sqlite3.connect("database3.db")
                thecursor=dbcon.cursor()
               
                varname=entryan.get()
                if(re.search(r'^[a-zA-Z]{1,10}\.?\s?[a-zA-Z]*\.?\s?[a-zA-Z]*$',varname)==None):

                    dbcon.close()
                    errorshow()
                    
                    
                else:
                    
                    varname2=thecursor.execute("select * from book_ where book_author_name= ? ",(varname,))
        
                    dbcon.commit()
                    
                    
                    master = Tk()
                    master.state('zoomed')
                    master.resizable(False,False)


                    frame = Frame(master)
                    frame.pack(fill = BOTH,expand=1)

                    scrollbar = Scrollbar(frame)
                    scrollbar.pack(side = RIGHT,fill=BOTH)

                    listbox = Listbox(frame)
                    listbox.pack(fill=BOTH,expand=1)

                    listbox.config(yscrollcommand = scrollbar.set)
                    scrollbar.config(command = listbox.yview)

                    b='                        BOOKS HAVING AUTHOR NAME ' + varname + '\n'+'\n'
                    listbox.insert(END,'{}'.format(b))


                    for row in varname2:

                        b=row[0]
                        listbox.insert(END,' Name of book is :-{}'.format(b))

                        b=str(row[1])
                        listbox.insert(END,' id of the book :- {}'.format(b))

                        b=str(row[2])
                        listbox.insert(END,' Name of author is  :- {}'.format(b))

                        b=str(row[3])
                        listbox.insert(END,' Price of the book :-{}'.format(b))

                        b=str(row[4])
                        listbox.insert(END,' Date of renewal :-  {}'.format(b))

                        b=str(row[5])
                        listbox.insert(END,' Date of issue:- {}'.format(b))

                        b=str(row[6])
                        listbox.insert(END,' Borrower :-{}'.format(b))

                
                        b=str(row[7])
                        listbox.insert(END,' Dues :- {}'.format(b))


                        b=str(row[8])
                        listbox.insert(END,' Genre :- {}'.format(b))


                        b='\n'
                        listbox.insert(END,'{}'.format(b))

                
                    master.mainloop() 
                    dbcon.close()



            objsan=Tk() 
            objsan.resizable(False,False)
            objsan.geometry('400x200')

            entryan=ttk.Entry(objsan,width=20)
            entryan.place(x=40,y=70)
            

            mylabsan=Label(objsan,text='Enter Name of Author',fg='black',font=('arial',10,'italic'))
            mylabsan.place(x=40,y=40)
        
            myb1an=Button(objsan,text='Clear',fg='black',font=('arial',10,'bold'),command=deletesan)
            myb1an.place(x=250,y=10)


            mybban=Button(objsan,text='Submit',fg='black',font=('arial',10,'bold'),command=submitsan)
            mybban.place(x=320,y=10)



        def showgn():

            def deletesgn():

                entryan.delete(0,END)


            


            def submitsgn():

                dbcon=sqlite3.connect("database3.db")
                thecursor=dbcon.cursor()
               
                varname=entryan.get()
                if(re.search(r'^[A-Z][a-z]{0,19}$',varname)==None):
                    errorshow()
                    dbcon.close()

                else:
            
                    varname2=thecursor.execute("select * from book_ where Genre= ? ",(varname,))
        
                    dbcon.commit()
                    
                    
                    master = Tk()
                    master.state('zoomed')
                    master.resizable(False,False)


                    frame = Frame(master)
                    frame.pack(fill = BOTH,expand=1)

                    scrollbar = Scrollbar(frame)
                    scrollbar.pack(side = RIGHT,fill=BOTH)

                    listbox = Listbox(frame)
                    listbox.pack(fill=BOTH,expand=1)

                    listbox.config(yscrollcommand = scrollbar.set)
                    scrollbar.config(command = listbox.yview)

                    b='                        BOOKS HAVING GENRE ' + varname + '\n'+'\n'
                    listbox.insert(END,'{}'.format(b))


                    for row in varname2:

                        b=row[0]
                        listbox.insert(END,' Name of book is :-{}'.format(b))

                        b=str(row[1])
                        listbox.insert(END,' id of the book :- {}'.format(b))

                        b=str(row[2])
                        listbox.insert(END,' Name of author is  :- {}'.format(b))

                        b=str(row[3])
                        listbox.insert(END,' Price of the book :-{}'.format(b))

                        b=str(row[4])
                        listbox.insert(END,' Date of renewal :-  {}'.format(b))

                        b=str(row[5])
                        listbox.insert(END,' Date of issue:- {}'.format(b))

                        b=str(row[6])
                        listbox.insert(END,' Borrower :-{}'.format(b))

                
                        b=str(row[7])
                        listbox.insert(END,' Dues :- {}'.format(b))


                        b=str(row[8])
                        listbox.insert(END,' Genre :- {}'.format(b))


                        b='\n'
                        listbox.insert(END,'{}'.format(b))

                
                    master.mainloop() 
                    dbcon.close()



            objsag=Tk() 
            objsag.resizable(False,False)
            objsag.geometry('400x200')

            entryan=ttk.Entry(objsag,width=20)
            entryan.place(x=40,y=70)
            

            mylabsag=Label(objsag,text='Enter Genre of the book',fg='black',font=('arial',10,'italic'))
            mylabsag.place(x=40,y=40)
        
            myb1ag=Button(objsag,text='Clear',fg='black',font=('arial',10,'bold'),command=deletesgn)
            myb1ag.place(x=250,y=10)


            mybbag=Button(objsag,text='Submit',fg='black',font=('arial',10,'bold'),command=submitsgn)
            mybbag.place(x=320,y=10)



    
            
            




            

        def showid():


            def submittse():


                str1=entry.get()
                str2=str(str1)
                if(re.search(r'^\d{4}$',str2)==None):
                    errorshow()
                    

                else:
                    
                    
                    dbcon=sqlite3.connect("database3.db")
                    thecursor=dbcon.cursor()
                    var=thecursor.execute("select * from book_ where book_id= ? ",(str1,))

                    for i in var:

                        Name ='Name Of Book:-      '+ i[0]
                        mylabdb0=Label(objsid,text=Name,fg='black',font=('arial',10,'italic'))
                        mylabdb0.place(x=40,y=100)

                        Bookid ='Book id:-      '+ str(i[1])
                        mylabdb1=Label(objsid,text=Bookid,fg='black',font=('arial',10,'italic'))
                        mylabdb1.place(x=75,y=120)
                        

                        An ='Authors Name:-     '+ i[2]
                        mylabdb2=Label(objsid,text=An,fg='black',font=('arial',10,'italic'))
                        mylabdb2.place(x=44,y=140)

                        P ='Price:-       '+ str(i[3])
                        mylabdb3=Label(objsid,text=P,fg='black',font=('arial',10,'italic'))
                        mylabdb3.place(x=85,y=160)

                        Doi ='Date of Issue:-     '+ str(i[4])
                        mylabdb4=Label(objsid,text=Doi,fg='black',font=('arial',10,'italic'))
                        mylabdb4.place(x=44,y=180)

                        Dor='Date of Renewal     '+ str(i[5])
                        mylabdb5=Label(objsid,text=Dor,fg='black',font=('arial',10,'italic'))
                        mylabdb5.place(x=42,y=200)

                        Bn ='Borrowers  Name:-  '+ i[6]
                        mylabdb6=Label(objsid,text=Bn,fg='black',font=('arial',10,'italic'))
                        mylabdb6.place(x=44,y=220)


                        Du ='Dues:-         '+ str(i[7])
                        mylabdb7=Label(objsid,text=Du,fg='black',font=('arial',10,'italic'))
                        mylabdb7.place(x=80,y=240)
            
                        Dg ='Genre:-         '+ str(i[8])
                        mylabdb8=Label(objsid,text=Dg,fg='black',font=('arial',10,'italic'))
                        mylabdb8.place(x=80,y=240)
            
            

                    dbcon.commit()
                    dbcon.close()



                
            
            def deletese():

                entry.delete(0,END)
                


            objsid=Tk() #constructor
            objsid.resizable(False,False)
            objsid.geometry('600x400')

            entry=ttk.Entry(objsid,width=20)
            entry.place(x=40,y=70)
            entry.insert(0,'4 digit id')
            mylabse=Label(objsid,text='Enter the id of book ',fg='black',font=('arial',10,'italic'))
            mylabse.place(x=40,y=40)
        
            myb1=Button(objsid,text='Clear',fg='black',font=('arial',10,'bold'),command=deletese)
            myb1.place(x=520,y=10)


            mybb=Button(objsid,text='Submit',fg='black',font=('arial',10,'bold'),command=submittse)
            mybb.place(x=450,y=10)





        def exit3():
            objse.destroy()


        mybuts0=Button(objse,text='SHOW BOOKS BY GENRE',bg='black',fg='yellow' ,font=('arial',13,'bold'),command=showgn)
        mybuts0.pack(side=LEFT,fill=X,ipadx=10,padx=20,pady=30,ipady=10,anchor='n')


        mybuts1=Button(objse,text='SHOW BOOKS BY ID ',bg='black',fg='yellow',font=('arial',13,'bold'),command=showid)
        mybuts1.pack(side=LEFT,fill=X,ipadx=10,padx=20,pady=30,ipady=10,anchor='n')

        mybuts2=Button(objse,text='SHOW BOOKS BY BORROWER',bg='black',fg='yellow',font=('arial',13,'bold'),command=showbw)
        mybuts2.pack(side=LEFT,fill=X,ipadx=10,ipady=10,padx=20,pady=30,anchor='n')


        mybuts3=Button(objse,text='SHOW BOOKS BY AUTHOR NAME',bg='black',fg='yellow',font=('arial',13,'bold'),command=showan)
        mybuts3.pack(side=LEFT,fill=X,ipadx=10,padx=20,ipady=10,pady=30,anchor='n')

       
        mybuts5=Button(objse,text='<- BACK',bg='black',fg='yellow',font=('arial',13,'bold'),command=exit3)
        mybuts5.pack(side=LEFT,fill=X,ipadx=10,padx=20,ipady=10,pady=30,anchor='n')

        


        


    def delentry():


        def submittse():


            str1=entry.get()
            if(re.search(r'^\d{4}$',str1)==None):
                    errorshow()
            else:
                    
                    
                dbcon=sqlite3.connect("database3.db")
                thecursor=dbcon.cursor()
                var=thecursor.execute("select * from  book_ where book_id= ? ",(str1,))

                for i in var:

                    Name ='Name Of Book:-      '+ i[0]
                    mylabdb0=Label(objsd,text=Name,fg='black',font=('arial',10,'italic'))
                    mylabdb0.place(x=40,y=100)

                    Bookid ='Book id:-      '+ str(i[1])
                    mylabdb1=Label(objsd,text=Bookid,fg='black',font=('arial',10,'italic'))
                    mylabdb1.place(x=75,y=120)
                        
     
                    An ='Authors Name:-     '+ i[2]
                    mylabdb2=Label(objsd,text=An,fg='black',font=('arial',10,'italic'))
                    mylabdb2.place(x=44,y=140)
                
                    P ='Price:-       '+ str(i[3])
                    mylabdb3=Label(objsd,text=P,fg='black',font=('arial',10,'italic'))
                    mylabdb3.place(x=85,y=160)

                    Doi ='Date of Issue:-     '+ str(i[4])
                    mylabdb4=Label(objsd,text=Doi,fg='black',font=('arial',10,'italic'))
                    mylabdb4.place(x=44,y=180)

                    Dor='Date of Renewal     '+ str(i[5])
                    mylabdb5=Label(objsd,text=Dor,fg='black',font=('arial',10,'italic'))
                    mylabdb5.place(x=42,y=200)

                    Bn ='Borrowers  Name:-  '+ i[6]
                    mylabdb6=Label(objsd,text=Bn,fg='black',font=('arial',10,'italic'))
                    mylabdb6.place(x=44,y=220)


                    Du ='Dues:-         '+ str(i[7])
                    mylabdb7=Label(objsd,text=Du,fg='black',font=('arial',10,'italic'))
                    mylabdb7.place(x=80,y=240)
            
                    Dg ='Genre:-         '+ str(i[8])
                    mylabdb8=Label(objsd,text=Dg,fg='black',font=('arial',10,'italic'))
                    mylabdb8.place(x=80,y=240)
                        
                thecursor.execute("delete from  book_ where book_id= ? ",(str1,))
            
                mylabdb8=Label(objsd,text='book is deleted ',fg='black',font=('arial',10,'italic'))
                mylabdb8.place(x=40,y=280)
                       

                dbcon.commit()
                dbcon.close()



                
            
        def deletese():

            entry.delete(0,END)
                


        objsd=Tk() #constructor
        objsd.resizable(False,False)
        objsd.geometry('600x400')

        entry=ttk.Entry(objsd,width=20)
        entry.place(x=40,y=70)
        entry.insert(0,'4 digit id')
        mylabse=Label(objsd,text='Enter the id of book to delete ',fg='black',font=('arial',10,'italic'))
        mylabse.place(x=40,y=40)
        
        myb1=Button(objsd,text='Clear',fg='black',font=('arial',10,'bold'),command=deletese)
        myb1.place(x=520,y=10)


        mybb=Button(objsd,text='Submit',fg='black',font=('arial',10,'bold'),command=submittse)
        mybb.place(x=450,y=10) 


    def documentation():

        obj7=Tk()
    
    
        obj7.state('zoomed')
        obj7.config(bg='black')
        obj7.resizable(False,False)
        obj7.title("ERROR MANAGEMENT")
        lb71=Label(obj7,text='!!_______________________WELCOME TO THE DOCUMENTATION  PART _____________________  !! ',font=('arial',20,'bold'),fg='red',bg='black')
        lb71.place(x=30,y=30)

        lb7=Label(obj7,text='1. The book\'s id must be 4 digit integer value only in ???? fotmat ',font=('arial',13,'bold'),fg='white',bg='black')
        lb7.place(x=30,y=80)
        
        lb71=Label(obj7,text='2. The Book \'s price must be a floating point  value only in the ????.?? format ',font=('arial',13,'bold'),fg='blue',bg='black')
        lb71.place(x=30,y=110)

        lb72=Label(obj7,text='3. The book \'s id must be unique for each book  ',font=('arial',13,'bold'),fg='tan',bg='black')
        lb72.place(x=30,y=140)
        
        lb73=Label(obj7,text='4. The Author \'s name must contain only alphabets. Word limit is 20 characters  ',font=('arial',13,'bold'),fg='green',bg='black')
        lb73.place(x=30,y=170)
        
        lb74=Label(obj7,text='5. The Borrower \'s name must contain only alphabets. Word limit is 20 characters  ',font=('arial',13,'bold'),fg='orange',bg='black')
        lb74.place(x=30,y=200)
        
        lb75=Label(obj7,text='6. The Genre \'s name must contain only  alphabets. Word limit is 20 characters  ',font=('arial',13,'bold'),fg='powderblue',bg='black')
        lb75.place(x=30,y=230)
            

        lb76=Label(obj7,text='7. The Books \'s name must contain only alphabets and digits. Word limit is 20 characters  ',font=('arial',13,'bold'),fg='khaki',bg='black')
        lb76.place(x=30,y=260)

        lb78=Label(obj7,text='8. The Dues \'s amount must be a floating point  value only in the ????.?? format ',font=('arial',13,'bold'),fg='yellow' ,bg='black')
        lb78.place(x=30,y=290)
            
        lb78=Label(obj7,text='9. The Renewal Date  must be a only in the  format yyyy-mm-dd ',font=('arial',13,'bold'),fg='white' ,bg='black')
        lb78.place(x=30,y=320)

        lb79=Label(obj7,text='10. The  Date of issue  must be a only in the  format yyyy-mm-dd ',font=('arial',13,'bold'),fg='brown' ,bg='black')
        lb79.place(x=30,y=350)

        lb710=Label(obj7,text='11.Once a book is deleted cannot be restored in the database ',font=('arial',13,'bold'),fg='lightgreen' ,bg='black')
        lb710.place(x=30,y=380)
      
        lb712=Label(obj7,text='12. If a BOOK is not borrowed by anyone then its renewal amd date of issued  must be in fotmat 0000-00-00',font=('arial',13,'bold'),fg='pink' ,bg='black')
        lb712.place(x=30,y=410)
      
        

        lb714=Label(obj7,text='13. If a BOOK is not borrowed by anyone then its borrower  must be None,and to update borrowers name delete and insert entry in database',font=('arial',13,'bold'),fg='skyblue' ,bg='black')
        lb714.place(x=30,y=440)
      
        lb715=Label(obj7,text='14. You cannot left any input box as empty to get error free result ',font=('arial',13,'bold'),fg='aqua' ,bg='black')
        lb715.place(x=30,y=470)

        lb716=Label(obj7,text='14. If a BOOK is not in database there would not be any output by pressing show book by id ',font=('arial',13,'bold'),fg='yellow' ,bg='black')
        lb716.place(x=30,y=500)

        lb717=Label(obj7,text='16. For any bugs and queries contact ,email us on kumarmk131@gmail.com ',font=('arial',13,'bold'),fg='blue' ,bg='black')
         
        lb717.place(x=30,y=560)



        lb719=Label(obj7,text='15. Genre\'s first letter must be capital ',font=('arial',13,'bold'),fg='red' ,bg='black')
        lb719.place(x=30,y=530)
      
      

        lb717=Label(obj7,text='DESIGNED BY ',font=('arial',10,'bold'),fg='blue' ,bg='black')
         
        lb717.place(x=1150,y=670)
      
        lb718=Label(obj7,text='MANU KUMAR ',font=('arial',13,'bold'),fg='blue' ,bg='black')
         
        lb718.place(x=1150,y=690)
    













    




    def showbooks():
              
        dbcon=sqlite3.connect("database3.db")
        thecursor=dbcon.cursor()
        
    
        result=thecursor.execute("select *from book_")
        result1=result.fetchall()
        dbcon.commit()
        dbcon.close()
        
        master = Tk()
        master.state('zoomed')
        master.resizable(False,False)

        frame = Frame(master)
        frame.pack(fill = BOTH,expand=1)

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side = RIGHT,fill=BOTH)

        listbox = Listbox(frame)
        listbox.pack(fill=BOTH,expand=1)

        listbox.config(yscrollcommand = scrollbar.set)
        scrollbar.config(command = listbox.yview)

        b='                        WELOCME TO BOOKS COLLECTION \n                          ' 
        listbox.insert(END,'{}'.format(b))


        for row in result1:

            b=row[0]
            listbox.insert(END,' Name of book is :-{}'.format(b))

            b=str(row[1])
            listbox.insert(END,' id of the book :- {}'.format(b))

            b=str(row[2])
            listbox.insert(END,' Name of author is  :- {}'.format(b))

            b=str(row[3])
            listbox.insert(END,' Price of the book :-{}'.format(b))

            b=str(row[4])
            listbox.insert(END,' Date of renewal :-  {}'.format(b))

            b=str(row[5])
            listbox.insert(END,' Date of issue:- {}'.format(b))

            b=str(row[6])
            listbox.insert(END,' Borrower :-{}'.format(b))

    
            b=str(row[7])
            listbox.insert(END,' Dues :- {}'.format(b))

            b=str(row[8])
            listbox.insert(END,' Genre :- {}'.format(b))


            b='\n'
            listbox.insert(END,'{}'.format(b))

    
        master.mainloop()








    def sortbk():

        def back2():
            obj9.destroy()

            
        def showbooksau():
              
            dbcon=sqlite3.connect("database3.db")
            thecursor=dbcon.cursor()
          
        
            result=thecursor.execute("select *from book_ order by  book_author_name  Asc")
            result1=result.fetchall()
            dbcon.commit()
            dbcon.close()
            
            master = Tk()
            master.config(bg='cyan')
            master.state('zoomed')
            master.resizable(False,False)

            frame = Frame(master)
            frame.pack(fill = BOTH,expand=1)

            scrollbar = Scrollbar(frame)
            scrollbar.pack(side = RIGHT,fill=BOTH)

            listbox = Listbox(frame)
            listbox.pack(fill=BOTH,expand=1)

            listbox.config(yscrollcommand = scrollbar.set)
            scrollbar.config(command = listbox.yview)

            b='                        WELOCME TO BOOKS SORTING \n   \n         \n              ' 
            listbox.insert(END,'{}'.format(b))


            for row in result1:

                b=row[2]
                listbox.insert(END,' Author of book is :-{}'.format(b))

                b=str(row[0])
                listbox.insert(END,' Nmme  of the book :- {}'.format(b))

                b=str(row[1])
                listbox.insert(END,' Id of the book :- {}'.format(b))


               


                b='\n'
                listbox.insert(END,'{}'.format(b))

        
            master.mainloop()



        def showbooksgk():
              
            dbcon=sqlite3.connect("database3.db")
            thecursor=dbcon.cursor()
          
        
            result=thecursor.execute("select *from book_ order by  Genre Asc")
            result1=result.fetchall()
            dbcon.commit()
            dbcon.close()
            
            master = Tk()
            master.config(bg='cyan')
            master.state('zoomed')
            master.resizable(False,False)

            frame = Frame(master)
            frame.pack(fill = BOTH,expand=1)

            scrollbar = Scrollbar(frame)
            scrollbar.pack(side = RIGHT,fill=BOTH)

            listbox = Listbox(frame)
            listbox.pack(fill=BOTH,expand=1)

            listbox.config(yscrollcommand = scrollbar.set)
            scrollbar.config(command = listbox.yview)

            b='                        WELOCME TO BOOKS SORTING \n   \n         \n              ' 
            listbox.insert(END,'{}'.format(b))


            for row in result1:

                b=row[8]
                listbox.insert(END,' Genre of book is :-{}'.format(b))

                b=str(row[0])
                listbox.insert(END,' Nmae of the book :- {}'.format(b))

                b=str(row[1])
                listbox.insert(END,' Id of the book :- {}'.format(b))


               


                b='\n'
                listbox.insert(END,'{}'.format(b))

        
            master.mainloop()



        def showbooksbk():
              
            dbcon=sqlite3.connect("database3.db")
            thecursor=dbcon.cursor()
          
        
            result=thecursor.execute("select *from book_ order by  book_name Asc")
            result1=result.fetchall()
            dbcon.commit()
            dbcon.close()
            
            master = Tk()
            master.config(bg='cyan')
            master.state('zoomed')
            master.resizable(False,False)

            frame = Frame(master)
            frame.pack(fill = BOTH,expand=1)

            scrollbar = Scrollbar(frame)
            scrollbar.pack(side = RIGHT,fill=BOTH)

            listbox = Listbox(frame)
            listbox.pack(fill=BOTH,expand=1)

            listbox.config(yscrollcommand = scrollbar.set)
            scrollbar.config(command = listbox.yview)

            b='                        WELOCME TO BOOKS SORTING \n                          ' 
            listbox.insert(END,'{}'.format(b))


            for row in result1:

                b=row[0]
                listbox.insert(END,' Name of book is :-{}'.format(b))

                b=str(row[1])
                listbox.insert(END,' id of the book :- {}'.format(b))

               


                b='\n'
                listbox.insert(END,'{}'.format(b))

        
            master.mainloop()







        def showbooksbp():
              
            dbcon=sqlite3.connect("database3.db")
            thecursor=dbcon.cursor()
          
        
            result=thecursor.execute("select *from book_ order by price  Asc")
            result1=result.fetchall()
            dbcon.commit()
            dbcon.close()
            
            master = Tk()
            master.config(bg='cyan')
            master.state('zoomed')
            master.resizable(False,False)

            frame = Frame(master)
            frame.pack(fill = BOTH,expand=1)

            scrollbar = Scrollbar(frame)
            scrollbar.pack(side = RIGHT,fill=BOTH)

            listbox = Listbox(frame)
            listbox.pack(fill=BOTH,expand=1)

            listbox.config(yscrollcommand = scrollbar.set)
            scrollbar.config(command = listbox.yview)

            b='                        WELOCME TO BOOKS SORTING \n                          ' 
            listbox.insert(END,'{}'.format(b))


            for row in result1:

                b=row[0]
                listbox.insert(END,' Name of book is :-{}'.format(b))

                b=str(row[1])
                listbox.insert(END,' id of the book :- {}'.format(b))
                

                b=str(row[3])
                listbox.insert(END,' price of the book :- {}'.format(b))
                


                b='\n'
                listbox.insert(END,'{}'.format(b))

        
            master.mainloop()




        




        


         

        obj9=Tk()
    
    
        obj9.state('zoomed')
        obj9.config(bg='black')
        obj9.resizable(False,False)
        obj9.title("SORTING MANAGEMENT")
        lb22=Label(obj9,text='Losing you is my biggest achievement ',font=('arial',30,'bold'),fg='red',bg='black')
        lb22.place(x=320,y=300)


        
        


        lb22=Label(obj9,text='Talent is not what you have been god gifted ,it is how large you do with the litle things ',font=('arial',25,'italic'),fg='grey',bg='black')
        lb22.place(x=100,y=570)


        mybuts0=Button(obj9,text='Sort BOOKS BY GENRE',fg='blue' ,font=('arial',14,'bold'),bg='black',command=showbooksgk)
        mybuts0.pack(side=LEFT,fill=X,ipadx=10,padx=20,pady=30,ipady=10,anchor='n')


        mybuts1=Button(obj9,text='SORT BY BOOK\'S AUTHOR ',fg='blue' ,font=('arial',14,'bold'),bg='black',command=showbooksau)
        mybuts1.pack(side=LEFT,fill=X,ipadx=10,padx=20,pady=30,ipady=10,anchor='n')

        mybuts2=Button(obj9,text='SORT BY BOOKS NAME ',fg='blue',font=('arial',14,'bold'),bg='black',command=showbooksbk)
        mybuts2.pack(side=LEFT,fill=X,ipadx=10,ipady=10,padx=20,pady=30,anchor='n')


        mybuts3=Button(obj9,text='SORT BOOKS BY PRICE',fg='blue',font=('arial',14,'bold'),bg='black',command=showbooksbp)
        mybuts3.pack(side=LEFT,fill=X,ipadx=10,padx=20,ipady=10,pady=30,anchor='n')

       
        mybuts5=Button(obj9,text='<- BACK',fg='blue',font=('arial',14,'bold'),bg='black',command=back2)
        mybuts5.pack(side=LEFT,fill=X,ipadx=10,padx=20,ipady=10,pady=30,anchor='n')

        
    

    











    
    mybut0=Button(obj1,text='SHOW BOOKS',fg='yellow' ,font=('arial',12,'bold'),bg='black',command=showbooks)
    mybut0.pack(side=LEFT,fill=X,ipadx=10,padx=20,pady=30,ipady=10,anchor='n')


    mybut1=Button(obj1,text='ENTRY BOOKS',fg='orange' ,font=('arial',12,'bold'),bg='black',command=entrybooks)
    mybut1.pack(side=LEFT,fill=X,ipadx=10,padx=20,pady=30,ipady=10,anchor='n')

    mybut2=Button(obj1,text='DOCUMENTATION',fg='green',font=('arial',12,'bold'),bg='black',command=documentation)
    mybut2.pack(side=LEFT,fill=X,ipadx=10,ipady=10,padx=20,pady=30,anchor='n')


    mybut3=Button(obj1,text='DELETE ENTRY',fg='red',font=('arial',12,'bold'),bg='black',command=delentry)
    mybut3.pack(side=LEFT,fill=X,ipadx=10,padx=20,ipady=10,pady=30,anchor='n')

    mybut4=Button(obj1,text='SORT BY',fg='khaki',font=('arial',12,'bold'),bg='black',command=sortbk)
    mybut4.pack(side=LEFT,fill=X,ipadx=10,padx=20,ipady=10,pady=30,anchor='n')

    mybut3=Button(obj1,text='ABOUT',fg='violet',font=('arial',12,'bold'),bg='black',command=about)
    mybut3.pack(side=LEFT,fill=X,ipadx=10,padx=20,ipady=10,pady=30,anchor='n')

    mybut4=Button(obj1,text='SEARCH',fg='aqua',font=('arial',12,'bold'),bg='black',command=search)
    mybut4.pack(side=LEFT,fill=X,ipadx=10,padx=20,ipady=10,pady=30,anchor='n')

    mybut5=Button(obj1,text='EXIT',fg='blue',font=('arial',12,'bold'),bg='black', command=exit_)
    mybut5.pack(side=LEFT,fill=X,ipadx=10,padx=20,ipady=10,pady=30,anchor='n')

  












obj.geometry('1080x592')
obj.resizable(False,False)

filename = PhotoImage(file = "dd.gif")

lb22=Label(obj,text='WELCOME TO LIBRARY            MANAGEMENT SYSTEM',font=('arial',22,'bold'),fg='white',image=filename)
lb22.pack(fill=BOTH,expand=True)

lb22.config(compound='center')


lb2b=Button(obj,text='->next',font=('arial',15,'bold'),fg='black',bg='cyan')
lb2b.place(x=950,y=500)
lb2b.bind('<ButtonPress>',lambda e:run())



obj.mainloop()
