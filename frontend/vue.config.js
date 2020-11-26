module.exports = {
  "transpileDependencies": [
    "vuetify"
  ],
  devServer: {
    proxy: {
      '/api': {
        //target: 'http://62.234.43.40/',
        target: 'http://localhost:8000/',
        changeOrigin: true,
      },
      'auth': {
        target: 'http://localhost:8000/',
        //target: 'http://62.234.43.40/',
        changeOrigin: true,
      }
    }
  }
}
