---
title: butterfly主题部署指南V2
date: 2025-08-09 14:25:50
tags:
---


---
title: butterfly主题部署指南
date: 2025-08-09 13:22:39
tags:
---

# hexo的butterfly主题美化，2024年初版

转载自：[https://blog.csdn.net/JesseXW](https://blog.csdn.net/JesseXW)

**先贴上butterfly主题作者的官方美化文档地址，如果有大佬比较会的可以直接看他的（~不过部分功能可能用不了了~）：**  
[Butterfly 安裝文檔(一) 快速開始 | Butterfly](https://butterfly.js.org/posts/21cfbf15/#%E5%8D%87%E7%B4%9A%E5%BB%BA%E8%AD%B0 "Butterfly 安裝文檔(一) 快速開始 | Butterfly")
<!-- more -->

**注意！！！如果发现配置不生效，请先执行 `hexo clean`，然后清除浏览器缓存试试。如果还是不行，请检查配置文件的缩进是否有问题！！！**

## 1\. 准备工作

### 1.1 安装butterfly

**在hexo的根目录下**键入以下命令：

```bash
npm install hexo-theme-butterfly
```

### 1.2 修改配置文件，应用butterfly主题

修改 `_config.yml` 中的 `theme` 属性为 `butterfly`。

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-0cc53ca3fb892aa2d472d0ca54158de2.png)

### 1.3 安装插件

**如果你没有 pug 以及 stylus 的渲染器，请下载安装：**

在hexo根目录下键入以下命令：

```bash
npm install hexo-renderer-pug hexo-renderer-stylus --save
```

### 1.4 推荐操作，复制一份butterfly主题专用的配置文件

在 hexo 的根目录创建一个文件 `_config.butterfly.yml`，后续对butterfly主题的美化配置就在该配置文件下进行修改即可。

**层级关系如下图所示：**

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-1799bd03088fb81ea0888bb1d2281fe7.png)

### 1.5 设置一个图片存储目录

在 `source` 目录下新建一个 `image` 文件夹，方便后续存储展示用的相关图片（~名字你可以随便取~）

**层级关系如下：**

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-6605915ba7f40cc826797d68d5ec67c2.png)

<!-- 其余内容保持不变 -->

## 2\. 网站资料配置

在 **\_config.yml** 文件里配置！

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-73d3ec6379f5c43af4daf6ebb114735e.png)

对应效果如图：

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-7a052ba48e20ceaf23d3c07bdf08a8cb.png)

##  3. 导航栏配置

这里我直接copy展示用的代码了（~毕竟完全不会~）

```bash
nav:
  logo: /image/test.gif
  display_title: true
  fixed: false # fixed navigation bar
post_asset_folder: true
menu:
  首页: / || fas fa-home
  时间轴: /archives/ || fas fa-archive
  标签: /tags/ || fas fa-tags
  分类: /categories/ || fas fa-folder-open
  清单||fa fa-heartbeat:
    音乐: /music/ || fas fa-music
    照片: /Gallery/ || fas fa-images
    电影: /movies/ || fas fa-video
```

效果（**搜索是额外配的，后面会说**）：

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-8df3966496d14fe526ad2041b0292d71.png)

##  4. 修改头像

将你喜欢的头像复制到之前配置的image文件夹里，路径如图所示：

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-bf8ed33c0aba5f9127240e0dca667294.png)

然后在你复制出来的主题配置文件，也就是  \_config.butterfly.yml 中添加如下配置：

```bash
#头像
avatar:
  img: /image/miku.jpg
  # effect: true # 头像会一直转，转的贼快，太鬼畜了
```

## 5\. 顶部图设置

代码如下：

```bash
#顶部图
index_img: /image/miku.jpg
default_top_img: /image/miku.jpg
index_top_img_height: 400px #顶部图高度
```

效果：

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-a8d37c483f102524a0544fb325c6e4a3.png)

**tips：**

1.  感觉400px差不多了，或者默认就是全屏，但是全屏得往下拉才能看见博客。~对于萌新不是很友好，我第一次进就是发现找半天找不到博客在哪~
2.  图片不要被宽屏误导了，请选择**竖屏**展示的图片，且清晰度越高越好（不然就是糊的）
3.  经过观察，设置为400px时，展示的图片位置大概就在中间，所以最好选择你最想展示的部分为中间的图片~

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-91f7084634b7b25deeef854ac1e509c6.png)

