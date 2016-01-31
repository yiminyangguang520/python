__author__ = 'ypw'
import re

html = """function assignSources(){

	var fileExt=".mp3"; if (bSUPPORTOGG==1) {fileExt=".ogg";}
	sourceFileA[0]='http://cdn.mynoise.net/Data/JAMMER/0b'+fileExt;
	sourceFileB[0]='http://cdn.mynoise.net/Data/JAMMER/0a'+fileExt;
		sourceFileA[1]='http://cdn.mynoise.net/Data/JAMMER/1a'+fileExt;
	sourceFileB[1]='http://cdn.mynoise.net/Data/JAMMER/1b'+fileExt;
		sourceFileA[2]='http://cdn.mynoise.net/Data/JAMMER/2b'+fileExt;
	sourceFileB[2]='http://cdn.mynoise.net/Data/JAMMER/2a'+fileExt;
		sourceFileA[3]='http://cdn.mynoise.net/Data/JAMMER/3a'+fileExt;
	sourceFileB[3]='http://cdn.mynoise.net/Data/JAMMER/3b'+fileExt;
		sourceFileA[4]='http://cdn.mynoise.net/Data/JAMMER/4a'+fileExt;
	sourceFileB[4]='http://cdn.mynoise.net/Data/JAMMER/4b'+fileExt;
			sourceFileA[5]='http://cdn.mynoise.net/Data/JAMMER/5b'+fileExt;
	sourceFileB[5]='http://cdn.mynoise.net/Data/JAMMER/5a'+fileExt;
		sourceFileA[6]='http://cdn.mynoise.net/Data/JAMMER/6a'+fileExt;
	sourceFileB[6]='http://cdn.mynoise.net/Data/JAMMER/6b'+fileExt;
		sourceFileA[7]='http://cdn.mynoise.net/Data/JAMMER/7a'+fileExt;
	sourceFileB[7]='http://cdn.mynoise.net/Data/JAMMER/7b'+fileExt;
		sourceFileA[8]='http://cdn.mynoise.net/Data/JAMMER/8a'+fileExt;
	sourceFileB[8]='http://cdn.mynoise.net/Data/JAMMER/8b'+fileExt;
		sourceFileA[9]='http://cdn.mynoise.net/Data/JAMMER/9b'+fileExt;
	sourceFileB[9]='http://cdn.mynoise.net/Data/JAMMER/9a'+fileExt;
	}
"""
p = re.compile(r'(http://cdn\.mynoise\.net/Data/.+?)\'')
url2s = p.findall(html)
for u in url2s:
    print u
