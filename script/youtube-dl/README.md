# intro
利用 python 

# requirement
需要先下載相關套件
```shell
apt install ffmpeg
pip install yt-dlp
```
# 執行
```shell
python ./script/youtube-dl/yt_playlist_dl.py \
  --id "PLqEyIPVxcpv1wpZgG850S6jWo4j2X_Rn-" --outDir ./tmp \
  --fromIndex 67 --audio-low
```