const test = require('tape')
const axios = require('axios')

const url = 'http://localhost:3000/predict' 

test('route should work', async t => {
  let r = ''

  r = await axios.get(url + `?
  x1=abc&
  x2=abc&
  x3=abc&
  x4=abc&
  x5=abc&
  x6=1&
  x7=1&
  x8=abc&
  x9=1&
  x10=1&
  x11=1&
  x12=1&
  x13=1&
  x14=1&
  x15=abc&
  x16=abc&
  x17=abc&
  x18=1&
  x19=1&
  x20=1&
  x21=1&
  x22=1&
  x23=abc&
  x24=abc&
  x25=abc&
  x26=abc
  `.replace(/[ \n]*/g, ''))

  t.ok('prediction' in r.data)

  t.end()
})

test('route should not work', async t => {
  let r = ''
  
  r = await axios.get('http://localhost:3000').catch(e => e)
  t.ok(r instanceof Error)

  r = await axios.get(url).catch(e => e)
  t.ok(r instanceof Error)
 
  r = await axios.get(url + '/').catch(e => e)
  t.ok(r instanceof Error)

  r = await axios.get(url + '/abc').catch(e => e)
  t.ok(r instanceof Error)

  r = await axios.get(url + '/x1=1').catch(e => e)
  t.ok(r instanceof Error)

  r = await axios.get(url + `?
  x2=abc&
  x3=abc&
  x4=abc&
  x5=abc&
  x6=1& 
  x7=1&
  x8=abc&
  x9=1&
  x10=1&
  x11=1&
  x12=1&
  x13=1&
  x14=1&
  x15=abc&
  x16=abc&
  x17=abc&
  x18=1&
  x19=1&
  x20=1&
  x21=1&
  x22=1&
  x23=abc&
  x24=abc&
  x25=abc&
  x26=abc
  `.replace(/[ \n]*/g, '')).catch(e => e)
  t.ok(r instanceof Error, 'x1 missing')

  r = await axios.get(url + `?
  x1=abc&x1=abc&
  x2=abc&
  x3=abc&
  x4=abc&
  x5=abc&
  x6=1& 
  x7=1&
  x8=abc&
  x9=1&
  x10=1&
  x11=1&
  x12=1&
  x13=1&
  x14=1&
  x15=abc&
  x16=abc&
  x17=abc&
  x18=1&
  x19=1&
  x20=1&
  x21=1&
  x22=1&
  x23=abc&
  x24=abc&
  x25=abc&
  x26=abc
  `.replace(/[ \n]*/g, '')).catch(e => e)
  t.ok(r instanceof Error, 'x1 wrong type')
  
  r = await axios.get(url + `?
  x1=abc&
  x2=abc&
  x3=abc&
  x4=abc&
  x5=abc&
  x6=abc& 
  x7=1&
  x8=abc&
  x9=1&
  x10=1&
  x11=1&
  x12=1&
  x13=1&
  x14=1&
  x15=abc&
  x16=abc&
  x17=abc&
  x18=1&
  x19=1&
  x20=1&
  x21=1&
  x22=1&
  x23=abc&
  x24=abc&
  x25=abc&
  x26=abc
  `.replace(/[ \n]*/g, '')).catch(e => e)
  t.ok(r instanceof Error, 'x6 wrong type')

  r = await axios.get(url + `?
  x1=abc&
  x2=abc&
  x3=abc&
  x4=abc&
  x5=abc&
  x6=1& 
  x7=abc&
  x8=abc&
  x9=1&
  x10=1&
  x11=1&
  x12=1&
  x13=1&
  x14=1&
  x15=abc&
  x16=abc&
  x17=abc&
  x18=1&
  x19=1&
  x20=1&
  x21=1&
  x22=1&
  x23=abc&
  x24=abc&
  x25=abc&
  x26=abc
  `.replace(/[ \n]*/g, '')).catch(e => e)
  t.ok(r instanceof Error, 'x7 wrong type')

  t.end()
})