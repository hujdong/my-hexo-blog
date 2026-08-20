@echo off
echo ===================================================
echo    Hexo Blog Deploy Script (Cloudflare Auto Publish)
echo ===================================================
echo.

echo [1/4] Entering blog directory...
cd /d D:\hexo-new-blog

echo [2/4] Downloading and uploading external images to image bed...
python tools\auto_migrate_to_pic.py

echo [3/4] Auto converting Simplified Chinese to Traditional Chinese...
node scripts\convert-to-tw.js

echo [4/4] Committing and pushing updates to GitHub...
git add .
git commit -m "Site updated"
git push origin main

echo.
echo ===================================================
echo   Success! Cloudflare is building the site in cloud.
echo   Please refresh your website in 1-2 minutes!
echo ===================================================
echo.
pause
