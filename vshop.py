import calendar
import datetime
import random


def is_valid_phone(phone):
   phone_str = str(phone)
   return phone_str.isdigit() and len(phone_str) == 10


def verify_otp(otp, generated_otp):
   return otp == generated_otp

def address():
   print("Address:--")
   print("1.Your current location\n2.Add new location")
   add=int(input("Your choice="))
   if add==1:
      add1="Location = <<<<VIT BHOPAL UNIVERSITY>>>>"
      print(add1)
   else:
      add1=input("Enter your  delivery address = ")

def delivery():
   print("\nWith this cart you got free  delivery😃")
   input("\npress enter for proceed to pay")
   print("OOPS!!😞 \n\t Online payment mode is not avaliable!!\n\n Only Cash On  delivery is avaliable")
   input("\nPress enter to confirm order in COD mode ")
   print("\n\t\t\t Congrats 💖 Your Order is placed ")
   delivery_time = datetime.datetime.now() + datetime.timedelta(
   seconds=random.randint(1, 30 * 24 * 60 * 60))
   print("Delivery will be done by", delivery_time.strftime("%A, %d %B %Y at %I:%M %p"))
   print("\n\n  delivery will be done by ")
   return ""


def show_receipt(shopped, spend):
   print("Your purchase(s):--")
   current_time = datetime.datetime.now()
   weekday = calendar.day_name[current_time.weekday()]
   print("Date and time:", weekday, current_time.strftime("%Y-%m-%d %H:%M:%S"))
   for item in shopped:
      print("\n", item, "\n")

   cost = 0
   for price in spend:
      cost += price
   print("\nTotal spend = ", cost)
   print("\n\n\n                      .............Thank you for shopping from V-SHOP!...........")



