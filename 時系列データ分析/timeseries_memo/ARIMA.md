## How to Create an ARIMA Model for Time Series Forecasting in Python
https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/  

### ARIMA-processの概要
ARIMA-processは時系列予測のための広く人気のあるモデル.  
ARIMA ... AutoRegressive Integrated Moving Average  

パラメータ  
- p : モデルに含まれるラグの数
- d : 差分の回数
- 移動平均窓のサイズ
(窓 ... 移動平均のように時間軸上のデータを範囲で区切る方法において,この範囲のことを窓と呼ぶ)

### Shampoo dataset
3年間のシャンプーの月別販売数(単位は販売数).

データセットには右上がりの明確な傾向がある.
これは時系列が非定常であることがしめしており,定常性を獲得するためには
差分をとる必要がある.  
自己相関を見ると,最初の10から12ラグに正の相関があり,最初の5ラグが有意である.
``モデルのパラメータの良い出発点は5にすると良い.``  何故??

## ARIMAモデルの実装
statsmodelsライブラリを使う.
dosp=0 : フィットするときに,線形モデルのデバッグ情報が提供されることをオフにする.

- 残差の折れ線グラフ : モデルによって補足されないトレンド情報が残存する可能性を示唆している.
- 残差のkdeプロット : 誤差がガウス分布であることを示唆しているが,ゼロを中心としていない可能性がある.
- 残差の要約統計量 : 残差の平均が0ではない=予測結果に偏りがあることを示している. 

## パラメータチューニング
``Box–Jenkins method``を用いてパラメータをチューニングする(要するにグリッドサーチ).  
``Box–Jenkins method``  
ステップ1 : プロット,要約統計量,トレンド,季節性,自己分散によって必要なラグサイズのアイデアを得る.  
ステップ2 : フィッティング手順を使用して回帰モデルのパラメータを推定する.  
ステップ3 : モデルによって説明できない時間的構造の種類と量を決定するために,残差誤差の
プロットと統計的検定を使用する.  

https://machinelearningmastery.com/grid-search-arima-hyperparameters-with-python/