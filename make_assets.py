# Rebuilds logo.png, icons, and og-image.png from the originals in brand/. Run: python3 make_assets.py (needs Pillow)
import os
from PIL import Image, ImageDraw, ImageFont
G=(31,58,52);GOLD=(224,178,90);CREAM=(243,236,216)
def F(sz):
    for p in ['/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf']:
        if os.path.exists(p): return ImageFont.truetype(p,sz)
    return ImageFont.load_default()
W=Image.open('brand/rlcc-logo-white.png').convert('RGBA'); W=W.crop(W.getchannel('A').getbbox())
h=W.height; mark=W.crop((0,0,h,h))          # the round leaf mark at the left of the logo
web=W.copy(); web.thumbnail((700,200)); web.save('logo.png')
def icon(n,k,path):
    im=Image.new('RGB',(n,n),G); m=mark.resize((int(n*k),int(n*k)),Image.LANCZOS); im.paste(m,((n-m.width)//2,(n-m.height)//2),m); im.save(path)
os.makedirs('icons',exist_ok=True)
icon(192,.62,'icons/icon-192.png');icon(512,.62,'icons/icon-512.png');icon(512,.46,'icons/icon-maskable-512.png')
icon(180,.62,'icons/apple-touch-icon.png');icon(64,.7,'icons/favicon.png')
og=Image.new('RGB',(1200,630),G);d=ImageDraw.Draw(og);d.rectangle([0,0,14,630],fill=GOLD)
lg=W.copy(); lg.thumbnail((620,120)); og.paste(lg,(70,70),lg)
d.text((70,230),'Wise Hours',font=F(104),fill=CREAM)
d.text((72,370),'Managing time and energy,',font=F(44),fill=CREAM)
d.text((72,428),'resting in Jesus',font=F(44),fill=CREAM)
d.text((72,540),'Ephesians 5:15-20',font=F(34),fill=GOLD)
og.save('og-image.png')
