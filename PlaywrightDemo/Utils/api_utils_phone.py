from http.client import responses

from playwright.sync_api import Playwright


login_payload = {"userEmail":"bhavesh.rana@mail.com","userPassword":"Bhavesh@8238"}
order_payload = {"orders":[{"country":"India","productOrderedId":"67a8df56c0d3e6622a297ccd"}]}

class APIUtils_Phone:

     def getTokem(self,playwright : Playwright):

         api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
         response = api_request_context.post(url="/api/ecom/auth/login",
                                             data=login_payload,
                                             headers={
                                                 "Content-Type" : "application/json"
                                             })

         response_body = response.json()
         token = response_body["token"]
         return token

     def createOrder(self,playwright : Playwright):
         token = self.getTokem(playwright)

         api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
         response_body = api_request_context.post(url="/api/ecom/order/create-order",
                                             data= order_payload,
                                             headers={
                                             "Authorization": token,
                                             "Content-Type": "application/json"
                                             })
         response = response_body.json()
         print(response)
         order_id = response["orders"][0]
         return order_id