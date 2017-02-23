import praw
import time

bot = "mars-rover"
sub = "indonesia+indonesiacirclejerk"

def mars_lyric():
	lyric = """
**M**ARILAH SELURUH RAKYAT INDONESIA

**A**RAHKAN PANDANGANMU KE DEPAN

**R**AIHLAH MIMPIMU BAGI NUSA BANGSA

**S**ATUKAN TEKADMU TUK MASA DEPAN
		
&nbsp;

**P**ANTANG... MENYERAH... ITULAH... PEDOMANMU

**E**NTASLAH KEMISKINAN CITA-CITAMU

**R**INTANGAN TAK MENGGETARKAN DIRIMU

**I**NDONESIA MAJU, SEJAHTERA, TUJUANMU

**N**YALAKAN API SEMANGAT PERJUANGAN

**D**ENGUNGKAN GEMA, NYATAKAN PERSATUAN

**O**LEH PERINDO... OLEH PERINDO.... 

&nbsp;

**JAYALAH INDONESIA**
		"""
	return lyric

def bot_login():
	print("Logging in...")
	reddit = praw.Reddit(bot)
	print("Logged in!")
	return reddit

def main(reddit):
	for comment in reddit.subreddit(sub).stream.comments():
		if ("mars perindo" in comment.body.lower()):
			name = comment.author.name
			if (bot != name):
				print("comment found! by " + name)
				print(">> " + comment.body)
				print("replying...")
				comment.reply(mars_lyric())
				time.sleep(60)

while True:
	reddit = bot_login()
	main(reddit)