#จงเขียนคำสั่งเพื่อแสดงความยาวของตัวอักษร "I am the best programmer"
me = "I am the best programmer"
print (len(me))

#จงเขียนคำสั่งเพื่อแสดงอักษรแรกของข้อความ "I am the best programmer"
print(me[0])

#จงเขียนคำสั่งเพื่อแสดง "best" ของข้อความ "I am the best programmer"
print(me[9:13])

#จงเขียนคำสั่งเพื่อแสดข้อความ "I am the best programmer" ที่ไม่มี space
print (me.replace(" ", ""))

#จงเขียนคำสั่งเพื่อแสดข้อความ "I am the best programmer" ให้เป็นตัวพิมใหญ่ทั้งหมด
print (me.upper())

#จงเขียนคำสั่งเพื่อแสดข้อความ "I am the best programmer" ให้เป็นตัวพิมเล็กทั้งหมด
print (me.lower())

#จงเขียนคำสั่งเพื่อแสดข้อความ "I am the best programmer" ที่ถูกแทนที่อักษร e ด้วย z ทั้งหมด
print (me.replace("e", "z"))

#จงเติมคำในช่องว่าเพื่อแสดงชื่อ
myname = "aof"
txt = "{} is the best programmer"
print(txt.format(myname))