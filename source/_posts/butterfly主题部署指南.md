---
title: butterfly主題部署指南
date: 2025-08-09 14:25:50
tags:
  - Butterfly
  - 主題部署
---

# hexo的butterfly主題美化，2024年初版

轉載自：https://blog.csdn.net/JesseXW

**先貼上butterfly主題作者的官方美化文件地址，如果有大老比較會的可直接看他的（~~不過部分功能可能用不了了~~）：**  
[Butterfly 安裝文檔(一) 快速開始 | Butterfly](https://butterfly.js.org/posts/21cfbf15/#%E5%8D%87%E7%B4%9A%E5%BB%BA%E8%AD%B0)

<!-- more -->

**注意！！！如果發現配置不生效，請先執行 `hexo clean`，然後清除瀏覽器快取試試。如果還是不行，請檢查配置檔案的縮排是否有問題！！！**

## 1. 準備工作

### 1.1 安裝butterfly

**在hexo的根目錄下**鍵入以下命令：

```bash
npm install hexo-theme-butterfly
```

### 1.2 修改配置檔案，應用butterfly主題

修改 `_config.yml` 中的 `theme` 屬性為 `butterfly`。

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-0cc53ca3fb892aa2d472d0ca54158de2.png)

### 1.3 安裝外掛

**如果你沒有 pug 以及 stylus 的渲染器，請下載安裝：**

在hexo根目錄下鍵入以下命令：

```bash
npm install hexo-renderer-pug hexo-renderer-stylus --save
```

### 1.4 推薦操作，複製一份butterfly主題專用的配置檔案

在 hexo 的根目錄建立一個檔案 `_config.butterfly.yml`，後續對butterfly主題的美化配置就在該配置檔案下進行修改即可。

**層級關係如下圖所示：**

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-1799bd03088fb81ea0888bb1d2281fe7.png)

### 1.5 設定一個圖片存儲目錄

在 `source` 目錄下新建一個 `image` 資料夾，方便後續存儲展示用的相關圖片（~~名字你可以隨便取~~）

**層級關係如下：**

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-6605915ba7f40cc826797d68d5ec67c2.png)

## 2. 網站資料配置

在 **_config.yml** 檔案裡配置！

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-73d3ec6379f5c43af4daf6ebb114735e.png)

對應效果如圖：

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-7a052ba48e20ceaf23d3c07bdf08a8cb.png)

## 3. 導覽列配置

這裡我直接copy展示用的程式碼了（~~畢竟完全不會~~）

```yaml
nav:
  logo: /image/test.gif
  display_title: true
  fixed: false # fixed navigation bar
post_asset_folder: true
menu:
  首頁: / || fas fa-home
  時間軸: /archives/ || fas fa-archive
  標籤: /tags/ || fas fa-tags
  分類: /categories/ || fas fa-folder-open
  清單||fa fa-heartbeat:
    音樂: /music/ || fas fa-music
    照片: /Gallery/ || fas fa-images
    電影: /movies/ || fas fa-video
```

效果（**搜尋是額外配的，後面會說**）：

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-8df3966496d14fe526ad2041b0292d71.png)

## 4. 修改頭像

將你喜歡的頭像複製到之前配置的image資料夾裡，路徑如圖所示：

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-bf8ed33c0aba5f9127240e0dca667294.png)

然後在你複製出來的主題配置檔案，也就是 `_config.butterfly.yml` 中添加如下配置：

```yaml
#頭像
avatar:
  img: /image/miku.jpg
  # effect: true # 頭像會一直轉，轉的賊快，太鬼畜了
```

## 5. 頂部圖設定

程式碼如下：

```yaml
#頂部圖
index_img: /image/miku.jpg
default_top_img: /image/miku.jpg
index_top_img_height: 400px #頂部圖高度
```

效果：

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-a8d37c483f102524a0544fb325c6e4a3.png)

**tips：**
1. 感覺400px差不多了，或者預設就是全螢幕，但是全螢幕得往下拉才能看見博客。~~對於新手不是很友好，我第一次進就是發現找半天找不到博客在哪~~
2. 圖片不要被寬螢幕誤導了，請選擇**直螢幕**展示的圖片，且清晰度越高越好（不然就是糊的）
3. 經過觀察，設定為400px時，展示的圖片位置大概就在中間，所以最好選擇你最想展示的部分為中間的圖片~

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-91f7084634b7b25deeef854ac1e509c6.png)

