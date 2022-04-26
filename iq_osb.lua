instrument {
    name = 'Outside Bar',
    short_name = 'OSB',
    icon = 'indicators:MA',
    overlay = true
}

MaFast_period = input(12,"Ma Fast period",input.integer,1,1000,1)
MaFast_average = input(2,"Ma Fast average", input.string_selection,averages.titles)
MaFast_title = input(1,"Ma Fast title", input.string_selection,inputs.titles)

MaSlow_period = input(26,"Ma Slow period",input.integer,1,1000,1)
MaSlow_average = input(2,"Ma Slow average", input.string_selection,averages.titles)
MaSlow_title = input(1,"Ma Slow title", input.string_selection,inputs.titles)

MaTrend_period = input(100,"Ma Trend period",input.integer,1,1000,5)
MaTrend_average = input(2,"Ma Trend average", input.string_selection,averages.titles)
MaTrend_title = input(1,"Ma Trend title", input.string_selection,inputs.titles)



input_group {
    "Area Up and Down",
    colorAreaUp = input { default = "rgba(34, 139, 34, 0.3)", type = input.color },  
    colorAreaDown = input { default = "rgba(220, 20, 60, 0.3)", type = input.color },
    visibleArea = input { default = true, type = input.plot_visibility } 
}

input_group {
    "Ma Fast Line",
    colorFast = input { default = "#ff56e8", type = input.color },
    widthFast = input { default = 1, type = input.line_width},
    visibleFast = input { default = false, type = input.plot_visibility }
}

input_group {
    "Ma Slow Line",
    colorSlow = input { default = "#2d2af7", type = input.color },
    widthSlow = input { default = 2, type = input.line_width},
    visibleSlow = input { default = false, type = input.plot_visibility }
}

input_group {
    "Ma Trend Line",
    colorTrend = input { default = "#f74200", type = input.color },
    widthTrend = input { default = 3, type = input.line_width},
    visibleTrend = input { default = false, type = input.plot_visibility }
}

input_group {
    "Buy Engulfing",
    colorBuy = input { default = "green", type = input.color },
    visibleBuy = input { default = false, type = input.plot_visibility }
}

input_group {
    "Sell Engulfing",
    colorSell = input { default = "red", type = input.color },
    visibleSell = input { default = false, type = input.plot_visibility }
}

input_group {
    "Buy Double Engulfing",
    colorBuy1 = input { default = "rgba(34, 139, 34, 0.8)", type = input.color }, 
    visibleBuy1 = input { default = false, type = input.plot_visibility }
}

