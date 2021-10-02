import json
import os

path = 'CC201'

# get array of folder titles
foldertitles = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path,name))]

# get array of file paths
folderinfo = []
for foltitle in foldertitles:
	curfol = '/'+foltitle
	folcontent = os.listdir(path+curfol)
	filelinks = [curfol+'/'+name for name in folcontent]
	# extract and clean file title from first line of file
	filetitles = []
	for flink in filelinks:
		with open(path+flink) as f: firline=f.readline().rstrip()
		rmspacehash=''.join(firline.split('# '),1)
		rmhash=''.join(rmspacehash.split('#'),1)
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
		'darkThemeToggler':'true',
		'sourcePath':'./CC201',
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

#wrap new docute and write to script.js

docutescript = 'new Docute(XXXXX)'
docutescript = docutescript.replace('XXXXX',json.dumps(jscomplete).replace('\\"','"').replace('["','[').replace('"]',']'))
print(docutescript)

f = open("script.js", "w")
f.write(docutescript)
f.close()
f = open("script.js", "r")
print(f.read())
f.close()

### manual template below
##j1 = json.dumps(
##	{
##		'title':'Zuoye',
##		'target':'#docute',
##		'theme':'dark',
##		'darkThemeToggler':'true',
##		'sourcePath':'./CC201',
##		'nav':[
##				{
##					'title':'Home','link':'/'
##				},
##				{
##					'title':'About','link':'/README2'
##				}
##		],
##		'sidebar': [
##			{
##				'title':foldertitles[0],'links':[
##					{
##						'title':filetitles[0],'link':filelinks[0]
##					},
##					{
##						'title':filetitles[1],'link':filelinks[1]
##					}
##				]
##			},
##		]
##	}
##)
##
##print(json.loads(j1))