import tkinter as tk
from tkinter import messagebox
import sqlite3 as sq
from tkinter import ttk


def create_table_database():
    with sq.connect('DataBase.db') as con:
        cursor = con.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Costs (
                cost INTEGER DEFAULT 0,
                category TEXT NOT NULL,
                month TEXT NOT NULL
            )''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Incomes (
                salary_Igor INTEGER DEFAULT 0,
                salary_Anastasiya INTEGER DEFAULT 0,
                bonus INTEGER DEFAULT 0,
                month TEXT NOT NULL
                )''')
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Obligations (
                        home_credit INTEGER DEFAULT 0,
                        auto_credit INTEGER DEFAULT 0,
                        creditcard INTEGER DEFAULT 0,
                        digi INTEGER DEFAULT 0,
                        strahovki INTEGER DEFAULT 0,
                        gasto_voda INTEGER DEFAULT 0,
                        gasto_gas INTEGER DEFAULT 0,
                        gasto_svet INTEGER DEFAULT 0,
                        ajuntamiento INTEGER DEFAULT 0,
                        communidad INTEGER DEFAULT 0,
                        GPT INTEGER DEFAULT 0,
                        amazon INTEGER DEFAULT 0,
                        obligations_month TEXT NOT NULL
                        )''')


months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

categories = [
    'Supermercado', 'Misc', 'Bar', 'Leo', 'FuelSeat', 'FuelPeugeot'
]


class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        widget.bind('<Enter>', self.show_tooltip)
        widget.bind('<Leave>', self.hide_tooltip)

    def show_tooltip(self, event):
        x = event.x_root + 20
        y = event.y_root + 20
        self.tooltip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f'+{x}+{y}')
        label = tk.Label(tw, text=self.text, bg='yellow', relief='solid', bd=4)
        label.pack()

    def hide_tooltip(self, event):
        if self.tooltip_window:
            self.tooltip_window.destroy()
        self.tooltip_window = None


def add_cost():
    cost = EnterText.get()
    selected_category = select_category_menu.get()
    select_category_menu.set(selected_category)
    selected_month = select_month_menu.get()
    select_month_menu.set(selected_month)
    if cost != '' and selected_category != 'Select category' and selected_month != 'Select month':
        with sq.connect('DataBase.db') as con:
            cursor = con.cursor()
            cursor.execute('''
                INSERT INTO Costs (cost, category, month) VALUES (?, ?, ?)
            ''', (cost, selected_category, selected_month))
            con.commit()
            EnterText.delete(0, 'end')
    else:
        messagebox.showinfo('Error', 'Error')
    update_balance()


def salary_settings_btn():
    global entry_igor_salary, entry_salary_anastasia, entry_bonus, salary_month

    new_window = tk.Toplevel(win)
    new_window.title('Salary settings')
    new_window.geometry('300x200+1200+700')
    new_window.resizable(False, False)
    new_window.config(bg='black')
    tk.Label(new_window, text='Igor:', bg='black', fg='orange', font=('Arial', 11)).grid(row=0, column=0, padx=5,
                                                                                            pady=5
                                                                                            )
    entry_igor_salary = tk.Entry(new_window)
    entry_igor_salary.grid(row=0, column=1, padx=5, pady=5)
    tk.Label(new_window, text='Anastasia:', bg='black', fg='orange', font=('Arial Bold', 11)).grid(row=1, column=0,
                                                                                                 padx=5, pady=5
                                                                                                 )
    entry_salary_anastasia = tk.Entry(new_window)
    entry_salary_anastasia.grid(row=1, column=1, padx=5, pady=5)
    tk.Label(new_window, text='Bonus:', bg='black', fg='orange', font=('Arial Bold', 11)).grid(row=2, column=0, padx=5,
                                                                                             pady=5
                                                                                             )
    entry_bonus = tk.Entry(new_window)
    entry_bonus.grid(row=2, column=1, padx=5, pady=5)
    tk.Label(new_window, text='Select month', bg='black', fg='orange', font=('Arial Bold', 11)).grid(row=3, column=0,
                                                                                                   padx=5, pady=5
                                                                                                   )
    salary_month = ttk.Combobox(new_window, values=months, state='readonly')
    salary_month.grid(row=3, column=1, padx=5, pady=5)
    salary_month.set('Select month')
    new_window.bind('<Return>', salary_data_save)
    salary_month.bind('<<ComboboxSelected>>', load_data_salary_settings)


