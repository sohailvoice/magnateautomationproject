
import time
import pytest

from PageObjects.LoginPage import LoginPage
from PageObjects.DashboardPage import DashboardPage
from PageObjects.stock import StockTransferPage
import global_funcations1

@pytest.mark.usefixtures("setup")
class TestStockTransfer:
    stock_transfter_qty=int(10)
    source_warehouse="Lahore"
    destionation_warehouse="RYK Store"
    product_name="Product 786"
    def test_001(self, setup):
        lg = LoginPage(self.driver)
        db = DashboardPage(self.driver)
        time.sleep(1)
        # Enter username
        lg.input_user("sohail.914")
        time.sleep(1)
        # Enter password
        lg.input_password("sohail@914")
        time.sleep(1)
        # click login button
        lg.login_button()
        time.sleep(2)
        print("Login successfully")
        time.sleep(2)

        assert self.driver.current_url == "http://xsmacc7cloudx.dyndns.org:84/dashboard"

    def test_go_Stock_transfer_page(self):
        # Navigate to the stock transfer page
        global_funcations1.click_button(self.driver, "/html[1]/body[1]/smacc-layouts[1]/div[1]/smacc-sidebar[1]/div[1]/div[2]/div[1]/ul[1]/li[5]/button[1]/i[1]")
        time.sleep(2)
        global_funcations1.click_button(self.driver, "//button[normalize-space()='Stock']")
        time.sleep(2)
        global_funcations1.click_button(self.driver, "//button[normalize-space()='Stock Transfer']")
        time.sleep(2)

    def test_create_stock_transfer(self):
        stock_transfer = StockTransferPage(self.driver)

        # Click the 'New' button to initiate a stock transfer
        global_funcations1.click_button(self.driver, "//span[normalize-space()='New']")
        time.sleep(1)
        # stock_transfer.calendar_date()

        # Select the source location by passing only the location name
        check1=stock_transfer.select_source_location(self.source_warehouse)
        time.sleep(1)
        # Select destination location
        check2=stock_transfer.select_destination_location(self.destionation_warehouse)
        if check1 == check2:
            print("Source Warehouse & Destionation Warehouse are same Please use Different warehouse")
        time.sleep(1)
        # stock_transfer.scroll_by(0, 500)
        # Enter item and quantity
        stock_transfer.enter_item(self.product_name)
        time.sleep(2)
        stock_transfer.enter_quantity(self.stock_transfter_qty)
        time.sleep(1)
        # click pluls icon
        stock_transfer.click_plus_icon()
        stock_transfer.enter_item2(self.product_name)
        time.sleep(2)
        stock_transfer.enter_quantity2(self.stock_transfter_qty)
        time.sleep(1)

        time.sleep(1)
        price_value=stock_transfer.get_price_value()
        # split string value
        numeric_price = float(price_value.split()[0])

        amount = numeric_price * self.stock_transfter_qty
        # Calculate the amount
        print(f"Total Amount: {amount}")  #


        tttt=stock_transfer.get_success_stock()
        avalible_stock = float(price_value.split()[0])
        # print(f"Avalibile Stock value get : {avalible_stock}")
        if self.stock_transfter_qty >= avalible_stock:
         print(f"Stock transfer quantity {self.stock_transfter_qty} is greater than or equal to {tttt}")
        else:
          print(f"Stock transfer quantity {self.stock_transfter_qty} is less than {tttt}")
        time.sleep(2)
        stock_transfer.click_space()

        stock_transfer.click_transfer()
        time.sleep(2)


        time.sleep(2)
        # assert stock_transfer.get_stock_transfter_number().is_displayed(), "Element is not visible after scrolling."
        document_number=stock_transfer.get_stock_transfter_number()
        # print(f"Document Number is : {document_number} type: {type(document_number)}")
        time.sleep(5)
        # click Transaction icon on view page
        stock_transfer.scrol_view()
        time.sleep(5)
        # get debit value
        debit_amount=stock_transfer.get_debit_value()
        print(f"Debit Value is : {debit_amount}")
        # get Credit value
        credit_amount = stock_transfer.get_debit_value()
        print(f"Credit Value is : {credit_amount}")
        # assert debit_amount == credit_amount, f"Debit ({debit_amount}) and Credit ({credit_amount}) values do not match!"
        if debit_amount == credit_amount:
            print("Debit or Credit Value are Equal ")
        else:
            print("Debit or Credit value Not equal")





        # ttt1=stock_transfer.get_stock_transfter_number()
        # print("Transation icon value : ",ttt1)
        # time.sleep(5)
        # time.sleep(5)
        # stock_transfer.scroll_down(500)
        # time.sleep(5)



    # def test_go_to_transaction_viewer_page(self):
    #
    #
    #     stock_transanctionPage=TransactionVewPage(self.driver)
    #     stock_transanctionPage.click_financial_module()
    #     time.sleep(5)
    #     stock_transanctionPage.click_search()
    #     # click transaction module Under finanace
    #     stock_transanctionPage.click_transaction_icon()
    #     time.sleep(5)
    #     # click transaction view page
    #     stock_transanctionPage.click_transaction_page()
    #     # click Fianancial Account
    #     stock_transanctionPage.click_transaction_account_page()
    #     stock_transanctionPage.click_last_document()





