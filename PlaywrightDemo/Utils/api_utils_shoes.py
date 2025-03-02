from playwright.sync_api import Playwright

login_payload = {"userEmail":"bhavesh.rana@mail.com","userPassword":"Bhavesh@8238"}
shoes_order_payload ={"orders":[{"country":"India","productOrderedId":"67a8df1ac0d3e6622a297ccb"}]}
class APIUtils_Shoes:


    def getToken(self,playwright : Playwright):
        api_response_body = playwright.request.new_context(base_url= "https://rahulshettyacademy.com")
        response = api_response_body.post(url="/api/ecom/auth/login",
                                               data=login_payload,
                                               headers={
                                                   "Content-Type" : "application/json"
                                               })
        assert response.ok
        print(response.json())
        response_body = response.json()
        token = response_body["token"]
        return token

    def createShoesOrder(self,playwright : Playwright):
        token = self.getToken(playwright)
        api_response_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response_body = api_response_context.post(url="/api/ecom/order/create-order",
                                                  data = shoes_order_payload,
                                                  headers={
                                                      "Authorization" : token,
                                                      "Content-Type" : "application/json"
                                                  })
        response = response_body.json()
        print(response)
        order_id = response["orders"][0]
        return order_id
