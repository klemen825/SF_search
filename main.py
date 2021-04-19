import requests

API_KEY="AIzaSyDx3Q_4iObyix8rdjLeYmb7aBuKGOxjPGs"#spremenljivka z api key za povezavo z apijem
ENGINE_ID="59218ae0ba9a96487"#spremenljiva z ID-jem iskalnika
LOKACIJA="si"#spremenljivka za določitev lokacije
start=1#APIjeva določena spremenljivka, ki pove indeks od katerega rezultate nej naprej išče
rezultat=[]
search=input("kaj želiš iskat jebemtimatr ")
for i in range(15):#for zanka za kolikokkrat se zažene query
    query="https://www.googleapis.com/customsearch/v1?key="+API_KEY+"&cx="+ENGINE_ID+"&gl="+LOKACIJA+"&q="+search+"&start="+str(start)#
    response=requests.get(query) #v get damo linki, k ga hočem poiskat, nazaj pa dobimo kar spletna stran vrne
    if response.status_code!=200:#pogoj da so pravilni rezultati, 200 je html koda za successful rezultat (npr.404 pomeni error)
        print ("but i wont do that... no no i wont do that") #moja briljantna šala
    temp=response.json()
    if int(temp["searchInformation"]["totalResults"])==0:
        break
    rezultat.extend(response.json()['items'])#spremenljivka v kateri so shranjeni rezultati iskanja v json formatu
    start+=10 #spremenljivki start povečamo vrednost za 10, ker query vrne samo 10 rezultatov na stran.
print (rezultat)# izpišemo rezultat json
vagina=[]#seznam v katerem so shranjeni linki
for dick in rezultat:#loop po vseh linki. loop bo šel čez vse rezultate in iz njih izbral polje link
   vagina.append(dick['link'])#zapis linka v seznam
print (vagina)#printanje rezultatov
bondage=set()#množica v katerem so domene
for fetus in vagina:#loop da gre čez vse linke 
    anus=fetus.split("/")#določimo po katerem znaku razbijemo link. rezultat je seznam naprimer: https:,'',www.neki.si,klemen je gej
    bdsm=anus[2].split("www.")#razbiti link vzamemo drugi element, da dobimo domeno LOGIČNO.rezultat je naprimer: '',neki.si
    bondage.add(bdsm[-1])#v množico zapišemo zadnji element(domena) iz array/seznama bdsm
print (len(bondage)) #sprintamo bondage len iziše število elementov znotraj seznama (en element=1link)
print (bondage)
qwdqwdwqdwqdwqdwqdwqd