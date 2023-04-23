#stmplib模块主要负责连接，登录和发送邮件的步骤
#email模块主要负责整合收发件人，正文和附件等内容
import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

#连接并登录邮箱
qqMail=smtplib.SMTP_SSL("smtp.qq.com",465)
mailUser="2972074454@qq.com"#发件人的邮箱
mailPass="yigtyjmfrbjiddjd"#授权码
qqMail.login(mailUser,mailPass)

#设置收发件人
sender="2972074454@qq.com"#发件人的邮箱
receiver=""#收件人的邮箱
#使用MIMEMultipart()类创建一个实例对象message，MIMEMultipart()用于整合邮件头，正文，附件等信息
message=MIMEMultipart()
#整合主题和收发件人到实例对象中
message["Subject"]=Header("给夜曲的一封信——小关")
message["From"]=Header(f"xiaoguan<{sender}>")#xiaoguan一定要写英文
message["To"]=Header(f"yqbc<{receiver}>")

textContent=""#写信的内容
#类MIMEText用来构建文件正文
mailContent=MIMEText(textContent,"plain","utf-8")#"plain"是纯文本格式，"utf-8"编码用来防止中文乱码
filePath=r""#前面加r防止转义
#读取图片文件,"rb"指的是read binary，以二进制形式读取文件内容
with open(filePath,"rb") as imageFile:
    fileContent=imageFile.read()

#设置邮件附件
attachment=MIMEImage(fileContent)
#添加附件标题
attachment.add_header("Content-Disposition","attachment",filename="")#要写与路径一样的后缀，文件名.png，"Content-Disposition","attachment"这两个为固定参数

#把编辑好的正文和附件添加到MIMEMultipart()类的message实例化对象中
message.attach(mailContent)
message.attach(attachment)

#发送邮件，使用对象qqMail的sendmail方法发送邮件
qqMail.sendmail(sender,receiver,message.as_string())#message.as_string()参数为邮件内容，将对象message变为字符串类型
print("发送成功")
