var express = require('express');
var app = express();
var path = require('path');

app.use(express.static('public'));

// Route to homepage
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/views/index.html');
});

// Route to recommender page
app.get('/anime-recommendation', (req, res) => {
  res.sendFile(__dirname + '/views/anime-recommendation.html');
});

// Route to about
app.get('/about', (req, res) => {
  res.sendFile(__dirname + '/views/about.html');
});

// Route to 404
app.get('*', (req, res) => {
  res.sendFile(__dirname + '/views/404.html');
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`App listening on port ${PORT}`);
  console.log('Press Ctrl+C to quit.');
});