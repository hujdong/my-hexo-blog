---
title: 在Linux中，如何進行系統更新和升級？
date: 2025-08-09 13:16:52
tags:
  - Linux
  - 系統更新
---

在 Linux 中，系統更新和維護是保證系統安全性與穩定性的重要環節。通常涉及核心與系統軟體包。不同 Linux 發行版有不同的包管理系統，以下是一些常見發行版中進行系統更新和升級的方法：

<!-- more -->

### 1. Debian / Ubuntu 系統

使用 `apt` 進行更新：

1. **更新軟體列表**：
   ```bash
   sudo apt update
   ```
   從軟體庫中獲取最新的軟體包列表資訊。

2. **升級已安裝軟體包**：
   ```bash
   sudo apt upgrade
   ```
   這會安裝所有可用的更新，但不會刪除任何軟體包。

3. **安裝最新版本核心**：
   如果系統提供最新版本核心，使用 `apt` 進行安裝：
   ```bash
   sudo apt install linux-image-generic
   ```
   （替換 `linux-image-generic` 為特定核心版本，有的話）

4. **清理不需要的依賴包**：
   ```bash
   sudo apt autoremove
   ```
   刪除那些作為依賴安裝但現在不再需要的軟體包。

---

### 2. Red Hat / CentOS 系統

使用 `yum` 或 `dnf` 進行更新：

1. **檢查可用更新列表**：
   ```bash
   sudo yum check-update
   ```
   或者系統使用 `dnf`：
   ```bash
   sudo dnf check-update
   ```

2. **升級所有已安裝軟體包**：
   ```bash
   sudo yum update
   ```
   使用 `dnf`：
   ```bash
   sudo dnf update
   ```

3. **安裝最新版本核心**：
   通常 Red Hat / CentOS 系統會自動提供最新核心。如需手動安裝特定核心：
   ```bash
   sudo yum install kernel
   ```
   使用 `dnf`：
   ```bash
   sudo dnf install kernel
   ```

4. **清理快取**：
   ```bash
   sudo yum clean all
   ```
   使用 `dnf`：
   ```bash
   sudo dnf clean all
   ```
   清除所有快取資料，釋放磁碟空間。