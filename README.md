# python_exercise

給初學者用來參考的 python 練習題。

## Build image
需要先具備 docker system 之後會比較容易使用隔離系統練習
```sh
## 下載程式碼
git clone git@github.com:wyubin/python_exercise.git
## 啟動安裝程式
sh python_exercise/docker/install.sh
## 進入 container 中執行程式
docker exec -it python_exercise ash
```

## Example

```sh
## prepare your ans with "ans_" prefix
## then test by exec python script
python set/test_ch3_set.py
```