def obligations_btn():
    global entry_kvartira, entry_seat, entry_credit_card, entry_strahovki, entry_communidad, obligations_month_menu
    global entry_ajuntamiento, entry_electro, entry_voda, entry_gas, entry_chatgpt, entry_DIGI, entry_amazon
    obligations_win = tk.Toplevel(win)
    obligations_win.title('Obligations')
    obligations_win.geometry('700x250+1400+900')
    obligations_win.config(bg='black')
    tk.Label(obligations_win, text='Kvartira', bg='black', fg='orange', font=('Arial Bold', 11)).grid(row=0, column=0,
                                                                                                      padx=5, pady=5,
                                                                                                      sticky='w'
                                                                                                      )

    entry_kvartira = tk.Entry(obligations_win)
    entry_kvartira.grid(row=0, column=1, padx=5, pady=5)
    tk.Label(obligations_win, text='Seat', bg='black', fg='orange', font=('Arial Bold', 11)).grid(row=1, column=0,
                                                                                                  padx=5, pady=5,
                                                                                                  sticky='w'
                                                                                                  )
    entry_seat = tk.Entry(obligations_win)
    entry_seat.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(obligations_win, text='Credit card', bg='black', fg='orange', font=('Arial Bold', 11)).grid(row=2, column=0,
                                                                                                         padx=5, pady=5,
                                                                                                         sticky='w'
                                                                                                         )
    entry_credit_card = tk.Entry(obligations_win)
    entry_credit_card.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(obligations_win, text='Strahovki', bg='black', fg='orange', font=('Arial Bold', 11)).grid(row=3, column=0,
                                                                                                       padx=5, pady=5,
                                                                                                       sticky='w'
                                                                                                       )
    entry_strahovki = tk.Entry(obligations_win)
    entry_strahovki.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(obligations_win, text='Communidad', bg='black', fg='orange', font=('Arial Bold', 11)).grid(row=4, column=0,
                                                                                                        padx=5, pady=5,
                                                                                                        sticky='w'
                                                                                                        )
    entry_communidad = tk.Entry(obligations_win)
    entry_communidad.grid(row=4, column=1, padx=5, pady=5)

    tk.Label(obligations_win, text='Ajutamiento', bg='black', fg='orange', font=('Arial Bold', 11)).grid(row=0, column=2,
                                                                                                         padx=5, pady=5,
                                                                                                         sticky='w'
                                                                                                         )
    entry_ajuntamiento = tk.Entry(obligations_win)
    entry_ajuntamiento.grid(row=0, column=3, padx=5, pady=5)

    tk.Label(obligations_win, text='Electro', bg='black', fg='orange', font=('Arial Bold', 11)).grid(row=1, column=2,
                                                                                                     padx=5, pady=5,
                                                                                                     sticky='w'
                                                                                                     )
    entry_electro = tk.Entry(obligations_win)
    entry_electro.grid(row=1, column=3, padx=5, pady=5)

    tk.Label(obligations_win, text='Voda', bg='black', fg='orange', font=('Arial Bold', 11)).grid(row=2, column=2,
                                                                                                  padx=5, pady=5,
                                                                                                  sticky='w'
                                                                                                  )
    entry_voda = tk.Entry(obligations_win)
    entry_voda.grid(row=2, column=3, padx=5, pady=5)

    tk.Label(obligations_win, text='Gas', bg='black', fg='orange', font=('Arial Bold', 11)).grid(row=3, column=2,
                                                                                                 padx=5, pady=5,
                                                                                                 sticky='w'
                                                                                                 )
    entry_gas = tk.Entry(obligations_win)
    entry_gas.grid(row=3, column=3, padx=5, pady=5)

    tk.Label(obligations_win, text='ChatGPT', bg='black', fg='orange', font=('Arial Bold', 11)).grid(row=0, column=4,
                                                                                                     padx=5, pady=5,
                                                                                                     sticky='w'
                                                                                                     )
    entry_chatgpt = tk.Entry(obligations_win)
    entry_chatgpt.grid(row=0, column=5, padx=5, pady=5)

    tk.Label(obligations_win, text='DIGI', bg='black', fg='orange', font=('Arial Bold', 11)).grid(row=1, column=4,
                                                                                                  padx=5, pady=5,
                                                                                                  sticky='w'
                                                                                                  )
    entry_DIGI = tk.Entry(obligations_win)
    entry_DIGI.grid(row=1, column=5, padx=5, pady=5)

    tk.Label(obligations_win, text='Amazon', bg='black', fg='orange', font=('Arial Bold', 11)).grid(row=2, column=4,
                                                                                                    padx=5, pady=5,
                                                                                                    sticky='w'
                                                                                                    )
    entry_amazon = tk.Entry(obligations_win)
    entry_amazon.grid(row=2, column=5, padx=5, pady=5)

    obligations_month_menu = ttk.Combobox(obligations_win, values=months, state='readonly')
    obligations_month_menu.set('Select month')
    obligations_month_menu.place(x=530, y=200)
    obligations_month_menu.bind('<<ComboboxSelected>>', load_data_obligations_settings)
    obligations_win.bind('<Return>', obligations_data_save)


