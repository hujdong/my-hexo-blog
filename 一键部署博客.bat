@echo off
echo ===================================================
echo    Hexo 静态博客一键构建与推送 (Cloudflare 自动发布)
echo ===================================================
echo.

echo [1/3] 正在进入新博客目录...
cd /d D:\hexo-new-blog

echo [2/3] 正在自动转换简体中文为繁体中文...
node scripts\convert-to-tw.js

echo [3/3] 正在提交并推送更新到 GitHub...
git add .
git commit -m "Site updated: %date% %time%"
git push origin main

echo.
echo ===================================================
echo        源码已推送！Cloudflare 正在云端进行自动部署，
echo             请在 1-2 分钟后刷新网站查看！
echo ===================================================
echo.
pause
