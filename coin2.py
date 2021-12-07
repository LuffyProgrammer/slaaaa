line = '=============='
from uuid import uuid4
import requests
from time import sleep
c = 0
print("""\
  _______                 
 |__   __|                
    | | _____  ____ _ ____
    | |/ _ \ \/ / _` |_  /
    | |  __/>  < (_| |/ / 
    |_|\___/_/\_\__,_/___|
""")
print('Tapjoy Bug AC By Marshall\n'+ line)

uid = 'bf81ffb4-3463-4e37-a762-57a79781b306'
print('\33[0m' + line)

headers={
 "cookies":"__cfduid=d0c98f07df2594b5f4aad802942cae1f01619569096",
        "authorization":"Basic NWJiNTM0OWUxYzlkNDQwMDA2NzUwNjgwOmM0ZDJmYmIxLTVlYjItNDM5MC05MDk3LTkxZjlmMjQ5NDI4OA=="
    }

for i in range(25):
        
        data = {
      "reward":{"ad_unit_id":"255884441431980_807351306285288","credentials_type":"publisher","custom_json":{"hashed_user_id":f"{uid}"},"demand_type":"sdk_bidding","event_id":f"{uuid4()}","network":"facebook","placement_tag":"default","reward_name":"Amino Coin","reward_valid":"true","reward_value":2,"shared_id":"dc042f0c-0c80-4dfd-9fde-87a5979d0d2f","version_id":"1569147951493","waterfall_id":"dc042f0c-0c80-4dfd-9fde-87a5979d0d2f"},
        "app":{"bundle_id":"com.narvii.amino.master","current_orientation":"portrait","release_version":"3.4.33567","user_agent":"Dalvik\/2.1.0 (Linux; U; Android 10; G8231 Build\/41.2.A.0.219; com.narvii.amino.master\/3.4.33567)"},"date_created":1620295485,"session_id":"49374c2c-1aa3-4094-b603-1cf2720dca67","device_user":{"country":"US","device":{"architecture":"aarch64","carrier":{"country_code":602,"name":"Vodafone","network_code":0},"is_phone":"true","model":"GT-S5360","model_type":"Samsung","operating_system":"android","operating_system_version":"29","screen_size":{"height":2260,"resolution":2.55,"width":1080}},"do_not_track":"false","idfa":"7495ec00-0490-4d53-8b9a-b5cc31ba885b","ip_address":"","locale":"en","timezone":{"location":"Asia\/Seoul","offset":"GMT+09:00"},"volume_enabled":"true"}
        } 
        respone = requests.post("https://ads.tapdaq.com/v4/analytics/reward",json=data, headers=headers)
        
        
        if respone.status_code == 204:
        	c += 2
        	print(f'{c}:- ' + '\33[33m2 Amino Coins Sended')
        else:
        		print("\33[31mError")
        		print(respone.content)
        		sleep(10)
        		
print('\33[0m' + line + '\nAll Coins Sended ✓')
