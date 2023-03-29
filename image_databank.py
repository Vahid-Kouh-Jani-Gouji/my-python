import requests

url="https://habibihello.com/"
image = requests.get(url)
with open ('image_data.jpg','wb') as file : file.write(image.content)
print("download completed")
 
 