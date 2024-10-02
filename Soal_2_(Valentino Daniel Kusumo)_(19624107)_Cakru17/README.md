# Penjelasan Soal 2 (Battle of Robots)

```python

# Program dimulai dengan memberikan pilihan robot kepada pemain, kemudian pemain diberikan kebebasan untuk memilih robot 1 & 2
# Setelah itu, permainan akan berlangsung dimana kedua robot saling bertarung hingga health habis (0)
# Terakhir, nama robot pemenang akan ditampilkan

Program dimulai dengan mengimport fungsi random, lalu membuat class Robot dengan beberapa atributnya (name, health, attack power)
Dalam class Robot sendiri, ada beberapa fungsi, seperti get_name (nama robot), get_health (nyawa robot), attack (robot perang dengan damage sekian)
-- take_damage (nyawa robot berkurang ketika menerima damage & memastikan nyawa robot akan berhenti di 0), dan is_defeated (robot sudah kalah)

Kemudian, membuat class Battle (kondisi perang) dengan mendefinisikan terlebih dahulu robot 1 dan 2, lalu membuat beberapa fungsi
-- seperti start_fight (perang dimulai --> robot 1 menyerang terlebih dahulu baru kemudian robot 2 menyerang dengan menampilkan kedua nyawa saat itu )
-- Ketika salah satu robot kalah, robot satunya akan dinyatakan sebagai pemenang. Begitupun juga sebaliknya

Terakhir, membuat class Game dengan kondisi awal robot belum ada, kemudian dibuatlah fungsi add_robot (untuk menambahkan robot)
-- lalu, ada start_game (ada syarat tertentu sebelum game dimulai --> robot harus berjumlah minimal 2 ), kemudian list robot akan ditampilkan
-- Setelah pemain memilih kedua robot, perang antara robot akan dimulai hingga salah satu robot kalah 