def salary_data_save(event=None):
    month = salary_month.get()
    salary_igor = entry_igor_salary.get()
    salary_anastasia = entry_salary_anastasia.get()
    bonus = entry_bonus.get()

    if month == 'Select month':
        messagebox.showerror('Error', 'Select a month')
        return

    with sq.connect('DataBase.db') as con:
        cursor = con.cursor()
        cursor.execute('SELECT 1 FROM Incomes WHERE month = ?', (month,))
        exists = cursor.fetchone()

        if exists:
            cursor.execute('''
                UPDATE Incomes
                SET salary_Igor = ?, salary_Anastasiya = ?, bonus = ? WHERE month = ?
            ''', (salary_igor, salary_anastasia, bonus, month))

            messagebox.showinfo('Success', 'Data updated successfully')
        else:
            cursor.execute('''
                INSERT INTO Incomes (salary_Igor, salary_Anastasiya, bonus, month) VALUES (?, ?, ?, ?)
            ''', (salary_igor, salary_anastasia, bonus, month))
            messagebox.showinfo('Success', 'Data saved successfully')

        con.commit()
        update_balance()


def obligations_data_save(event=None):
    obligations_month = obligations_month_menu.get()
    home_credit = entry_kvartira.get()
    auto_credit = entry_seat.get()
    creditcard = entry_credit_card.get()
    digi = entry_DIGI.get()
    strahovki = entry_strahovki.get()
    gasto_voda = entry_voda.get()
    gasto_svet = entry_electro.get()
    gasto_gas = entry_gas.get()
    ajuntamiento = entry_ajuntamiento.get()
    communidad = entry_communidad.get()
    GPT = entry_chatgpt.get()
    amazon = entry_amazon.get()

    if obligations_month == 'Select month':
        messagebox.showerror('Error', 'Select month')
        return

    with sq.connect('DataBase.db') as con:
        cursor = con.cursor()
        cursor.execute('''SELECT 1 FROM Obligations WHERE obligations_month = ?''', (obligations_month,))
        exists = cursor.fetchone()

        if not exists:
            cursor.execute('''
                INSERT INTO Obligations (home_credit, auto_credit, creditcard, digi, strahovki, gasto_voda, gasto_gas, 
                gasto_svet, ajuntamiento, communidad, GPT, amazon, obligations_month) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,
                 ?, ?, ?, ?)''',
                           (home_credit, auto_credit, creditcard, digi, strahovki, gasto_voda, gasto_gas,
                            gasto_svet,ajuntamiento, communidad, GPT, amazon, obligations_month))
            messagebox.showinfo('Success', 'Data saved successfully')
        else:
            cursor.execute('''
                UPDATE Obligations
                SET home_credit = ?, auto_credit = ?, creditcard = ?, digi = ?, strahovki = ?, gasto_voda = ?, 
                gasto_gas = ?, gasto_svet = ?, ajuntamiento = ?, communidad = ?, GPT = ?, amazon = ? 
                WHERE obligations_month = ?''',
                           (home_credit, auto_credit, creditcard, digi, strahovki, gasto_voda, gasto_gas,
                            gasto_svet, ajuntamiento, communidad,GPT, amazon, obligations_month))
            messagebox.showinfo('Success', 'Data updated successfully')


