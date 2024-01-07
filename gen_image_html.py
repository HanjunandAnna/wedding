from glob import glob


def gen_template(img_file_name):
    new_name = img_file_name.replace('jpeg', 'jpg')
    html_str = """<div class="col-md-2">"""
    html_str += f"<a class=\"fancybox\" rel=\"group\" href=\"img/pics/{img_file_name}\">"
    html_str += """<div class="img-wrap"> <div class="overlay"> <i class="fa fa-search"></i> </div>"""
    html_str += f"<img src=\"img/pics_cropped/{new_name}\" alt=\"\"/>"
    html_str += "</div> </a> </div>"
    return html_str

imgs = glob("./img/pics/*")

entire_html = ""
for img_path in imgs:
    img_name = img_path.split('/')[-1]
    entire_html += gen_template(img_name)
print(entire_html)