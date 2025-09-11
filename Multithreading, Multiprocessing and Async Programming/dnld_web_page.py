import requests
import multiprocessing


def Download(url,name):
    print(f"Downloading page{name}!!")
    response = requests.get(url)
    open(f"Downloaded Files/page{name+1}.html","wb").write(response.content)
    print(f"Page{name} Downloaded!!")

if __name__ == "__main__":
    url = 'https://en.wikipedia.org/wiki/Special:Random'
    for x in range(100):
        Pros = multiprocessing.Process(target = Download, args = [url, x])
        Pros.start()



