import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv("x_final.csv")

# 정규화
data = df1[["hospital", "product", "pharmacy", "foster_place", "beauty", "all_facilities", "ratio"]]
data_mm = (data - data.min(axis=0)) / (data.max(axis=0) - data.min(axis=0))
df1[["hospital", "product", "pharmacy", "foster_place", "beauty", "all_facilities", "ratio"]] = data_mm
df1.to_csv("x_final_normalization.csv", encoding='utf-8-sig', index=False)

f, axes = plt.subplots(2, 3)
f.set_size_inches((20, 15))
plt.subplots_adjust(wspace=0.3, hspace=0.3)

df1 = df1.sort_values(by=["all_facilities"], ascending=False)
axes[0, 0].bar(df1["행정동"], df1["hospital"], label="hospital", color="red", alpha=0.3)
axes[0, 0].bar(df1["행정동"], df1["product"], label="product", bottom=df1["hospital"], color="orange", alpha=0.3)
axes[0, 0].bar(df1["행정동"], df1["pharmacy"], label="pharmacy", bottom=df1["hospital"] + df1["product"], color="yellow", alpha=0.3)
axes[0, 0].bar(df1["행정동"], df1["foster_place"], label="foster_place", bottom=df1["hospital"] + df1["product"] + df1["pharmacy"], color="green", alpha=0.3)
axes[0, 0].bar(df1["행정동"], df1["beauty"], label="beauty", bottom=df1["hospital"] + df1["product"] + df1["pharmacy"] + df1["foster_place"], color="purple", alpha=0.3)
axes[0, 0].plot(df1["행정동"], df1["ratio"]*5, label="ratio", color="black", alpha=0.7)
axes[0, 0].set_title("반려견 시설(전체)별 반려인 수")
axes[0, 0].legend()
axes[0, 0].tick_params(labelrotation=45)

df1 = df1.sort_values(by=["hospital"], ascending=False)
axes[0, 1].bar(df1["행정동"], df1["hospital"], label="hospital", color="red", alpha=0.3)
axes[0, 1].plot(df1["행정동"], df1["ratio"], label="ratio", color="black", alpha=0.7)
axes[0, 1].set_title("반려견 시설(병원)별 반려인 수")
axes[0, 1].legend()
axes[0, 1].tick_params(labelrotation=45)

df1 = df1.sort_values(by=["product"], ascending=False)
axes[0, 2].bar(df1["행정동"], df1["product"], label="product", color="orange", alpha=0.3)
axes[0, 2].plot(df1["행정동"], df1["ratio"], label="ratio", color="black", alpha=0.7)
axes[0, 2].set_title("반려견 시설(용품)별 반려인 수")
axes[0, 2].legend()
axes[0, 2].tick_params(labelrotation=45)

df1 = df1.sort_values(by=["pharmacy"], ascending=False)
axes[1, 0].bar(df1["행정동"], df1["pharmacy"], label="pharmacy", color="yellow", alpha=0.3)
axes[1, 0].plot(df1["행정동"], df1["ratio"], label="ratio", color="black", alpha=0.7)
axes[1, 0].set_title("반려견 시설(약국)별 반려인 수")
axes[1, 0].legend()
axes[1, 0].tick_params(labelrotation=45)

df1 = df1.sort_values(by=["foster_place"], ascending=False)
axes[1, 1].bar(df1["행정동"], df1["foster_place"], label="foster_place", color="green", alpha=0.3)
axes[1, 1].plot(df1["행정동"], df1["ratio"], label="ratio", color="black", alpha=0.7)
axes[1, 1].set_title("반려견 시설(위탁)별 반려인 수")
axes[1, 1].legend()
axes[1, 1].tick_params(labelrotation=45)

df1 = df1.sort_values(by=["beauty"], ascending=False)
axes[1, 2].bar(df1["행정동"], df1["beauty"], label="beauty", color="purple", alpha=0.3)
axes[1, 2].plot(df1["행정동"], df1["ratio"], label="ratio", color="black", alpha=0.7)
axes[1, 2].set_title("반려견 시설(미용)별 반려인 수")
axes[1, 2].legend()
axes[1, 2].tick_params(labelrotation=45)

plt.rc("font", family="Malgun Gothic")
plt.savefig('visualization_plt.png')
plt.show()
