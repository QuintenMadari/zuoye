import json
import os

path = './CC201'

# get array of folder titles
foldertitles = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path,name))]

# get array of file paths
folderinfo = []
for foltitle in foldertitles:
	curfol = '/'+foltitle
	folcontent = os.listdir(path+curfol)
	sfolcontent = sorted(folcontent)
	filelinks = [curfol+'/'+name for name in sfolcontent]

	# extract and clean file title from first line of file
	filetitles = []
	for flink in filelinks:
		with open(path+flink) as f: firline=f.readline().rstrip()
		rmspacehash=''.join(firline.split('# '))
		rmhash=''.join(rmspacehash.split('#'))
		filetitles.append(rmhash)
	linkinfo = []
	for i in range(len(filelinks)):
		ln = json.dumps(
			{
			'title':filetitles[i],'link':filelinks[i]
			}
		)
		linkinfo.append(ln)
	#comma join of several json dumps
	jslinks = ','.join(linkinfo)
	#wrap folder/guide title around jslinks
	folwraptemplate = json.dumps(
		{
			'title':foltitle,'links':[
				'XXXXXXXXXX'
			]
		}
	)
	folcomplete = folwraptemplate.replace('XXXXXXXXXX',jslinks)
	folderinfo.append(folcomplete)
jsfolders = ','.join(folderinfo)

#sidebar collection: wrap around appended folders

jsidebar = json.dumps(
	{
		'sidebar':[jsfolders]
	}
)

#combine jhead to jsidebar

jhead = json.dumps(
	{
		'title':'作业',
		'target':'#docute',
		'theme':'dark',
		'darkThemeToggler':'false',
		'editLinkBase':'https://github.com/QuintenMadari/yiqizuozuoye/src/main/',
		'editLinkText':'编辑这篇文章 在 GitHub',
		'sourcePath':path,
		'nav':[
				{
					'title':'Home','link':'/'
				},
				{
					'title':'About','link':'/README2'
				}
		]
	}
)

dictA = json.loads(jhead)
dictB = json.loads(jsidebar)
jscomplete = dictA.copy()
jscomplete.update(dictB)

#also clean up the json from errant backslashes and double quotes

replacement = json.dumps(jscomplete).replace('\\"','"').replace('["','[').replace('"]',']').replace('\\\\u','\\u')

#wrap new docute and write to script.js
readable = json.dumps(json.loads(replacement),indent=4)
print(readable)

docutescript = 'new Docute(XXXXX)'.replace('XXXXX',replacement)

f = open("./assets/script.js", "w")
f.write(docutescript)
f.close()

#f = open("script.js", "r")
#print(f.read())
#f.close()

