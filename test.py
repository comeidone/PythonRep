import requests

def main ():
    req=requests.get("http://google.it")
    print("REQUEST IS: ",req.reason)
    
    writer=open("page.txt","w")
    writer.write(req.text)
    writer.close

    print("WRITE!")

if __name__ == "__main__":
    main()
