from ringcentral import SDK

RECIPIENT_ONE = '6505186090'
# RECIPIENT_TWO = '6505186090'

RINGCENTRAL_CLIENTID = 'f43HS3lMQk22XjUCCer82w'
RINGCENTRAL_CLIENTSECRET = 'VhqONcPwRe67YLsevCUxdQum8x2mHPQlab1i8mG3q-CQ'
RINGCENTRAL_SERVER = 'https://platform.devtest.ringcentral.com'

RINGCENTRAL_USERNAME = 'VhqONcPwRe67YLsevCUxdQum8x2mHPQlab1i8mG3q-CQ'
RINGCENTRAL_PASSWORD = 'YouNeedAPassword1'
RINGCENTRAL_EXTENSION = '101'

rcsdk = SDK( RINGCENTRAL_CLIENTID, RINGCENTRAL_CLIENTSECRET, RINGCENTRAL_SERVER)
platform = rcsdk.platform()
platform.login(RINGCENTRAL_USERNAME, RINGCENTRAL_EXTENSION, RINGCENTRAL_PASSWORD)

platform.post('/restapi/v1.0/account/~/extension/~/sms',
              {
                  'from' : { 'phoneNumber': RINGCENTRAL_USERNAME },
                  'to'   : [ {'phoneNumber': RECIPIENT_ONE} ],
                  'text' : 'Hello World from Python'
              })

# platform.post('/restapi/v1.0/account/~/extension/~/sms',
#               {
#                   'from' : { 'phoneNumber': RINGCENTRAL_USERNAME },
#                   'to'   : [ {'phoneNumber': RECIPIENT_TWO} ],
#                   'text' : 'Hello World from Python'
#               })