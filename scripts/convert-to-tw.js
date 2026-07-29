const fs = require('fs');
const path = require('path');

const postsDir = path.join(__dirname, '../source/_posts');

const zhMap = {
  '系统': '系統', '软件': '軟體', '服务器': '伺服器', '默认': '預設', '项目': '項目',
  '配置': '配置', '更新': '更新', '发布': '發布', '标签': '標籤', '分类': '分類',
  '网络': '網路', '客户端': '客戶端', '服务端': '伺服器端', '协议': '協定', '脚本': '腳本',
  '端口': '埠號', '域名': '功能點', '缓存': '快取', '下载': '下載', '设置': '設定',
  '文件': '檔案', '文件夹': '資料夾', '代码': '程式碼', '插件': '外掛', '浏览器': '瀏覽器',
  '图标': '圖示', '动画': '動畫', '搜索': '搜尋', '简单': '簡單', '方便': '方便',
  '个人': '個人', '首页': '首頁', '关于': '關於', '内容': '內容', '欢迎': '歡迎',
  '准备': '準備', '推荐': '推薦', '显示': '顯示', '进行': '進行', '升级': '升級',
  '通过': '透過', '运行': '運行', '修改': '修改', '点击': '點擊', '爱心': '愛心'
};

const charMap = {
  '国': '國', '学': '學', '网': '網', '关': '關', '门': '門', '书': '書', '东': '東', '车': '車',
  '长': '長', '开': '開', '发': '發', '见': '見', '问': '問', '观': '觀', '语': '語', '简': '簡',
  '繁': '繁', '体': '體', '乐': '樂', '头': '頭', '飞': '飛', '电': '電', '机': '機', '场': '場',
  '边': '邊', '换': '換', '转': '轉', '页': '頁', '选': '選', '择': '擇', '数': '數', '据': '據'
};

function convertText(text) {
  let codeBlocks = [];
  text = text.replace(/(`[\s\S]*?`|[^]+)/g, function(match) {
    codeBlocks.push(match);
    return '__CODE_BLOCK_' + (codeBlocks.length - 1) + '__';
  });

  for (let key in zhMap) {
    text = text.replaceAll(key, zhMap[key]);
  }
  for (let key in charMap) {
    text = text.replaceAll(key, charMap[key]);
  }

  text = text.replace(/__CODE_BLOCK_(\d+)__/g, function(_, index) {
    return codeBlocks[index];
  });
  return text;
}

function processPosts() {
  if (!fs.existsSync(postsDir)) return;
  const files = fs.readdirSync(postsDir);
  files.forEach(function(file) {
    if (path.extname(file) === '.md') {
      const filePath = path.join(postsDir, file);
      const content = fs.readFileSync(filePath, 'utf8');
      const converted = convertText(content);
      if (content !== converted) {
        fs.writeFileSync(filePath, converted, 'utf8');
        console.log('[Auto Convert] Converted: ' + file);
      }
    }
  });
}

processPosts();