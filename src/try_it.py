import mesop as me
# import mesop.labs as mel
import requests, json

def get_cat_image():
    image_url = ""
    data = requests.get("https://api.thecatapi.com/v1/images/search").json()[0]
    print(data)
    if 'url' in data:
        image_url += data['url']
    return image_url

@me.page()
def page():

    # image = 

    me.image(
        src=get_cat_image(),
        alt="Meow!",
        style=me.Style(width="100%")
    )
    # mel.chat(title="What??")
    me.text("Have you heard of any updog around here?")
    me.button("What is updog?")
