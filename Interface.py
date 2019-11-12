from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


try:
    con = mysql.connector.connect(host='localhost',
                                  user='root',
                                  passwd='root',
                                  database='assignment')
    cur = con.cursor()

except mysql.connector.Error as a:
    print(a)

interface = Tk()
interface.geometry('500x250')
interface.title('Softwarica Collage ot IT and E-Commerce')

# =================================================   Functions   ==================================================== #


class Function:
    def __init__(self, form):
        self.form = form

        self.frame1 = Frame(self.form, bg='Royal Blue')
        self.frame1.place(x=0, y=0, width=500, height=150)

        self.frame2 = Frame(self.form, bg='Grey')
        self.frame2.place(x=0, y=150, width=500, height=100)

        # For Frame 1:

        self.text = Label(self.frame1, text='Welcome\n To\n Softwarica Collage of IT\n And\n E-Commerce',
                          font=('Algerian', 20), bg='Royal Blue')
        self.text.pack()

        # Buttons for  frame2:

        self.add_btn = ttk.Button(self.frame2, text='Add Student', command=self.form_fill)
        self.add_btn.grid(row=1, column=0, padx=40, pady=40)

        self.detail_btn = ttk.Button(self.frame2, text='View Details', command=self.show_details)
        self.detail_btn.grid(row=1, column=1,  padx=40, pady=40)

        self.update_btn = ttk.Button(self.frame2, text='Edit', command=self.update_form)
        self.update_btn.grid(row=1, column=2,  padx=40, pady=40)

    def form_fill(self):
        self.form = Toplevel()
        self.form.geometry('300x400')

        self.form.frame1 = Frame(self.form)
        self.form.frame1.pack()

        self.form.frame2 = Frame(self.form)
        self.form.frame2.pack()

        self.form.f_name = Label(self.form.frame1, text='First Name:')
        self.form.f_name.grid(row=0, column=0, padx=10, pady=10)
        self.form.f_name_entry = Entry(self.form.frame1)
        self.form.f_name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.form.l_name = Label(self.form.frame1, text='Last  Name:')
        self.form.l_name.grid(row=1, column=0, padx=10, pady=10)
        self.form.l_name_entry = Entry(self.form.frame1)
        self.form.l_name_entry.grid(row=1, column=1, padx=10, pady=10)

        self.form.student_id = Label(self.form.frame1, text='Student ID: ')
        self.form.student_id.grid(row=2, column=0, padx=10, pady=10)
        self.form.student_id_entry = Entry(self.form.frame1)
        self.form.student_id_entry.grid(row=2, column=1, padx=10, pady=10)

        self.form.address = Label(self.form.frame1, text='Address:')
        self.form.address.grid(row=3, column=0, padx=10, pady=10)
        self.form.address_entry = Entry(self.form.frame1)
        self.form.address_entry.grid(row=3, column=1, padx=10, pady=10)

        self.form.contact_no = Label(self.form.frame1, text='Contact Number:')
        self.form.contact_no.grid(row=4, column=0, padx=10, pady=10)
        self.form.contact_no_entry = Entry(self.form.frame1)
        self.form.contact_no_entry.grid(row=4, column=1, padx=10, pady=10)

        self.form.degree = Label(self.form.frame1, text='Degree:')
        self.form.degree.grid(row=5, column=0, padx=10, pady=10)
        self.form.degree_entry = Entry(self.form.frame1)
        self.form.degree_entry.grid(row=5, column=1, padx=10, pady=10)

        self.form.submit = ttk.Button(self.form.frame2, text='Submit', command=self.submit)
        self.form.submit.grid(row=6, column=0, padx=10, pady=10)

        self.form.clear = ttk.Button(self.form.frame2, text='Clear', command=self.clear)
        self.form.clear.grid(row=6, column=1, padx=10, pady=10)

    def submit(self):
        try:
            self.form.f_name = self.form.f_name_entry.get()
            self.form.l_name = self.form.l_name_entry.get()
            self.form.student_id = self.form.student_id_entry.get()
            self.form.address = self.form.address_entry.get()
            self.form.contact_no = self.form.contact_no_entry.get()
            self.form.degree = self.form.degree_entry.get()

            if self.form.f_name_entry or self.form.l_name_entry or self.form.student_id_entry or self.form.address_entry\
                    or self.form.contact_no_entry or self.form.degree_entry == '':
                messagebox.showerror('Error', 'Please fill all the blanks !!!')
                return

            if self.form.f_name or self.form.l_name or self.form.address or self.form.degree is not str:
                messagebox.showerror('Error', 'Name, Address and Degree should be in alphabet only.')
                return

            if self.form.student_id or self.form.contact_no is not int:
                messagebox.showerror('Error', 'Student ID and Contact No. should be in number only.')
                return

            query = 'insert into student_data values(%s, %s, %s, %s, %s, %s)'
            values = (self.form.f_name, self.form.l_name, self.form.student_id, self.form.address, self.form.contact_no,
                      self.form.degree)
            cur.execute(query, values)
            con.commit()
            messagebox.showinfo('Data Saved !!!', 'Your data is saved successfully...')
            self.clear()

        except mysql.connector.errors.DatabaseError:
            if self.form.f_name_entry or self.form.l_name_entry or self.form.student_id_entry or self.form.address_entry \
                    or self.form.contact_no_entry or self.form.degree_entry == '':
                messagebox.showerror('Error', 'Please enter valid information !!!')

    def clear(self):
        self.form.f_name_entry.delete(0, END)
        self.form.l_name_entry.delete(0, END)
        self.form.student_id_entry.delete(0, END)
        self.form.address_entry.delete(0, END)
        self.form.contact_no_entry.delete(0, END)
        self.form.degree_entry.delete(0, END)

    def show_details(self):

        self.table()
        query = 'select * from student_data '
        cur.execute(query)
        result = cur.fetchall()
        con.commit()

    def update(self):
        try:

            query = 'update student_data set F_Name=%s, L_Name=%s, Contact=%s, Address=%s, degree=%s where S_id=%s'
            self.form.f_name = self.form.f_name_entry.get()
            self.form.l_name = self.form.l_name_entry.get()
            self.form.student_id = self.form.student_id_entry.get()
            self.form.address = self.form.address_entry.get()
            self.form.contact_no = self.form.contact_no_entry.get()
            self.form.degree = self.form.degree_entry.get()

            if self.form.f_name or self.form.l_name or self.form.address or self.form.degree is not str:
                messagebox.showerror('Error', 'Name, Address and Degree should be in alphabet only.')
                return

            elif self.form.student_id or self.form.contact_no is not int:
                messagebox.showerror('Error', 'Student ID and Contact No. should be in number only.')
                return

            values = (self.form.f_name, self.form.l_name, self.form.contact_no, self.form.address, self.form.degree,
                      self.form.student_id)
            answer = messagebox.askquestion('Update', 'Do you want to update information ?')
            if answer == 'yes':
                cur.execute(query, values)
                con.commit()
                self.clear()
                self.show()
        except ValueError:
            pass

    def delete(self):
        self.form.delete = int(self.form.student_id_entry.get())
        query = 'delete from student_data where S_id=%s'
        values = (self.form.delete,)
        delete = messagebox.askquestion('Delete', 'Do you want to delete information ?')
        if delete == 'yes':
            cur.execute(query, values)
            con.commit()
            self.show()
            self.clear()

    def search(self, a_list=None):

        if not a_list:
            query = "select * from student_data"
            cur.execute(query)
            self.form.result = cur.fetchall()
        else:
            self.form.result = a_list

        self.form.lets_search = self.form.search_combo.get()
        self.form.go_search = self.form.search_entry.get()

        if self.form.go_search and self.form.lets_search:
            if self.form.lets_search == "First Name":
                self.form.go_search = self.form.search_entry.get().title()
                self.show_column = 0

            elif self.form.lets_search == "Last Name":
                self.form.go_search = self.form.search_entry.get().title()
                self.show_column = 1

            elif self.form.lets_search == "ID No.":
                if not self.form.go_search.isdigit():
                    messagebox.showinfo("Info", "Invalid SID.")
                    return
                else:
                    self.show_column = 2
                    self.form.go_search = int(self.form.search_entry.get())

            elif self.form.lets_search == "Address":
                self.form.go_search = self.form.search_entry.get()
                self.show_column = 3

            elif self.form.lets_search == "Contact No.":
                self.form.go_search = self.form.search_entry.get()
                self.show_column = 4

            elif self.form.lets_search == "Degree":
                self.form.go_search = self.form.search_entry.get()
                self.show_column = 5

            self.form.title = ['First Name', 'Last Name', 'ID No.', 'Address', 'Contact No.', 'Degree']
