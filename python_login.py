import requests                        #immports the reqd libs

with requests.Session() as c:
    url = 'http://phc.prontonetworks.com/cgi-bin/authlogin?URI=http://www.google.co.in/'  #use the target url , url given in here was my target url(GDG)
    Username = "please use yours ;p"   #stores the reg.no
    Password = "idk or use crunch"     #stores the password
    c.get(url)                         #to access the given url
    token = c.cookies['csrftoken']     #to get the cookies and store it
    login_details = dict(csrfmiddlewaretoken = token , username = Username , password = Password)   #storing the login details in a dictionary for accessing
    c.post(url, data=login_details, headers={"Referer": "http://phc.prontonetworks.com/"})          #page to visit after logging with prior login details
    page = c.get('http://phc.prontonetworks.com/cgi-bin/authlogin?URI=http://go.microsoft.com/fwlink/')   #gets the content of the page
    print(page.content)                                                       #prints the content