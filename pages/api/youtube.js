export default async function handler(req, res) {
  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const response = await fetch(
      `https://www.googleapis.com/youtube/v3/search?part=snippet&q=${encodeURIComponent(req.query.q || '')}&key=${process.env.YOUTUBE_API_KEY}`
    );
    const data = await response.json();
    return res.status(response.ok ? 200 : 500).json(data);
  } catch (err) {
    return res.status(500).json({ error: 'Failed to reach YouTube API' });
  }
}