## 6. 統計功能

推薦使用百度的api，首先你需要到百度統計官網申請id：  
[百度統計——一站式智能數據分析與應用平台](https://tongji.baidu.com/web/welcome/login?castk=LTE=)

具體咋申請我忘了……自己多找找看吧 

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-876d0858b5e0ed68987f94a2687f181d.png)

問號後面的程式碼就是id，在 `_config.yml` 中添加如下配置：

```yaml
baidu_analytics: 你的id
```

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-3c3b203d3e5d6b9b7471f5d93c107ce8.png)

## 7. 運行時間

程式碼如下：

```yaml
runtimeshow:
  enable: true
  publish_date: 1/4/2024 00:00:00
```

> `publish_date` 就是你博客的建立時間，格式是 **日/月/年**

效果：

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-c9384bcd31aa16e260033db92cd67a53.png)

## 8. 本地搜尋

在主題配置檔案下 `_config.butterfly.yml` 加入如下程式碼：

```yaml
local_search:
  enable: true
  # Preload the search data when the page loads.
  preload: false
  # Show top n results per article, show all results by setting to -1
  top_n_per_article: 1
  # Unescape html strings to the readable one.
  unescape: true
  CDN:
```

效果：

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-a000ed1fafef91f52335e97a62526f75.png)

## 9. 背景特效

詳見官方文檔：[Butterfly 安裝文檔(四) 主題配置-2 | Butterfly](https://butterfly.js.org/posts/ceeb73f/#%E8%83%8C%E6%99%AF%E7%89%B9%E6%95%88)

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-03fc5e060d723a7f7330230a141d29b9.png)

我的博客選的是動態彩帶，程式碼如下：

```yaml
canvas_fluttering_ribbon:
  enable: true
  mobile: false # false 手機端不顯示 true 手機端顯示
```

## 10. 滑鼠點擊特效

目前官方文檔中**滑鼠點擊特效的文字特效已無法使用（截至2024/1/18）**，目前我的博客採用的是愛心效果，程式碼如下：

```yaml
# 點擊出現愛心
click_heart:
  enable: true
  mobile: false
```

## 11. 網站副標題（循環打字特效）

添加如下程式碼即可（速度我已經進行了相應調整，你可以根據自己的喜好進行修改）：

```yaml
# 主頁subtitle
subtitle:
  enable: true
  # Typewriter Effect (打字效果)
  effect: true
  startDelay: 300 # time before typing starts in milliseconds
  typeSpeed: 200 # type speed in milliseconds
  backSpeed: 800 # backspacing speed in milliseconds
  # loop (循環打字)
  loop: true
  # source 調用三方服務
  # source: false 開關調用
  # subtitle 會先顯示 source , 再顯示 sub 的內容
  source: true
  # 如果關閉打字效果，subtitle 只會顯示 sub 的第一行文字
  sub:
    - 自小刺頭深草裡 &#44; 而今漸覺出蓬蒿
    - 時人不識凌雲木 &#44; 直待凌雲始道高
```

效果：

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-65eefc231690ca91c91853ddd6869514.png)

## 12. 頁面載入動畫

在主題配置檔案 `_config.butterfly.yml` 加入以下程式碼即可：

```yaml
#載入動畫
preloader:
  enable: true
  source: 1 #可選項1=fullpage或2=progress bar，可查看https://codebyzach.github.io/pace/
  pace_css_url:
```

效果：

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-a2b85380e130b323fdae2e6c5f2ead27.png)

> 這個載入動畫是butterfly預設的，目前在百度上沒有找到可以直接使用的載入動畫程式碼或url，只能湊合著用了，呃呃。

## 13. 池塘養魚

在主題配置檔案 `_config.butterfly.yml` 加入以下程式碼即可：

```yaml
inject:
  head:

  bottom:
       - <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.min.js"></script>
       - <script src="https://cdn.jsdelivr.net/gh/xiabo2/CDN@latest/fishes.js"></script>
```

**有時候會遇到cdn解析失敗，導致魚塘載入不出來，建議還是以js檔案格式本地引入，操作方法見下👇👇👇**

