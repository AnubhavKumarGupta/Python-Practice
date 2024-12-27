import qrcode

img = qrcode.make(
    "https://www.google.com/imgres?imgurl=https%3A%2F%2Fpbs.twimg.com%2Fmedia%2FEWCOaieWkAEF0xk.jpg%3Alarge&tbnid=kHAG9RjDPMyziM&vet=12ahUKEwju75vZkf-AAxWx2zgGHdARAT4QMygKegQIARBd..i&imgrefurl=https%3A%2F%2Ftwitter.com%2Fambadkercaravan%2Fstatus%2F1252157294999150592&docid=62AlDRq5BnPTpM&w=552&h=311&q=ja%20na%20laude&ved=2ahUKEwju75vZkf-AAxWx2zgGHdARAT4QMygKegQIARBd"
)
img.save("MyQr.png")
img.show()
