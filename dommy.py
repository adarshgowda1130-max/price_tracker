import os
from dotenv import load_dotenv
load_dotenv()
import smtplib
email=os.getenv("my_email")
password=os.getenv("email_password")
reciever=os.getenv("to_adderss")
product_title="chain"
actual_price=90
message=f"your product\n{product_title}\n it price is now affordable,it is {actual_price}"
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(user=email,password=password)
connection.sendmail(from_addr=email,to_addrs=reciever,msg=f"subject:price alert!!\n\n{message}".encode("utf-8"))
connection.close()