import requests

def Download(url,name):
    print("Download started!!")
    response = requests.get(url)
    open(f"Downloaded Files/page{name+1}.html","wb").write(response.content)
    print("Download Finished!!")

if __name__ == "__main__":
    url = [
    "https://theuselessweb.com/",
    "https://pointerpointer.com/",
    "https://www.zoomquilt.org/",
    "https://www.boredbutton.com/",
    "https://thispersondoesnotexist.com/",
    "https://longdogechallenge.com/",
    "https://smashthewalls.com/",
    "https://heeeeeeeey.com/",
    "https://eelslap.com/",
    "https://ninjaflex.com/",
    "https://cat-bounce.com/",
    "https://www.staggeringbeauty.com/",
    "https://www.republiquedesmangues.fr/",
    "https://clickingbad.com/",
    "https://www.fallingfalling.com/",
    "https://zoomquilt.org/",
    "https://endless.horse/",
    "https://chrismckenzie.com/",
    "https://zombo.com/",
    "https://www.patience-is-a-virtue.org/",
    "https://thatsthefinger.com/",
    "https://weirdorconfusing.com/",
    "https://www.trypap.com/",
    "https://www.donothingfor2minutes.com/",
    "https://www.hackertyper.com/",
    "https://geektyper.com/",
    "https://fakeupdate.net/",
    "https://www.rainymood.com/",
    "https://mondrianandme.com/",
    "https://koalastothemax.com/",
    "https://pixelsfighting.com/",
    "https://beesbeesbees.com/",
    "https://www.autodraw.com/",
    "https://radio.garden/",
    "https://www.typatone.com/",
    "https://musclewiki.com/",
    "https://neal.fun/deep-sea/",
    "https://neal.fun/absurd-trolley-problems/",
    "https://neal.fun/draw-your-island/",
    "https://neal.fun/infinite-craft/",
    "https://thewikigame.com/",
    "https://www.window-swap.com/",
    "https://littlealchemy2.com/",
    "https://sketchful.io/",
    "https://www.chess.com/analysis",
    "https://volcano.discovery/",
    "https://www.foddy.net/CLOP.html",
    "https://www.windows93.net/",
    "https://www.sanger.dk/",
    "https://dogs.are.the.most.moe/"]
    for x in range(10):
        Download(url[x],x)

