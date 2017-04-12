const { resolve } = require('path');
var webpack = require('webpack');

var entries = [
    'react-hot-loader/patch',
    // activate HMR for React

    'webpack-dev-server/client?http://0.0.0.0:8080',
    // bundle the client for webpack-dev-server
    // and connect to the provided endpoint

    'webpack/hot/only-dev-server',
    // bundle the client for hot reloading
    // only- means to only hot reload for successful updates

    'babel-polyfill',

    './index.js'
    // the entry point of our app
  ];

module.exports = {
  entry: entries,
  output: {
    filename: 'bundle.js',
    path: resolve(__dirname, 'static'),
    publicPath: 'http://127.0.0.1:8080/static/'
  },
  context: resolve(__dirname, 'client'),
  devtool: 'inline-source-map',
  devServer: {
    hot: true,
    // enable HMR on the server
    port: 8080,
    host: '0.0.0.0',

    contentBase: resolve(__dirname, 'static'),
    // match the output path

    publicPath: '/'
    // match the output `publicPath`
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        loaders: ['babel-loader'],
        include: resolve(__dirname, 'client'),
        exclude: /node_modules/
      },
      {
        test: /\.scss$/,
        use: ["style-loader", "css-loader", "sass-loader"]
      },
      {
        test: /\.css$/,
        use: ["style-loader", "css-loader"]
      }
    ]
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    // enable HMR globally

    new webpack.NamedModulesPlugin(),
    // prints more readable module names in the browser console on HMR updates
  ],
};