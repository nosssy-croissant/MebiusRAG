![image](https://github.com/user-attachments/assets/3f172527-e48e-4938-b72a-f0a846ae1036)


readmeがんばってかきこみちゅうです

※本リポジトリはGigantic整地鯖非公式で開発を進めています!


[Gigantic整地鯖公式サイト](https://www.seichi.network/)


# 最低限の目標

**Mebiusくんと簡単な会話ができるようにする！！！**

最終的に[SeichiAssist](https://github.com/GiganticMinecraft/SeichiAssist/)へのサブモジュールかなんらかの形での統合を目指したい


# 仕様
## 💬 通常時（9割くらい）→ 従来の定型文を送る

参照先: [SeichiAssist/.../MebiusMessages.scala](https://github.com/GiganticMinecraft/SeichiAssist/blob/a48e4748fe0141d35d3d0f4eae5dbe00ffadd2a1/src/main/scala/com/github/unchama/seichiassist/subsystems/mebius/domain/resources/MebiusMessages.scala)

例： 
> 「ポコポコポコ…整地の音ってやっぱり落ち着くねぇ」 
> 「今日はどこまで掘るのかなー？」 
> 「僕たちはこの世界のどこかに埋まってるんだー。整地して僕の兄弟も見つけて欲しいな！」 

## 🤖 特別時（1割）→ GPT-3.5-turbo に接続して返答する

- プレイヤーがMebiusに話しかける
  - **整地鯖公式サイトなどに記載された公開情報をMarkdownで纏めて、RAGで質問に答えられるようにしたい**
    - AIの返答には誤りが含まれる可能性があることについて明記しておく  
  - スパム対策で専用コマンドから話しかけるように設計するべきか
  - 送りまくる人は出そう
- 何らかのイベントを検知（レベルアップ時・投票時・30分整地量ランキング発表時など）

# 懸念
- 整地鯖において必須機能にはなりえない
- FastAPIサーバーは若干とはいえメモリを食べる可能性
- gpt-3.5-turboは安価（1日100回、1回平均500トークン(文字)のリクエストで月数十~100円ほど）みたいだけど、めちゃくちゃリクエストが来たら大変！
  - RAGを用いると一気にトークン数が増えるので金額増の懸念が増す


# その他
- やりとりの履歴を若干保持しておきたい
  - データベース圧迫の懸念
  - メビウスの各個体によってやりとりの履歴を分けるべき?
    - マイクラ側のメビウスのアイテムにもユニーク性を与える変更が必要そう


# テスト用WebApp

現在FastAPIサーバー上 'localhost:8000' でWebAppが立つので簡単なやりとりをテスト出来ます ※自分のChatgpt Api Keyが必要です
