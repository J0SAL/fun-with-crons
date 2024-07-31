import os
from flask_mail import Message 
from dotenv import load_dotenv

load_dotenv() 

def send_personalized_email(mail):
    try:
        subject = 'Maximize Your Financial Future with Bank of Baroda'
        msg = Message(
            subject,
            sender=(os.getenv('MAIL_SENDER'), os.getenv('SENDER_MAIL_ID')),
            recipients=['gauravparulekar02@gmail.com']
        )
        msg.html = "<html><body style='font-family: Arial, sans-serif;'><div style='background-color: orange; padding: 20px; text-align: center;'><h1 style='color: white;'>Bank of Baroda Retirement Plans</h1></div><img src='https://ik.imagekit.io/553gmaygy/DALL_E%202024-07-31%2002.29.47%20-%20An%20advertisement%20for%20a%20home%20loan%20targeting%20Ram,%20a%2048-year-old%20salaried%20employee%20living%20in%20Delhi.%20The%20ad%20features%20Ram%20with%20his%20family%20in%20front%20of%20a%20spa.webp?updatedAt=1722373370627' alt='Bank of Baroda Advertisement' style='display: block; margin: 20px auto; max-width: 100%; height: auto;'/><div style='padding: 20px;'><h2>Dear Valued Customer,</h2><p>As you plan for your future, we at Bank of Baroda are here to help you make the most of your financial journey. With your current spending patterns and future goals in mind, we have tailored some investment opportunities and services just for you.</p><h3>Investment Opportunities</h3><ul><li><strong>Alternate Investment Products:</strong> Explore a diverse range of options including Portfolio Management Services, Alternative Investment Funds, and more to enhance your portfolio.</li><li><strong>Mutual Fund Investment:</strong> Invest in a variety of mutual funds through our Investment Services Account, with easy digital access and professional management.</li><li><strong>Baroda M-Invest App:</strong> Simplify your investing with our mobile app, allowing you to manage your investments and track your portfolio effortlessly.</li></ul><h3>Optimize Your Credit Card Usage</h3><p>With your recent credit card spending, consider utilizing our rewards program to maximize your benefits. Earn points on every purchase and redeem them for exciting rewards tailored to your lifestyle.</p><h3>Customized Retirement Plan</h3><p>At 26, you have a fantastic opportunity to secure your financial future. Based on your retirement age of 60 and life expectancy of 80, we recommend starting a retirement savings plan that aligns with your goal of accumulating approximately ₹15,187,365. Our <strong>IndiaFirst Life Guaranteed Pension Plan</strong> offers a secure way to ensure a steady income post-retirement.</p><p>Let us help you take the next steps towards a prosperous future. For more information, feel free to reach out to us or visit our website.</p><p>Best Regards,<br/>Bank Of Baroda</p></div><footer style='text-align: center; padding: 20px;'><p>Website: <a href='https://www.bankofbaroda.in/' style='color: orange;'>www.bankofbaroda.in</a></p></footer></body></html>"
        mail.send(msg)
        print('Email sent successfully')
    except Exception as e:
        print(f'Failed to send email: {e}')