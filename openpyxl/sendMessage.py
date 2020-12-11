import smtplib
import pandas as pd

your_name = "Username"
your_email = "my_email@gmail.com"
your_password = "my_password"


smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(your_email, your_password)

email_list = pd.read_excel('due_records.xlsx')

names = email_list['Name']
emails = email_list['Email']
expenses = email_list['Expense']


for i in range(len(emails)):
    name = names[i]
    email = emails[i]
    expense = expenses[i]

    if expense < 100:

        body = 'subject: Greetings.\nDear ' + name + \
            '\nGood morning!\nYour expense is: ' + str(expense)

        sendMessageStatus = smtpObj.sendmail(
            'my_email@gmail.com', email, body)

        if sendMessageStatus != {}:
            print('there was a problem sending email to:    ', email)

smtpObj.quit()
