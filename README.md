# big_data_view
将大屏展示的html模板嵌套到django中，并通过mariadb存取数据。
<br>
使用方法：<br>
1.mariadb创建数据库show1 <br>
create database show1 default charset=utf8; <br>
2.可以使用SQL直接创建表show1Model_show1_month_plan <br>
```sql
Create Table: CREATE TABLE `show1Model_show1_month_plan` ( 
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `complete` int(11) DEFAULT NULL,
  `plan` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8；
```
3.show1Model_show1_month_plan表中插入页面显示数据 <br>
```sql
MariaDB [show1]> select * from show1Model_show1_month_plan;
+----+----------+-------+
| id | complete | plan  |
+----+----------+-------+
|  1 |    15633 | 68000 |
+----+----------+-------+
1 row in set (0.00 sec)
```
4.根据实际情况修改HelloWorld/settings.py中信息 <br>
ALLOWED_HOSTS = ['\*'] 默认允许所有访问 <br>
DATABASES 部分根据实际数据库信息进行修改 <br>
5.启动应用，访问 http://127.0.0.1:8000/show 可查看大屏展示 <br>
```python
python3 manage.py runserver 0.0.0.0:8000
```
![Alt text](https://github.com/zsx0728/big_data_view/blob/main/static/images/20211011144634.png)