## 6\. 统计功能

推荐使用百度的api，首先你需要到百度统计官网申请id：

[百度统计——一站式智能数据分析与应用平台](https://tongji.baidu.com/web/welcome/login?castk=LTE%3D "百度统计——一站式智能数据分析与应用平台")

具体咋申请我忘了......自己多找找看吧 

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-876d0858b5e0ed68987f94a2687f181d.png)

问号后面的代码就是id，在 \_config.yml 中添加如下配置

```bash
baidu_analytics: 你的id
```

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-3c3b203d3e5d6b9b7471f5d93c107ce8.png)

## 7. 运行时间

 代码如下：

```bash
runtimeshow:
  enable: true
  publish_date: 1/4/2024 00:00:00
```

> publish\_date 就是你博客的创建时间，格式是 **日/月/年** 

效果：

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-c9384bcd31aa16e260033db92cd67a53.png)

## 8\. 本地搜索

在主题配置文件下 \_config.butterfly.yml 加入如下代码：

```bash
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

## 9\. 背景特效

详见官方文档：[Butterfly 安裝文檔(四) 主題配置-2 | Butterfly](https://butterfly.js.org/posts/ceeb73f/#%E8%83%8C%E6%99%AF%E7%89%B9%E6%95%88 "Butterfly 安裝文檔(四) 主題配置-2 | Butterfly")

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-03fc5e060d723a7f7330230a141d29b9.png)

我的博客选的是动态彩带，代码如下：

```bash
canvas_fluttering_ribbon:
  enable: true
  mobile: false # false 手机端不显示 true 手机端显示
```

## 10\. 鼠标点击特效

目前官方文档中**鼠标点击特效的文字特效已无法使用（截至2024/1/18）**，目前我的博客采用的是爱心效果，代码如下：

```bash
# 点击出现爱心
click_heart:
  enable: true
  mobile: false
```

## 11\. 网站副标题（循环打字特效）

添加如下代码即可（速度我已经进行了相应调整，您可以根据自己的喜好进行修改）：

```bash
# 主页subtitle
subtitle:
  enable: true
  # Typewriter Effect (打字效果)
  effect: true
  startDelay: 300 # time before typing starts in milliseconds
  typeSpeed: 200 # type speed in milliseconds
  backSpeed: 800 # backspacing speed in milliseconds
  # loop (循环打字)
  loop: true
  # source 调用三方服务
  # source: false 开关调用
  # subtitle 会先显示 source , 再显示 sub 的內容
  source: true
  # 如果关闭打字效果，subtitle 只会显示 sub 的第一行文字
  sub:
    - 自小刺头深草里 &#44; 而今渐觉出蓬蒿
    - 时人不识凌云木 &#44; 直待凌云始道高
```

效果：

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-65eefc231690ca91c91853ddd6869514.png)

## 12\. 页面加载动画

在主题配置文件 \_config.butterfly.yml 加入以下代码即可：

```bash
#加载动画
preloader:
  enable: true
  source: 1 #可选值1=fullpage或2=progress bar，可查看https://codebyzach.github.io/pace/
  pace_css_url:
```

效果：

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-a2b85380e130b323fdae2e6c5f2ead27.png)

> 这个加载动画是butterfly默认的，目前在百度上没有找到可以直接使用的加载动画代码或url，只能凑合着用了，呃呃。

## 13\. 池塘养鱼

在主题配置文件 \_config.butterfly.yml 加入以下代码即可：

```bash
inject:
  head:

  bottom:
       - <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.min.js"></script>
       - <script src="https://cdn.jsdelivr.net/gh/xiabo2/CDN@latest/fishes.js"></script>
