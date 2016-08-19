#coding:utf8
from django.shortcuts import render
from django.http import HttpResponse
import re

from api import *

# Create your views here.

def verify_url(url,url_type):
    pattern = re.compile(r'http:\/\/music\.163\.com\/#\/' + url_type + '\?id=[0-9]+')#判断输入的url符合规则
    pattern2 = re.compile(r'http:\/\/music\.163\.com\/#\/' + url_type + '\?id=[0-9]+[^\d]+')#如果正常url后面跟有非数字的字符>
    if re.match(pattern,url) and not re.match(pattern2,url):
        return True
    else:
        return False

def url_split(url):
    pattern = re.compile(r'=')
    return re.split(pattern,url)[1]

def index (request):
    url = request.GET.get('url',-1)
    if url == -1:
        return render(request, 'index.html')
    ne = NetEase()
    #先判断传入的参数是否为url或id，如果是url则切割为id，如果为id则直接传入，都不是则报错
    url_valid = verify_url(url, 'song')
    id_legal = True
    if url_valid:
        song_id = url_split(url)
        valid = True
        url_legal = True
    else:
        valid = False
        url_legal = False
        song_id = 0
    song_list = []
    if valid and url_legal:
        try:
            i = ne.song_detail(song_id)[0]
            song_item = {
                    'id':i['id'],
                    'title':i['name'],
                    'artist':i['artists'][0]['name'],
                    'album':i['album']['name'],
                    'cover_url':i['album']['picUrl'],
                    'mp3_url':ne.songs_detail_new_api([i['id']])[0]['url']
                    }
            song_list.append(song_item)
        except:
            id_legal = False
            valid = False
    return render(request, 'index.html', {'valid':valid, 'url_legal':url_legal, 'id_legal':id_legal, 'song_list':song_list})

def about(request):
    return render(request,'about.html')

def play_list(request):
    url = request.GET.get('url',-1)
    if url == -1:
        return render(request, 'list.html')
    ne = NetEase()
    url_valid = verify_url(url, 'playlist')
    id_legal =True
    if url_valid:
        playlist_id = url_split(url)
        valid = True
        url_legal = True
    else:
        valid = False
        url_legal = False
        playlist_id = 0
    song_list = []
    if valid and url_legal:
        try:
            for i in ne.playlist_detail(playlist_id):
                song_item = {
                        'id':i['id'],
                        'title':i['name'],
                        'artist':i['artists'][0]['name'],
                        'album':i['album']['name'],
                        'cover_url':i['album']['picUrl'],
                        'mp3_url':ne.songs_detail_new_api([i['id']])[0]['url']
                        }
                song_list.append(song_item)
        except:
            id_legal = False
            valid = False
    return render(request, 'list.html', {'valid':valid, 'url_legal':url_legal, 'id_legal':id_legal, 'song_list':song_list})

def album(request):
    url = request.GET.get('url',-1)
    if url == -1:
        return render(request, 'album.html')
    ne = NetEase()
    url_valid = verify_url(url, 'album')
    id_legal =True
    if url_valid:
        album_id = url_split(url)
        valid = True
        url_legal = True
    else:
        valid = False
        url_legal = False
        album_id = 0
    song_list = []
    if valid and url_legal:
        try:
            for i in ne.album(album_id):
                song_item = {
                        'id':i['id'],
                        'title':i['name'],
                        'artist':i['artists'][0]['name'],
                        'album':i['album']['name'],
                        'cover_url':i['album']['picUrl'],
                        'mp3_url':ne.songs_detail_new_api([i['id']])[0]['url']
                        }
                song_list.append(song_item)
        except:
            id_legal = False
            valid = False
    return render(request, 'album.html', {'valid':valid, 'url_legal':url_legal, 'id_legal':id_legal, 'song_list':song_list})

