
from selenium.webdriver.common.by import By

class Locators():

    # --------- HOME -----------

    PAGE_TITLE = (By.CLASS_NAME, "page-title")
    MOBILE_LINK = (By.XPATH,"//*[@id='nav']/ol/li[1]/a")
    HOME_MOBILE_LINK = (By.XPATH,"//*[@id='nav']/ol/li[1]/a")
    HOME_ACCOUNT_BUTTON = (By.XPATH,"//*[@id='header']/div/div[2]/div/a")
    HOME_MYACCOUNT_LINK = (By.XPATH,"//*[@id='header-account']/div/ul/li[1]/a")
    HOME_LOGIN_LINK = (By.XPATH, "//*[@id='header-account']/div/ul/li[6]/a")
    HOME_ADVANCE_SEARCH = (By.XPATH, "//*[@id=\"top\"]/body/div/div/div[3]/div/div[3]/ul/li[3]/a")

    #------------ ADVANCE SEARCH ------------------------------------
    ADVANCESEARCH_PRICE = (By.ID, "price")
    ADVANCESEARCH_PRICETO = (By.ID, "price_to")
    ADVANCESEARCH_SEARCH_BUTTON = (By.XPATH, "//*[@id=\"form-validate\"]/div[2]/button")

    #------------- ADVANCE SEARCH RESULTS-----------------------------
    ADVANCESEARCH_PRODUCT_NAME = (By.CLASS_NAME, "product-name")
    ADVANCESEARCH_PRODUCT_PRICE = (By.CLASS_NAME, "price-box")
    ADVANCESEARCH_MODIFYYOURSEARCH_LINK = (By.LINK_TEXT, "Modify your search")



    #------------ LOGIN BACK ------------------------------
    LOGINBACK_USERNAME_INPUT = (By.ID, "username")
    LOGINBACK_PASSWORD_INPUT = (By.ID, "login")
    LOGINBACK_LOGIN_BUTTON = (By.XPATH, "//*[@id=\"loginForm\"]/div/div[5]/input")

    #---------- REVIEW PAGE ----------------------------------------
    REVIEWPAGE_REVIEW_FIELD = (By.ID, "review_field")
    REVIEWPAGE_SUMMARY_FIELD = (By.ID, "summary_field")
    REVIEWPAGE_NICKNAME_FIELD = (By.ID, "nickname_field")
    REVIEWPAGE_SUBMIT_BUTTON = (By.XPATH, "//*[@id=\"review-form\"]/div[2]/button")


    #--------------- CUSTOMERS BACK --------------------------------
    CUSTOMERSBACK_CLOSEALERT = (By.XPATH, "//*[@id=\"message-popup-window\"]/div[1]/a")
    CUSTOMERSBACK_SALES_LINK = (By.XPATH, "//*[@id=\"nav\"]/li[1]/a")
    CUSTOMERSBACK_INVOICES_LINK = (By.XPATH, "//*[@id=\"nav\"]/li[1]/ul/li[2]/a")
    CUSTOMERSBACK_ORDERS_LINK = (By.XPATH, "//*[@id=\"nav\"]/li[1]/ul/li[1]/a")
    CUSTOMERSBACK_CATALOG_LINK = (By.XPATH, "//*[@id=\"nav\"]/li[2]/a")
    CUSTOMERSBACK_REVIEWS_AND_RATINGS = (By.XPATH, "//*[@id=\"nav\"]/li[2]/ul/li/a")
    CUSTOMERSBACK_CUSTOMER_REVIEWS = (By.XPATH, "//*[@id=\"nav\"]/li[2]/ul/li/ul/li[1]/a")
    CUSTOMERSBACK_PENDING_REVIEWS = (By.XPATH, "//*[@id=\"nav\"]/li[2]/ul/li/ul/li[1]/ul/li[1]/a")
    CUSTOMERSBACK_CUSTOMERS_LINK = (By.XPATH, "//*[@id=\"nav\"]/li[3]/a")
    CUSTOMERSBACK_MANAGECUSTOMERS_LINK = (By.XPATH, "//*[@id=\"nav\"]/li[3]/ul/li/a")


    #------------ MANAGE CUSTOMERS BACK ----------------------------------
    MANAGECUSTOMERSBACK_FIRSTEDIT = (By.XPATH, "//*[@id=\"customerGrid_table\"]/tbody/tr[1]/td[11]/a")

    #------------- CUSTOMER INFO BACK ----------------------------------
    CUSTOMERINFOBACK_ACCOUNT_INFORMATION = (By.LINK_TEXT, "Account Information")
    CUSTOMERINFOBACK_WEBSITEASSOCIATED = (By.ID, "_accountwebsite_id")
    CUSTOMERINFOBACK_CREATED_FROM = (By.ID, "_accountcreated_in")
    CUSTOMERINFOBACK_NEWPASS = (By.ID, "_accountnew_password")

    #---------------- PENDING REVIEWS BACK ---------------------------------
    PENDINGREVIEWSBACK_REVIEW_ID = (By.NAME, "review_id")
    PENDINGREVIEWSBACK_CHECK_REVIEWS = (By.NAME, "reviews")
    PENDINGREVIEWSBACK_EDIT_LINK = (By.LINK_TEXT, "Edit")


    #------------------- INVOICES BACK ------------------------------------------
    INVOICESBACK_INVOICE_DATE = (By.NAME, "created_at")
    INVOICESBACK_DATE_FIRST_ROW = (By.XPATH, "/html/body/div[1]/div[4]/div/div[3]/div/div[2]/div/table/tbody/tr[1]/td[3]")



    #--------------- EDIT REVIEW BACK --------------------------------
    EDITREVIEWBACK_STATUS = (By.ID, "status_id")
    EDITREVIEWBACK_SAVE_REVIEW = (By.ID, "save_button")

    #------------ ORDERS BACK --------------------------------------
    ORDERSBACK_FORMAT_SELECTOR = (By.ID, "sales_order_grid_export")
    ORDERSBACK_EXPORT_BUTTON = (By.XPATH, "/html/body/div[1]/div[4]/div/div[3]/div/table/tbody/tr/td[2]/button")
    ORDERSBACK_STATUS_SELECTOR = (By.ID, "sales_order_grid_filter_status")
    ORDERSBACK_SEARCH_BUTTON = (By.XPATH, "/html/body/div[1]/div[4]/div/div[3]/div/table/tbody/tr/td[3]/button[2]")
    ORDERSBACK_ORDERS_CHECKBOX = (By.NAME, "order_ids")
    ORDERSBACK_ACTIONS_SELECTOR = (By.ID, "sales_order_grid_massaction-select")
    ORDERSBACK_SUBMIT_BUTTON = (By.XPATH, "/html/body/div[1]/div[4]/div/div[3]/div/div[1]/table/tbody/tr/td[2]/div/div[1]/form/fieldset/span[4]/button")
    ORDERSBACK_MSGS = (By.ID, "messages")


    # ----------- MOBILE --------------------------
    MOBILE_PAGE_TITLE = (By.CSS_SELECTOR,".category-title")
    DROPDOWN = (By.XPATH,"//*[@id='top']/body/div/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[1]/div/select")
    PRODUCT_NAME = (By.CLASS_NAME,"product-name")
    MOBILE_PRODUCT_PRICE = (By.ID,"product-price-1")
    MOBILE_IMAGE_XPERIA = (By.ID,"product-collection-image-1")
    MOBILE_ADDTOCART_XPERIA = (By.XPATH,"//*[@id='top']/body/div/div/div[2]/div/div[2]/div[1]/div[3]/ul/li[1]/div/div[3]/button")
    MOBILE_ADDTOCART_IPHONE = (By.XPATH, "//*[@id=\"top\"]/body/div/div/div[2]/div/div[2]/div[1]/div[3]/ul/li[2]/div/div[3]/button")
    MOBILE_ADDTOCOMPARE_XPERIA = (By.XPATH,"//*[@id='top']/body/div/div/div[2]/div/div[2]/div[1]/div[3]/ul/li[1]/div/div[3]/ul/li[2]/a")
    MOBILE_ADDTOCOMPARE_IPHONE = (By.XPATH,"//*[@id='top']/body/div/div/div[2]/div/div[2]/div[1]/div[3]/ul/li[2]/div/div[3]/ul/li[2]/a")
    MOBILE_COMPARE_BUTTON = (By.CSS_SELECTOR,"body > div > div > div.main-container.col3-layout > div > div.col-right.sidebar > div.block.block-list.block-compare > div.block-content > div > button > span > span")
    MOBILE_REVIEW_TAB= (By.XPATH, "//*[@id=\"top\"]/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/ul/li[2]")
    MOBILE_REVIEW_COMMENT = (By.XPATH, "//*[@id=\"customer-reviews\"]/dl/dt[1]")

    #-------  PRODUCT PAGE MOBILE ---------------
    PP_MOBILE_PRICE = (By.CLASS_NAME,"price")


    #-------- CART -------------------------------

    CART_INPUT_QTY = (By.XPATH,"//*[@id='shopping-cart-table']/tbody/tr/td[4]/input")
    CART_UPDATE_QTY = (By.XPATH,"//*[@id='shopping-cart-table']/tbody/tr/td[4]/button")
    CART_ERROR_MSG = (By.XPATH,"//*[@id='shopping-cart-table']/tbody/tr/td[2]/p")
    CART_EMPTYCART_BUTTON = (By.ID,"empty_cart_button")
    CART_EMPTYCART_MST = (By.XPATH,"//*[@id='top']/body/div/div/div[2]/div/div/div[1]/h1")
    CART_COUNTRY_SELECTOR = (By.ID, "country")
    CART_REGION_SELECTOR = (By.ID, "region_id")
    CART_ZIPCODE_INPUT = (By.ID, "postcode")
    CART_ESTIMATE_LINK = (By.ID, "//*[@id='shipping-zip-form']/div/button")
    CART_RATE_RADIO = (By.XPATH, "s_method_flatrate_flatrate")
    CART_SHIPPINGCOST = (By.XPATH, "//*[@id='co-shipping-method-form']/dl/dd/ul/li/label/span")
    CART_UPDATETOTAL_BUTTON = (By.XPATH, "//*[@id=\"co-shipping-method-form\"]/div/button")
    CART_SUBTOTAL = (By.XPATH, "//*[@id=\"shopping-cart-totals-table\"]/tbody/tr[1]/td[2]/span")
    CART_GRANDTOTAL = (By.XPATH, "//*[@id=\"shopping-cart-totals-table\"]/tfoot/tr/td[2]/strong/span")
    CART_PROCEEDTOCHECKOUT_BUTTON = (By.XPATH, "//*[@id=\"top\"]/body/div/div/div[2]/div/div/div/div[3]/div/ul/li[1]/button")
    CART_COUPONCODE_INPUT = (By.ID, "coupon_code")
    CART_APPLYCOUPON_BUTTON = (By.XPATH, "//*[@id=\"discount-coupon-form\"]/div/div/div/div/button")
    CART_COUPON_DISCOUNT = (By.XPATH, "//*[@id=\"shopping-cart-totals-table\"]/tbody/tr[2]/td[2]")



    #--------- CHECKOUT ----------------------------------------------

    CHECKOUT_FIRSTNAME = (By.ID, "billing:firstname")
    CHECKOUT_LASTNAME = (By.ID, "billing:lastname")
    CHECKOUT_ADDRESS = (By.ID, "billing:street1")
    CHECKOUT_CITY = (By.ID, "billing:city")
    CHECKOUT_REGION = (By.ID, "billing:region_id")
    CHECKOUT_ZIP = (By.ID, "billing:postcode")
    CHECKOUT_TELEPHONE = (By.ID, "billing:telephone")
    CHECKOUT_BILLINGINFO_CONTINUEBUTTON = (By.XPATH, "//*[@id=\"billing-buttons-container\"]/button")
    CHECKOUT_SHIPPINGMETHOD_CONTINUEBUTTON = (By.XPATH, "//*[@id=\"shipping-method-buttons-container\"]/button")
    CHECKOUT_CHECKMONEY_RADIO = (By.ID, "p_method_checkmo")
    CHECKOUT_PAYMENTINFORMATION_CONTINUEBUTTON = (By.XPATH, "//*[@id=\"payment-buttons-container\"]/button")
    CHECKOUT_PLACEORDER = (By.XPATH, "//*[@id=\"review-buttons-container\"]/button")





    #---------- LOGIN ----------------------------------------------

    LOGIN_CREATEACCOUNT_BUTTON = (By.XPATH,"//*[@id='login-form']/div/div[1]/div[2]/a")
    LOGIN_EMAIL = (By.ID, "email")
    LOGIN_PASSWORD = (By.ID, "pass")
    LOGIN_LOGIN_BUTTON = (By.ID, "send2")


    #-------- CREATE ACCOUNT ------------------------------
    CREATEACCOUNT_FIRSTNAME = (By.ID,"firstname")
    CREATEACCOUNT_MIDDLENAME = (By.ID,"middlename")
    CREATEACCOUNT_LASTNAME = (By.ID,"lastname")
    CREATEACCOUNT_EMAIL = (By.ID,"email_address")
    CREATEACCOUNT_PASSWORD = (By.ID,"password")
    CREATEACCOUNT_CONFIRMPASSWORD = (By.ID,"confirmation")
    CREATEACCOUNT_REGISTER_BUTTON = (By.XPATH,"//*[@id='form-validate']/div[2]/button")

    #---------- ACCOUNT -----------------------------------------
    ACCOUNT_MSG = (By.XPATH,"//*[@id='top']/body/div/div/div[2]/div/div[2]/div/div/ul/li/ul/li/span")
    ACCOUNT_TV_LINK =(By.XPATH,"//*[@id='nav']/ol/li[2]")
    ACCOUNT_MYWISHLIST_LINK = (By.XPATH, "//*[@id='top']/body/div/div/div[2]/div/div[1]/div/div[2]/ul/li[8]/a")
    ACCOUNT_MYORDERS_LINK = (By.XPATH, "//*[@id=\"top\"]/body/div/div/div[2]/div/div[1]/div/div[2]/ul/li[4]/a")
    ACCOUNT_REORDER_LINK = (By.XPATH, "//*[@id=\"my-orders-table\"]/tbody/tr/td[6]/span/a[2]")

    #---------------- TV -----------------------------------------
    TV_WISHLIST_LGLCD_LINK = (By.XPATH,"//*[@id='top']/body/div/div/div[2]/div/div[2]/div[1]/div[2]/ul/li[1]/div/div[3]/ul/li[1]/a")


    #------------ MY WISHLIST --------------------------------------
    MYWISHLIST_SHAREWISHLIST_BUTTON = (By.NAME, "save_and_share")
    MYWISHLIST_MSG = (By.XPATH, "//*[@id='top']/body/div/div/div[2]/div/div[2]/div/div[1]/ul/li/ul/li/span")
    MYWISHLIST_ADDTOCART_BUTTON = (By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div/div[1]/form[1]/div/table/tbody/tr/td[5]/div/button")



    #----------- MY ORDERS  ----------------------------------------------

    MYORDERS_VIEWORDER_LINK = (By.XPATH, "//*[@id=\"my-orders-table\"]/tbody/tr/td[6]/span/a[1]")
    MYORDERS_FIRSTORDER = (By.XPATH, "//*[@id=\"my-orders-table\"]/tbody/tr/td[1]")
    MYORDERS_STATUSFIRSTORDER = (By.XPATH, "//*[@id=\"my-orders-table\"]/tbody/tr/td[5]/em")




    #----------- ORDER PAGE -----------------------------------

    ORDERPAGE_PRINTORDER_LINK = (By.XPATH, "//*[@id=\"top\"]/body/div/div/div[2]/div/div[2]/div/div[1]/a[2]")

    # ------------- SHARE YOUR WISHLIST -----------------------------
    SHAREWISHLIST_EMAIL = (By.ID, "email_address")
    SHAREWISHLIST_BUTTON = (By.XPATH, "//*[@id='form-validate']/div[2]/button")




    #------------ THANK YOU PAGE ----------------------------------------
    THANKYPAGE_ORDERNUMBER = (By.XPATH, "//*[@id=\"top\"]/body/div/div/div[2]/div/div/p[1]/a")
    THANKYPAGE_MSG = (By.TAG_NAME, "h1")