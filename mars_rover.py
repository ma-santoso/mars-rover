import praw
import config
import time

def mars_lyric():
	lyric = """
		MARILAH SELURUH RAKYAT INDONESIA
		ARAHKAN PANDANGANMU KE DEPAN
		RAIHLAH MIMPIMU BAGI NUSA BANGSA
		SATUKAN TEKADMU TUK MASA DEPAN
		PANTANG.... MENYERAH.... 
		ITULAH ... PEDOMANMU
		ENTASLAH KEMISKINAN CITA-CITAMU
		RINTANGAN TAK MENGGETARKAN DIRIMU
		INDONESIA MAJU, SEJAHTERA, TUJUANMU
		NYALAKAN API SEMANGAT PERJUANGAN
		DENGUNGKAN GEMA, NYATAKAN PERSATUAN
		OLEH PERINDO....OLEH PERINDO.... 
		JAYALAH INDONESIA
		"""
	return lyric

def bot_login():
	print("Loggin in...")
	reddit = praw.Reddit(username = config.username,
		password = config.password,
		client_id = config.client_id,
		client_secret = config.client_secret,
		user_agent = "mars-rover")
	print("Logged in!")
	return reddit

def run_bot(reddit):
	sub = reddit.subreddit("mharcss")
	bot = "mars-rover"
	for comment in sub.stream.comments():
		if ("perindo" in comment.body.lower() or 
			"mars" in comment.body.lower()):
				name = comment.author.name
				if (bot != name):
					print("comment found! by " + name)
					comment.reply(mars_lyric())

	time.sleep(10)

while True:
	reddit = bot_login()
	run_bot(reddit)