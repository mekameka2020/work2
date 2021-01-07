# work2
ROSに関する講義中のノードの実行に関するコードを配置

# ロボットシステム学＿課題２＿提出用リポジトリ

# 使用したもの
- ラズベリーパイ４
- ROS

# インストール方法
```sh
git clone https://github.com/mekameka2020/work2.git
```
と打ち込む。

# count.py 使用方法
 ## Tab1
 ```sh 
 roscore
 ```
 ## Tab2
 ```sh
 rosrun mypkg count.py
 ```
 ## Tab3
 1.ノードの確認
 ```sh
 rosnode list
 ```
 2.トピックの確認
 ```sh
 rostopic list
 ```
 3.『0.1秒につき1カウントしているか』を確認
 ```sh
 rostopic echo /count_up
 ```
 ⇒『data: N』 N:数字
     ___
      .
      .
      .
      と、表示されてゆけば成功。
 
# twice.py 使用方法
## Tab1
 ```sh 
 roscore
 ```
 ## Tab2
 ```sh
 rosrun mypkg count.py
 ```
 ## Tab3
 ```sh
 rosrun mypkg twice.py
 ```
 ## Tab4
 1.ノードの確認
 ```sh
 rosnode list
 ```
 2.トピックの確認
 ```sh
 rostopic list
 ```
 3.『0.1秒につき1カウントしているか』を確認
 ```sh
 rostopic echo /twice
 ```
 ⇒『data: M』 M:2の倍数である数字
     ___
      .
      .
      .
      と、表示されてゆけば成功。
 
 

# 参照動画
https://www.youtube.com/watch?v=iaYpV31U7j4

# ライセンス
GNU General Public License v3.0

# 参考にしたページ(講義動画)のリンク
https://www.youtube.com/watch?v=PL85Pw_zQH0

# Ryuichi UedaによるROSのインストールページ(Ubuntu20.04のみ)のリンク
https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_server
# 参考にした方
- Ryuichi Ueda
- GitHub:https://github.com/ryuichiueda
# GitHubへのアップロード内容に関して参照した方
- kentaobata
- 参照したページのリンク:https://github.com/kentaobata/Robosys_Task2
