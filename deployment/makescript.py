import json
import os

# open config
print(os.getcwd())
config = open('./deployment/config.json', "r")
confstatic = json.loads(config.read())
config.close()

# get path and array of folder titles
path = confstatic['sourcePath']
foldertitles = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path,name))]

# get array of file paths only if ends in ".md"
folderinfo = []
for foltitle in foldertitles:
	curfol = '/'+foltitle
	folcontent = os.listdir(path+curfol)
	sfolcontent = sorted(folcontent)
	filelinks = [curfol+'/'+name for name in sfolcontent if name[-3:].lower() == ".md"]
	## extract and clean file title from first line of markdownfile
	filetitles = []
	for flink in filelinks:
		with open(path+flink) as f: firline=f.readline().rstrip()
		rmspacehash=''.join(firline.split('# '))
		rmhash=''.join(rmspacehash.split('#'))
		filetitles.append(rmhash)
	linkinfo = []
	for i in range(len(filelinks)):
	## manualjsonify
		ln = "{\"title\":\""+filetitles[i]+"\",\"link\":\""+filelinks[i]+"\"}"
		linkinfo.append(ln)
	## comma join link info (stringified json)
	jslinks = ','.join(linkinfo)
	## wrap folder/guide title around jslinks
	folwraptemplate = "{ \"title\":\""+foltitle+"\",\"links\":[XXXXXXXXXX] }"
	folcomplete = folwraptemplate.replace('XXXXXXXXXX',jslinks)
	folderinfo.append(folcomplete)

# end of loop through files/folders. gather all info
jsfolders = [json.loads(folderi) for folderi in folderinfo]
# create variable part of final json
dynamic =  {'sidebar':jsfolders }
# > currently only to fill sidebar ToC with folder info

completeconf = confstatic.copy()
completeconf.update(dynamic)

stringjson = json.dumps(completeconf,ensure_ascii=False).encode('utf8')
readable = json.dumps(completeconf,ensure_ascii=False,indent=4).encode('utf8')
print(readable.decode())

# wrap in new vue docute element and write to script
docutescript = 'new Docute(XXXXX)'.replace('XXXXX',stringjson.decode())
newscript = open("./assets/script.js", "w")
newscript.write(docutescript)
newscript.close()
