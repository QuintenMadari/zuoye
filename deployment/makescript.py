import json
import os

# open config
print(os.getcwd())
config = open('./deployment/config.json', "r")
dictStatic = json.loads(config.read())
config.close()

# get path and array of folder titles
path = dictStatic['sourcePath']
foldertitles = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path,name))]

# get array of file paths only if ends in ".md"
folderinfo = []
for foltitle in foldertitles:
	curfol = '/'+foltitle
	folcontent = os.listdir(path+curfol)
	sfolcontent = sorted(folcontent)
	filelinks = [curfol+'/'+name for name in sfolcontent if name[-3:].lower() == ".md"]
	print(filelinks)
	## extract and clean file title from first line of markdownfile
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
	## comma join of json dumps of link info (stringified json)
	jslinks = ','.join(linkinfo)
	## wrap folder/guide title around jslinks
	folwraptemplate = json.dumps( { 'title':foltitle,'links':['XXXXXXXXXX'] } )
	folcomplete = folwraptemplate.replace('XXXXXXXXXX',jslinks)
	folderinfo.append(folcomplete)

# end of loop through files/folders. joining all info
jsfolders = ','.join(folderinfo)

# create variable part of final json
jdynamic = json.dumps( { 'sidebar':[jsfolders] } )
# > currently only to fill sidebar ToC with folder info

# combine dynamic into static config dict and turn into final json
dictDynamic = json.loads(jdynamic)
jscomplete = dictStatic.copy()
jscomplete.update(dictDynamic)

# clean up the json from errant backslashes and double quotes (caused by json dump)
replacement = json.dumps(jscomplete).replace('\\"','"').replace('["','[').replace('"]',']').replace('\\\\u','\\u')

# pretty print the final json for debugging/visual inspection
readable = json.dumps(json.loads(replacement),indent=4)
print(readable)

# wrap in new vue docute element and write to script
docutescript = 'new Docute(XXXXX)'.replace('XXXXX',replacement)
newscript = open("./assets/script.js", "w")
newscript.write(docutescript)
newscript.close()