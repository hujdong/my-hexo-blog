---
title: 【代理新姿勢】科學上網最新AnyTLS協定快速上手，reality依舊穩如老狗！
date: 2025-05-17 11:18:00
tags:
  - 科學上網
  - AnyTLS
  - 代理協定
categories:
  - 科學上網
---

> 📖 [文章圖文原址](https://bulianglin.com/archives/anytls.html)

---

## 🎥 影片教學

* YouTube 影片地址：[立即觀看](https://youtu.be/yUJ--0eUs_o)

---

## 🛡️ AnyTLS 協定

* 官方項目倉庫：[anytls/anytls-go](https://github.com/anytls/anytls-go)

AnyTLS 是旨在解決 **嵌套 TLS 指紋 (TLS in TLS)** 的傳輸協定。`anytls-go` 是該協定的 Go 語言參考實現。

<!-- more -->

### 主要特點
* 靈活的分包
* 支援多路復用，降低延遲
* 極簡配置

---

## 📱 支援 AnyTLS 協定的客戶端

### 1. sing-box
* 項目地址：[SagerNet/sing-box](https://github.com/SagerNet/sing-box)
* *註：同時支援 anytls 協定的伺服器端和客戶端實現。*

### 2. mihomo (原 Clash Meta)
* 項目地址：[MetaCubeX/mihomo](https://github.com/MetaCubeX/mihomo)
* *註：同時支援 anytls 協定的伺服器端和客戶端實現。*

### 3. Shadowrocket (小火箭)
* 客戶端版本：Shadowrocket 2.2.65+
* *註：實現 anytls 協定的 iOS 客戶端。*

### 4. NekoBox For Android
* 下載地址：[NekoBoxForAndroid Releases](https://github.com/MatsuriDayo/NekoBoxForAndroid/releases)
* *註：NekoBox For Android 1.3.8+ 實現 anytls 協定的客戶端。*

---

## 🚀 架設方式

### 方式一：透過 `anytls-go` 官方

#### 1. 伺服器端
```bash
# 監聽 8443 埠號：
./anytls-server -l 0.0.0.0:8443 -p 你的密碼

# 後台預設
nohup ./anytls-server -l 0.0.0.0:8443 -p 你的密碼 > /dev/null 2>&1 &

# 結束後台
pkill -f anytls-server
```

#### 2. 客戶端
```bash
./anytls-client -l 127.0.0.1:1080 -s 伺服器IP:8443 -p 你的密碼
```

---

### 方式二：透過 `mihomo` 架設

#### 1. 自簽名證書
```bash
openssl req -x509 -newkey ec:<(openssl ecparam -name prime256v1) -keyout "./server.key" -out "./server.crt" -days 36500 -nodes -subj "/CN=bing.com"
```

#### 2. 編寫 `config.yaml` 檔案
```yaml
listeners:
- name: anytls-in-1
  type: anytls
  port: 8443
  listen: 0.0.0.0
  users:
    username1: 密碼1
    username2: 密碼2
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

#### 3. 執行指令
```bash
# 啟動 mihomo
./mihomo -d ./

# 後台運行
nohup ./mihomo -d ./ > /dev/null 2>&1 &

# 結束
pkill -f mihomo
```

---

## 💡 協定背景與反饋

穩定的需要比較高的成本建立與維護。

目前常見協定的表現（根據過去一段時間統計）：
* **SS (Shadowsocks) 節點**：普通 VPS 上架設使用，初始很短（第二天）就會被封鎖 IP。
* **VMess + WS (Websocket) 節點**：容易被精確識別並封埠號，需要頻繁換埠號，目前已不推薦使用。
* **VLESS + Vision 節點**：表現還可以。部分封鎖是因為免費功能點 `nip.io` 被直接污染，而非協定本身。
* **VLESS + Vision + Reality 節點**：穩定沒有被封的跡象，建議將目標偽裝修改為大廠功能點。

### TLS in TLS 的問題
「TLS in TLS」 指在加密隧道傳輸另一個加密協定，目前容易被牆識別。AnyTLS 透過自訂填充資料打破該指紋。

對比傳統 Vision（採用固定資料包頭位元組填充）等，AnyTLS 支援 **自訂 padding 填充方案**，使用者可設定資料包每位元組範圍，提升防牆難度。