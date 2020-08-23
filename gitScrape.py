import bs4
from urllib.request import urlopen as urlReq
from bs4 import BeautifulSoup as soup

username = input("Enter Username :")
myurl = "https://github.com/"+username+"?tab=repositories"

uClient = urlReq(myurl)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html , "html.parser")

containers = page_soup.findAll("div", {"class":"col-10 col-lg-9 d-inline-block"})

repo_count = page_soup.findAll("span",{"class":"Counter"})
print("Total number of commits: ",repo_count[0].text)

filename = "Repo_list.csv"
f = open(filename, "w")

headers = "Repository_name, Language, Last_update\n"

f.write(headers)

for container in containers:
    repo = container.findAll("h3" , {"class":"wb-break-all"})
    repo_name = ((repo[0].text).replace(" ","")).replace("\n","")

    lang = container.findAll("span",{"itemprop":"programmingLanguage"})
    repo_lang = lang[0].text

    last_update = container.findAll("relative-time")
    update_time = (last_update[0].text).replace("," , "")

    print("Repository Name: "+repo_name+" ("+repo_lang+")"+" Last Update: "+update_time)

    f.write(repo_name+ "," + repo_lang + ","+ update_time+"\n")

f.close()