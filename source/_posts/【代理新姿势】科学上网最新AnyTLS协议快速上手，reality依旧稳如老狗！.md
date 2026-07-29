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

> 📖 [文章图文原址](https://bulianglin.com/archives/anytls.html)

---

## 🎥 视频教程

* YouTube 视频地址：[立即观看](https://youtu.be/yUJ--0eUs_o)

---

## 🛡️ AnyTLS 协议

* 官方项目仓库：[anytls/anytls-go](https://github.com/anytls/anytls-go)

AnyTLS 是一个旨在解决 **嵌套的 TLS 指纹 (TLS in TLS)** 的传输协议。`anytls-go` 是该协议的 Go 语言参考实现。

<!-- more -->

### 主要特点
* 灵活的分包
* 支持多路复用，降低延迟
* 极简配置

---

## 📱 支持 AnyTLS 协议的客户端

### 1. sing-box
* 项目地址：[SagerNet/sing-box](https://github.com/SagerNet/sing-box)
* *注：同时支持 anytls 协议的服务端和客户端实现。*

### 2. mihomo (原 Clash Meta)
* 项目地址：[MetaCubeX/mihomo](https://github.com/MetaCubeX/mihomo)
* *注：同时支持 anytls 协议的服务端和客户端实现。*

### 3. Shadowrocket (小火箭)
* 客户端版本：Shadowrocket 2.2.65+
* *注：实现 anytls 协议的 iOS 客户端。*

### 4. NekoBox For Android
* 下载地址：[NekoBoxForAndroid Releases](https://github.com/MatsuriDayo/NekoBoxForAndroid/releases)
* *注：NekoBox For Android 1.3.8+ 实现 anytls 协议的客户端。*

---

## 🚀 搭建方式

### 方式一：通过 `anytls-go` 官方

#### 1. 服务端
```bash
# 监听 8443 端口：
./anytls-server -l 0.0.0.0:8443 -p 你的密码

# 后台默认
nohup ./anytls-server -l 0.0.0.0:8443 -p 你的密码 > /dev/null 2>&1 &

# 结束后台
pkill -f anytls-server
```

#### 2. 客户端
```bash
./anytls-client -l 127.0.0.1:1080 -s 服务器IP:8443 -p 你的密码
```

---

### 方式二：通过 `mihomo` 搭建

#### 1. 自签名证书
```bash
openssl req -x509 -newkey ec:<(openssl ecparam -name prime256v1) -keyout "./server.key" -out "./server.crt" -days 36500 -nodes -subj "/CN=bing.com"
```

#### 2. 编写 `config.yaml` 文件
```yaml
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
```

#### 3. 运行指令
```bash
# 启动 mihomo
./mihomo -d ./

# 后台运行
nohup ./mihomo -d ./ > /dev/null 2>&1 &

# 结束
pkill -f mihomo
```

---

## 💡 协议背景与反馈

稳定的需要比较高的成本建立和维护。

目前常见协议的表现（根据过去一段时间统计）：
* **SS (Shadowsocks) 节点**：普通 VPS 上搭建使用，初始很短（第二天）就会被封锁 IP。
* **VMess + WS (Websocket) 节点**：容易被精确识别并封端口，需要频繁换端口，目前已不推荐使用。
* **VLESS + Vision 节点**：表现还可以。部分封锁是因为免费域名 `nip.io` 被直接污染，而非协议本身。
* **VLESS + Vision + Reality 节点**：稳定没有被封的迹象，建议将目标伪装修改为大厂域名。

### TLS in TLS 的问题
“TLS in TLS” 指在加密隧道传输另一个加密协议，目前容易被墙识别。AnyTLS 通过自定义填充数据打破该指纹。

对比传统 Vision（采用固定数据包头字节填充）等，AnyTLS 支持 **自定义 padding 填充方案**，用户可设定数据包每字节范围，提升防墙难度。