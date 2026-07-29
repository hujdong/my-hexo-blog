---
title: 【代理新姿势】科学上网最新AnyTLS协议快速上手，reality依旧稳如老狗！
date: 2025-05-17 11:18:00
tags:
  - 科学上网
  - AnyTLS
  - 代理协议
categories:
  - 科学上网
---


> 引用[不良林博客](https://bulianglin.com/archives/anytls.html)。在推送到您的博客之前，请务必编辑以下内容：

---

## 视频教程

* YouTube 播放地址：[点击观看](https://youtu.be/yUJ--0eUs_o)
---

## AnyTLS 协议介绍

* 官方项目仓库：[anytls/anytls-go](https://github.com/anytls/anytls-go)

AnyTLS 是一个试图缓解 **嵌套的 TLS 握手指纹 (TLS in TLS)** 阻断问题的代理协议。`anytls-go` 是该协议的 Go 语言参考实现。

### 主要特点
* 灵活的分包和填充策略
* 支持连接复用，降低代理延迟
* 配置简洁易懂

---

## 支持 AnyTLS 协议的代理工具

### 1. sing-box
* 项目地址：[SagerNet/sing-box](https://github.com/SagerNet/sing-box)
* *注：同时包含 anytls 协议的服务端和客户端实现。*

### 2. mihomo (原 Clash Meta)
* 项目地址：[MetaCubeX/mihomo](https://github.com/MetaCubeX/mihomo)
* *注：同时包含 anytls 协议的服务端和客户端实现。*

### 3. Shadowrocket (小火箭)
* 客户端版本：Shadowrocket 2.2.65+
* *注：实现了 anytls 协议的 iOS 客户端。*

### 4. NekoBox For Android
* 下载地址：[NekoBoxForAndroid Releases](https://github.com/MatsuriDayo/NekoBoxForAndroid/releases)
* *注：NekoBox For Android 1.3.8+ 实现了 anytls 协议的客户端。*

---

## 搭建方式

### 方法一：通过 `anytls-go` 官方程序

#### 1. 服务端部署
```bash
# 启动服务端监听 8443 端口，设置您的密码
./anytls-server -l 0.0.0.0:8443 -p 您的密码

# 后台静默运行
nohup ./anytls-server -l 0.0.0.0:8443 -p 您的密码 > /dev/null 2>&1 &

# 结束后台进程
pkill -f anytls-server
```

#### 2. 客户端运行
```bash
./anytls-client -l 127.0.0.1:1080 -s 服务器IP:8443 -p 您的密码
```

---

### 方法二：通过 `mihomo` 部署

#### 1. 生成自签证书
```bash
openssl req -x509 -newkey ec:<(openssl ecparam -name prime256v1) -keyout "./server.key" -out "./server.crt" -days 36500 -nodes -subj "/CN=bing.com"
```

#### 2. 编写 `config.yaml` 配置文件
```yaml
listeners:
- name: anytls-in-1
  type: anytls
  port: 8443
  listen: 0.0.0.0
  users:
    username1: 您的密码1
    username2: 您的密码2
  certificate: ./server.crt
  private-key: ./server.key
  padding-scheme: |
   stop=8
   0=30-30
   1=100-400
   2=400-500,c,500-1000,c,500-1000,c,500-1000,c,500-1000
   3=9-9,500-1000
   4=500-1000
   5=500-1000
   6=500-1000
   7=500-1000
```

#### 3. 启动指令
```bash
# 启动 mihomo
./mihomo -d ./

# 后台运行
nohup ./mihomo -d ./ > /dev/null 2>&1 &

# 结束进程
pkill -f mihomo
```

---

## 协议背景与反馈分享

对于稳定要求比较高的用户建议自己搭建。

目前网络上几种主流协议的被封锁反馈（基于过去两年的统计）：
* **SS (Shadowsocks) 节点**：在普通 VPS 上搭建使用，大概率极短时间内（第二天）就会被封锁 IP。
* **VMess + WS (Websocket) 节点**：容易被精确识别并封锁端口，需要频繁更换端口，目前已不推荐使用。
* **VLESS + Vision 节点**：近期有部分用户反馈被阻断。排查后发现多是因为免费证书域名（如 `nip.io`）被防火墙直接污染，与协议本身关联不大。
* **VLESS + Vision + Reality 节点**：表现最稳定，几乎没有被封锁的反馈。如果偶尔遇到白名单地区阻断，建议将目标域名修改为大厂域名。

### TLS in TLS 的特征缓解
“TLS in TLS” 指在加密隧道里传输另一个加密隧道，该流量指纹目前极易被防火墙识别。AnyTLS 通过自定义填充机制来消除该特征。

与传统的 Vision流控（采用固定的数据包开头字节填充）相比，AnyTLS 支持**自定义 padding 填充参数**。用户可以灵活设定填充的数据包数量、每个包的字节范围，极大增加了防火墙特征分析的难度。
