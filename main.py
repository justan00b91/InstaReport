import os
import time

files = sorted(os.listdir(), reverse=True)

txt = [file for file in files if file.endswith('.txt')]
img = [file for file in files if file.endswith('.jpg')]
vid = [file for file in files if file.endswith('.mp4')]

Page_title_text = "InstaReport by justan00b91"
text = "[Default Description of Posts]"
link = " "
content = " "
tmp = " "

for i in files:
    date = i.split('_')[0]

    if tmp != date:
        text = "[Default Description of Posts]"

    if i in txt:
        with open(i) as f:
            text = f.read()

    if i in img:
        link_img = i
        content_img = f'''

        <div class="accordion" style="display: flex;align-items:flex-start; gap: 2rem;">
            <div class="left">
                <img class="accordion-img" src="{link_img}" alt="img not avaiable">
            </div>
            <div class="right">
                <div class="left-text" style="margin-bottom: 1rem;font-size: 1.25rem;">{text}</div>
                <div class="right-text" style="color: rgb(51, 51, 51); font-weight: 600;">Image</div>
                <div class="right-text" style="color: rgb(51, 51, 51); font-weight: 600;">{date}</div>
            </div>
        </div>
        '''
        content = content + content_img
        
        

    if i in vid:
        link_vid = i
        content_vid = f'''

        <div class="accordion" style="display: flex;align-items:flex-start; gap: 2rem;">
            <div class="left">
                <video class="accordion-img" src="{link_vid}" alt="vid not avaliable" width:300px>
            </div>
            <div class="right">
                <div class="left-text" style="margin-bottom: 1rem;font-size: 1.25rem;">{text}</div>
                <div class="right-text" style="color: rgb(51, 51, 51); font-weight: 600;">Video</div>
                <div class="right-text" style="color: rgb(51, 51, 51); font-weight: 600;">{date}</div>
            </div>
        </div>
        '''
        content = content + content_vid

    tmp = date                          # Change This!

html = f'''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>InstaReport</title>
    <style>        
        h1 {{
            border-bottom: 0.1rem solid #000;
            padding-bottom: 1rem;
         }}

        .accordion {{
            cursor: pointer;
            position: relative;
            padding: 0.5rem 2rem;
        }}

        .accordion:nth-child(even) {{
            background-color: rgb(224, 224, 224);
        }}
    
        .accordion-img {{
            width: 100px;
        }}

    </style>
</head>

<body>
    <h1 style="text-align: center;">{Page_title_text}</h1>
    <div class="accordion-container">
        {content}
    </div>
</body>

</html>
'''

with open('index.html', 'w') as f:
    f.write(html)
