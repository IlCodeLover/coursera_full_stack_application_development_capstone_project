const http = require('http');
const url = require('url');

// Create the server
const server = http.createServer((req, res) => {
  const method = req.method;
  const parsedUrl = url.parse(req.url, true);

  // CORS headers to allow communication from different origins
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  // Handle OPTIONS pre-flight request
  if (method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  if (parsedUrl.pathname === '/submit' && method === 'POST') {
    let body = '';

    // Collect request body data
    req.on('data', chunk => {
      body += chunk;
    });

    req.on('end', () => {
      try {
        // Parse the body data (JSON)
        const data = JSON.parse(body);
        const { name, message } = data;

        // Send a response back to the frontend
        const response = {
          status: 'success',
          receivedData: {
            name: name,
            message: message
          }
        };

        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify(response));
      } catch (error) {
        console.error('Error parsing the data:', error);
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ status: 'error', message: 'Invalid data' }));
      }
    });

  } else {
    // 404 for other routes
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not Found');
  }
});

// Start the server
const PORT = 3000;
server.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