# making a empty list name self.list_output
            self.form.output = []

            if self.form.lets_search in self.form.title:
                for data in self.form.result:
                    if self.form.go_search == data[self.show_column]:
                        self.form.output.append(data)
                if len(self.form.output) != 0:
                    self.form.table.delete(*self.form.table.get_children())
                for list in self.form.output:
                    self.form.table.insert("", 'end', values=list)
                    con.commit()
                if not self.form.output:
                    messagebox.showinfo("Info", 'No data found in the database.')
            # shows error if no value is selected in combobox
            else:
                messagebox.showinfo("info","No valid data selected. please select value from the combobox.")
        # shows messagebox if no value is entered in search box.
        else:
            messagebox.showerror("Info", "No value selected.")
        return self.form.output

    def sorting(self, list, start, end):
        self.form.entry_sort = self.form.sort_entry.get()

        if self.form.entry_sort == "First Name":
            self.show_column = 0
        elif self.form.entry_sort == "Last Name":
            self.show_column = 1
        elif self.form.entry_sort == "ID No.":
            self.show_column = 2
        elif self.form.entry_sort == "Address":
            self.show_column = 3
        elif self.form.entry_sort == "Contact No.":
            self.show_column = 4
        elif self.form.entry_sort == "Degree":
            self.show_column = 5
        else:
            messagebox.showerror("Info", "Cannot sort by the value entered.")
            return
        num_sort = (start - 1)
        pivot = list[end][self.show_column]
        for var in range(start, end):
            if list[var][self.show_column] <= pivot:
                num_sort = num_sort + 1
                list[num_sort], list[var] = list[var], list[num_sort]

        list[num_sort + 1], list[end] = list[end], list[num_sort + 1]
        return num_sort + 1

    def quick_sort(self, list, start, end):
        if start < end:
            self.form.quick = self.sorting(list, start, end)
            self.quick_sort(list, start, self.form.quick - 1)
            self.quick_sort(list, self.form.quick + 1, end)

    def final_sort(self):
        self.form.entry_sort = self.form.sort_entry.get()
        if self.form.entry_sort:
            query = "select * from student_data"
            cur.execute(query)
            self.form.o_list = cur.fetchall()

            self.quick_sort(self.form.o_list, 0, len(self.form.o_list) - 1)

            self.form.table.delete(*self.form.table.get_children())
            for value in self.form.o_list:
                self.form.table.insert("", 'end', values=value)
                con.commit()
        else:
            messagebox.showerror("info", "No value selected.")

    def table(self):

        self.form.table = Toplevel()
        self.form.table.title('Student Details')
        self.form.table.geometry('650x400')

        self.form.search_frame = Frame(self.form.table, bd=5, relief=RIDGE)
        self.form.search_frame.place(x=0, y=0, width=650, height=100)

        self.form.search = ttk.Button(self.form.search_frame, text='Search', command=self.search)
        self.form.search.grid(row=0, column=0, padx=50, pady=5)

        self.form.search_combo = ttk.Combobox(self.form.search_frame, values=['First Name',
                                                                              'Last Name',
                                                                              'ID No.',
                                                                              'Address',
                                                                              'Contact No.',
                                                                              'Degree'])
        self.form.search_combo.grid(row=0, column=1, padx=5, pady=5)

        self.form.search_entry = Entry(self.form.search_frame)
        self.form.search_entry.grid(row=1, column=1, padx=5, pady=5)

        self.form.sort = ttk.Button(self.form.search_frame, text='Sort By', command=self.final_sort)
        self.form.sort.grid(row=0, column=2, padx=40, pady=5)

        self.form.sort_entry = ttk.Combobox(self.form.search_frame, values=['First Name',
                                                                            'Last Name',
                                                                            'ID No.',
                                                                            'Address',
                                                                            'Contact No.',
                                                                            'Degree'])
        self.form.sort_entry.grid(row=0, column=3, padx=5, pady=5)

        self.form.show_data = ttk.Button(self.form.search_frame, text='Show Data', command=self.show)
        self.form.show_data.grid(row=1, column=2, padx=40, pady=5)

