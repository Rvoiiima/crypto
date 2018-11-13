#! -*- coding:utf-8 -*-
from Crypto.Util.number import long_to_bytes, bytes_to_long

#文字列を数字にするまでの流れ
print u'文字列を数字にするまでの流れ(ファイル読み込みから計算まで)'
print '-----------------------------------------'
#文字列を16進数に変換する(encode)
x = "Hello".encode("hex")
print  'x =  "Hello', x

#16進数を10進数に変換する
i = int(x, 16)
print 'i = int(x, 16):', i

print '-----------------------------------------'
#RSAなどの計算
print
#RSAの計算終了
print u'計算した数字を文字に戻すまでの流れ'
print '-----------------------------------------'
#10進数を16進数にする
h = hex(i)
print 'h=hex(i):', h

#hex()関数は 先頭に0x(16進数を表す文字)やl(long型であることを示す文字)がつくため，文字列として返してしまう
print 'type(h):', type(h) 

#先頭の0xを取り除く
print 'h[2:]', h[2:]

#long型の場合には一番後ろも取り除く
#print h[2:-1]

# 16進数の部分だけ取り出したら文字列に戻せる
print "h[2:].decode('hex')", h[2:].decode('hex')

print '-----------------------------------------'

print u'上の計算を自動でやってくれる関数'
print '-----------------------------------------'
print 'from Crypto.Util.number import bytes_to_long, long_to_bytes'

print "bytes_to_long('Hello'): ", bytes_to_long('Hello')
print 'long_to_bytes(310939249775): ', long_to_bytes(310939249775)

print '-----------------------------------------'

#16進数から文字列に戻す(decode)
print '48656c6c6f'.decode('hex')
