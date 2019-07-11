import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
from config import mail, to, password

SUBJECT = "A product on your Watchlist is in sale!"


def send_mail(data:dict):
    if data["notify"] == "False":
        msg = MIMEMultipart()
        msg["From"] = mail
        msg["To"] = to
        msg["Subject"] = SUBJECT
        product_name = data["Name"]
        product_url = data["url"]
        product_price = data["price"]
        product_price_amazon = data["amazon_price"]
        message = f"""
        Hey,
        {product_name} is now in sale! 
        Price: {product_price_amazon}€
        Price you wanna: {product_price}€
        You can buy it here: {product_url}
        """
        msg.attach(MIMEText(message, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(mail, password)
        text = msg.as_string()
        server.sendmail(mail, to, text)
        server.quit()
        update_notify(data["Name"])

    return


def update_notify(name:str):
    with open("./src/articles.json") as fp:
        data_list = json.load(fp)
    _index = [i for i, _ in enumerate(data_list) if _["Name"] == name][0]
    mod_dict = data_list[_index]
    del data_list[_index]
    mod_dict["notify"] = "True"
    data_list.append(mod_dict)
    with open("./src/articles.json", "w") as fp:
        json.dump(data_list, fp, indent=2)