# ==================================================================================================================== #

        self.form.table_frame = Frame(self.form.table, bd=5, relief=RIDGE)
        self.form.table_frame.place(x=00, y=100, width=650, height=400)

        self.form.table = ttk.Treeview(self.form.table_frame, columns=('f_name', 'l_name',
                                                                       'student_id', 'address', 'contact_no', 'degree'))

        self.form.table.heading('f_name', text='First Name')
        self.form.table.column('f_name', width=100)

        self.form.table.heading('l_name', text='Last Name')
        self.form.table.column('l_name', width=100)

        self.form.table.heading('student_id', text='Student ID')
        self.form.table.column('student_id', width=100)

        self.form.table.heading('address', text='Address')
        self.form.table.column('address', width=100)

        self.form.table.heading('contact_no', text='Contact No.')
        self.form.table.column('contact_no', width=100)

        self.form.table.heading('degree', text='Degree')
        self.form.table.column('degree', width=100)

        self.form.table['show'] = 'headings'
        self.show()

        self.form.table.pack(fill=BOTH, expand=TRUE)

    def show(self):
        query = 'select * from student_data'
        cur.execute(query)
        rows = cur.fetchall()
        if len(rows) != 0:
            self.form.table.delete(*self.form.table.get_children())
            for row in rows:
                self.form.table.insert('', END, values=row)
                con.commit()

    def pointer(self):
        try:
            self.form.point = self.form.table.focus()
            self.form.content = self.form.table.item(self.form.point)
            self.form.row = self.form.content['values']
            self.clear()

            self.form.f_name_entry.insert(0, self.form.row[0])
            self.form.l_name_entry.insert(0, self.form.row[1])
            self.form.student_id_entry.insert(0, self.form.row[2])
            self.form.address_entry.insert(0, self.form.row[3])
            self.form.contact_no_entry.insert(0, self.form.row[4])
            self.form.degree_entry.insert(0, self.form.row[5])

        except IndexError:
            pass

    def update_form(self):
        try:
            self.form.update_form = Toplevel()
            self.form.update_form.geometry('1000x300')
            self.form.update_frame = Frame(self.form.update_form, bd=5, relief=RIDGE)
            self.form.update_frame.place(x=0, y=0, width=300, height=300)

            self.form.f_name = Label(self.form.update_frame, text='First Name:')
            self.form.f_name.grid(row=0, column=0, padx=10, pady=10)
            self.form.f_name_entry = Entry(self.form.update_frame)
            self.form.f_name_entry.grid(row=0, column=1, padx=10, pady=10)

            self.form.l_name = Label(self.form.update_frame, text='Last  Name:')
            self.form.l_name.grid(row=1, column=0, padx=10, pady=10)
            self.form.l_name_entry = Entry(self.form.update_frame)
            self.form.l_name_entry.grid(row=1, column=1, padx=10, pady=10)

            self.form.student_id = Label(self.form.update_frame, text='Student ID: ')
            self.form.student_id.grid(row=2, column=0, padx=10, pady=10)
            self.form.student_id_entry = Entry(self.form.update_frame)
            self.form.student_id_entry.grid(row=2, column=1, padx=10, pady=10)

            self.form.address = Label(self.form.update_frame, text='Address:')
            self.form.address.grid(row=3, column=0, padx=10, pady=10)
            self.form.address_entry = Entry(self.form.update_frame)
            self.form.address_entry.grid(row=3, column=1, padx=10, pady=10)

            self.form.contact_no = Label(self.form.update_frame, text='Contact Number:')
            self.form.contact_no.grid(row=4, column=0, padx=10, pady=10)
            self.form.contact_no_entry = Entry(self.form.update_frame)
            self.form.contact_no_entry.grid(row=4, column=1, padx=10, pady=10)

            self.form.degree = Label(self.form.update_frame, text='Degree:', anchor=W)
            self.form.degree.grid(row=5, column=0, padx=10, pady=10)
            self.form.degree_entry = Entry(self.form.update_frame)
            self.form.degree_entry.grid(row=5, column=1, padx=10, pady=10)

            self.form.submit = ttk.Button(self.form.update_frame, text='Update', command=self.update)
            self.form.submit.grid(row=6, column=0, padx=10, pady=10)

            self.form.clear = ttk.Button(self.form.update_frame, text='Delete', command=self.delete)
            self.form.clear.grid(row=6, column=1, padx=10, pady=10)

        except mysql.connector.errors.DatabaseError:
            if self.form.f_name_entry or self.form.l_name_entry or self.form.student_id_entry or self.form.address_entry\
                        or self.form.contact_no_entry or self.form.degree_entry == '':
                messagebox.showerror('Error', 'Please enter valid information !!!')

