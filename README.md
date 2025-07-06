# 仕様
## 💬 通常時（9割くらい）→ 従来の定型文を送る

参考: [SeichiAssist](https://github.com/GiganticMinecraft/SeichiAssist/blob/a48e4748fe0141d35d3d0f4eae5dbe00ffadd2a1/src/main/scala/com/github/unchama/seichiassist/subsystems/mebius/domain/resources/MebiusMessages.scala)

例： 
> 「ポコポコポコ…整地の音ってやっぱり落ち着くねぇ」 
> 「今日はどこまで掘るのかなー？」 
> 「僕たちはこの世界のどこかに埋まってるんだー。整地して僕の兄弟も見つけて欲しいな！」 

## 🤖 特別時（1割）→ GPT-3.5-turbo に接続して返答する

- プレイヤーがMebiusに話しかける
- 何らかのイベントを検知（レベルアップ時・投票時・30分整地量ランキング発表時など）

- **整地鯖公式サイトなどに記載された公開情報をMarkdownで纏めて、RAGで質問に答えられるようにしたい**
  - AIの返答には誤りが含まれる可能性があることについて明記しておく 

# テスト用WebApp

現在FastAPIサーバー上 'localhost:8000' にHTMLページを埋め込んで簡単なやりとりをテスト出来ます