### 13.1 在 source 目錄下新建一個 styles 資料夾，用於存放相關檔案

層級如下：

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-7c2572b09870a5a68e0bdddf11c80d99.png)

### 13.2 添加如下兩個檔案

**注意：這兩個檔案的目錄是基於我設定的styles目錄下，如果你的資料夾名稱是你自己設定的，請同步修改檔案中涉及到的檔案引用地址路徑！！！**

### 13.3 在主題配置檔案下引入這兩個檔案

程式碼如下：

```html
- <script src="/styles/fish.js"></script>
```

一樣也得引入 jquery：

```html
- <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.min.js"></script>
```

層級關係如圖所示：

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-31312e6864b3c409009395c283fe049d.png)

## 14. 漸變色設定

在styles目錄下新建一個 **main.css** 檔案，鍵入程式碼。

**同樣，也需要在主題配置檔案中引入這個css檔案：**

```html
- <link rel="stylesheet" href="/styles/main.css">
```

層級關係如下圖所示：

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-bdb856e8341b07ec8de0c064c5dc4b3a.png)

## 15. 瀏覽器圖示修改

先找一個你喜歡的圖示，注意格式需為32*32。可以從阿里的向量圖庫中下載自己喜歡的：  
[iconfont-阿里巴巴矢量图标库](https://www.iconfont.cn/)

保存後放在image資料夾內（或者你自己自訂存圖片的資料夾）：

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-bca7c5ac07ec6206bbc7f616b20dfb66.png)

在你的主題配置檔案內添加如下程式碼即可：

```yaml
favicon: /image/动物.png
```

效果如圖所示：

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-036dc8e31a6c90ace72e655c6b7f99fd.png)

## 16. 添加功能點備案資訊（butterfly主題）

在你的主題配置檔案下加入以下程式碼：

```yaml
footer:
  owner:
    enable: true
    since: 2024
  custom_text: <img src="https://haiyong.site/img/icp.png"><a href="https://beian.miit.gov.cn/#/Integrated/index" style="color:black" target="_blank">xICP备xxx号-1(你的icp备案号)</a>
  copyright: true
```

## 17. nginx配置監聽轉發

安裝好後加入如下配置，有的話直接替換就行了：

```nginx
server{
  listen 80; # 監聽的埠號
  server_name  xxxx; # 監聽的地址，相當於就是你的功能點地址
  index  index.php index.html index.htm;

  location / {
    proxy_pass xxxx; # 轉發地址，帶上埠號
    proxy_set_header Host $proxy_host; # 修改轉發請求頭，讓8080埠號的應用可以受到真實的請求
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  }
}
```

## 18. 搬運自己的csdn文章到hexo

百度一搜尋一大堆，這裡自己簡單總結下：

### 18.1 獲取文章資訊

打開自己寫的文章，打開開發者模式（F12），搜尋 **article_content**：

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-07a8150976be516c41ce40a67270d779.png)

### 18.2 將複製的文章資訊轉換為md格式

進入下方網站，按照序號操作，最後轉換的檔案不用下載，可以直接全選複製到typora裡操作。  
[markdown编辑器 - 在线工具](https://tool.lu/markdown/)

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-fd14b2e6cf8f2b449c9dbb95294c074e.png)

### 18.3 對於圖片的處理

csdn是有防盜鏈的，所以你直接複製貼上放到hexo上圖片是載入不出來的。

方法一：另存為後複製貼上（超級無腦）

方法二：結合之前我寫的文章  
[腾讯云图床（对象存储）+typora+picgo实现图片一键上传-CSDN博客](https://blog.csdn.net/JesseXW/article/details/135740635?spm=1001.2014.3001.5501)

全自動上傳，記得開一下這個設定，會自動進行url替換

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-266310ebad104d5bb1209b8347956ad7.png)

### 18.4 圖片壓縮

可以使用tx雲對象存儲自帶的壓縮，也可以自己手動壓縮成webp格式。步驟如下：  
[Online PNG to WebP image converter](https://ezgif.com/png-to-webp?err=expired)

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-86fd084319c35d88934998c8ebfc6805.png)

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-f970b1bc2e2a236cd003f6647a7aba72.png)

webp的展示效果還是不錯的，體積壓縮了不少但清晰度還是挺能打的。

後面對於該圖片替換就可以了