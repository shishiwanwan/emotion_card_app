import streamlit as st

# ページ設定
st.set_page_config(page_title="Feeling Card App", page_icon="😊", layout="wide")

st.title(" 感情表出カード")
st.write("クリックして、今の気持ちを選んでみましょう。")

# 絵カードリスト（helpは除外）
cards = [
    {"label": "トイレに行きたい", "file": "assets/toilet.png"},
    {"label": "おなかがすいた", "file": "assets/food.png"},
    {"label": "ねむい", "file": "assets/rest.png"},
    {"label": "うれしい", "file": "assets/happy.png"},
    {"label": "かなしい", "file": "assets/sad.png"},
]

# カードを横並びで表示
cols = st.columns(5)

# 選択したカードを格納する変数
selected = None

for i, card in enumerate(cards):
    with cols[i]:
        if st.button(card["label"]):
            selected = card["label"]
        st.image(card["file"], use_container_width=True)

# 結果表示
st.markdown("---")
if selected:
    st.success(f"✅ 選ばれたカード: **{selected}**")
else:
    st.info("まだカードが選ばれていません。クリックして選んでください。")