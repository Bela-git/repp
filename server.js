const express = require('express');
const cors = require('cors');
const app = express();

// 使用 CORS 中介軟體，允許來自指定來源的請求
app.use(cors({
  origin: 'https://repp-weld.vercel.app', // 替換為你的前端網址
}));

// 設定一個 API 路由來回傳一些資料
app.get('/api/data', (req, res) => {
  res.json({ name: 'John', job: 'Developer' });
});

// 啟動伺服器，並監聽 3000 端口
app.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});
