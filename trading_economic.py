import tradingeconomics as te
import json

te.login()

# def on_message(ws, message):
#   print(json.loads(message))

# te.subscribe('/calendar/country/US?importance=3')
# te.run(on_message)

print(te.getCalendarData(country='italy', output_type='df'))
# print(te.getIndicatorData(country=['united states']))