def load_data_salary_settings(event=None):
    month = salary_month.get()

    if month == 'Select month':
        return

    with sq.connect('DataBase.db') as con:
        cursor = con.cursor()
        cursor.execute('''
            SELECT salary_Igor, salary_Anastasiya, bonus FROM Incomes WHERE month = ?
        ''', (month,))
    result = cursor.fetchone()

    if result:
        entry_igor_salary.delete(0, tk.END)
        entry_igor_salary.insert(0, result[0])
        entry_salary_anastasia.delete(0, tk.END)
        entry_salary_anastasia.insert(0, result[1])
        entry_bonus.delete(0, tk.END)
        entry_bonus.insert(0, result[2])
    else:
        entry_igor_salary.delete(0, tk.END)
        entry_salary_anastasia.delete(0, tk.END)
        entry_bonus.delete(0, tk.END)


def load_data_obligations_settings(event=None):
    obligations_month = obligations_month_menu.get()

    if obligations_month == 'Select month':
        entry_kvartira.delete(0, tk.END)
        entry_kvartira.insert(0, '0')
        entry_seat.delete(0, tk.END)
        entry_seat.insert(0, '0')
        entry_credit_card.delete(0, tk.END)
        entry_credit_card.insert(0, '0')
        entry_DIGI.delete(0, tk.END)
        entry_DIGI.insert(0, '0')
        entry_strahovki.delete(0, tk.END)
        entry_strahovki.insert(0, '0')
        entry_voda.delete(0, tk.END)
        entry_voda.insert(0, '0')
        entry_gas.delete(0, tk.END)
        entry_gas.insert(0, '0')
        entry_electro.delete(0, tk.END)
        entry_electro.insert(0, '0')
        entry_ajuntamiento.delete(0, tk.END)
        entry_ajuntamiento.insert(0, '0')
        entry_communidad.delete(0, tk.END)
        entry_communidad.insert(0, '0')
        entry_chatgpt.delete(0, tk.END)
        entry_chatgpt.insert(0, '0')
        entry_amazon.delete(0, tk.END)
        entry_amazon.insert(0, '0')
        return

    with sq.connect('DataBase.db') as con:
        cur = con.cursor()
        cur.execute('''SELECT home_credit, auto_credit, creditcard, digi, strahovki, gasto_voda, gasto_gas, 
            gasto_svet, ajuntamiento, communidad, GPT, amazon FROM Obligations WHERE obligations_month = ?''',
                    (obligations_month,))
        exists = cur.fetchone()

        if exists:
            entry_kvartira.delete(0, tk.END)
            entry_kvartira.insert(0, str(exists[0] if exists[0] is not None else 0))
            entry_seat.delete(0, tk.END)
            entry_seat.insert(0, str(exists[1] if exists[1] is not None else 0))
            entry_credit_card.delete(0, tk.END)
            entry_credit_card.insert(0, str(exists[2] if exists[2] is not None else 0))
            entry_DIGI.delete(0, tk.END)
            entry_DIGI.insert(0, str(exists[3] if exists[3] is not None else 0))
            entry_strahovki.delete(0, tk.END)
            entry_strahovki.insert(0, str(exists[4] if exists[4] is not None else 0))
            entry_voda.delete(0, tk.END)
            entry_voda.insert(0, str(exists[5] if exists[5] is not None else 0))
            entry_gas.delete(0, tk.END)
            entry_gas.insert(0, str(exists[6] if exists[6] is not None else 0))
            entry_electro.delete(0, tk.END)
            entry_electro.insert(0, str(exists[7] if exists[7] is not None else 0))
            entry_ajuntamiento.delete(0, tk.END)
            entry_ajuntamiento.insert(0, str(exists[8] if exists[8] is not None else 0))
            entry_communidad.delete(0, tk.END)
            entry_communidad.insert(0, str(exists[9] if exists[9] is not None else 0))
            entry_chatgpt.delete(0, tk.END)
            entry_chatgpt.insert(0, str(exists[10] if exists[10] is not None else 0))
            entry_amazon.delete(0, tk.END)
            entry_amazon.insert(0, str(exists[11] if exists[11] is not None else 0))

        else:
            entry_kvartira.delete(0, tk.END)
            entry_kvartira.insert(0, 0)
            entry_seat.delete(0, tk.END)
            entry_seat.insert(0, 0)
            entry_credit_card.delete(0, tk.END)
            entry_credit_card.insert(0, 0)
            entry_DIGI.delete(0, tk.END)
            entry_DIGI.insert(0, 0)
            entry_strahovki.delete(0, tk.END)
            entry_strahovki.insert(0, 0)
            entry_voda.delete(0, tk.END)
            entry_voda.insert(0, 0)
            entry_gas.delete(0, tk.END)
            entry_gas.insert(0, 0)
            entry_electro.delete(0, tk.END)
            entry_electro.insert(0, 0)
            entry_ajuntamiento.delete(0, tk.END)
            entry_ajuntamiento.insert(0, 0)
            entry_communidad.delete(0, tk.END)
            entry_communidad.insert(0, 0)
            entry_chatgpt.delete(0, tk.END)
            entry_chatgpt.insert(0, 0)
            entry_amazon.delete(0, tk.END)
            entry_amazon.insert(0, 0)


