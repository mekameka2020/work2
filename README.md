# work2
- ロボットシステム学＿課題２＿提出用リポジトリ
# 内容
ROSを用いた『先に100になった方の負けゲーム』の実行
※『先に100になった方の負けゲーム』とは？
- ２人のプレイヤーが一人ずつ1～9までの数値を打ち込み、最終的に総計を100にしてしまった方の負け、というルールのゲーム。

# 使用したもの
- ラズベリーパイ４
- ROS
- 通信用ケーブル(USB-TypeCケーブル、LANケーブル)

# インストール方法
```sh
git clone https://github.com/mekameka2020/work2.git
```
と打ち込む。

#　準備
 ## Tab1
- roscoreの起動
 ```sh 
 roscore
 ```
 ## Tab2
- Plyaer1(参加者１)用のタブ
 ```sh
 rosrun mypkg Player1.py
 ```
 ## Tab3
- Plyaer2(参加者２)用のタブ
 ```sh
 rosrun mypkg Player2.py
 ```
 ## Tab4
- 双方の打ち込んだ数字を足し合わせた結果の表示・および勝者の表示のためのタブ
 ```sh
 rosrun mypkg judgement.py
 ```
 ## Tab5
- ノード・トピックの確認用タブ

 1.ノードの確認
 ```sh
 rosnode list
 ```
 2.トピックの確認
 ```sh
 rostopic list
 ```
# 使用方法
 1.
 ## Tab2
- Plyaer1(参加者１)用のタブに1～9までの数字を打ち込む
 2.
 ## Tab4
　に打ち込んだ数値が表示される
 3.
 ## Tab3
- Plyaer2(参加者２)用のタブに1～9までの数字を打ち込む
 4.
 ## Tab4
 2.で打ち込んだ数値と3.で打ち込んだ数値の総計が表示される
 5.
- 1. 3. を繰り返し行う。
 6.総計が100を超えたとき、勝った側のPlayer名が呼ばれる。

# 参照動画

# ライセンス
GNU General Public License v3.0

# 参考にしたページのリンク

# Ryuichi UedaによるROSのインストールページ(Ubuntu20.04のみ)のリンク
https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_server
# 参考にした方
iwaikaira
Github内参考ページリンク：https://github.com/iwaikaira/myROS
# GitHubへのアップロード内容の書式に関して参照した方
- kentaobata
- 参照したページのリンク:https://github.com/kentaobata/Robosys_Task2
