# import matplotlib
import matplotlib as mpl
# get matplotlibrc path
mpl.matplotlib_fname()

# clear cash
mpl.font_manager._rebuild()

# test japanese 
import matplotlib.pyplot as plt
x=[1,2,3]

plt.plot(x,x,label="日本語テスト")
plt.legend()
plt.savefig("result.png")