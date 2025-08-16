import requests
API_KEY = 'p6sMC3jvBDJVTMHRBfyXL9fn' 
input_path = 'backremover1.jpg'
output_path = 'output.png'
with open(input_path, 'rb') as image_file:
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': image_file},
        data={'size': 'auto'},
        headers={'X-Api-Key': API_KEY},
    )
if response.status_code == requests.codes.ok:
    with open(output_path, 'wb') as out:
        out.write(response.content)
    print("Background removed successfully and saved to", output_path)
else:
    print("Error:", response.status_code, response.text)
