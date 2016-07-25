
import sys, os, gzip, urllib.request

sources = {
	"Bluetack LVL 1": "http://list.iblocklist.com/?list=bt_level1&fileformat=p2p&archiveformat=gz",
	"Bluetack LVL 2": "http://list.iblocklist.com/?list=bt_level2&fileformat=p2p&archiveformat=gz",
	"Bluetack LVL 3": "http://list.iblocklist.com/?list=bt_level3&fileformat=p2p&archiveformat=gz",
	"Bluetack edu": "http://list.iblocklist.com/?list=bt_edu&fileformat=p2p&archiveformat=gz",
	"Bluetack ads": "http://list.iblocklist.com/?list=bt_ads&fileformat=p2p&archiveformat=gz",
	"Bluetack spyware": "http://list.iblocklist.com/?list=bt_spyware&fileformat=p2p&archiveformat=gz",
	"Bluetack proxy": "http://list.iblocklist.com/?list=bt_proxy&fileformat=p2p&archiveformat=gz",
	"Bluetack badpeers": "http://list.iblocklist.com/?list=bt_templist&fileformat=p2p&archiveformat=gz",
	"Bluetack Microsoft": "http://list.iblocklist.com/?list=bt_microsoft&fileformat=p2p&archiveformat=gz",
	"Bluetack spider": "http://list.iblocklist.com/?list=bt_spider&fileformat=p2p&archiveformat=gz",
	"Bluetack hijacked": "http://list.iblocklist.com/?list=bt_hijacked&fileformat=p2p&archiveformat=gz",
	"Bluetack dshield": "http://list.iblocklist.com/?list=bt_dshield&fileformat=p2p&archiveformat=gz",
	"Bluetack forumspam": "http://list.iblocklist.com/?list=ficutxiwawokxlcyoeye&fileformat=p2p&archiveformat=gz",
	"Bluetack webexploit": "http://list.iblocklist.com/?list=ghlzqtqxnzctvvajwwag&fileformat=p2p&archiveformat=gz",
	"TBG Primary Threats": "http://list.iblocklist.com/?list=ijfqtofzixtwayqovmxn&fileformat=p2p&archiveformat=gz",
	"TBG General Corporate Range": "http://list.iblocklist.com/?list=ecqbsykllnadihkdirsh&fileformat=p2p&archiveformat=gz",
	"TBG Buissness ISPs": "http://list.iblocklist.com/?list=jcjfaxgyyshvdbceroxf&fileformat=p2p&archiveformat=gz",
	"TBG Educational Institutions": "http://list.iblocklist.com/?list=lljggjrpmefcwqknpalp&fileformat=p2p&archiveformat=gz"
}

whereami = os.path.dirname(os.path.abspath(sys.argv[0]))

if os.path.isfile(whereami + '/blocklist.txt'):
	os.remove(whereami + '/blocklist.txt')

with open(whereami + '/blocklist.txt', 'a+') as newlist:
	for k, v in sources.items():
		print("Fetching: {} ({})".format(k, v))

		response = urllib.request.urlopen(v)

		saveto = ''.join([whereami, '/lists/', k, '.gz'])

		with open(saveto, 'wb') as tmp:
			print("> Downloading list ({})".format(saveto))

			while True:
				d = response.read(1024)

				if len(d) == 0:
					break

				tmp.write(d)

		gz = gzip.GzipFile(saveto)

		for line in gz:
			newlist.write(str(line))

		print("> Appended to blocklist")
