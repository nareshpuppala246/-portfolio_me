import yfinance as yf
import matplotlib.pyplot as plt

ticker = 'AAPL'
data = yf.download(ticker, period='5d', interval='1h')

plt.plot(data['Close'], marker='o')
plt.title(f"{ticker} Stock Price (Last 5 Days)")
plt.xlabel("DateTime")
plt.ylabel("Close Price")
plt.grid(True)
plt.savefig("stock_output.png")
