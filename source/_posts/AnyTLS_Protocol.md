---
title: 【代理新姿勢】科學上網最新 AnyTLS 協定快速上手，收集了兩年的各代理協定反饋分享，reality 依舊穩如老狗！
date: 2026-08-01 15:50:00
tags:
  - 網絡技術
  - AnyTLS
  - 代理協定
categories:
  - 網絡技術
---

AnyTLS 是一個旨在緩解嵌套 TLS 握手指紋 (TLS in TLS) 特徵的全新代理協定，支援靈活的分包與填充策略及連接復用。本文包含 AnyTLS 原理、主流客戶端支援、anytls-go / mihomo 兩種搭建方式以及作者收集了兩年的各代理協定防封經驗反饋。

<!-- more -->

> **作者**：不良林 | **發布時間**：2025 年 05 月 17 日 | **來源**：[不良林博客](https://bulianglin.com/archives/anytls.html)

---

## 🎥 視頻教程与相关推荐

* YouTube 播放地址：[https://youtu.be/yUJ--0eUs_o](https://youtu.be/yUJ--0eUs_o)
* **GIA 高速 VPS 推薦**：[https://d.m123.org](https://d.m123.org)
* **家寬住宅 VPS 推薦**：[https://v.m123.org](https://v.m123.org)
* **自用專線機場推薦**：[https://b.m123.org](https://b.m123.org)

---

# AnyTLS 協議簡介

* 项目地址：[https://github.com/anytls/anytls-go](https://github.com/anytls/anytls-go)

`anytls` 是一个试图缓解**嵌套 TLS 握手指纹 (TLS in TLS)** 问题的代理协议。`anytls-go` 是该协议的参考实现。

* **灵活的分包和填充策略**
* **连接复用，降低代理延迟**
* **简洁的配置**

---

## 支持 AnyTLS 协议的代理工具

### 1. sing-box
* [https://github.com/SagerNet/sing-box](https://github.com/SagerNet/sing-box)
> 包含 anytls 协议的服务器端和客户端。

### 2. mihomo (Clash Meta)
* [https://github.com/MetaCubeX/mihomo](https://github.com/MetaCubeX/mihomo)
> 包含 anytls 协议的服务器端和客户端。

### 3. Shadowrocket (小火箭)
* [iOS App Store 链接](https://apps.apple.com/app/shadowrocket/id932747118)
> Shadowrocket 2.2.65+ 实现了 anytls 协议的客户端支持。

### 4. NekoBox For Android
* [https://github.com/MatsuriDayo/NekoBoxForAndroid/releases](https://github.com/MatsuriDayo/NekoBoxForAndroid/releases)
> NekoBox For Android 1.3.8+ 实现了 anytls 协议的客户端支持。

---

## 搭建方式

### 方式一：通过 anytls-go 官方程序搭建

#### 服务端配置
```shell
./anytls-server -l 0.0.0.0:8443 -p 你的密码

# 后台运行
nohup ./anytls-server -l 0.0.0.0:8443 -p 你的密码 > /dev/null 2>&1 &

# 结束进程
pkill -f anytls-server
```

#### 客户端配置
```shell
./anytls-client -l 127.0.0.1:1080 -s 服务器ip:8443 -p 你的密码
```

---

### 方式二：通过 mihomo (Clash Meta) 搭建

#### 1. 生成自签证书
```shell
openssl req -x509 -newkey ec:<(openssl ecparam -name prime256v1) -keyout "./server.key" -out "./server.crt" -days 36500 -nodes -subj "/CN=bing.com"
```

#### 2. 生成配置文件 (config.yaml)
```yaml
cat > config.yaml << 'EOF'
listeners:
- name: anytls-in-1
  type: anytls
  port: 8443
  listen: 0.0.0.0
  users:
    username1: 密码1
    username2: 密码2
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
EOF
```

#### 3. 启动指令
```shell
./mihomo -d ./

# 后台运行
nohup ./mihomo -d ./ > /dev/null 2>&1 &

# 结束进程
pkill -f mihomo
```

---

## 视频文稿与两年代理防封心得总结

对稳定要求比较高的用户建议自己搭建。根据我多年被墙经验，以及这两年收到的反馈，总结如下：

1. **SS 节点（Shadowsocks）**：
   在使用同款 VPS 的情况下，搭建使用 SS 节点，第二天大概率会被封 IP。反馈 IP 被封的用户无一例外都是搭建并使用了 SS 节点。
2. **VMess + WS 节点**：
   第二天大概率被封端口（但不会直接封 IP），换个端口能继续使用，但第二天又会被封端口。因此现在**不推荐**使用 VMess + WS。
3. **VLESS + Vision 节点**：
   部分用户反馈节点用不了（端口未被封），经排查是因为教程中用到的证书域名 `nip.io` 被防火墙阻断导致，和协议本身无关，更换域名即可。
4. **VLESS + Vision + Reality 节点**：
   这两年一例被封的反馈都没有，真的**一例都没有**！极少数白名单地区用户改成大厂域名后也能正常使用。目前 **REALITY 依然是稳如老狗**！
5. **AnyTLS 原理**：
   针对 TLS in TLS 特征，Vision 流控是通过固定随机数据填充；而 AnyTLS 则可以通过参数灵活指定要填充的数据包数量及填充长度范围，支持更加灵活个性化的设定，以此增加防火墙识别的难度。
