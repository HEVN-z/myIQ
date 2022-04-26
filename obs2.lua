instrument {
    name = 'Outside Bar 2',
    short_name = 'OSB',
    icon = 'indicators:MA',
    overlay = true
}
input_group {
    "Buy Outside Bar",
    colorBuy2 = input { default = "rgba(0, 0, 255, 0.8)", type = input.color }, 
    visibleBuy2 = input { default = true, type = input.plot_visibility }
}

input_group {
    "Sell Outside Bar",
    colorSell2 = input { default = "rgba(255, 20, 147, 0.8)", type = input.color },
    visibleSell2 = input { default = true, type = input.plot_visibility }
}
plot_shape((open[3] < close[3] and open[2] < close[2] and open[1] > close[1] and close[1] > open[2] and open[1] > open[2] and open < close),
                "Call2",
                shape_style.arrowup,
                shape_size.huge,
                colorBuy2,
                shape_location.belowbar,
                0,
                "OSB",
                colorBuy2  
) 
plot_shape((open[3] > close[3] and open[2] > close[2] and open[1] < close[1] and close[1] < open[2] and open[1] < open[2] and open > close),
                "Put2",
                shape_style.arrowdown,
                shape_size.huge,
                colorSell2,
                shape_location.abovebar,
                0,
                "OSB",
                colorSell2
            )