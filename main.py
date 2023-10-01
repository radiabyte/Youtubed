import os
import pytube
import re
from pytube import YouTube



currentloc=str(os.getcwd())
req=currentloc+'\Downloaded'
if os.path.exists(req)==False:
    os.system('md Downloaded')


def extract_variable_value(stream_metadata, variable_name):
    match=re.search(rf'{variable_name}="(.+?)" ',stream_metadata)
    if match:
        return match.group(1)
    else:
        return None
link=input('Give link : ')
yt=YouTube(link)
print('''So you're looking for''',yt.title)


list_audio=yt.streams.filter(only_audio=True)
a=[]
b=[]
for items in list_audio:
    x=int((str(extract_variable_value(str(items),'abr'))).strip('kbps'))
    y=str(extract_variable_value(str(items),'itag'))
    a.append(x)
    b.append(y)



mydic={}
for i in range(0,len(a)):
    mydic[a[i]]=b[i]
mykeys=list(mydic.keys())
mykeys.sort()
sorteddic={i:mydic[i] for i in mykeys}
sorteddiclist=list(sorteddic.keys())
print('''Here's What We Got : ''','\n')
print('Audio')
print('\n')

for lo in range(0,len(list(sorteddic.keys()))):
    gettagsize=sorteddiclist[lo]
    ids=sorteddic[gettagsize]
    streamsize=yt.streams.get_by_itag(ids)
    sizeof=int(streamsize.filesize/(1048576))
    print(str(lo+1)+'.'+str((list(sorteddic.keys()))[lo]),'kbps','('+str(sizeof),'MB'+')')
print('\n')

def downloader(idno,res): 
    stream=yt.streams.get_by_itag(idno)
    name=yt.title+str(res)+'kbps'+'.mp3'
    stream.download(filename=name , output_path=req)
    
    
gettag=int(input('Which one would you like to download : '))
if gettag<=len(sorteddiclist) and gettag>0:
    gettagres=sorteddiclist[gettag-1]
    idx=sorteddic[gettagres]
    downloader(int(idx),gettagres)
    print('Done')
else:
    print('Invalid Input')

