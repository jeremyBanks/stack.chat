from .room_messages import RoomMessages


def test():
    parsed = RoomMessages(EXAMPLE_DATA)
    print(parsed)


EXAMPLE_DATA = r'''{"events":[
{"event_type":1,"time_stamp":1511353847,"content":"tpu- by suraj on \u003ca href=\"//askubuntu.com/questions/979130\"\u003ehttp://tophealthydiet.com/protesto-virility/\u003c/a\u003e \u0026#91;\u003ca href=\"http://metasmoke.erwaysoftware.com/post/94658\" rel=\"nofollow noopener noreferrer\"\u003eMS\u003c/a\u003e]","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41294188},
{"event_type":1,"time_stamp":1511353858,"content":"tpu- by suraj","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41294190},
{"event_type":1,"time_stamp":1511353911,"content":"[ \u003ca href=\"//goo.gl/eLDYqh\" rel=\"nofollow noopener noreferrer\"\u003eSmokeDetector\u003c/a\u003e | \u003ca href=\"//m.erwaysoftware.com/posts/by-url?url=//superuser.com/questions/1270782\" rel=\"nofollow noopener noreferrer\"\u003eMS\u003c/a\u003e ] Link at end of body: \u003ca href=\"//superuser.com/questions/1270782\"\u003eHTTP Post request transfer to Trello request LUA\u003c/a\u003e by \u003ca href=\"//superuser.com/users/823128\"\u003eSomeoneIsHere...Watching\u003c/a\u003e on \u003ccode\u003esuperuser.com\u003c/code\u003e","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41294202},
{"event_type":1,"time_stamp":1511353967,"content":"fp- by paper1111","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41294225},
{"event_type":1,"time_stamp":1511354632,"content":"tpu- by DavidPostill on \u003ca href=\"//stackoverflow.com/questions/47434020\"\u003eWanting a clearer light on C# Sockets, Threading and Overall Design Architecture of a Program\u003c/a\u003e \u0026#91;\u003ca href=\"http://metasmoke.erwaysoftware.com/post/94656\" rel=\"nofollow noopener noreferrer\"\u003eMS\u003c/a\u003e]","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41294394},
{"event_type":1,"time_stamp":1511355558,"content":"[ \u003ca href=\"//goo.gl/eLDYqh\" rel=\"nofollow noopener noreferrer\"\u003eSmokeDetector\u003c/a\u003e | \u003ca href=\"//m.erwaysoftware.com/posts/by-url?url=//stackoverflow.com/questions/47435374\" rel=\"nofollow noopener noreferrer\"\u003eMS\u003c/a\u003e ] Bad keyword in body: \u003ca href=\"//stackoverflow.com/questions/47435374\"\u003eOptimize CSS Delivery\u003c/a\u003e by \u003ca href=\"//stackoverflow.com/users/8990019\"\u003esilklogisticspk\u003c/a\u003e on \u003ccode\u003estackoverflow.com\u003c/code\u003e","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41294662},
{"event_type":1,"time_stamp":1511355690,"content":"@SmokeDetector why","user_id":205208,"user_name":"A J","room_id":11540,"message_id":41294703,"parent_id":41294662,"show_parent":true},
{"event_type":1,"time_stamp":1511355692,"content":"@AJ Body - Position 466-508: Packers and Movers in Karachi pakistan\u0026lt;/a\u0026gt;","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41294705,"parent_id":41294703,"show_parent":true},
{"event_type":1,"time_stamp":1511355750,"content":"tpu- by DavidPostill","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41294721},
{"event_type":1,"time_stamp":1511355885,"content":"!!/watch silklogistics\\.com\\.pk","user_id":62118,"user_name":"tripleee","room_id":11540,"message_id":41294750},
{"event_type":1,"time_stamp":1511355895,"content":"@tripleee Added silklogistics\\.com\\.pk to watchlist","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41294752,"parent_id":41294750,"show_parent":true},
{"event_type":1,"time_stamp":1511355995,"content":"\u003ca href=\"https://travis-ci.org/Charcoal-SE/SmokeDetector/builds/305794219?utm_source=github_status\u0026amp;utm_medium=notification\" rel=\"nofollow noopener noreferrer\"\u003eCI\u003c/a\u003e on \u003ca href=\"https://github.com/Charcoal-SE/SmokeDetector/commit/2a085a5\" rel=\"nofollow noopener noreferrer\"\u003e\u003ccode\u003e2a085a5\u003c/code\u003e\u003c/a\u003e succeeded. Message contains \u0026#39;autopull\u0026#39;, pulling...","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41294769},
{"event_type":1,"time_stamp":1511356017,"content":"[ \u003ca href=\"//github.com/Charcoal-SE/SmokeDetector\" rel=\"nofollow noopener noreferrer\"\u003eSmokeDetector\u003c/a\u003e ] SmokeDetector started at \u003ca href=\"//github.com/Charcoal-SE/SmokeDetector/commit/2a085a5\" rel=\"nofollow noopener noreferrer\"\u003erev 2a085a5 (SmokeDetector: \u003ci\u003eAuto watch of silklogistics\\.com\\.pk by tripleee --autopull\u003c/i\u003e)\u003c/a\u003e (running on Henders/EC2)","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41294771},
{"event_type":1,"time_stamp":1511356023,"content":"Restart: API quota is 12391.","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41294772},
{"event_type":1,"time_stamp":1511356559,"content":"[ \u003ca href=\"//goo.gl/eLDYqh\" rel=\"nofollow noopener noreferrer\"\u003eSmokeDetector\u003c/a\u003e | \u003ca href=\"//m.erwaysoftware.com/posts/by-url?url=//travel.stackexchange.com/a/105656\" rel=\"nofollow noopener noreferrer\"\u003eMS\u003c/a\u003e ] Potentially bad keyword in answer: \u003ca href=\"//travel.stackexchange.com/a/105656\"\u003eTaxis from Heathrow with a lot of luggage\u003c/a\u003e by \u003ca href=\"//travel.stackexchange.com/users/70607\"\u003eFederico Arata\u003c/a\u003e on \u003ccode\u003etravel.SE\u003c/code\u003e","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41294931},
{"event_type":1,"time_stamp":1511356633,"content":"[ \u003ca href=\"//goo.gl/eLDYqh\" rel=\"nofollow noopener noreferrer\"\u003eSmokeDetector\u003c/a\u003e | \u003ca href=\"//m.erwaysoftware.com/posts/by-url?url=//askubuntu.com/questions/979142\" rel=\"nofollow noopener noreferrer\"\u003eMS\u003c/a\u003e ] URL-only title, bad keyword in body, blacklisted website in body, blacklisted website in title, link at end of body, +3 more: \u003ca href=\"//askubuntu.com/questions/979142\"\u003esupplementch3mistry.com/alpha-plus-test-booster/\u003c/a\u003e by \u003ca href=\"//askubuntu.com/users/763018\"\u003eWorivePurte\u003c/a\u003e on \u003ccode\u003easkubuntu.com\u003c/code\u003e","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41294952},
{"event_type":1,"time_stamp":1511356675,"content":"tpu- by paper1111","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41294973},
{"event_type":1,"time_stamp":1511356751,"content":"tpu- by DavidPostill on \u003ca href=\"//travel.stackexchange.com/a/105656\"\u003eTaxis from Heathrow with a lot of luggage\u003c/a\u003e \u0026#91;\u003ca href=\"http://metasmoke.erwaysoftware.com/post/94662\" rel=\"nofollow noopener noreferrer\"\u003eMS\u003c/a\u003e]","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41295011},
{"event_type":1,"time_stamp":1511356855,"content":"@SmokeDetector tpu-","user_id":205208,"user_name":"A J","room_id":11540,"message_id":41295038,"parent_id":41294931,"show_parent":true},
{"event_type":1,"time_stamp":1511357075,"content":"[ \u003ca href=\"//goo.gl/eLDYqh\" rel=\"nofollow noopener noreferrer\"\u003eSmokeDetector\u003c/a\u003e | \u003ca href=\"//m.erwaysoftware.com/posts/by-url?url=//sqa.stackexchange.com/a/30675\" rel=\"nofollow noopener noreferrer\"\u003eMS\u003c/a\u003e ] Pattern-matching website in answer: \u003ca href=\"//sqa.stackexchange.com/a/30675\"\u003eWhich tool is used for website link checking and spelling checking in manual testing\u003c/a\u003e by \u003ca href=\"//sqa.stackexchange.com/users/29207\"\u003eAlan\u003c/a\u003e on \u003ccode\u003esqa.SE\u003c/code\u003e","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41295090},
{"event_type":1,"time_stamp":1511357318,"content":"[ \u003ca href=\"//goo.gl/eLDYqh\" rel=\"nofollow noopener noreferrer\"\u003eSmokeDetector\u003c/a\u003e | \u003ca href=\"//m.erwaysoftware.com/posts/by-url?url=//security.stackexchange.com/questions/174092\" rel=\"nofollow noopener noreferrer\"\u003eMS\u003c/a\u003e ] Bad keyword with email in body: \u003ca href=\"//security.stackexchange.com/questions/174092\"\u003eInfoSec consultancy/implementation/management jobs? (part-time)\u003c/a\u003e by \u003ca href=\"//security.stackexchange.com/users/164379\"\u003ejohan vd Pluijm\u003c/a\u003e on \u003ccode\u003esecurity.SE\u003c/code\u003e","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41295222},
{"event_type":1,"time_stamp":1511357334,"content":"fp- by Mithrandir","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41295232},
{"event_type":1,"time_stamp":1511357339,"content":"tpu- by Henders","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41295236},
{"event_type":1,"time_stamp":1511357345,"content":"Conflicting feedback on \u003ca href=\"//metasmoke.erwaysoftware.com/post/94665\" rel=\"nofollow noopener noreferrer\"\u003eInfoSec consultancy/implementation/management jobs? (part-time)\u003c/a\u003e.","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41295239},
{"event_type":1,"time_stamp":1511357357,"content":"Oops","user_id":211021,"user_name":"Henders","room_id":11540,"message_id":41295248},
{"event_type":1,"time_stamp":1511357417,"content":"@SmokeDetector f","user_id":211021,"user_name":"Henders","room_id":11540,"message_id":41295288,"parent_id":41295222,"show_parent":true},
{"event_type":1,"time_stamp":1511357456,"content":"@JF and @quartata I added the number of items for ease checking how many items there are and validation of how many there are. The same reason SE adds it to their API responses. If you don\u0026#39;t want it there I can pull it off","user_id":66258,"user_name":"Andy","room_id":11540,"message_id":41295310,"parent_id":41292818,"show_parent":true},
{"event_type":1,"time_stamp":1511357489,"content":"!!/rmblu https://security.stackexchange.com/users/164379/johan-vd-pluijm","user_id":211021,"user_name":"Henders","room_id":11540,"message_id":41295325},
{"event_type":1,"time_stamp":1511357491,"content":"@Henders User removed from blacklist (\u003ccode\u003e164379\u003c/code\u003e on \u003ccode\u003esecurity.stackexchange.com\u003c/code\u003e).","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41295327,"parent_id":41295325,"show_parent":true},
{"event_type":1,"time_stamp":1511357507,"content":"not spam, but completely off topic","user_id":133031,"user_name":"Mithrandir","room_id":11540,"message_id":41295339},
{"event_type":1,"time_stamp":1511357524,"content":"Yeah, sorry, I forgot that was an option :P","user_id":211021,"user_name":"Henders","room_id":11540,"message_id":41295351},
{"event_type":1,"time_stamp":1511357718,"content":"[ \u003ca href=\"//goo.gl/eLDYqh\" rel=\"nofollow noopener noreferrer\"\u003eSmokeDetector\u003c/a\u003e | \u003ca href=\"//m.erwaysoftware.com/posts/by-url?url=//astronomy.stackexchange.com/questions/23645\" rel=\"nofollow noopener noreferrer\"\u003eMS\u003c/a\u003e ] URL in title, bad NS for domain in body, bad NS for domain in title, bad keyword in body, bad keyword in title, +5 more: \u003ca href=\"//astronomy.stackexchange.com/questions/23645\"\u003etophealthydiet.com/protesto-virility/\u003c/a\u003e by \u003ca href=\"//astronomy.stackexchange.com/users/19793\"\u003emureal bagge\u003c/a\u003e on \u003ccode\u003eastronomy.SE\u003c/code\u003e","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41295433},
{"event_type":1,"time_stamp":1511357878,"content":"[ \u003ca href=\"//goo.gl/eLDYqh\" rel=\"nofollow noopener noreferrer\"\u003eSmokeDetector\u003c/a\u003e | \u003ca href=\"//m.erwaysoftware.com/posts/by-url?url=//stackoverflow.com/questions/47436138\" rel=\"nofollow noopener noreferrer\"\u003eMS\u003c/a\u003e ] Blacklisted user: \u003ca href=\"//stackoverflow.com/questions/47436138\"\u003eHow to write php uolpad code into coldfusion\u003c/a\u003e by \u003ca href=\"//stackoverflow.com/users/8785466\"\u003ePintu Kumar\u003c/a\u003e on \u003ccode\u003estackoverflow.com\u003c/code\u003e","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41295502},
{"event_type":1,"time_stamp":1511357929,"content":"fp- by paper1111","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41295524},
{"event_type":1,"time_stamp":1511357934,"content":"sd - f","user_id":133031,"user_name":"Mithrandir","room_id":11540,"message_id":41295526},
{"event_type":1,"time_stamp":1511358068,"content":"[ \u003ca href=\"//goo.gl/eLDYqh\" rel=\"nofollow noopener noreferrer\"\u003eSmokeDetector\u003c/a\u003e | \u003ca href=\"//m.erwaysoftware.com/posts/by-url?url=//english.stackexchange.com/a/419404\" rel=\"nofollow noopener noreferrer\"\u003eMS\u003c/a\u003e ] Link at end of answer: \u003ca href=\"//english.stackexchange.com/a/419404\"\u003eShould \u0026quot;Los Angeles\u0026quot; rhyme with \u0026quot;cheese\u0026quot; or \u0026quot;mess\u0026quot;\u003c/a\u003e by \u003ca href=\"//english.stackexchange.com/users/268176\"\u003eJames Wayne\u003c/a\u003e on \u003ccode\u003eenglish.SE\u003c/code\u003e","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41295577},
{"event_type":1,"time_stamp":1511358172,"content":"[ \u003ca href=\"//goo.gl/eLDYqh\" rel=\"nofollow noopener noreferrer\"\u003eSmokeDetector\u003c/a\u003e | \u003ca href=\"//m.erwaysoftware.com/posts/by-url?url=//apple.stackexchange.com/questions/306565\" rel=\"nofollow noopener noreferrer\"\u003eMS\u003c/a\u003e ] URL in title, bad NS for domain in body, bad NS for domain in title, bad keyword in body, bad keyword in title, +5 more: \u003ca href=\"//apple.stackexchange.com/questions/306565\"\u003etophealthydiet.com/protesto-virility/\u003c/a\u003e by \u003ca href=\"//apple.stackexchange.com/users/264955\"\u003euser264955\u003c/a\u003e on \u003ccode\u003eapple.SE\u003c/code\u003e","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41295620},
{"event_type":1,"time_stamp":1511358190,"content":"tpu- by Henders","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41295628},
{"event_type":1,"time_stamp":1511359541,"content":"@SmokeDetector tpu-","user_id":155243,"user_name":"Nisse Engström","room_id":11540,"message_id":41296051,"parent_id":41295577,"show_parent":true},
{"event_type":1,"time_stamp":1511360279,"content":"naa- by Cai on \u003ca href=\"//meta.stackexchange.com/a/303559\"\u003eDisplay embedded YouTube videos in markdown preview\u003c/a\u003e \u0026#91;\u003ca href=\"http://metasmoke.erwaysoftware.com/post/94655\" rel=\"nofollow noopener noreferrer\"\u003eMS\u003c/a\u003e]","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41296313},
{"event_type":1,"time_stamp":1511360284,"content":"fp feedback on autoflagged post: \u003ca href=\"//metasmoke.erwaysoftware.com/post/94655\" rel=\"nofollow noopener noreferrer\"\u003eDisplay embedded YouTube videos in markdown preview\u003c/a\u003e","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41296315},
{"event_type":1,"time_stamp":1511361335,"content":"[ \u003ca href=\"//goo.gl/eLDYqh\" rel=\"nofollow noopener noreferrer\"\u003eSmokeDetector\u003c/a\u003e | \u003ca href=\"//m.erwaysoftware.com/posts/by-url?url=//stackoverflow.com/questions/47437223\" rel=\"nofollow noopener noreferrer\"\u003eMS\u003c/a\u003e ] Bad NS for domain in body: \u003ca href=\"//stackoverflow.com/questions/47437223\"\u003ehow can I stop gmail from blocking mail from PHP script\u003c/a\u003e by \u003ca href=\"//stackoverflow.com/users/8984799\"\u003eKevin\u003c/a\u003e on \u003ccode\u003estackoverflow.com\u003c/code\u003e","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41296696},
{"event_type":1,"time_stamp":1511362388,"content":"[ \u003ca href=\"//goo.gl/eLDYqh\" rel=\"nofollow noopener noreferrer\"\u003eSmokeDetector\u003c/a\u003e | \u003ca href=\"//m.erwaysoftware.com/posts/by-url?url=//stackoverflow.com/questions/47437658\" rel=\"nofollow noopener noreferrer\"\u003eMS\u003c/a\u003e ] Bad NS for domain in body: \u003ca href=\"//stackoverflow.com/questions/47437658\"\u003eyii2 unknown property exception in GridView widget\u003c/a\u003e by \u003ca href=\"//stackoverflow.com/users/8990784\"\u003eSabbar hussain\u003c/a\u003e on \u003ccode\u003estackoverflow.com\u003c/code\u003e","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41297148},
{"event_type":1,"time_stamp":1511363473,"content":"[ \u003ca href=\"//goo.gl/eLDYqh\" rel=\"nofollow noopener noreferrer\"\u003eSmokeDetector\u003c/a\u003e | \u003ca href=\"//m.erwaysoftware.com/posts/by-url?url=//apple.stackexchange.com/a/306578\" rel=\"nofollow noopener noreferrer\"\u003eMS\u003c/a\u003e ] Bad keyword with email in answer: \u003ca href=\"//apple.stackexchange.com/a/306578\"\u003eI know my apple ID but don\u0026#39;t know my iCloud id or password, is it the same?\u003c/a\u003e by \u003ca href=\"//apple.stackexchange.com/users/263274\"\u003eJames Winthrop\u003c/a\u003e on \u003ccode\u003eapple.SE\u003c/code\u003e","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41297623},
{"event_type":1,"time_stamp":1511363534,"content":"fp- by Henders","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41297649},
{"event_type":1,"time_stamp":1511363937,"content":"[ \u003ca href=\"//goo.gl/eLDYqh\" rel=\"nofollow noopener noreferrer\"\u003eSmokeDetector\u003c/a\u003e | \u003ca href=\"//m.erwaysoftware.com/posts/by-url?url=//stackoverflow.com/questions/47438200\" rel=\"nofollow noopener noreferrer\"\u003eMS\u003c/a\u003e ] Offensive body detected: \u003ca href=\"//stackoverflow.com/questions/47438200\"\u003ei\u0026#39;m new to programming and thought should start with C language this code give me incorrect outputs\u003c/a\u003e by \u003ca href=\"//stackoverflow.com/users/5033535\"\u003eZen\u003c/a\u003e on \u003ccode\u003estackoverflow.com\u003c/code\u003e","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41297831},
{"event_type":1,"time_stamp":1511364281,"content":"[ \u003ca href=\"//goo.gl/eLDYqh\" rel=\"nofollow noopener noreferrer\"\u003eSmokeDetector\u003c/a\u003e | \u003ca href=\"//m.erwaysoftware.com/posts/by-url?url=//expressionengine.stackexchange.com/questions/40024\" rel=\"nofollow noopener noreferrer\"\u003eMS\u003c/a\u003e ] URL in title: \u003ca href=\"//expressionengine.stackexchange.com/questions/40024\"\u003eadd to cart w/captcha bypass for adidas uk (www.adidas.com/yeezy) also known as a bot\u003c/a\u003e by \u003ca href=\"//expressionengine.stackexchange.com/users/9303\"\u003ebogdan\u003c/a\u003e on \u003ccode\u003eexpressionengine.SE\u003c/code\u003e","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41297957},
{"event_type":1,"time_stamp":1511364877,"content":"fp- by DavidPostill on \u003ca href=\"//stackoverflow.com/questions/47438200\"\u003ei\u0026#39;m new to programming and thought should start with C language this code give me incorrect outputs\u003c/a\u003e \u0026#91;\u003ca href=\"http://metasmoke.erwaysoftware.com/post/94673\" rel=\"nofollow noopener noreferrer\"\u003eMS\u003c/a\u003e]","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41298174},
{"event_type":1,"time_stamp":1511364908,"content":"fp- by DavidPostill","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41298186},
{"event_type":1,"time_stamp":1511364969,"content":"fp- by DavidPostill on \u003ca href=\"//stackoverflow.com/questions/47437658\"\u003eyii2 unknown property exception in GridView widget\u003c/a\u003e \u0026#91;\u003ca href=\"http://metasmoke.erwaysoftware.com/post/94671\" rel=\"nofollow noopener noreferrer\"\u003eMS\u003c/a\u003e]","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41298204},
{"event_type":1,"time_stamp":1511365006,"content":"fp- by DavidPostill on \u003ca href=\"//stackoverflow.com/questions/47437223\"\u003ehow can I stop gmail from blocking mail from PHP script\u003c/a\u003e \u0026#91;\u003ca href=\"http://metasmoke.erwaysoftware.com/post/94670\" rel=\"nofollow noopener noreferrer\"\u003eMS\u003c/a\u003e]","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41298215},
{"event_type":1,"time_stamp":1511368475,"content":"[ \u003ca href=\"//goo.gl/eLDYqh\" rel=\"nofollow noopener noreferrer\"\u003eSmokeDetector\u003c/a\u003e | \u003ca href=\"//m.erwaysoftware.com/posts/by-url?url=//stackoverflow.com/a/18238757\" rel=\"nofollow noopener noreferrer\"\u003eMS\u003c/a\u003e ] Link at end of answer: \u003ca href=\"//stackoverflow.com/a/18238757\"\u003eCombining pdf files with file name bookmark and a template page between each combined file using ghostscript\u003c/a\u003e by \u003ca href=\"//stackoverflow.com/users/2683520\"\u003eJobj\u003c/a\u003e on \u003ccode\u003estackoverflow.com\u003c/code\u003e","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41299826},
{"event_type":1,"time_stamp":1511368624,"content":"[ \u003ca href=\"//goo.gl/eLDYqh\" rel=\"nofollow noopener noreferrer\"\u003eSmokeDetector\u003c/a\u003e | \u003ca href=\"//m.erwaysoftware.com/posts/by-url?url=//ru.stackoverflow.com/a/748260\" rel=\"nofollow noopener noreferrer\"\u003eMS\u003c/a\u003e ] Pattern-matching website in answer: \u003ca href=\"//ru.stackoverflow.com/a/748260\"\u003eвосстановление outlook пароля\u003c/a\u003e by \u003ca href=\"//ru.stackoverflow.com/users/275010\"\u003ekoganartem\u003c/a\u003e on \u003ccode\u003eru.stackoverflow.com\u003c/code\u003e","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41299893},
{"event_type":1,"time_stamp":1511368946,"content":"Hi","user_id":318454,"user_name":"Jake Symons","room_id":11540,"message_id":41300017},
{"event_type":1,"time_stamp":1511368955,"content":"anyone there","user_id":318454,"user_name":"Jake Symons","room_id":11540,"message_id":41300020},
{"event_type":1,"time_stamp":1511368991,"content":"tpu- by Mego on \u003ca href=\"//stackoverflow.com/a/18238757\"\u003eCombining pdf files with file name bookmark and a template page between each combined file using ghostscript\u003c/a\u003e \u0026#91;\u003ca href=\"http://metasmoke.erwaysoftware.com/post/94675\" rel=\"nofollow noopener noreferrer\"\u003eMS\u003c/a\u003e]","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41300027},
{"event_type":1,"time_stamp":1511368996,"content":"tpu- by Mego","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41300029},
{"event_type":1,"time_stamp":1511369060,"content":"[ \u003ca href=\"//goo.gl/eLDYqh\" rel=\"nofollow noopener noreferrer\"\u003eSmokeDetector\u003c/a\u003e | \u003ca href=\"//m.erwaysoftware.com/posts/by-url?url=//stackoverflow.com/a/47439892\" rel=\"nofollow noopener noreferrer\"\u003eMS\u003c/a\u003e ] Link at end of answer: \u003ca href=\"//stackoverflow.com/a/47439892\"\u003e.HTAccess redirecting rewriting pages based on partial URL pattern?\u003c/a\u003e by \u003ca href=\"//stackoverflow.com/users/6364643\"\u003enaimanj\u003c/a\u003e on \u003ccode\u003estackoverflow.com\u003c/code\u003e","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41300057},
{"event_type":1,"time_stamp":1511369583,"content":"@SmokeDetector why","user_id":318454,"user_name":"Jake Symons","room_id":11540,"message_id":41300248,"parent_id":41297831,"show_parent":true},
{"event_type":1,"time_stamp":1511369584,"user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41300249,"parent_id":41300248,"show_parent":true},
{"event_type":1,"time_stamp":1511372215,"content":"\u003cdiv class=\"onebox ob-message\"\u003e\u003ca rel=\"noopener noreferrer\" class=\"roomname\" href=\"/transcript/message/41277246#41277246\"\u003e\u003cspan title=\"2017-11-21 17:27:50Z\"\u003eyesterday\u003c/span\u003e\u003c/a\u003e, by \u003cspan class=\"user-name\"\u003eHenders\u003c/span\u003e \u003cbr/\u003e\u003cdiv class=\"quote\"\u003e@JakeSymons - A few people have asked you to stop doing \u0026#39;why\u0026#39; when you can get the same result from Clicking the MS link instead. Would you be able to click \u0026#39;MS\u0026#39; in the future so it doesn\u0026#39;t fill up the room, please?\u003c/div\u003e\u003c/div\u003e","user_id":211021,"user_name":"Henders","room_id":11540,"message_id":41301176},
{"event_type":1,"time_stamp":1511372226,"content":"You never responded to my question, @JakeSymons","user_id":211021,"user_name":"Henders","room_id":11540,"message_id":41301180,"parent_id":41300248},
{"event_type":1,"time_stamp":1511372271,"content":"Someone specifically asked you not to do \u0026#39;why\u0026#39; for \u0026#39;offensive body detected\u0026#39; yesterday too.","user_id":211021,"user_name":"Henders","room_id":11540,"message_id":41301198},
{"event_type":1,"time_stamp":1511373073,"user_id":318454,"user_name":"Jake Symons","room_id":11540,"message_id":41301455},
{"event_type":1,"time_stamp":1511373398,"content":"@Henders That was me. I don\u0026#39;t really care up until the point that it risks Smokey getting flagged which is now","user_id":167070,"user_name":"quartata","room_id":11540,"message_id":41301612,"parent_id":41301198},
{"event_type":1,"time_stamp":1511373436,"content":"like, you don\u0026#39;t need to have every obscenity posted in chat","user_id":167070,"user_name":"quartata","room_id":11540,"message_id":41301634},
{"event_type":1,"time_stamp":1511373660,"content":"... someone\u0026#39;s flagging stuff here?","user_id":73046,"user_name":"Undo","room_id":11540,"message_id":41301734},
{"event_type":1,"time_stamp":1511373892,"content":"No but when the transcript is filled with \u003ccode\u003eBody: Position 1-42: \u0026lt;obscenity\u0026gt;\u003c/code\u003e I\u0026#39;m not comfortable with the chances of someone showing up and flagging it","user_id":167070,"user_name":"quartata","room_id":11540,"message_id":41301864},
{"event_type":1,"time_stamp":1511373925,"content":"Yeah, we\u0026#39;ll deal with that when it happens","user_id":73046,"user_name":"Undo","room_id":11540,"message_id":41301880},
{"event_type":1,"time_stamp":1511373968,"content":"Well we\u0026#39;ve already been dealing with it just by trashing said messages","user_id":167070,"user_name":"quartata","room_id":11540,"message_id":41301915},
{"event_type":1,"time_stamp":1511373992,"content":"They\u0026#39;re not important anyways, it\u0026#39;s just the why data. It\u0026#39;s really a nuisance.","user_id":167070,"user_name":"quartata","room_id":11540,"message_id":41301929},
{"event_type":1,"time_stamp":1511374004,"content":"and honestly, nothing bad will happen if someone did flag and it got validated. Smokey will be suspended for a few minutes, someone will ping me and I\u0026#39;ll ping Shog to unsuspend","user_id":73046,"user_name":"Undo","room_id":11540,"message_id":41301935},
{"event_type":1,"time_stamp":1511374010,"content":"Or I\u0026#39;d just do it if it was super clear cut.","user_id":73046,"user_name":"Undo","room_id":11540,"message_id":41301938},
{"event_type":1,"time_stamp":1511374022,"content":"Shog or some other somewhat-neutral moderator to review it","user_id":73046,"user_name":"Undo","room_id":11540,"message_id":41301945},
{"event_type":1,"time_stamp":1511374044,"content":"and we\u0026#39;ll track down the flagger and explain some things","user_id":73046,"user_name":"Undo","room_id":11540,"message_id":41301959},
{"event_type":1,"time_stamp":1511374053,"content":"@quartata Now this is a valid reason.","user_id":73046,"user_name":"Undo","room_id":11540,"message_id":41301963,"parent_id":41301929,"show_parent":true},
{"event_type":1,"time_stamp":1511374410,"content":"why don\u0026#39;t we disable -why for only experienced users with an account on Smokey. It could be a privallged command such as replying to smokey with TPU","user_id":318454,"user_name":"Jake Symons","room_id":11540,"message_id":41302128},
{"event_type":1,"time_stamp":1511374423,"content":"Because we shouldn\u0026#39;t have to","user_id":73046,"user_name":"Undo","room_id":11540,"message_id":41302136},
{"event_type":1,"time_stamp":1511374459,"content":"@Undo so what do you think we should do?","user_id":318454,"user_name":"Jake Symons","room_id":11540,"message_id":41302153,"parent_id":41302136,"show_parent":true},
{"event_type":1,"time_stamp":1511374479,"content":"Why data is totally public via Metasmoke, it doesn\u0026#39;t make sense to have it as a privileged command","user_id":167070,"user_name":"quartata","room_id":11540,"message_id":41302167},
{"event_type":1,"time_stamp":1511374486,"content":"Can we just use the MS link?","user_id":73046,"user_name":"Undo","room_id":11540,"message_id":41302170},
{"event_type":1,"time_stamp":1511374502,"content":"Sometimes training people is cheaper than making system changes","user_id":73046,"user_name":"Undo","room_id":11540,"message_id":41302176},
{"event_type":1,"time_stamp":1511374525,"content":"\u003cdiv class=\"onebox ob-message\"\u003e\u003ca rel=\"noopener noreferrer\" class=\"roomname\" href=\"/transcript/message/41277246#41277246\"\u003e\u003cspan title=\"2017-11-21 17:27:50Z\"\u003eyesterday\u003c/span\u003e\u003c/a\u003e, by \u003cspan class=\"user-name\"\u003eHenders\u003c/span\u003e \u003cbr/\u003e\u003cdiv class=\"quote\"\u003e@JakeSymons - A few people have asked you to stop doing \u0026#39;why\u0026#39; when you can get the same result from Clicking the MS link instead. Would you be able to click \u0026#39;MS\u0026#39; in the future so it doesn\u0026#39;t fill up the room, please?\u003c/div\u003e\u003c/div\u003e","user_id":167070,"user_name":"quartata","room_id":11540,"message_id":41302187,"message_stars":1},
{"event_type":1,"time_stamp":1511374564,"content":"Metasmoke is so pretty anyways, go and admire its elegant totally-not-stock-Bootstrap design","user_id":167070,"user_name":"quartata","room_id":11540,"message_id":41302203},
{"event_type":1,"time_stamp":1511374580,"content":"@quartata what about having a three strikes and your out policy. Using why three times or the overuse of it could result in suspension form chat. Can we pause the chat for those users","user_id":318454,"user_name":"Jake Symons","room_id":11540,"message_id":41302211,"parent_id":41302167,"message_edits":1,"show_parent":true},
{"event_type":1,"time_stamp":1511374581,"content":"[ \u003ca href=\"//goo.gl/eLDYqh\" rel=\"nofollow noopener noreferrer\"\u003eSmokeDetector\u003c/a\u003e | \u003ca href=\"//m.erwaysoftware.com/posts/by-url?url=//academia.stackexchange.com/questions/99287\" rel=\"nofollow noopener noreferrer\"\u003eMS\u003c/a\u003e ] Blacklisted website in body: \u003ca href=\"//academia.stackexchange.com/questions/99287\"\u003eWebsite review - pls share\u003c/a\u003e by \u003ca href=\"//academia.stackexchange.com/users/83263\"\u003euser83263\u003c/a\u003e on \u003ccode\u003eacademia.SE\u003c/code\u003e","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41302212},
{"event_type":1,"time_stamp":1511374633,"content":"@JakeSymons You\u0026#39;re the only one doing this. Pretty easy for you to fix :P","user_id":73046,"user_name":"Undo","room_id":11540,"message_id":41302243,"parent_id":41302211,"show_parent":true},
{"event_type":1,"time_stamp":1511374650,"content":"We\u0026#39;ve gone a long time without hard rules there; I don\u0026#39;t need to start adding broad policy for one case","user_id":73046,"user_name":"Undo","room_id":11540,"message_id":41302250},
{"event_type":1,"time_stamp":1511374738,"content":"So would it be best if I left altogther","user_id":318454,"user_name":"Jake Symons","room_id":11540,"message_id":41302280,"message_edits":1},
{"event_type":1,"time_stamp":1511374793,"content":"That\u0026#39;s not what I said.","user_id":73046,"user_name":"Undo","room_id":11540,"message_id":41302310},
{"event_type":1,"time_stamp":1511374798,"content":"@JakeSymons Why do you always jump straight to that? It seems like you\u0026#39;re just trying to be dramatic.","user_id":169713,"user_name":"Mego","room_id":11540,"message_id":41302314,"parent_id":41302280,"show_parent":true},
{"event_type":1,"time_stamp":1511374809,"content":"@Mego I don\u0026#39;t want any arguments","user_id":318454,"user_name":"Jake Symons","room_id":11540,"message_id":41302318,"parent_id":41302314,"show_parent":true},
{"event_type":1,"time_stamp":1511374837,"content":"So if you don\u0026#39;t want any arguments, it would be a good idea if you listened to what we tell you.","user_id":133031,"user_name":"Mithrandir","room_id":11540,"message_id":41302326,"message_stars":3},
{"event_type":1,"time_stamp":1511374872,"content":"Meh. Just stop engaging for a while.","user_id":73046,"user_name":"Undo","room_id":11540,"message_id":41302338},
{"event_type":1,"time_stamp":1511374896,"content":"tpu- by doppelgreener","user_id":120914,"user_name":"SmokeDetector","room_id":11540,"message_id":41302348},
{"event_type":1,"time_stamp":1511374928,"content":"@SmokeDetector k","user_id":133031,"user_name":"Mithrandir","room_id":11540,"message_id":41302358,"parent_id":41302212,"show_parent":true},
{"event_type":1,"time_stamp":1511374983,"content":"@Mithrandir I am listerning. I understand looking at all your reputations that you are much higher then me. Clearly as a minor I need to accept I have no experience in this forum. Thank you for trying to help but it proably best if I just left, I clearly need to get much more experience before even attempting to come on a forum like this","user_id":318454,"user_name":"Jake Symons","room_id":11540,"message_id":41302377,"parent_id":41302326,"show_parent":true},
{"event_type":1,"time_stamp":1511375012,"content":"You\u0026#39;re welcome back whenever you think you\u0026#39;re ready :)","user_id":73046,"user_name":"Undo","room_id":11540,"message_id":41302392,"message_edits":1},
{"event_type":1,"time_stamp":1511375038,"content":"Fun fact: Art, hichris and I are all pretty young","user_id":73046,"user_name":"Undo","room_id":11540,"message_id":41302403},
{"event_type":1,"time_stamp":1511375049,"content":"Was 13-15 when we started on this stuff","user_id":73046,"user_name":"Undo","room_id":11540,"message_id":41302406}],"time":81818807,"sync":1511383213,"ms":1}'''
