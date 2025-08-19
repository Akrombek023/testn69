# loyihaga TZ

"""
classlar 4 ta boladi
1.User
2.Teacher
3.Group
4.Student

1. user classni xususyatlari
 * name
 * phone
 * email
 * login
 * password
 * role - "admin" "teacher" "student"

user classni metodlari
 * login_panel - login va parol tekshirib, roliga mos panel ochadi

2. teacher class xususyatlari
 * name
 * phone
 * email
 * groups - teacher oqitadigan grouplar ruyxati

teacher class metodlari
 * view_my_group - faqat oziga tegishli grouplarni korsatadi

3. group class xususyatlari
 * group_name
 * teacher - teacher objectiga boglanadi
 * student - student objectlari ruyxati
 * homeworks - vazifa nomi va vazifa matni
 * grades - student baxo

group class metodlari
 * view_students - faqat shu group studentlarnini korsatadi
 * add_homework - vazifa matnini
 * view_homework - faqat shu group vazifalarini korsatadi


4. student class xususyatlari
 * name
 * phone
 * email
 * group - group objectiga boglangan
 * grades - vazifa baxo

student class metodlari
 * view_homeworks - faqat o‘z groupidagi vazifalarni ko‘rsatadi
 * view_grades - faqat o‘z baholarini ko‘rsatadi


BOG'LANISHLAR
 * Admin - barcha teacher, group, studentlarni boshqaradi.
 * Teacher - faqat o‘z grouplarini ko‘radi, vazifa beradi.
 * Group - bitta teacherga tegishli, ichida studentlar bor.
 * Student - bitta groupga tegishli.
 * Student - faqat o‘z vazifasi va o‘z bahosini ko‘radi.
 * Teacher - boshqa teacherlarning grouplarini ko‘ra olmaydi.
"""