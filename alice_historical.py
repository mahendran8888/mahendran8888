import http.client
import json

conn = http.client.HTTPSConnection("a3.aliceblueonline.com")
payload = json.dumps({
  "token": "1594",
  "resolution": "D",
  "from": "1660128489000",
  "to": "1660221861000",
  "exchange": "NSE"
})
headers = {
  'Authorization': 'Bearer userId gx7tCTLbjGDSRb7ltQNDBfOVYz73avMG41j7FHHnnUmLOtizMfCJaLjPSf126I4RCnA1HU5eaA5bruVL9U0Tm59JW1if4EhnHM1NDLZIfgrQv5T2QkOCWBO7Ky2AfinWQOYq9ka7Wp1PcsKJn18JEHy05VM1nprddH4C5d2C8Mclijqb9YaoccXSpK2WCaZfUyteXANRh4hvz2fNgPZbGVM3viXty6F3i0ucSnW0GSMrum9bCXMzOCUiiekkvj7y',
  'Content-Type': 'application/json'
}
conn.request("POST", "/rest/AliceBlueAPIService/api/chart/history", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))