print("                                  ............WELCOME TO V-shop.......... \n\n\n      ")
name=input("Enter your name= ")
phone=int(input("Enter your phone no.="))
if is_valid_phone(phone):
  p=str(phone)
  generated_otp = random.randint(1000, 9999)
  print(f"OTP has been sent to your mobile no.=XXXXXXX{p[-3::1]}")
  print(f"                                    otp={generated_otp}")
  otp=int(input("Enter otp="))
  if verify_otp(otp, generated_otp):
      shopped = []
      spend = []
      print(address())
      while True:
         print(f"Hello, dear coustomer {name}\n\t Welcome to V-Shop")
         print("\n\n  !!!FIND WHAT YOU LOVE💕,\n         LOVE WHAT YOU FIND🎀🎁!!!")
         print("Products:---")
         print("1.CLOTHES👚\n2.HAIR CARE🧴\n3.BODYCARE🧼 \n4.FOOTWEAR👟\n")
         item = None; rate = None; product=int(input("Enter your preference:--"))
         if product==1:
            print("1.Female\n2.Male\n3.Childern")
            type=int(input("Enter your choice:--"))
            if type==1:
               print("1.XS\n2.S\n3.M\n4.L\n5.XL\n6.XXL")
               size=int(input("Enter your size :--"))
               print("\n1.Dresses\n2.Kurties\n3.Bottom Wear\n4.Tops & T-shirts")
               choice=int(input("Enter your favorite wear:--"))
               if choice==1:
                  print("\n1.Sage Meadow Dress in Green Botanical Print\t~₹3,299")
                  print("\n2.Women's Orange Georgette Floral Printed Tiered Dress\t~₹800")
                  print("\n3.Women's Pink Bandhani Print Tiered Maxi Dress\t~₹409")
                  cart=int(input("Add the item to cart="))
                  if cart==1:
                    print("Your cart value is :-- ₹3,299\n")
                    print(delivery())
                    item="Sage Meadow Dress in Green Botanical Print \t~₹3,299"
                    rate=3299
                  elif cart==2:
                    print("Your cart value= ₹800")
                    print(delivery())
                    item="Women's Orange Georgette Floral Printed Tiered Dress \t~₹800"
                    rate=800
                  elif cart==3:
                    print("Your cart value =₹409")
                    print(delivery())
                    item="Women's Pink Bandhani Print Tiered Maxi Dress \t~₹409"
                    rate=409
                  else:
                   print("\nOOPS!!😞 No Data Found!!!")
               elif choice==2:
                  print("\n\n1.Kritika Women Floral Print Straight Kurti (Black)\t~ ₹273") 
                  print("\n2.Anouk Women Printed Sequinned Kurta \t~ ₹388")   
                  print ("\n3.Kimakshi Women Cotton Blend Embroidered Straight Kurti (Brown)\t ~ ₹500")
                  cart=int(input("Add the item to cart="))
                  if cart==1:
                    print("\nYour cart value is :-- ₹273")
                    print(delivery())
                    item="Kritika Women Floral Print Straight Kurti (Black)\t~ ₹273"
                    rate=273

                  elif cart==2:
                    print("\nYour cart value= ₹388")
                    print(delivery())
                    item="Anouk Women Printed Sequinned Kurta  \t~ ₹388"
                    rate=388
                  elif cart==3:
                    print("Your cart value =₹500")
                    print(delivery())
                    item="Kimakshi Women Cotton Blend Embroidered Straight Kurti (Brown) \t ~ ₹500"
                    rate=500

                  else:
                     print("\nOOPS!!😞 No Data Found!!!")
               elif choice==3:
                  print("\n\n1.Cotton Blend Ladies Trousers | Versatile & Soft | Perfect for Work & Casual Outings (Beige)\t~₹279")
                  print("\n2.Nermosa High-Waist Korean Trousers with Wide Baggy Fit (Brown) \t~₹499")
                  print("\n3.Nifty Women's Denim Strechable High Waist Baggy Jeans for Women \t~₹729")
                  cart=int(input("Add the item to cart="))
                  if cart==1:
                     print("Your cart value is :-- ₹279")
                     print(delivery())
                     item="Cotton Blend Ladies Trousers | Versatile & Soft | Perfect for Work & Casual Outings (Beige) \t~₹279"
                     rate=279

                  elif cart==2:
                     print("Your cart value= ₹499")
                     print(delivery())
                     item="Nermosa High-Waist Korean Trousers with Wide Baggy Fit (Brown)  \t~₹499"
                     rate=499

                  elif cart==3:
                     print("Your cart value =₹729")
                     print(delivery())
                     item="Nifty Women's Denim Strechable High Waist Baggy Jeans for Women \t~₹729"
                     rate=729
                  else:
                     print("\nOOPS!!😞 No Data Found!!!")                
               elif choice==4:
                  print("\n\n1. Vintage Graphic Print Halter Neck Fitted Top in Coffee Brown \t~ ₹499") 
                  print("\n2. Brown Round Neck Peplum Top \t~ ₹849")   
                  print ("\n3. Floral Printed Square Neck Fitted Top \t ~ ₹367")
                  cart=int(input("Add the item to cart="))
                  if cart==1:
                     print("Your cart value is :-- ₹499")
                     print(delivery())
                     item="Vintage Graphic Print Halter Neck Fitted Top in Coffee Brown \t~ ₹499"
                     rate=499

                  elif cart==2:
                     print("Your cart value= ₹849")
                     print(delivery())
                     item="Brown Round Neck Peplum Top \t~ ₹849"
                     rate=849

                  elif cart==3:
                     print("Your cart value =₹367")
                     print(delivery())
                     item="Floral Printed Square Neck Fitted Top \t ~ ₹367"
                     rate=367

                  else:
                      print("\nOOPS!!😞 No Data Found!!!")
            elif type==2:
               print("1.38\n2.40\n3.42\n4.44")
               size=int(input("Enter your size:--"))
               print("\n1.Gym Wear\n2.T-shirts\n3.Kurta\n4.Jeans\n5.Shirts\n")
               choice=int(input("Enter your favourite wear="))
               if choice==1:
                 print("\n1.Tank Tops Sleevless T-Shirt for Gym Wear Vest Solid Stylish Round Neck \t~₹199")
                 print("\n2.Nicky Boy Graphic Print Men Track Suit\t~₹437")
                 print("\n3.Jugular Men's Cotton Blend Track Suit\t~₹449")
                 cart=int(input("Add the item to cart="))
                 if cart==1:
                    print("Your cart value is :-- ₹199")
                    print(delivery())
                    item="Tank Tops Sleevless T-Shirt for Gym Wear Vest Solid Stylish Round Neck \t~₹199"
                    rate=199

                 elif cart==2:
                    print("Your cart value= ₹437")
                    print(delivery())
                    item="Nicky Boy Graphic Print Men Track Suit \t~₹437"
                    rate=437

                 elif cart==3:
                    print("Your cart value =₹449")
                    print(delivery())
                    item="Jugular Men's Cotton Blend Track Suit \t~₹449"
                    rate=449

                 else:
                    print("\nOOPS!!😞 No Data Found!!!")

               elif choice==2:
                 print("\n1.Jump cuts || Polo Tshirts for Men ||Polo Neck \t~₹319")
                 print("\n2.Black Panther Typography Printed Relaxed Fit Drop-Shoulder Sleeves T-Shirt \t~215")
                 print("\n3.VeBNor Men Mandarin Collar Pockets T-shirt \t~₹333")
                 cart=int(input("Add the item to cart="))
                 if cart==1:
                    print("Your cart value is :-- ₹319")
                    print(delivery())
                    item="Jump cuts || Polo Tshirts for Men ||Polo Neck \t~₹319"
                    rate=319

                 elif cart==2:
                    print("Your cart value= ₹215")
                    print(delivery())
                    item="Black Panther Typography Printed Relaxed Fit Drop-Shoulder Sleeves T-Shirt \t~215"
                    rate=215

                 elif cart==3:
                    print("Your cart value =₹333")
                    print(delivery())
                    item="VeBNor Men Mandarin Collar Pockets T-shirt \t~₹333"
                    rate=333

                 else:
                    print("\nOOPS!!😞 No Data Found!!!")
               elif choice==3:
                 print("\n1.SHOPYCLICK Men Printed Straight Kurta(White) \t~₹398")
                 print("\n2.DEELMO Mens's Cottoon Blend Mandarin Collar Self One Design Full Sleeve Casual Short Kurta\t~₹457")
                 print("\n3.FUBAR Men Geometric Embroidered Straight Kurta \t~₹491")
                 cart=int(input("Add the item to cart="))
                 if cart==1:
                    print("Your cart value is :-- ₹398")
                    print(delivery())
                    item="SHOPYCLICK Men Printed Straight Kurta(White) \t~₹398"
                    rate=398

                 elif cart==2:
                    print("Your cart value= ₹457")
                    print(delivery())
                    item="DEELMO Mens's Cottoon Blend Mandarin Collar Self One Design Full Sleeve Casual Short Kurta \t~₹457"
                    rate=457

                 elif cart==3:
                    print("Your cart value =₹491")
                    print(delivery())
                    item="FUBAR Men Geometric Embroidered Straight Kurta \t~₹491"
                    rate=491

                 else:
                    print("\nOOPS!!😞 No Data Found!!!")
                
               elif choice==4:
                 print("\n1.EVERFADE Men Straight Fit Mid-Rise Light Fade Jeans \t~₹447")
                 print("\n2.KOTTY Regular Men Grey Jeans\t~₹467")
                 print("\n3.Wanted Men Regular Fit Mid Rise Stretchable Jeans \t~₹599")
                 cart=int(input("Add the item to cart="))
                 if cart==1:
                    print("Your cart value is :-- ₹447")
                    print(delivery())
                    item="EVERFADE Men Straight Fit Mid-Rise Light Fade Jeans \t~₹447"
                    rate=447

                 elif cart==2:
                    print("Your cart value= ₹467")
                    print(delivery())
                    item="KOTTY Regular Men Grey Jeans \t~₹467"
                    rate=467

                 elif cart==3:
                    print("Your cart value =₹599")
                    print(delivery())
                    item="Wanted Men Regular Fit Mid Rise Stretchable Jeans \t~₹599"
                    rate=599

                 else:
                    print("\nOOPS!!😞 No Data Found!!!")
                
               elif choice==5:
                 print("\n1.Men Straight Striped Casual Shirt \t~₹399")
                 print("\n2.Men Colourblocked Polo Collar Slim Fit T-shirt\t~₹287")
                 print("\n3.Pure Cotton Mandrain Collar Thread Work Short Kurta\t~₹645")
                 cart=int(input("Add the item to cart="))
                 if cart==1:
                    print("Your cart value is :-- ₹399")
                    print(delivery())
                    item="Men Straight Striped Casual Shirt \t~₹399"
                    rate=399

                 elif cart==2:
                    print("Your cart value= ₹287")
                    print(delivery())
                    item="Men Colourblocked Polo Collar Slim Fit T-shirt \t~₹287"
                    rate=287

                 elif cart==3:
                    print("Your cart value =₹645")
                    print(delivery())
                    item="Pure Cotton Mandrain Collar Thread Work Short Kurta \t~₹645"
                    rate=645

                 else:
                    print("\nOOPS!!😞 No Data Found!!!")
            elif type==3:
               print("\n1.0-2 years\n2.2-4 years\n3.4-6 years\n4.6-8 years\n5.8-10 years")
               age=int(input("Enter your child's age range :--"))
               print("\n1.Girls\n2.Boys")
               gender=int(input("Enter your choice:--"))   
               if gender==1:
                  print("\n1.Frocks\n2.Tops & T-shirts\n3.Bottom Wear\n4.Dresses")
                  wear=int(input("Enter your favorite wear:--"))
                  if wear==1:
                    print("\n1.Baby Girl Cotton Floral Frock (Yellow) \t~₹299")
                    print("\n2.Zisba dresses Baby Girls Midi/Knee Length Party Dress  \t~₹500")
                    print("\n3.Mehek Cotton Blend Frock For Girls(Blue)  \t~₹490")
                    cart=int(input("Add the item to cart="))
                    if cart==1:
                       print("Your cart value is :-- ₹299")
                       print(delivery())
                       item="Baby Girl Cotton Floral Frock (Yellow)\t~₹299"
                       rate=299
                    elif cart==2:
                       print("Your cart value= ₹500")
                       print(delivery())
                       item="Zisba dresses Baby Girls Midi/Knee Length Party Dress  \t~₹500"
                       rate=500
                    elif cart==3:
                       print("Your cart value =₹490")
                       print(delivery()) 
                       item="Mehek Cotton Blend Frock For Girls(Blue)  \t~₹490"
                       rate=490          
                    else:
                       print("\nOOPS!!😞 No Data Found!!!")

                  elif wear==2:
                    print("\n1.FOREVER FRIDAY Girls Graphic Embroidered Regular Top \t~₹512")
                    print("\n2.Square Neck Floral Tie Strap Sleeveless Crop Top \t~₹499")
                    print("\n3.Bow Gauze Top \t~₹756")
                    cart=int(input("Add the item to cart="))
                    if cart==1:
                       print("Your cart value is :-- ₹512")
                       print(delivery())
                       item="FOREVER FRIDAY Girls Graphic Embroidered Regular Top \t~₹512"
                       rate=512
                    elif cart==2:
                       print("Your cart value= ₹499")
                       print(delivery())
                       item="Square Neck Floral Tie Strap Sleeveless Crop Top \t~₹499"
                       rate=499
                    elif cart==3:
                       print("Your cart value =₹756")
                       print(delivery())
                       item="Bow Gauze Top \t~₹756"
                       rate=756
                    else:
                       print("\nOOPS!!😞 No Data Found!!!")

                  elif wear==3:
                    print("\n1.Bow Applique Laced Hem Jeans \t~₹599")
                    print("\n2.Capri For Girls Casual Solid Denim  \t~₹400")
                    print("\n3.Butterfly Applique Denim Shorts \t~₹500")
                    cart=int(input("Add the item to cart="))
                    if cart==1:
                       print("Your cart value is :-- ₹599")
                       print(delivery())
                       item="Bow Applique Laced Hem Jeans  \t~₹599"
                       rate=599
                    elif cart==2:
                       print("Your cart value= ₹400")
                       print(delivery())
                       item="Capri For Girls Casual Solid Denim \t~₹400"
                       rate=400
                    elif cart==3:
                       print("Your cart value =₹500")
                       print(delivery())
                       item="Butterfly Applique Denim Shorts \t~₹500"
                       rate=500
                    else:
                       print("\nOOPS!!😞 No Data Found!!!")
                  elif wear==4:
                    print("\n1.Woven Half Sleeves Bow & Rose Applique Party Dress  \t~₹999")
                    print("\n2.Girls Pink Textured One Shoulder Top with Flared Hem Pants Set  \t~₹859")
                    print("\n3.Girls Pink sleevless Shoulder Strap Ruffles Dress  \t~₹779")
                    cart=int(input("Add the item to cart="))
                    if cart==1:
                       print("Your cart value is :-- ₹999")
                       print(delivery()) 
                       item="Woven Half Sleeves Bow & Rose Applique Party Dress \t~₹999"
                       rate=999
                    elif cart==2:
                       print("Your cart value= ₹859")
                       print(delivery())
                       item="Girls Pink Textured One Shoulder Top with Flared Hem Pants Set \t~₹859"
                       rate=859
                    elif cart==3:
                       print("Your cart value =₹779")
                       print(delivery())
                       item="Girls Pink sleevless Shoulder Strap Ruffles Dress \t~₹779"
                       rate=779
                    else:
                       print("\nOOPS!!😞 No Data Found!!!")
               elif gender==2:
                   print("\n1.Shirts\n2.T-shirts \n3.Bottom Wear\n4.Hoodies and Track Pants")
                   wear=int(input("Enter your favorite wear:--"))
                   if wear==1:
                    print("\n1.HELLCAT Boys Round Neck Printed Blended Cotton Tshirt -Combo Pack of 2  \t~₹300")
                    print("\n2.Rare Ones Kids Printed Casual Shirt  \t~₹649")
                    print("\n3. TAGAS Boys' Shirt|Casual Short Sleeve Shirts for Kids \t~₹349")
                    cart=int(input("Add the item to cart="))
                    if cart==1:
                       print("Your cart value is :-- ₹300")
                       print(delivery())
                       item="HELLCAT Boys Round Neck Printed Blended Cotton Tshirt -Combo Pack of 2  \t~₹300"
                       rate=300
                    elif cart==2:
                       print("Your cart value= ₹649")
                       print(delivery())
                       item="Rare Ones Kids Printed Casual Shirt \t~₹649"
                       rate=649
                    elif cart==3:
                       print("Your cart value =₹349")
                       print(delivery())  
                       item="TAGAS Boys' Shirt|Casual Short Sleeve Shirts for Kids \t~₹349"
                       rate=349         
                    else:
                       print("\nOOPS!!😞 No Data Found!!!")

                   elif wear==2:
                      print("\n1.Marvel Young Boys The Mightiest Cotton T-Shirt \t~₹449")
                      print("\n2.Hellcat Boys Regular Fit Crew-Neck T-Shirt \t~₹220")
                      print("\n3.Boys Oversized Polo T-Shirt | Cotton Blend Half Sleeve Collar Neck Casual & Sports Wear \t~₹299")
                      cart=int(input("Add the item to cart="))
                      if cart==1:
                        print("Your cart value is :-- ₹449")
                        print(delivery())
                        item="Marvel Young Boys The Mightiest Cotton T-Shirt \t~₹449"
                        rate=449
                      elif cart==2:
                         print("Your cart value= ₹220")
                         print(delivery())
                         item="Hellcat Boys Regular Fit Crew-Neck T-Shirt  \t~₹220"
                         rate=220
                      elif cart==3:
                         print("Your cart value =₹299")
                         print(delivery())
                         item="Boys Oversized Polo T-Shirt | Cotton Blend Half Sleeve Collar Neck Casual & Sports Wear \t~₹299"
                         rate=299
                      else:
                         print("\nOOPS!!😞 No Data Found!!!")

                   elif wear==3:
                     print("\n1.Urbano Juniors Boys Slim Jeans \t~₹399")
                     print("\n2.Rare Ones Kids Loet-1 Regular Fit Jeans  \t~₹600")
                     print("\n3.Lymio Junior's Boys Jeans Pant Kids Jeans for Boys \t~₹749")
                     cart=int(input("Add the item to cart="))
                     if cart==1:
                       print("Your cart value is :-- ₹399")
                       print(delivery())
                       item="Urbano Juniors Boys Slim Jeans \t~₹399"
                       rate=399 
                     elif cart==2:
                       print("Your cart value= ₹600")
                       print(delivery())
                       item="Rare Ones Kids Loet-1 Regular Fit Jeans  \t~₹600"
                       rate=600
                     elif cart==3:
                       print("Your cart value =₹749")
                       print(delivery())
                       item="Lymio Junior's Boys Jeans Pant Kids Jeans for Boys \t~₹749"
                       rate=749
                     else:
                       print("\nOOPS!!😞 No Data Found!!!")
                   elif wear==4:
                     print("\n1.Grey & Navy Baby Boy Hoddie and Pants Set  \t~₹234")
                     print("\n2.BAESD Infant Boys Printed Hooded Sweatshirt with Joggers  \t~₹439")
                     print("\n3.Baby Boys Winter Hoodie Tracksuit Set | Fleece Hooded Sweatshirt & Jogger Pant Co-Ord Set \t~₹325")
                     cart=int(input("Add the item to cart="))
                     if cart==1:
                       print("Your cart value is :-- ₹234")
                       print(delivery())
                       item="Grey & Navy Baby Boy Hoddie and Pants Set \t~₹234"
                       rate=234
                     elif cart==2:
                       print("Your cart value= ₹439")
                       print(delivery())
                       item="BAESD Infant Boys Printed Hooded Sweatshirt with Joggers \t~₹439"
                       rate=439
                     elif cart==3:
                       print("Your cart value =₹325")
                       print(delivery())
                       item="Baby Boys Winter Hoodie Tracksuit Set | Fleece Hooded Sweatshirt & Jogger Pant Co-Ord Set \t~₹325"
                       rate=325
                     else:
                       print("\nOOPS!!😞 No Data Found!!!")
               else:
                  print("\nOOPS!!😞 No Data Found!!!")
         elif product==2:
            print("Products:---")
            print("1. Shampoo\n2. Conditioner\n3. Hair Oil\n")
            choice=int(input("Enter your choice="))
            if choice==1:
               print("1.TRESemme Keratin Smooth Shampoo \t~₹170")
               print("2.L'Oreal Paris Moisture Filling Shampoo\t~₹210")
               print("3. Mama Earth Rosemary Hair Fall Control Kit \t~₹510")
               cart=int(input("Add the item to cart="))
               if cart==1:
                  print("Your cart value is :-- ₹170")
                  print(delivery())
                  item="TRESemme Keratin Smooth Shampoo \t~₹170"
                  rate=170
               elif cart==2:
                  print("Your cart value= ₹210")
                  print(delivery())
                  item="L'Oreal Paris Moisture Filling Shampoo \t~₹210"
                  rate=210
               elif cart==3:
                   print("Your cart value =₹510")
                   print(delivery())
                   item="Mama Earth Rosemary Hair Fall Control Kit \t~₹510"
                   rate=510
               else:
                   print("\nOOPS!!😞 No Data Found!!!")
            elif choice==2:
               print("1.L'Oreal Paris Hyaluron Moisture 72H Moisture Sealing Conditioner \t~₹210")
               print("2.Tresemme Keratin Smooth Conditioner\t~₹107")
               print("3.WishCare Multi Peptide Anti Hairfall Conditioner \t~₹300")
               cart=int(input("Add the item to cart="))
               if cart==1:
                  print("Your cart value is :-- ₹210")
                  print(delivery())
                  item="L'Oreal Paris Hyaluron Moisture 72H Moisture Sealing Conditioner\t~₹210"
                  rate=210
               elif cart==2:
                  print("Your cart value= ₹107")
                  print(delivery())
                  item="Tresemme Keratin Smooth Conditioner \t~₹107"
                  rate=107
               elif cart==3:
                  print("Your cart value =₹300")
                  print(delivery())
                  item="WishCare Multi Peptide Anti Hairfall Conditioner \t~₹300"
                  rate=300
                       
               else:
                   print("\nOOPS!!😞 No Data Found!!!")
            elif choice==3:
               print("1.Bajaj Almond Drops Hair Oil\t~₹70")
               print("2.Nihar Naturals Shanti Amla Hair Oil\t~₹100")
               print("3.Emami 7 Oils In One Hair Oil Makes Hair 20x Stronger And Manageable Hair Oil\t~₹200")
               cart=int(input("Add the item to cart="))
               if cart==1:
                  print("Your cart value is :-- ₹70")
                  print(delivery())
                  item=".Bajaj Almond Drops Hair Oil \t~₹70"
                  rate=70
               elif cart==2:
                  print("Your cart value= ₹100")
                  print(delivery())
                  item="Nihar Naturals Shanti Amla Hair Oil \t~₹100"
                  rate=100
               elif cart==3:
                  print("Your cart value =₹200")
                  print(delivery())
                  item="Emami 7 Oils In One Hair Oil Makes Hair 20x Stronger And Manageable Hair Oil \t~₹200"
                  rate=200
               else:
                  print("\nOOPS!!😞 No Data Found!!!")
         elif product==3:
           print("Products:---")
           print("1. Body Wash\n2. Soap\n 3. Face Wash\n4. Lotions and Cream")
           type=int(input("Enter your preference:--"))
           if type==1:
               print("\n\n1.Dove Relaxing Care Nourishing Body Wash Shea Butter & Vanilla\t~₹379")
               print("\n2.Brillare Coconut Body Wash\t~₹217")
               print("\n3.Minimalist Salicylic Acid + LHA Body Wash \t~₹314")
               cart=int(input("Add the item to cart="))
               if cart==1:
                   print("Your cart value is :-- ₹379")
                   print(delivery())    
                   item="Dove Relaxing Care Nourishing Body Wash Shea Butter & Vanilla \t~₹379"  
                   rate=379   
               elif cart==2:
                  print("Your cart value= ₹217")
                  print(delivery())
                  item="Brillare Coconut Body Wash\t~₹217"
                  rate=217
               elif cart==3:
                  print("Your cart value =₹314")
                  print(delivery())
                  item="Minimalist Salicylic Acid + LHA Body Wash \t~₹314"
                  rate=314
               else:
                  print("\nOOPS!!😞 No Data Found!!!")
           elif type==2:
               print("\n1.Ghar Soaps Sandalwood & Saffron Magic Soap\t~₹123")
               print("\n2.Pears Soft & Fresh Soap Bar\t~₹150")
               print("\n3. Dove Cream Beauty Bathing Bar\t~₹160")
               cart=int(input("Add the item to cart="))
               if cart==1:
                 print("Your cart value is :-- ₹123")
                 print(delivery())      
                 item="Ghar Soaps Sandalwood & Saffron Magic Soap \t~₹123" 
                 rate= 123               
               elif cart==2:
                 print("Your cart value= ₹150")
                 print(delivery())
                 item="Pears Soft & Fresh Soap Bar \t~₹150"
                 rate=150
               elif cart==3:
                  print("Your cart value =₹160")
                  print(delivery())
                  item=" Dove Cream Beauty Bathing Bar \t~₹160"
                  rate=160
               else:
                   print("\nOOPS!!😞 No Data Found!!!")
           elif type==3:
               print("\n1.Clean and Clear Foaming Facewash for Oily Skin, Brown Face Wash (240 ml)\t~₹250")
               print("\n2.Dot & Key Hydrating Gentle Face Wash | Ceramide Face Cleanser | For Dry, Normal & Sensitive Skin | Unisex | 3.38 fl oz (100 ml)\t~₹1720")
               print("\n3.Cetaphil Gentle Cleanser Skin\t~₹181")
               cart=int(input("Add the item to cart="))
               if cart==1:
                  print("Your cart value is :-- ₹250")
                  print(delivery())
                  item="Clean and Clear Foaming Facewash for Oily Skin, Brown Face Wash (240 ml) \t~₹181"
                  rate=250
               elif cart==2:
                  print("Your cart value= ₹1720")
                  print(delivery())
                  item="Dot & Key Hydrating Gentle Face Wash | Ceramide Face Cleanser | For Dry, Normal & Sensitive Skin | Unisex | 3.38 fl oz (100 ml) \t~₹1720"
                  rate=1720
               elif cart==3:
                  print("Your cart value =₹181")
                  print(delivery())
                  item="Cetaphil Gentle Cleanser Skin \t~₹181"
                  rate=181
               else:
                  print("\nOOPS!!😞 No Data Found!!!")
           elif type==4: 
               print("\n1.POND's Triple Vitamin Moisturising Body Lotion, 275Ml, For Dry Skin, Smooth And Soft Skin\t~₹224")
               print("\n2.NIVEA Body Lotion Rose Petal & Care, Body Cream with Deep Care Serum for 72 Hours of Moisture(400ml) \t ~₹400")
               print("\n3.Vitamin C + E Super Bright Gel Moisturizer for Face \t ~₹500")
               cart=int(input("Add the item to cart="))
               if cart==1:
                  print("Your cart value is :-- ₹224")
                  print(delivery())
                  item="POND's Triple Vitamin Moisturising Body Lotion, 275Ml, For Dry Skin, Smooth And Soft Skin \t~₹224"
                  rate=224
               elif cart==2:
                  print("Your cart value= ₹400")
                  print(delivery())
                  item="NIVEA Body Lotion Rose Petal & Care, Body Cream with Deep Care Serum for 72 Hours of Moisture(400ml) \t ~₹400"
                  rate=400

               elif cart==3:
                  print("Your cart value =₹500")
                  print(delivery())
                  item="Vitamin C + E Super Bright Gel Moisturizer for Face \t ~₹500"
                  rate=500
               else:
                     print("\nOOPS!!😞 No Data Found!!!")
           else:
               print("\nOOPS!!😞 No Data Found!!!")
         elif product==4:
            print("Products:---")
            print("1.Sneakers\n2.Heels\n3.Sandals\n4.Sports Shoes\n")
            footwear_type = int(input("Enter your preference:--"))
            if footwear_type == 1:
               print("\n1.Puma Womens Street Runner Sneakers \t~₹3,299")
               print("\n2.Adidas Cloudfoam Pure Sneakers \t~₹4,299")
               print("\n3.Nike Air Max Motion Sneakers \t~₹5,499")
               cart=int(input("Add the item to cart="))
               if cart==1:
                   print("Your cart value is :-- ₹3,299")
                   print(delivery())
                   item="Puma Womens Street Runner Sneakers \t~₹3,299"
                   rate=3299
               elif cart==2:
                   print("Your cart value= ₹4,299")
                   print(delivery())
                   item="Adidas Cloudfoam Pure Sneakers \t~₹4,299"
                   rate=4299
               elif cart==3:
                   print("Your cart value =₹5,499")
                   print(delivery())
                   item="Nike Air Max Motion Sneakers \t~₹5,499"
                   rate=5499
               else:
                   print("\nOOPS!!😞 No Data Found!!!")
            elif footwear_type == 2:
               print("\n1.Marks & Spencer Women Heels \t~₹2,499")
               print("\n2.Bata Fashion Heels \t~₹1,899")
               print("\n3.Skechers Party Heels \t~₹2,799")
               cart=int(input("Add the item to cart="))
               if cart==1:
                   print("Your cart value is :-- ₹2,499")
                   print(delivery())
                   item="Marks & Spencer Women Heels \t~₹2,499"
                   rate=2499
               elif cart==2:
                   print("Your cart value= ₹1,899")
                   print(delivery())
                   item="Bata Fashion Heels \t~₹1,899"
                   rate=1899
               elif cart==3:
                   print("Your cart value =₹2,799")
                   print(delivery())
                   item="Skechers Party Heels \t~₹2,799"
                   rate=2799
               else:
                   print("\nOOPS!!😞 No Data Found!!!")
            elif footwear_type == 3:
               print("\n1.Hush Puppies Leather Sandals \t~₹1,299")
               print("\n2.Dressberry Ladies Sandals \t~₹1,799")
               print("\n3.Crocs Everyday Sandals \t~₹2,199")
               cart=int(input("Add the item to cart="))
               if cart==1:
                   print("Your cart value is :-- ₹1,299")
                   print(delivery())
                   item="Hush Puppies Leather Sandals \t~₹1,299"
                   rate=1299
               elif cart==2:
                   print("Your cart value= ₹1,799")
                   print(delivery())
                   item="Dressberry Ladies Sandals \t~₹1,799"
                   rate=1799
               elif cart==3:
                   print("Your cart value =₹2,199")
                   print(delivery())
                   item="Crocs Everyday Sandals \t~₹2,199"
                   rate=2199
               else:
                   print("\nOOPS!!😞 No Data Found!!!")
            elif footwear_type == 4:
               print("\n1.Nike Running Sports Shoes \t~₹4,599")
               print("\n2.Puma Training Sports Shoes \t~₹3,999")
               print("\n3.Adidas Ultra Boost Sports Shoes \t~₹6,299")
               cart=int(input("Add the item to cart="))
               if cart==1:
                   print("Your cart value is :-- ₹4,599")
                   print(delivery())
                   item="Nike Running Sports Shoes \t~₹4,599"
                   rate=4599
               elif cart==2:
                   print("Your cart value= ₹3,999")
                   print(delivery())
                   item="Puma Training Sports Shoes \t~₹3,999"
                   rate=3999
               elif cart==3:
                   print("Your cart value =₹6,299")
                   print(delivery())
                   item="Adidas Ultra Boost Sports Shoes \t~₹6,299"
                   rate=6299
               else:
                   print("\nOOPS!!😞 No Data Found!!!")
            else:
               print("\nOOPS!!😞 No Data Found!!!")
         else:
            print("\nOOPS!!😞 No Data Found!!!")
         print("Want to shop again ?")
         if item is not None:
            shopped.append(item)
            spend.append(rate)
         shop_again = input("Enter 1 or Yes to continue; anything else to exit: ").strip().lower()
      
         if shop_again in ("1", "yes"):
            continue
         show_receipt(shopped, spend)
         break
      else:
         print("\nOOPS!!😞 No Data Found!!!")
   
  else:
    print("\nIncorrect OTP. Please try again.")
else:
    print("\nInvalid phone number. Please enter a valid 10-digit mobile number.")