def update_balance(event=None):
    month = select_month_menu.get()

    with sq.connect('DataBase.db') as con:
        cursor = con.cursor()
        cursor.execute('''SELECT 1 FROM Incomes WHERE month = ?''', (month,))
        exists = cursor.fetchone()

        if exists:
            cursor.execute('''
                SELECT SUM(salary_Igor + salary_Anastasiya + bonus) FROM Incomes WHERE month = ?''', (month,))
            total_income = cursor.fetchone()[0] or 0
            cursor.execute('''SELECT SUM(home_credit + auto_credit + creditcard + digi + strahovki + gasto_voda + gasto_gas + 
                gasto_svet + ajuntamiento + communidad + GPT + amazon) FROM Obligations WHERE obligations_month = ?''',
                           (month,))
            total_obligations = cursor.fetchone()[0] or 0
            cursor.execute('''
                SELECT SUM(cost) FROM Costs WHERE month = ?''', (month,))
            total_cost = cursor.fetchone()[0] or 0
            balance = total_income - total_cost - total_obligations
            if balance > 0:
                label_balance.config(text=f'Balance: {balance:.2f} €', fg='green')
            else:
                label_balance.config(text=f'Balance: {balance:.2f} €', fg='red')

        else:
            balance = 0.00
            label_balance.config(text=f'Balance: {balance:.2f} €', fg='orange')
    update_costs()
    con.commit()


