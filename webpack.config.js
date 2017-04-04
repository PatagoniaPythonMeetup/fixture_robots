var path = require('path');
var webpack = require('webpack');

var entries = ['./client/index'];

module.exports = {
  entry: entries,
  output: {
    path: path.join(__dirname, 'static'),
    filename: 'bundle.js',
    publicPath: '/static/'
  },
  module: {
    loaders: [
      {
        test: /\.js$/,
        loaders: ['babel-loader'],
        include: path.join(__dirname, 'client')
      },
      { test: /\.css$/, loader: "style-loader!css-loader" }
    ]
  },
  resolve: {
    alias: {
      "jquery-bracket": "jquery-bracket/dist/jquery.bracket.min.js",
    }
  }
};