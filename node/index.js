const express = require('express')
const axios = require('axios')

const app = express()
const port = 3000

const message = `Please send a GET request to /predict with the following query keys:
  x1 str,
  x2 str,
  x3 str,
  x4 str,
  x5 str,
  x6 num,
  x7 num,
  x8 str,
  x9 num,
  x10 num,
  x11 num,
  x12 num,
  x13 num,
  x14 num,
  x15 str,
  x16 str,
  x17 str,
  x18 num,
  x19 num,
  x20 num,
  x21 num,
  x22 num,
  x23 str,
  x24 str,
  x25 str,
  x26 str
`

app.get('/', (req, res) => {
  res.status(400).send(message)
})


app.get('/predict', async (req, res) => {
  const { query } = req

  if (
    isKeyValid(query, 'x1', 'string')
    && isKeyValid(query, 'x2', 'string')
    && isKeyValid(query, 'x3', 'string')
    && isKeyValid(query, 'x4', 'string')
    && isKeyValid(query, 'x5', 'string')
    && isKeyValid(query, 'x6', 'number')
    && isKeyValid(query, 'x7', 'number')
    && isKeyValid(query, 'x8', 'string')
    && isKeyValid(query, 'x9', 'number')
    && isKeyValid(query, 'x10', 'number')
    && isKeyValid(query, 'x11', 'number')
    && isKeyValid(query, 'x12', 'number')
    && isKeyValid(query, 'x13', 'number')
    && isKeyValid(query, 'x14', 'number')
    && isKeyValid(query, 'x15', 'string')
    && isKeyValid(query, 'x16', 'string')
    && isKeyValid(query, 'x17', 'string')
    && isKeyValid(query, 'x18', 'number')
    && isKeyValid(query, 'x19', 'number')
    && isKeyValid(query, 'x20', 'number')
    && isKeyValid(query, 'x21', 'number')
    && isKeyValid(query, 'x22', 'number')
    && isKeyValid(query, 'x23', 'string')
    && isKeyValid(query, 'x24', 'string')
    && isKeyValid(query, 'x25', 'string')
    && isKeyValid(query, 'x26', 'string')
  ) {
    const prediction = await axios({
      method: 'post',
      url: 'http://127.0.0.1:5555/predict',
      data: query,
    }).catch(e => e)
    if (prediction instanceof Error) {
      console.log('the error', prediction)
      res.status(500).send('Sorry there is an error processing your request')
      return
    }
    res.send({ prediction: prediction.data })
    return
  }
  res.status(400).send(message)
})

app.use('*', (req, res) => {
  res.status(400).send(message)
})

app.listen(port, () => console.log(`App listening on port ${port}!`))

function isKeyValid(obj, key, type) {
  const v = obj[key]
  if (typeof(v) !== 'string') return false
  if (type === 'string') {
    if (typeof(v) === 'string') {
      obj[key] = [v]
      return true
    }
    return false
  }
  if (type === 'number') {
    const parsed = parseFloat(v)
    if (!Number.isFinite(parsed)) return false
    if (parsed >= 0) {
      obj[key] = [parsed] // mutate the object
      return true
    }
    return false
  }
  return false
}