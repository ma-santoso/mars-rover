import praw

bot = "mars-rover"

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
	print("Logging in...")
	reddit = praw.Reddit(bot)
	print("Logged in!")
	return reddit

def main(reddit):
	sub = reddit.subreddit("indonesia")
	for comment in sub.stream.comments():
		if ("perindo" in comment.body.lower() or 
			"mars" in comment.body.lower()):
				name = comment.author.name
				if (bot != name):
					print("comment found! by " + name)
					print(comment.body)
					#comment.reply(mars_lyric())

while True:
	reddit = bot_login()
	main(reddit)
