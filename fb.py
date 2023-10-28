import __facebookLoginV2
#or import src.__facebookLoginV2 if you place the calling file outside of src
user = "Booking.MinhHuyDev"
passw = "123abcxyz@"
twofa = None
clientLogin = __facebookLoginV2.loginFB(user, passw, twofa)
resultLogin = clientLogin.main()
print(resultLogin)
