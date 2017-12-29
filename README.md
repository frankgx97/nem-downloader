### 关于本项目
由于2016年网易云音乐的API变化，由旧API解析出的mp3文件URL全部失效。因此我基于musicbox项目中封装的新版API制作了这个下载器，用于通过歌曲，歌单或专辑id解析及下载mp3文件。
本站生成的下载地址仅限使用中国大陆境内IP下载，否则将返回404。
请将本服务部署在中国境内，或者连接至中国境内的代理。否则API返回的下载地址全部为`None`
### 部署
```
docker run --name=nem -p 8000:8000 nyanim/nem-downloader
```
手动部署请参考Dockerfile
API相关文档请移步https://github.com/darknessomi/musicbox/wiki
### DEMO
http://nem-downloader.nyan.im/
### 关于URL格式
网易云音乐的URL格式有很多种，例如：
http://music.163.com/#/my/m/music/playlist?id=3756532（歌单）
http://music.163.com/song/22635188/?userid=xxxxxxx（歌曲）
本站仅接受形为http://music.163.com/#/[song|playlist|album]?id=[0-9]+的URL，如果为其他格式请自行修改。
### 关于我
https://blog.nyan.im/me
### 鸣谢
[musicbox](https://github.com/darknessomi/musicbox)高品质网易云音乐命令行版本，简洁优雅，丝般顺滑，基于Python编写。
