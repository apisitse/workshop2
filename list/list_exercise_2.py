#จงแสดง "rat"
animal = ["cat", "bat", "rat", "dog"]
print(2)

#จงแก้ไขข้อมูลจาก "cat" เป็น "hen"
animal = ["cat", "bat", "rat", "dog"]
animal[0] = "hen"

#จงเพิ่ม "hen" ไปยัง animal list
animal = ["cat", "bat", "rat", "dog"]
animal.append("hen")

#จงเพิ่ม "hen" ไประหว่าง "rat" กับ "ิิdog"
animal = ["cat", "bat", "rat", "dog"]
animal.insert(2,"hen")

#จงลบ "rat" จาก list
animal = ["cat", "bat", "rat", "dog"]
animal.remove("rat")

#จงแสดงตัวสุดท้ายของ animal
animal = ["cat", "bat", "rat", "dog"]
print(animal[3])

#จงแสดงจำนวนของ animal
animal = ["cat", "bat", "rat", "dog"]
print(len(animal))
