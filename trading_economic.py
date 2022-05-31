import tradingeconomics as te
import json

te.login('guest:guest')

# def on_message(ws, message):
#   print(json.loads(message))

# te.subscribe('/calendar/country/US?importance=3')
# te.run(on_message)

print(te.getCalendarData(importance='3', output_type='df'))
