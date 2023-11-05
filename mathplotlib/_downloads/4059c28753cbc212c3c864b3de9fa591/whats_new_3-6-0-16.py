plt.rcParams["font.size"] = 20
fig = plt.figure(figsize=(4.75, 1.85))

text = "There are 几个汉字 in between!"
fig.text(0.05, 0.65, text, family=["Noto Sans CJK JP", "Noto Sans TC"])
fig.text(0.05, 0.45, text, family=["DejaVu Sans", "Noto Sans CJK JP", "Noto Sans TC"])