---
title: Hexo Butterfly 主题高颜值美化与部署指南
date: 2025-08-09 14:25:00
tags:
  - Hexo
  - Butterfly
  - 主题美化
categories:
  - 建站美化
---

Butterfly 是 Hexo 社区中非常受欢迎的高颜值美化主题之一。本文整理记录了 Butterfly 主题的安装、基础配置以及各种个性化特效（如背景彩带、爱心点击等）的设置方法。

<!-- more -->

> 💡 **小贴士**：修改主题配置后，若页面未生效，请先执行 `hexo clean` 清理缓存，再强制刷新浏览器页面。

---

## 🛠️ 1. 安装与初始化

在 Hexo 项目的根目录下执行安装命令：

```bash
# 1. 安装主题核心包
npm install hexo-theme-butterfly --save

# 2. 安装必需的 HTML 和 Stylus 渲染器
npm install hexo-renderer-pug hexo-renderer-stylus --save
```

推荐在 Hexo 根目录下复制一份专门的主题配置文件 `_config.butterfly.yml`，后续所有修改在此文件中独立进行。

---

## 🎨 2. 核心外观配置

### 2.1 导航栏与 Logo
在 `_config.butterfly.yml` 中配置：

```yaml
nav:
  logo: /image/logo.png
  display_title: true
  fixed: true
menu:
  首页: / || fas fa-home
  时间轴: /archives/ || fas fa-archive
  标签: /tags/ || fas fa-tags
  分类: /categories/ || fas fa-folder-open
```

### 2.2 站点头像与 Banner 顶部图
```yaml
# 博主头像设置
avatar:
  img: /image/avatar.png
  effect: false

# 顶部 Banner 图
index_img: /image/banner.jpg
default_top_img: /image/banner.jpg
index_top_img_height: 400px
```

---

## ✨ 3. 页面动效与特效

### 3.1 动态彩带背景
```yaml
canvas_fluttering_ribbon:
  enable: true
  mobile: false # 是否在移动端开启
```

### 3.2 鼠标点击爱心特效
```yaml
click_heart:
  enable: true
  mobile: false
```

### 3.3 打字机循环字幕
```yaml
subtitle:
  enable: true
  effect: true
  typeSpeed: 150
  backSpeed: 800
  loop: true
  sub:
    - 自小刺头深草里，而今渐觉出蓬蒿。
    - 时人不识凌云木，直待凌云始道高。
```