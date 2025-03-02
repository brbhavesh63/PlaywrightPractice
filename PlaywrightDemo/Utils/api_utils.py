from playwright.sync_api import Playwright
order_payload = {"orders":[{"country":"India","productOrderedId":"67a8dde5c0d3e6622a297cc8"}]}
login_payload = {"userEmail":"bhavesh.rana@mail.com","userPassword":"Bhavesh@8238"}

class APIUtils:

    def GetToken(self,playwright : Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post(url="/api/ecom/auth/login",
                                            data=login_payload)
        assert response.ok
        print(response.json())
        responseBody = response.json()
        return responseBody["token"]


    def CreateOrder(self,playwright : Playwright):
        token = self.GetToken(playwright)

        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post(url="/api/ecom/order/create-order",
                                            data=order_payload,
                                            headers={"Authorization":token,
                                                     "Content-Type" : "application/json",
                                                     })
        print(response.json())
        response_body = response.json()
        order_id = response_body["orders"][0]
        return order_id