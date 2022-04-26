instrument {
    name = 'CCI',
    icon = 'indicators:BB',
    overlay = true
}
input_group{
    "BUY",
    buy_color = input {default = "lime", type = input.color}
}

input_group{
    "SELL",
    sell_color = input {default = "aqua", type = input.color}
}

-- Define Strategy

base = sma(close,14)
upperband = base + (stdev(close,14)*2)
lowerband = base - (stdev(close,14)*2)

mycci = cci(close,14)

BuyCondition  = iff(close < lowerband and mycci < -200,true, false)
SellCondition = iff(close > upperband and mycci > 200, true, false)

-- Plate Signals

plot_shape ((BuyCondition  == true),"BUY"  ,shape_style.arrowup, shape_size.huge, buy_color , shape_location.belowbar, 0, "Buy", buy_color)
plot_shape ((SellCondition == true),"SELL" ,shape_style.arrowdown, shape_size.huge, sell_color, shape_location.abovebar, 0, "Sell", sell_color)
