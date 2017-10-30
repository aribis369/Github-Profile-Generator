from flask import Flask, redirect, url_for, request, render_template
from urllib.request import urlopen
import json
import sklearn
from bs4 import BeautifulSoup
import os
import sys
import sklearn


data = {"arindambiswas":{"name":"Arindam Biswas", "gh_handle":"aribis369" ,"fb_link":"https://facebook.com/aribis369", "bio":"to be written by the member", "pic_src":"link", "role":"Core Team Member"}, "dibyaprakashdas":{"name":"Dibya Prakash Das", "gh_handle":"dibyadas", "fb_link":"https://facebook.com/user_name", "bio":"whatever you like", "pic_src":"link", "role":"Core Team Member"},
"pranitbauva":{"name":"Panit Bauva", "gh_handle":"pranitbauva1997" ,"fb_link":"https://facebook.com/user_name", "bio":"to be written by the member", "pic_src":"link", "role":"Executive Lead Marketing"},
"himanshumishra":{"name":"Himanshu Mishra", "gh_handle":"orkohunter" ,"fb_link":"https://facebook.com/user_name", "bio":"to be written by the member", "pic_src":"link", "role":"Advisor"},
"ayushgoyal":{"name":"Ayush Goyal", "gh_handle":"Defcon-007" ,"fb_link":"https://facebook.com/user_name", "bio":"to be written by the member", "pic_src":"lnik of the repo", "role":"Executive Head Projects"}}

r=0
f=0
app = Flask(__name__)


@app.route('/<name>')
def main(name):
    mname = data[name]["gh_handle"]
    repos = []
    repolink = []
    pinned_repos=[]
    pinned_repolinks=[]
    blog = str()
    pic=str()
    content={}
    gh_link = "https://github.com/"+mname

    httpob = urlopen("https://api.github.com/users/"+mname+"/repos")
    decob = httpob.read().decode("utf-8")
    jsonob = json.loads(decob)
    for j in jsonob:
        if str(j["fork"])=="False":
            repos.append(j["name"])
            repolink.append("https://www.github.com/"+j["full_name"])
    
    httpob = urlopen("https://api.github.com/users/"+mname)
    decob = httpob.read().decode("utf-8")
    jsonob = json.loads(decob)
    blog = jsonob["blog"]
    pic=jsonob["avatar_url"]
    bio=jsonob["bio"]
  
    u=urlopen("https://github.com/"+mname)
    s=BeautifulSoup(u)
    l=s.find_all("span",{"class":"repo js-repo"})
    for i in l:
        pinned_repos.append(i.get("title"))
        pinned_repolinks.append("https://github.com/"+mname+"/"+i.get("title"))
    print(pinned_repos)
    print("\n\n")
    print(pinned_repolinks)  

    content = {"name":data[name]["name"], "gh_handle":data[name]["gh_handle"], "fblink":data[name]["fb_link"], "bio":bio, "picsrc":pic, "repos":repos, "repolink":repolink, "blog":blog, "role":data[name]["role"], "pinned":pinned_repos, "pinnedlinks":pinned_repolinks}

   # return render_template('test.html', mem_name=data[name]["name"], gh_handle=data[name]["gh_handle"], fblink=data[name]["fb_link"], bio=data[name]["bio"], picsrc=data[name]["pic_src"], mrepos=repos, mrepolink=repolink, mblog=blog) 
    x = render_template('temp.html', content=content)
    with open("templates/t2.html","w") as f:
        f.write(x)
    return "True"

if __name__ == "__main__":  # This is for local testing
    print("initialising")
    k=0
    print("init end")
    app.run(host='localhost', port=3453, debug=True)

# if __name__ == "__main__":  # This will come in use when
#     port = int(os.environ.get("PORT", 5000))  # the app is deployed on heroku
#     app.run(host='0.0.0.0', port=port)