```

**有时候会遇到cdn解析失败，导致鱼塘加载不出来，建议还是以js文件格式本地引入，操作方法见下👇👇👇**

### 13.1 在 source 目录下新建一个 styles 文件夹，用于存放相关文件

层级如下：

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-7c2572b09870a5a68e0bdddf11c80d99.png)

### 13.2 添加如下两个文件

**注意：这两个文件的目录是基于我设置的styles目录下，如果你的文件夹名称是你自己设置的，请同步修改文件中涉及到的文件引用地址路径！！！**

**文件一：fish-base.js**

```bash
// 省略，内容同原文
```

**文件二：fish.js**

```bash
// 省略，内容同原文
```

### 13.3 在主题配置文件下引入这两个文件

代码如下：

```bash
- <script src="/styles/fish.js"></script>
```

一样也得引入 jquery：

```bash
- <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.min.js"></script>
```

层级关系如图所示：

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-31312e6864b3c409009395c283fe049d.png)

## 14\. 渐变色设置

在styles目录下新建一个 **main.css** 文件，键入以下代码：

```bash
/* 省略，内容同原文 */
```

**同样，也需要在主题配置文件中引入这个css文件：**

```bash
- <link rel="stylesheet" href="/styles/main.css">
```

层级关系如下图所示：

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-bdb856e8341b07ec8de0c064c5dc4b3a.png)

## 15\. 浏览器图标修改

先找一个你喜欢的图标，注意格式需为32\*32。可以从阿里的矢量图库中下载自己喜欢的：

[iconfont-阿里巴巴矢量图标库](https://www.iconfont.cn/ "iconfont-阿里巴巴矢量图标库")

保存后放在image文件夹内（或者你自己自定义存图片的文件夹）：

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-bca7c5ac07ec6206bbc7f616b20dfb66.png)

 在你的主题配置文件内添加如下代码即可：

```bash
favicon: /image/动物.png
```

 效果如图所示：

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-036dc8e31a6c90ace72e655c6b7f99fd.png)

## 16\. 添加域名备案信息（butterfly主题） 

在你的主题配置文件下加入以下代码：

```bash
footer:
  owner:
    enable: true
    since: 2024
  custom_text: <img src="https://haiyong.site/img/icp.png"><a href="https://beian.miit.gov.cn/#/Integrated/index" style="color:black" target="_blank">xICP备xxx号-1(你的icp备案号)</a>
  copyright: true
```

## 17\. nginx配置监听转发

安装好后加入如下配置，如果有的话直接替换就行了：

```bash
server{
  listen 80; # 监听的端口
  server_name  xxxx; # 监听的地址，相当于就是你的域名地址
  index  index.php index.html index.htm;

  location / {
    proxy_pass xxxx; # 转发地址，带上端口号
    proxy_set_header Host $proxy_host; # 修改转发请求头，让8080端口的应用可以受到真实的请求
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  }
}
```

## 18\. 搬运自己的csdn文章到hexo

百度一搜一大堆，这里自己简单总结下：

### 18.1 获取文章信息

打开自己写的文章，打开开发者模式（F12），搜索**article\_content**：

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-07a8150976be516c41ce40a67270d779.png)

### 18.2 将复制的文章信息转换为md格式

进入下方网站，按照序号操作，最后转换的文件不用下载，可以直接全选复制到typora里操作。

[markdown编辑器 - 在线工具](https://tool.lu/markdown/ "markdown编辑器 - 在线工具")

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-fd14b2e6cf8f2b449c9dbb95294c074e.png)

### 18.3 对于图片的处理

csdn是有防盗链的，所以你直接复制粘贴放到hexo上图片是加载不出来的。

方法一：另存为后复制粘贴（超级无脑）

方法二：结合之前我写的文章

[腾讯云图床（对象存储）+typora+picgo实现图片一键上传-CSDN博客](https://blog.csdn.net/JesseXW/article/details/135740635?spm=1001.2014.3001.5501 "腾讯云图床（对象存储）+typora+picgo实现图片一键上传-CSDN博客")

全自动上传，记得开一下这个设置，会自动进行url替换![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-266310ebad104d5bb1209b8347956ad7.png)

### 18.4 图片压缩

可以使用tx云对象存储自带的压缩，也可以自己手动压缩成webp格式。步骤如下：

[Online PNG to WebP image converter](https://ezgif.com/png-to-webp?err=expired "Online PNG to WebP image converter")

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-86fd084319c35d88934998c8ebfc6805.png)

![](https://raw.githubusercontent.com/hujdong/image_auto/main/obsidian/1754448416-f970b1bc2e2a236cd003f6647a7aba72.png)

webp的展示效果还是不错的，体积压缩了不少但清晰度还是挺能打的。

后面对该图片替换就可以了