const express = require('express')
const app = express()
const port = 3000

resolve = require('path').resolve

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.get('/index', (req, res) => {
    res.sendFile(resolve("static/index.html"))
    // res.send('Hello World!')
  })

app.get('/index.js', (req, res) => {
    res.sendFile(resolve("static/index.js"))
// re s.send('Hello World!')
})

app.get('/jquery-3.5.1.min.js', (req, res) => {
    res.sendFile(resolve("static/jquery-3.5.1.min.js"))
// re s.send('Hello World!')
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})