from string import Template
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib


# Email do qual você vai enviar.
meu_email = 'SEUGMAIL@GMAIL.COM' 
# Senha do email acima.
minha_senha = 'SUASENHA'                


data_hoje = datetime.now().strftime('%d/%m/%Y')

with open(r'string_template_email\template.html', 'r') as html:
    template = Template(html.read())
    corpo_msg = template.substitute(nome='Banana Verde', data=data_hoje) # podendo usar .safe_substitude se não for utilizar todos os placeholder


msg = MIMEMultipart()
# Seu nome.
msg['from'] = 'SEU NOME' 
# Email para quem voce deseja enviar.
msg['to'] = 'EMAILDOCLIENTE@GMAIL.COM' 
# Assunto.
msg['subject'] = 'ASSUNTO DO EMAIL' 

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)


# Aqui você utiliza o with para abrir sua mensagem e inserir na mensagem que será enviada (A imagem vai em anexo).
with open(r'Caminho_imagem.png', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        # Teste de conexão.
        smtp.ehlo()
        smtp.starttls()
        # Autenticação.
        smtp.login(meu_email, minha_senha)
        # Envio do email.
        smtp.send_message(msg)
        print('E-mail enviado com sucesso.')
    except Exception as error:
        print('E-mail não enviado...')
        print(f'Erro: {error}')


#print(corpo_msg)