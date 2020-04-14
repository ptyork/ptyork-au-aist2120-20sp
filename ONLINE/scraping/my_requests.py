import requests

# Generic way of saving a web file
def save(filename, rsp):
    with open(filename, 'wb') as file:
        for bytes in rsp.iter_content(10000):
            file.write(bytes)


rsp = requests.get("https://en.wikipedia.org/wiki/Tower_Records")
# print(rsp.status_code)
rsp.raise_for_status()

print(rsp.text)

save('tower.html', rsp)

rsp = requests.get("https://upload.wikimedia.org/wikipedia/en/thumb/d/db/Towersignheader.png/330px-Towersignheader.png")
rsp.raise_for_status()
print(rsp.text)
save('tower.png', rsp)
