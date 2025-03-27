export default function handler(req, res) {
    // 這裡返回 JSON 資料
    res.status(200).json({
        name: 'John Doe',
        job: 'Developer'
    });
}
