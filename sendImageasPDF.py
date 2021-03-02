import tkinter as tk
from tkinter import filedialog
import img2pdf as converter
import os
import smtplib
from email.message import EmailMessage

def send_email_right_now():
    useremail = os.environ.get('useremail', 'Enter Your email here')
    password = os.environ.get('userpass', 'Enter Your Password')
    filename = input('Name for PDF: ')
    dataset = convert2pdf(filename)
    if dataset[0]:
        msg = EmailMessage()
        msg['Subject'] = 'Sending Images as PDF'
        msg['From'] = useremail
        msg['To'] = 'acharyaraj9865032909@gmail.com'
        msg.set_content('College Documents: PDF :: Notes')
        with open(dataset[1],'rb') as f:
            file_data = f.read()
            file_name = f.name
            fileArrayString = f.name.split('/')
            file_name = fileArrayString[len(fileArrayString) - 1]
            print(file_name)
            msg.add_attachment(file_data, maintype='image', subtype='video', filename=file_name)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            print('Sending Message\r', end='')
            smtp.login(useremail, password)
            smtp.send_message(msg)
            print('Message has been sent')
    else:
        print('Cannot Send Image as PDF has not been created')
def get_file_list():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    root.title('Choose Images')
    files = filedialog.askopenfilenames(title='Choose Images')
    return files
def convert2pdf(title):
    files = get_file_list()
    try:
        out = open(f'{title}.pdf', 'wb')
        out.write(converter.convert(files))
        out.close()
        print('Converted')
        return [True, '{}.pdf'.format(title)]
    except Exception:
        print('Cannot Convert to PDF')
        return [False]

if __name__ == '__main__':
    current = os.path.dirname(__file__)
    data = os.path.join(current, 'log.txt')
    f = open(data, 'r+')
    line = f.readlines()
    if len(line) == 0:
        print('Please Install Required Package')
        f.write('logged')
    else:
        send_email_right_now()