input_group {
    "Sell Double Engulfing",
    colorSell1 = input { default = "rgba(220, 20, 60, 0.8)", type = input.color },
    visibleSell1 = input { default = false, type = input.plot_visibility }
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

local avgFast = averages[MaFast_average]
local titleFast = inputs[MaFast_title]

local avgSlow = averages[MaSlow_average]
local titleSlow = inputs[MaSlow_title]

local avgTrend = averages[MaTrend_average]
local titleTrend = inputs[MaTrend_title]

if visibleFast == true then
    plot(avgFast(titleFast,MaFast_period),"Ma Fast",colorFast,widthFast)
end

if visibleSlow == true then
    plot(avgSlow(titleSlow,MaSlow_period),"Ma Slow",colorSlow,widthSlow)
end

if visibleTrend == true then
    plot(avgTrend(titleTrend,MaTrend_period),"Ma Trend",colorTrend,widthTrend)
end

candle_time = {"1s", "5s", "10s", "15s", "30s", "1m", "2m", "5m", "10m", "15m", "30m", "1H", "2H", "4H", "8H", "12H", "1D", "1W", "1M", "1Y"}
candle_time_res = input(6,"Candle check resolution",input.string_selection,candle_time)

sec = security (current_ticker_id, candle_time[candle_time_res])

filter_source = {"1s", "5s", "10s", "15s", "30s", "1m", "2m", "5m", "10m", "15m", "30m", "1H", "2H", "4H", "8H", "12H", "1D", "1W", "1M", "1Y"}
filter_pa_index = input(8,"Candle check resolution",input.string_selection,filter_source)

filter_pa = security (current_ticker_id, filter_source[filter_pa_index])

--print(filter_source[filter_pa_index])

if (sec ~= nil) then
    
    MaFast0 = avgFast(titleFast,MaFast_period) --Ma Fast bar 0
    MaFast1 = MaFast0[1]                       --Ma Fast bar 1
    
    MaSlow0 = avgSlow(titleSlow,MaSlow_period) --Ma Slow bar 0
    MaSlow1 = MaSlow0[1]
    
    MaTrend0 = avgTrend(titleTrend,MaTrend_period)
    MaTrend1 = MaTrend0[1]
    
    if(visibleBuy == true) then
        plot_shape((close > open and close[1] < open[1] and close > MaFast0 and MaFast0 > MaSlow0 and MaSlow0 > MaTrend0 and close > open[1] and open <= close[1] and abs(close-open) > abs(close[1]-open[1])),
            "Call",
            shape_style.arrowup,
            shape_size.huge,
            colorBuy,
            shape_location.belowbar,
            0,
            "Eng",
            colorBuy  
           ) 
    end
    
    if (visibleSell == true) then
        plot_shape((close < open and close[1] > open[1] and close < MaFast0 and MaFast0 < MaSlow0 and MaSlow0 < MaTrend0 and close < open[1] and open >= close[1] and abs(close-open) > abs(close[1]-open[1])),
            "Put",
            shape_style.arrowdown,
            shape_size.huge,
            colorSell,
            shape_location.abovebar,
            0,
            "Eng",
            colorSell
        )
    end


    if(visibleBuy1 == true) then 
        if(filter_pa.close[1] > filter_pa.open[1] and filter_pa.close[2] < filter_pa.open[2] and filter_pa.close[1] > filter_pa.open[2] and filter_pa.open[1] <= filter_pa.close[2] and abs(filter_pa.close[1]-filter_pa.open[1]) > abs(filter_pa.close[2]-filter_pa.open[2]) ) then                                 
            plot_shape((close > open and close[1] < open[1] and close > open[1] and open <= close[1] and abs(close-open) > abs(close[1]-open[1])),
                "Call1",
                shape_style.arrowup,
                shape_size.huge,
                colorBuy1,
                shape_location.belowbar,
                0,
                "DouEng",
                colorBuy1  
               ) 
    end
    end
    
    if (visibleSell1 == true) then
        if(filter_pa.close[1] < filter_pa.open[1] and filter_pa.close[2] > filter_pa.open[2] and filter_pa.close[1] < filter_pa.open[2] and filter_pa.open[1] >= filter_pa.close[2] and abs(filter_pa.close[1]-filter_pa.open[1]) > abs(filter_pa.close[2]-filter_pa.open[2]) ) then                                 
            plot_shape((close < open and close[1] > open[1] and close < open[1] and open >= close[1] and abs(close-open) > abs(close[1]-open[1])),
                "Put1",
                shape_style.arrowdown,
                shape_size.huge,
                colorSell1,
                shape_location.abovebar,
                0,
                "DouEng",
                colorSell1
            )
        end
    end


     if(visibleBuy2 == true) then 
        --if(filter_pa.close[1] > filter_pa.open[1] and filter_pa.close[2] < filter_pa.open[2] and filter_pa.close[1] > filter_pa.open[2] and filter_pa.open[1] <= filter_pa.close[2] and abs(filter_pa.close[1]-filter_pa.open[1]) > abs(filter_pa.close[2]-filter_pa.open[2]) ) then                                 
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
    --end
    end

    if (visibleSell2 == true) then
        --if(filter_pa.close[1] < filter_pa.open[1] and filter_pa.close[2] > filter_pa.open[2] and filter_pa.close[1] < filter_pa.open[2] and filter_pa.open[1] >= filter_pa.close[2] and abs(filter_pa.close[1]-filter_pa.open[1]) > abs(filter_pa.close[2]-filter_pa.open[2]) ) then                                 
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
        --end
    end




    if (visibleArea == true) then
        fill(MaFast0,MaSlow0,"Area", MaFast0 > MaSlow0 and colorAreaUp or MaFast0 < MaSlow0 and colorAreaDown )
    
   end


end