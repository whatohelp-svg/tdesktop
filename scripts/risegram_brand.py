"""Render the supplied monochrome RiseGram mark into desktop icon resources."""
from pathlib import Path
import re
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "Telegram/Resources/art"
# Outline traced from the owner's supplied 1536px logo; normalized using its circle.
PLANE = [(1051,554),(1054,563),(1057,602),(1054,687),(1045,757),(1029,839),(1013,898),(982,980),(952,1031),(942,1041),(930,1048),(910,1051),(884,1045),(855,1034),(818,1014),(784,989),(749,955),(732,934),(722,916),(721,894),(732,871),(829,782),(844,766),(848,758),(851,745),(848,722),(841,711),(831,701),(815,694),(793,694),(777,701),(612,852),(597,858),(540,859),(495,852),(463,841),(451,834),(436,821),(429,809),(426,786),(432,768),(445,752),(489,711),(550,666),(594,639),(651,609),(710,583),(765,563),(852,539),(946,525),(1018,525),(1037,535)]
def icon(size, margin=0.0):
    s = size * 4
    pad = s * margin
    diameter = s - 2 * pad
    image = Image.new("RGBA", (s,s), (0,0,0,0))
    draw = ImageDraw.Draw(image)
    draw.ellipse((pad,pad,s-pad-1,s-pad-1), fill=(0,0,0,255))
    draw.polygon([(pad+(x-192)*diameter/1151, pad+(y-193)*diameter/1151) for x,y in PLANE], fill="white")
    return image.resize((size,size), Image.Resampling.LANCZOS)
for path in ART.glob("icon*.png"):
    if not re.fullmatch(r"icon(?:_round)?\d+(?:@2x)?\.png|icon_green\.png|iconbig_green\.png",path.name):
        continue
    with Image.open(path) as old:
        w,h=old.size
    if w != h:
        raise ValueError(f"Unexpected icon shape: {path}")
    icon(w, 0.025).save(path)
for name, margin in [("logo_256.png",0.055),("logo_256_no_margin.png",0.0)]:
    path=ART/name
    with Image.open(path) as old:
        w,h=old.size
    assert w==h
    icon(w,margin).save(path)
icon(256,0.025).save(ART/"icon256.ico",sizes=[(16,16),(24,24),(32,32),(48,48),(64,64),(128,128),(256,256)])
# Keep legal notices, external URLs and internal identifiers intact.
for path in [ROOT/"Telegram/Resources/langs/lang.strings", ROOT/"Telegram/Resources/langs/cloud_lang.strings"]:
    text=path.read_text(encoding="utf-8")
    lines=[]
    for line in text.splitlines(keepends=True):
        if re.match(r'^"[^"]+"\s*=',line):
            line=re.sub(r'(?<![\w./:@-])Telegram Desktop(?![\w./:@-])',"RiseGram Desktop",line)
            line=re.sub(r'(?<![\w./:@-])Telegram(?![\w./:@-])',"RiseGram",line)
            line=line.replace("Welcome to the official RiseGram Desktop app.","Welcome to RiseGram Desktop.")
        lines.append(line)
    path.write_text("".join(lines),encoding="utf-8")
print("RiseGram desktop icon and built-in interface strings prepared")
