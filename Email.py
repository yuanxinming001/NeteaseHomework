import smtplib
from email.mime.text import MIMEText
import result


def emailya(result):
    # 登陆邮箱
    sent = smtplib.SMTP()
    sent.connect('smtp.qq.com', 25)
    mail_name = "2431542413@qq.com"  # 发送人邮箱地址
    mail_password = "rmuhrohrwfzodifa"  # 注意：这里不是密码，而应该填写授权码！！
    sent.login(mail_name, mail_password)  # 登陆

    # 编辑邮件内容
    to = ['2431542413@qq.com']  # 收件人邮箱地址
    content = MIMEText(result)  # 正文内容
    print(result)
    content['Subject'] = '漂流瓶'  # 邮件标题
    content['From'] = mail_name  # 发件人
    content['To'] = ','.join(to)  # 收件人，用逗号连接多个邮件，实现群发

    # 发送邮件
    try:
        sent.sendmail(mail_name, to, content.as_string())  # 3个参数 发送人，收件人，邮件内容
        print('Success')
        sent.close()
    except smtplib.SMTPException:
        print("Error：Fail")



