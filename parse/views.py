#coding:utf8
from django.shortcuts import render
from django.http import HttpResponse
import re

from api import *
from song import *

# Create your views here.

def index (request):
    url = request.GET.get('url',-1)
    if url == -1:
        return render(request, 'index.html')
    ne = NetEase()
    #先判断传入的参数是否为url或id，如果是url则切割为id，如果为id则直接传入，都不是则报错
    pattern = re.compile(r'http:\/\/music\.163\.com\/#\/song\?id=[0-9]+')#判断输入的url符合规则
    pattern2 = re.compile(r'http:\/\/music\.163\.com\/#\/song\?id=[0-9]+[^\d]+')#如果正常url后面跟有非数字的字符也会被上面的表达式匹配
    url_valid = re.match(pattern,url) and not re.match(pattern2,url)#如url匹配第一个表达式且不匹配第二个表达式则有效
    id_legal = True
    if url_valid:
        pattern = re.compile(r'=')
        song_id = re.split(pattern,url)[1]
        valid = True
        url_legal = True
    else:
        valid = False
        song_id = 0
        url_legal = False
    if valid and url_legal:
        mp3_url = ne.songs_detail_new_api([song_id])[0]['url']
        try:
            s = Song(song_id)
            title = s.title
            artist = s.artist
            album = s.album_title
            cover_url = s.album_cover_url
        except:
            mp3_url = ''
            title = ''
            artist = ''
            album = ''
            cover_url = ''
            id_legal = False
            valid = False
    else:
        mp3_url = ''
        title = ''
        artist = ''
        album = ''
        cover_url = ''
    return render(request, 'index.html',{'mp3_url': mp3_url,'valid':valid,'url_legal':url_legal,'id_legal':id_legal,'title':title,'artist':artist,'album':album,'cover_url':cover_url})

def about(request):
    return render(request,'about.html')
