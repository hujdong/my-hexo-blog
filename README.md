# 📝 个人博客维护指南 (Hexo + Fluid + Cloudflare Pages)

这是一个基于 **Hexo** 框架、**Fluid** 主题，托管在 **GitHub** 源码仓库，并由 **Cloudflare Pages** 进行云端自动构建与分发的个人博客项目。

---

## 🚀 架构设计

* **源码托管**：GitHub 上的私有仓库 `hujdong/my-hexo-blog`（仅存放 Markdown 源文件与配置文件，安全防泄露）。
* **自动化构建**：Cloudflare Pages 自动检测 GitHub 推送，云端一键打包，全球 CDN 加速发布。

---

## 🛠️ 日常维护指令

在项目根目录 `D:\hexo-new-blog` 下打开终端（PowerShell 或 Git Bash）使用以下指令：

### 1. 本地预览调试
在发布前，您可以在本地启动临时服务器预览博客效果：
```powershell
# 清理缓存并生成本地静态文件，启动调试服务
npx hexo clean && npx hexo server
```
* 启动后，在浏览器中访问：`http://localhost:4000` 即可预览。
* 按 `Ctrl + C` 可停止本地预览服务。

### 2. 撰写并发布新文章
1. **创建新文章**：
   ```powershell
   npx hexo new "我的新文章标题"
   ```
   该命令会在 `source/_posts/` 目录下自动生成一个 `我的新文章标题.md` 的模板文件。

2. **编辑文章**：
   使用您常用的 Markdown 编辑器（如 Typora, VS Code）打开并编辑该 `.md` 文件。确保补充好文章顶部的 `Front Matter` 信息：
   ```yaml
   ---
   title: 我的新文章标题
   date: 2026-07-29 11:30:00  # 自动生成，可手动微调
   tags:                      # 文章标签
     - 标签一
     - 标签二
   categories:                # 文章分类
     - 技术分享
   ---
   ```

3. **一键推送上线**：
   保存文件后，在终端执行以下三条 Git 命令直接推送源码，Cloudflare Pages 会在云端自动编译并发布：
   ```powershell
   git add .
   git commit -m "feat: 新增文章 我的新文章标题"
   git push
   ```

---

## 📥 移植/导入外部文章流程

当您想把其他网站的文章（例如技术教程、个人笔记等）搬迁到自己的博客时，请遵循以下标准流程：

1. **内容转换**：
   将目标网页内容转换为干净的 **Markdown** 文本格式（剔除网页多余的广告、侧边栏和脚本）。

2. **添加 Front Matter（Hexo 头部标签）**：
   在 Markdown 文件最顶部加上 Hexo 的标志性头部信息，使博客能够正确检索：
   ```yaml
   ---
   title: 移植过来的文章标题
   date: 2026-07-29 12:00:00   # 原文发布时间或当前时间
   tags:
     - 标签
   categories:
     - 分类
   ---
   ```

3. **存放并调整链接**：
   * 将该 `.md` 文件放入项目的 `source/_posts/` 目录中。
   * **编辑内容**：手动检查并删除原文中可能携带的推广链接、失效的图片链接，并修改文章内可能涉及的敏感默认密码。

4. **推送发布**：
   在根目录下运行 Git 命令推送，等待云端编译上线即可：
   ```powershell
   git add .
   git commit -m "feat: 移植文章 移植过来的文章标题"
   git push
   ```

---

## 💻 换电脑/环境重建指南

如果您更换了电脑或重装了系统，只需要执行以下几步即可找回完整的开发环境：

1. 安装 **Git** 和 **Node.js**（推荐 Lts 版本）。
2. 在新电脑的终端克隆您的 GitHub 私有源码仓库：
   ```powershell
   git clone https://github.com/hujdong/my-hexo-blog.git
   ```
3. 进入克隆后的项目文件夹，重新安装依赖项：
   ```powershell
   cd my-hexo-blog
   npm install
   ```
4. 运行 `npx hexo server` 确认本地跑通，即可重新开始写博。
