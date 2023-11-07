import requests,json,os
s = requests.session()
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
chat_id = os.getenv('TELEGRAM_CHAT_ID')
# print(bot_token)
item_numbers = ["MTV53HX/A", "MTV63HX/A", "MTV43HX/A", "MTV43HX/A"]
for item in item_numbers:
    a = s.post("https://www.idigital.co.il/AppServices/SVClientApplicationJSONWSContent.asmx/GetBranchesForAvailability", json={"itemNo": item})
    result = json.loads(a.text)
    rs1 = "Idigital: " +result['d'][17]['Title']+": AvailabilInStock: "+str(result['d'][17]['AvailabilInStock'])
    s.get("https://api.telegram.org/bot"+bot_token+"/sendMessage?chat_id="+chat_id+"&text="+rs1)
    rs1 = "Idigital: " +result['d'][18]['Title']+": AvailabilInStock: "+str(result['d'][18]['AvailabilInStock'])
    s.get("https://api.telegram.org/bot"+bot_token+"/sendMessage?chat_id="+chat_id+"&text="+rs1)
    rs1 = "Idigital: " +result['d'][7]['Title']+": AvailabilInStock: "+str(result['d'][7]['AvailabilInStock'])
    s.get("https://api.telegram.org/bot"+bot_token+"/sendMessage?chat_id="+chat_id+"&text="+rs1)

