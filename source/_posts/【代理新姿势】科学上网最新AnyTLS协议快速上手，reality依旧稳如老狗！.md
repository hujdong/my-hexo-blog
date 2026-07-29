---
title: 【代理新姿势】科学上网最新 AnyTLS 协议快速上手，Reality 依旧稳如老狗！
date: 2025-05-17 11:18:00
tags:
  - 科学上网
  - AnyTLS
  - 代理协议
categories:
  - 网络技术
---

随着防火墙对 TLS in TLS（嵌套加密隧道）指纹识别能力的提升，全新的 AnyTLS 协议应运而生。本文将为您盘点目前主流代理协议的现状，并介绍 AnyTLS 的核心机制与部署方法。

<!-- more -->

> 📖 **声明**：本文内容引自技术博主 *不良林* 的分享与测试实录。

---

## 📊 主流代理协议稳定度近况盘点

根据近两年的部署反馈与实测表现总结如下：

| 协议组合 | 稳定度表现 | 现状与建议 |
| :--- | :--- | :--- |
| **SS (Shadowsocks)** | 🔴 极易被封 | 普通 VPS 搭建后大概率极短时间内被直接封禁 IP，不推荐 |
| **VMess + WS** | 🟡 频繁封端口 | 特征明显，容易被精准封锁端口，需要频繁更换端口，不推荐 |
| **VLESS + Vision** | 🟢 较为稳定 | 表现尚可。若遇到阻断多是因为免费节点域名（如 `nip.io`）被污染，换用正常域名即可 |
| **VLESS + Reality** | 🟢🟢 **稳如老狗** | **最推荐**。几乎零被封记录，抗封锁能力极强 |

---

## 🛡️ 什么是 AnyTLS？

* 官方 GitHub 仓库：[anytls/anytls-go](https://github.com/anytls/anytls-go)

**AnyTLS** 是一个旨在缓解 **TLS in TLS 握手指纹识别** 问题的全新代理协议。

### 核心优势
1. **灵活的分包与填充策略**：支持自定义数据包填充字节长度与包数量，大幅增加防火墙特征分析难度。
2. **连接复用**：降低代理握手延迟，提升访问流畅度。
3. **简洁配置**：支持自签证书与极简指令运行。

---

## 📱 支持 AnyTLS 的客户端与工具

* **sing-box**：内置服务端与客户端支持（[GitHub 仓库](https://github.com/SagerNet/sing-box)）
* **mihomo (Clash Meta)**：内置服务端与客户端支持（[GitHub 仓库](https://github.com/MetaCubeX/mihomo)）
* **Shadowrocket (小火箭)**：iOS 客户端 2.2.65+ 版本已完美支持
* **NekoBox For Android**：安卓客户端 1.3.8+ 版本已支持

---

## 🚀 极速部署教程

### 方法一：使用 `anytls-go` 官方程序

#### 1. 服务端部署
```bash
# 启动服务端监听 8443 端口
./anytls-server -l 0.0.0.0:8443 -p 你的自定义密码

# 后台静默运行
nohup ./anytls-server -l 0.0.0.0:8443 -p 你的自定义密码 > /dev/null 2>&1 &

# 结束后台进程
pkill -f anytls-server
```

#### 2. 客户端运行
```bash
./anytls-client -l 127.0.0.1:1080 -s 服务器IP:8443 -p 你的自定义密码
```

---

### 方法二：通过 `mihomo` 自定义 Padding 填充部署

#### 1. 生成自签证书
```bash
openssl req -x509 -newkey ec:<(openssl ecparam -name prime256v1) -keyout "./server.key" -out "./server.crt" -days 36500 -nodes -subj "/CN=bing.com"
```

#### 2. 配置文件 `config.yaml`
```yaml
listeners:
- name: anytls-in-1
  type: anytls
  port: 8443
  listen: 0.0.0.0
  users:
    user1: 你的自定义密码
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
./mihomo -d ./
```