def update_incomes(event=None):
    month = select_month_menu.get()

    with sq.connect('DataBase.db') as con:
        cur = con.cursor()
        cur.execute('''
            SELECT 1 FROM Incomes WHERE month = ?''', (month,))
        exists = cur.fetchone()
        if exists:
            cur.execute('''
                SELECT SUM(salary_Igor + salary_Anastasiya + bonus) FROM Incomes WHERE month = ?''', (month,))
            total_income = cur.fetchone()[0] or 0
            label_incomes.config(text=f'Incomes: {total_income:.2f} €', fg='green')

        else:
            total_income = 0.00
            label_incomes.config(text=f'Incomes: {total_income:.2f} €', fg='orange')


def update_costs(event=None):
    month = select_month_menu.get()

    with sq.connect('DataBase.db') as con:
        cur = con.cursor()
        cur.execute('''
            SELECT 1 FROM Costs WHERE month = ?''', (month,))
        exists = cur.fetchone()
        if exists:
            cur.execute('''
                SELECT SUM(cost) FROM Costs WHERE month = ?''', (month,))
            total_cost = cur.fetchone()[0] or 0
            label_costs.config(text=f'Current costs: {total_cost:.2f} €', fg='red')

        else:
            total_cost = 0.00
            label_costs.config(text=f'Current costs: {total_cost:.2f} €', fg='orange')

    con.commit()


def update_obligations(event=None):
    month = select_month_menu.get()

    with sq.connect('DataBase.db') as con:
        cur = con.cursor()
        cur.execute('''
            SELECT 1 FROM Obligations WHERE obligations_month = ?''', (month,))
        exists = cur.fetchone()
        if exists:
            cur.execute('''
                SELECT SUM(home_credit + auto_credit + creditcard + digi + strahovki + gasto_voda + gasto_gas + 
                gasto_svet + ajuntamiento + communidad + GPT + amazon) FROM Obligations WHERE obligations_month = ?''', (month,))
            total_obligations = cur.fetchone()[0] or 0
            label_obligations.config(text=f'Obligations: {total_obligations:.2f} €', fg='red')

        else:
            total_obligations = 0.00
            label_obligations.config(text=f'Obligations: {total_obligations:.2f} €', fg='orange')


def category_sum(event=None):
    month = select_month_menu.get()

    with sq.connect('DataBase.db') as con:
        cur = con.cursor()
        cur.execute('''
            SELECT SUM(cost) FROM Costs WHERE category = 'Supermercado' AND month = ?
            ''', (month,))
        result = cur.fetchone()[0] or 0

        cur.execute('''
                        SELECT SUM(cost) FROM Costs WHERE category = 'Misc' AND month = ?
                        ''', (month,))
        result1 = cur.fetchone()[0] or 0

        cur.execute('''
                        SELECT SUM(cost) FROM Costs WHERE category = 'Bar' AND month = ?
                        ''', (month,))
        result2 = cur.fetchone()[0] or 0

        cur.execute('''
                        SELECT SUM(cost) FROM Costs WHERE category = 'Leo' AND month = ?
                        ''', (month,))
        result3 = cur.fetchone()[0] or 0

        cur.execute('''
                        SELECT SUM(cost) FROM Costs WHERE category = 'FuelSeat' AND month = ?
                        ''', (month,))
        result4 = cur.fetchone()[0] or 0

        cur.execute('''
                        SELECT SUM(cost) FROM Costs WHERE category = 'FuelPeugeot' AND month = ?
                        ''', (month,))
        result5 = cur.fetchone()[0] or 0

    return result, result1, result2, result3, result4, result5


def update_tooltip():
    result = category_sum()
    tooltip_text = (f'Supermercado: {result[0]:.2f}€\n'
                    f'Misc:         {result[1]:.2f}€\n'
                    f'Bar:          {result[2]:.2f}€\n'
                    f'Leo:          {result[3]:.2f}€\n'
                    f'FuelSeat:     {result[4]:.2f}€\n'
                    f'FuelPeugeot:  {result[5]:.2f}€')
    ToolTip(label_costs, tooltip_text)