# ==================================================================================================================== #
        self.form.search_frame = Frame(self.form.update_form, bd=5, relief=RIDGE)
        self.form.search_frame.place(x=300, y=0, width=700, height=100)

        self.form.search = ttk.Button(self.form.search_frame, text='Search', command=self.search)
        self.form.search.grid(row=0, column=0, padx=50, pady=5)

        self.form.search_combo = ttk.Combobox(self.form.search_frame, values=['First Name',
                                                                              'Last Name',
                                                                              'ID No.',
                                                                              'Address',
                                                                              'Contact No.',
                                                                              'Degree'])
        self.form.search_combo.grid(row=0, column=1, padx=5, pady=5)

        self.form.search_entry = Entry(self.form.search_frame)
        self.form.search_entry.grid(row=1, column=1, padx=5, pady=5)

        self.form.sort = ttk.Button(self.form.search_frame, text='Sort By', command=self.final_sort)
        self.form.sort.grid(row=0, column=2, padx=50, pady=5)

        self.form.sort_entry = ttk.Combobox(self.form.search_frame, values=[' First Name',
                                                                            ' Last Name',
                                                                            ' ID No.',
                                                                            ' Address',
                                                                            ' Contact No.',
                                                                            ' Degree'])
        self.form.sort_entry.grid(row=0, column=3, padx=5, pady=5)

        self.form.show_data = ttk.Button(self.form.search_frame, text='Show Data', command=self.show)
        self.form.show_data.grid(row=1, column=2, padx=40, pady=5)

        self.form.table_frame = Frame(self.form.update_form, bd=5, relief=RIDGE, bg='Red')
        self.form.table_frame.place(x=300, y=100, width=700, height=200)

        self.form.table = ttk.Treeview(self.form.table_frame, columns=('f_name', 'l_name',
                                                                       'student_id', 'address', 'contact_no', 'degree'))

        self.form.table.heading('f_name', text='First Name')
        self.form.table.column('f_name', width=100)

        self.form.table.heading('l_name', text='Last Name')
        self.form.table.column('l_name', width=100)

        self.form.table.heading('student_id', text='Student ID')
        self.form.table.column('student_id', width=100)

        self.form.table.heading('address', text='Address')
        self.form.table.column('address', width=100)

        self.form.table.heading('contact_no', text='Contact No.')
        self.form.table.column('contact_no', width=100)

        self.form.table.heading('degree', text='Degree')
        self.form.table.column('degree', width=100)

        self.form.table['show'] = 'headings'
        self.show()

        self.form.table.bind('<ButtonRelease-1>', lambda e: self.pointer())
        self.form.table.pack(fill=BOTH, expand=TRUE)


call = Function(interface)
interface.mainloop()