def all_func_for_one_event(event=None):
    update_balance()
    update_incomes()
    update_tooltip()
    update_costs()
    update_obligations()


def enter_click(event):
    add_cost()


def focus_out(event):
    if EnterText.get() == '':
        EnterText.insert(0, 'add cost...')
        EnterText.config(fg='grey')


def focus_on(event):
    if EnterText.get() == 'add cost...':
        EnterText.delete(0, 'end')
        EnterText.insert(0, '')
        EnterText.config(fg='black')


create_table_database()

win = tk.Tk()

win.title('Expense Management')            # TITLE
win.geometry('600x400+1000+500')           # WINDOW SIZE
win.resizable(True, True)     # RESIZABLE
# win.minsize(500, 600)
# win.maxsize(800, 900)

icon = tk.PhotoImage(file='icon.png')      # UKAZYVAEM PUT' K IKONKE
win.iconphoto(False, icon)          # STAVIM IKONKU
win.config(bg='black')                     # CVET FONA

# create frames
top_frame = tk.Frame(win, bg='black')
top_frame.pack(pady=10)

middle_frame = tk.Frame(win, bg='black')
middle_frame.pack(pady=10)

bottom_frame = tk.Frame(win, bg='black')
bottom_frame.pack(pady=10)

# top frame elements
EnterText = tk.Entry(top_frame, fg='grey')
EnterText.insert(0, 'add cost...')
EnterText.bind('<FocusIn>', focus_on)
EnterText.bind('<FocusOut>', focus_out)
EnterText.grid(row=0, column=0, padx=10)
EnterText.bind('<Return>', enter_click)


select_month_menu = ttk.Combobox(top_frame, values=months, state='readonly')
select_month_menu.set('Select month')
select_month_menu.bind('<<ComboboxSelected>>', all_func_for_one_event)
select_month_menu.grid(row=0, column=2, padx=10)


select_category_menu = ttk.Combobox(top_frame, values=categories, state='readonly')
select_category_menu.set('Select category')
select_category_menu.grid(row=0, column=1, padx=10)


btn_addCost = tk.Button(top_frame, text='add',
                        fg='orange',
                        bg='black',
                        relief=tk.RAISED,
                        bd=4,
                        activebackground='black',
                        command=add_cost
                        )
btn_addCost.grid(row=0, column=3, padx=10)

# middle frame elements
btn_salary_settings = tk.Button(middle_frame, text='Salary settings',
                                bg='black',
                                fg='orange',
                                relief=tk.RAISED,
                                bd=4,
                                command=salary_settings_btn
                                )
btn_salary_settings.grid(row=0, column=0, padx=10)

obligations_btn_settings = tk.Button(middle_frame, text='Obligations settings',
                                     bg='black',
                                     fg='orange',
                                     relief=tk.RAISED,
                                     bd=4,
                                     command=obligations_btn
                                     )
obligations_btn_settings.grid(row=0, column=1, padx=10)

# bottom frame elements
label_incomes = tk.Label(bottom_frame, bg='black', fg='orange', font=('Arial Bold', 15), text='Incomes: 0.00 €')
label_incomes.grid(row=0, column=0, sticky='w')
label_costs = tk.Label(bottom_frame, bg='black', fg='orange', font=('Arial Bold', 15), text='Current costs: 0.00 €')
label_costs.grid(row=1, column=0, sticky='w')
label_balance = tk.Label(bottom_frame, bg='black', fg='orange', font=('Arial Bold', 15), text='Balance: 0.00 €')
label_balance.grid(row=1, column=1, padx=20, sticky='w')
label_obligations = tk.Label(bottom_frame, bg='black', fg='orange', font=('Arial Bold', 15), text='Obligations: 0.00 €')
label_obligations.grid(row=2, column=0, sticky='w')

update_tooltip()

win.mainloop()
