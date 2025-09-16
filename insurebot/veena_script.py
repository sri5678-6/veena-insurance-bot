veena_script={ 
  "start":{
  "text": {
  "english": "Good Morning Sir. May I speak to {policy_holder}?",
  "hindi": "नमस्ते, मैं विनी हूँ, वैल्यूएनेबल लाइफ इंश्योरेंस से। क्या मैं {policy_holder} से बात कर सकती हूँ?",
  "marathi": "नमस्कार, मी विना बोलतेय व्हॅल्युएनेबल लाइफ इन्शुरन्समधून. मी {policy_holder} शी बोलू शकते का?",
   "gujarati": "નમસ્તે, હું વીના છું વૅલ્યુએનેબલ લાઇફ ઇન્શ્યોરન્સ તરફથી. શું હું {policy_holder} સાથે વાત કરી શકું?",
  },
    "options": {
    "english": {
    "yes tell me": "branch_busy_check",
    "yes i am pratik": "branch_busy_check",
    "yes i am": "branch_busy_check",
    "yes speaking": "branch_busy_check",
    "speaking": "branch_busy_check",
    "tell me": "branch_busy_check",
    "yes": "branch_busy_check",
    "yes you can": "branch_busy_check",
    },
    "hindi": {
    "हाँ": "branch_busy_check",
    "मैं बोल रही हूँ": "branch_busy_check",
    "मैं बोल रहा हूँ": "branch_busy_check",
    "बोलो": "branch_busy_check",
    "कहिए": "branch_busy_check",
    "हाँ बताइए": "branch_busy_check",
    },
    "marathi": {
    "हो": "branch_busy_check",
    "मी बोलतो आहे": "branch_busy_check",
    "मी बोलते आहे": "branch_busy_check",
    "बोल": "branch_busy_check",
    "हो सांगा": "branch_busy_check",
    },
   "gujarati": {
    "હા": "branch_busy_check",
    "હું બોલું છું": "branch_busy_check",
    "હા કહો": "branch_busy_check",
    "હા બોલો": "branch_busy_check",
    "હા બતાવો": "branch_busy_check",
  },
  "fallback": "greeting"
},
  },
"branch_busy_check": {
    "text":{
  "english": "Are you busy right now?",
  "hindi": "क्या आप अभी व्यस्त हैं?",
  "marathi": "तुम्ही आत्ता व्यस्त आहात का?",   
  "gujarati": "શું તમે અત્યારે વ્યસ્ત છો?",
},
  "options": {
    "english": {
    "yes i am busy": "not_interested_branch",
    "busy": "not_interested_branch",
    "yes": "not_interested_branch",
    "no i am free": "branch_policy_due_info",
    "no i am": "branch_policy_due_info",
    "i am free": "branch_policy_due_info",
    "free": "branch_policy_due_info",
    "no": "branch_policy_due_info",
    },
    "hindi": {
    "हाँ, मैं व्यस्त हूँ": "not_interested_branch",
    "व्यस्त हूँ": "not_interested_branch",
    "हाँ": "not_interested_branch",
    "नहीं, मैं फ्री हूँ": "branch_policy_due_info",
    "मैं फ्री हूँ": "branch_policy_due_info",
    "नहीं": "branch_policy_due_info",
    "फ्री हूँ": "branch_policy_due_info",
    },
    "marathi": {
    "हो, मी व्यस्त आहे": "not_interested_branch",
    "मी बिझी आहे": "not_interested_branch",
    "हो": "not_interested_branch",
    "नाही, मी मोकळा आहे": "branch_policy_due_info",
    "मी मोकळा आहे": "branch_policy_due_info",
    "मोकळा आहे": "branch_policy_due_info",
    "नाही": "branch_policy_due_info",
    },
   "gujarati": {
    "હા, હું વ્યસ્ત છું": "not_interested_branch",
    "હું વ્યસ્ત છું": "not_interested_branch",
    "હા": "not_interested_branch",
    "ના, હું ફ્રી છું": "branch_policy_due_info",
    "હું ફ્રી છું": "branch_policy_due_info",

    "ના": "branch_policy_due_info",
    "ફ્રી છું": "branch_policy_due_info",
  },
  "fallback": "branch_busy_check"
},
},
"branch_callback_offer": {
    "text":{
  "english": "Would you like me to call you back later?",
  "hindi": "क्या आप चाहते हैं कि मैं आपको बाद में कॉल करूं?",
  "marathi": "तुम्हाला वाटतं का की मी तुम्हाला नंतर कॉल करू?",   
  "gujarati": "શું તમે ઇચ્છો છો કે હું તમને પછીથી ફોન કરું?",
},
  "options": {
    "english": {
    "yes call me later": "branch_callback_time",
    "yes": "branch_callback_time",
    "ok": "branch_callback_time",
    "no don't call": "branch_closure",
    "no": "branch_closure",
    },
    "hindi": {
    "हाँ बाद में कॉल करो": "branch_callback_time",
    "हाँ": "branch_callback_time",
    "ठीक है": "branch_callback_time",
    "नहीं कॉल मत करना": "branch_closure",
    "नहीं": "branch_closure",
    },
    "marathi": {
    "हो नंतर कॉल करा": "branch_callback_time",
    "हो": "branch_callback_time",
    "ठीक आहे": "branch_callback_time",
    "नको कॉल करू नका": "branch_closure",
    "नको": "branch_closure",
    },
   "gujarati": {
    "હા પછી કોલ કરો": "branch_callback_time",
    "હા": "branch_callback_time",
    "સારો છે": "branch_callback_time",
    "ના કોલ કરશો નહીં": "branch_closure",
    "ના": "branch_closure",
  },
  "fallback": "not_interested_branch"
},
},
"branch_callback_time": {
    "text":{
    "english": "Okay, i will call back later.Have a great day",
    "hindi": "ठीक है, कृपया वह समय बताइए जब आपको कॉल चाहिए।",
    "marathi": "ठीक आहे, कृपया तुम्हाला केव्हा कॉल हवा आहे ते सांगा.",
   "gujarati": "સારું, કૃપા કરીને તમારું સંકલન સમય જણાવો કે જ્યારે તમે ફોન આપવા ઇચ્છો છો.",
  },
  "followup": {
    "options": {
      "english": "Thank you. I will schedule your call at . Have a great day!",
      "hindi": "धन्यवाद। मैं आपकी कॉल  पर शेड्यूल कर दूंगी। आपका दिन शुभ हो!",
      "marathi": "धन्यवाद. मी तुमचा कॉल  ला शेड्यूल करेन. तुम्हाला शुभेच्छा!",
       "gujarati": "આભાર. હું તમારો કોલ  વાગે શેડ્યૂલ કરી દઇશ. તમારો દિવસ શુભ રહે!",
    },
  },
},
"branch_policy_due_info": {
    "text":{
  "english": "The due date for renewal premium payment was on {premium_due_date}. Grace period is over due to non-payment, and you're losing benefits. Would you like to know your policy's benefits if you resume paying?",
  "hindi": "नवीनीकरण प्रीमियम भुगतान की नियत तारीख {premium_due_date} थी। भुगतान न होने के कारण ग्रेस पीरियड समाप्त हो गया है और आपके लाभ समाप्त हो रहे हैं। क्या आप जानना चाहेंगे कि भुगतान फिर से शुरू करने पर आपको क्या लाभ मिलेंगे?",
  "marathi": "{premium_due_date} रोजी प्रीमियम भरण्याची अंतिम तारीख होती. वेळेत पैसे न भरल्यामुळे ग्रेस पीरियड संपला आहे आणि तुम्हाला लाभांचा तोटा होतो आहे. तुम्हाला पुन्हा पैसे भरल्यास काय फायदे मिळतील हे जाणून घ्यायचं आहे का?",   "gujarati": "પુનઃપ્રેમિયમ ચુકવણી માટેની ચુકવણી તારીખ {premium_due_date} હતી. ચુકવણી ન થવાને કારણે ગ્રેસ પિરિયડ સમાપ્ત થઈ ગયો છે અને તમે લાભ ગુમાવી રહ્યા છો. જો તમે ચુકવણી ફરી શરૂ કરો તો શું તમે તમારા પોલિસીના લાભો વિશે જાણવા માંગો છો?",
},
  "options": {
    "english": {
      "yes i want to know": "branch_benefits",
      "i want to know": "branch_benefits",
      "yes tell me": "branch_benefits",
      "tell me": "branch_benefits",
      "yes": "branch_benefits",
      "ok": "branch_benefits",
      "no i don’t want to": "convince_short",
      "no i am busy": "convince_short",
      "no": "convince_short",
    },
    "hindi": {
      "हाँ मुझे जानना है": "branch_benefits",
      "बताओ": "branch_benefits",
      "हाँ": "branch_benefits",
      "नहीं मैं नहीं चाहता": "convince_short",
      "नहीं": "convince_short",
      "अभी व्यस्त हूँ": "convince_short",
    },
    "marathi": {
      "हो मला माहिती हवी आहे": "branch_benefits",
      "हो सांगा": "branch_benefits",
      "हो": "branch_benefits",
      "नको मला माहिती नको": "convince_short",
      "नाही": "convince_short",
      "मी व्यस्त आहे": "convince_short",
    },   "gujarati": {
      "હા મને જાણવા ઇચ્છા છે": "branch_benefits",
      "હા કહો": "branch_benefits",
      "હા": "branch_benefits",
      "નહી મને નથી જાણવા": "convince_short",
      "નહીં": "convince_short",
      "હું વ્યસ્ત છું": "convince_short",
    },
  },
},
"branch_benefits": {
  "text": {
    "english": "You get maximum allocation in high-growth funds, loyalty additions worth ₹22,000, and full tax benefits under Sec 80C & 10(10D). Your effective return is already 11.47%, and charges reduce going forward. By paying now, your ₹10 lakh life cover is fully restored, and you avoid shifting to a low-interest inactive fund. Would you like to continue and make the premium payment now?",
    
    "hindi": "आपको हाई-ग्रोथ फंड्स में अधिकतम आवंटन, ₹22,000 की लॉयल्टी ऐडिशन्स और सेक्शन 80C और 10(10D) के तहत पूरा टैक्स बेनिफिट मिलता है। आपकी रिटर्न पहले से ही 11.47% है, और आगे चार्जेस कम हो जाते हैं। अभी भुगतान करने पर, ₹10 लाख का लाइफ कवर पूरी तरह से बहाल हो जाएगा और आप कम ब्याज वाले फंड में शिफ्ट होने से बचेंगे। क्या आप प्रीमियम का भुगतान करना चाहते हैं?",
    
    "marathi": "आपल्याला उच्च-वाढीच्या फंडांमध्ये जास्तीत जास्त वाटप, ₹22,000 ची लॉयल्टी अ‍ॅडिशन आणि सेक्शन 80C आणि 10(10D) अंतर्गत कर सवलत मिळते. तुमचा परतावा 11.47% आहे आणि शुल्क कमी होईल. तुम्ही आता पेमेंट केल्यास ₹10 लाखचे लाईफ कव्हर पुन्हा मिळेल. तुम्हाला पेमेंट करायचे आहे का?",
    
   "gujarati": "તમને હાઇ ગ્રોથ ફંડમાં વધુ ફાળો મળે છે, ₹22,000 લોયલ્ટી બોનસ અને 80C અને 10(10D) હેઠળ પૂરો ટેક્સ લાભ મળે છે. તમારું રિટર્ન પહેલેથી જ 11.47% છે અને ચાર્જ ઓછા થશે. તમે હવે પેમેન્ટ કરશો તો ₹10 લાખનો લાઇફ કવર ફરીથી સક્રિય થશે. શું તમે હવે પેમેન્ટ કરશો?",
  },
  "options": {
    "english": {
      "yes i will pay": "branch_payment_mode",
      "yes": "branch_payment_mode",
      "ok": "branch_payment_mode",
      "yes i will": "branch_payment_mode",
      "i will pay": "branch_payment_mode",
      "no i have already paid": "branch_payment_confirmation",
      "i already paid": "branch_payment_confirmation",
      "i have already paid": "branch_payment_confirmation",
      "no":"convince_short",
      "no i don’t want to": "convince_short",
      "no i am busy": "convince_short",
      "no": "convince_short",
    },
    "hindi": {
      "हाँ": "branch_payment_mode",
      "हाँ मैं पेमेंट करूंगा": "branch_payment_mode",
      "मैं पेमेंट करूंगा": "branch_payment_mode",
      "मैंने पहले ही भुगतान कर दिया है": "branch_payment_confirmation",
      "मैंने पहले ही पे किया है": "branch_payment_confirmation",
      "नहीं मैं नहीं चाहता": "convince_short",
      "नहीं": "convince_short",
      "अभी व्यस्त हूँ": "convince_short",
    },
    "marathi": {
      "होय मी पेमेंट करेन": "branch_payment_mode",
      "होय": "branch_payment_mode",
      "मी पेमेंट करेन": "branch_payment_mode",
      "मी आधीच पेमेंट केलंय": "branch_payment_confirmation",
       "नको मला माहिती नको": "convince_short",
      "नाही": "convince_short",
      "मी व्यस्त आहे": "convince_short",
    },
   "gujarati": {
      "હા": "branch_payment_mode",
      "હા હું પેમેન્ટ કરીશ": "branch_payment_mode",
      "હું પેમેન્ટ કરીશ": "branch_payment_mode",
      "હું પહેલેથી જ પેમેન્ટ કર્યું છે": "branch_payment_confirmation",
      "મારે પહેલેથી જ ચૂકવણી કરી છે": "branch_payment_confirmation",
       "નહી મને નથી જાણવા": "convince_short",
      "નહીં": "convince_short",
      "હું વ્યસ્ત છું": "convince_short",
    },
  },
  "fallback": "branch_benefits"
},
"branch_payment_mode": {
  "text": {
    "english": "How will you make the payment? Cash, cheque, or online?",
    "hindi": "आप कैसे भुगतान करेंगे? नकद, चेक या ऑनलाइन?",
    "marathi": "तुम्ही पैसे कसे भरणार? रोख, चेक की ऑनलाइन?",
   "gujarati": "તમે ચુકવણી કેવી રીતે કરશો? રોકડ, ચેક કે ઓનલાઈન?",
  },
  "options": {
    "english": {
      "cash": "confirm_payment_cash",
      "cheque": "confirm_payment_cash",
      "check": "confirm_payment_cash",
      "online": "branch_payment_online",
      "google pay": "branch_payment_online",
      "phonepe": "branch_payment_online",
      "upi": "branch_payment_online",
      "branch visit": "branch_offline_option",
    },
    "hindi": {
      "नकद": "confirm_payment_cash",
      "नकद से करूंगा": "confirm_payment_cash",
      "चेक": "confirm_payment_cash",
      "चेक से भुगतान करूंगा": "confirm_payment_cash",
      "ऑनलाइन": "branch_payment_online",
      "गूगल पे": "branch_payment_online",
      "फोनपे": "branch_payment_online",
      "गूगल पे से भुगतान": "branch_payment_online",
      "फोनपे से भुगतान": "branch_payment_online",
      "ब्रांच जाकर": "branch_offline_option",
    },
    "marathi": {
      "रोख": "confirm_payment_cash",
      "चेक": "confirm_payment_cash",
      "ऑनलाईन": "branch_payment_online",
      "गुगल पे": "branch_payment_online",
      "फोन पे": "branch_payment_online",
      "ब्रँचमध्ये जाऊन": "branch_offline_option",
    },
   "gujarati": {
      "રોકડ": "confirm_payment_cash",
      "ચેક": "confirm_payment_cash",
      "ઑનલાઇન": "branch_payment_online",
      "ગૂગલ પે": "branch_payment_online",
      "ફોનપે": "branch_payment_online",
      "શાખામાં જઈને": "branch_offline_option",
    },
  },
  "fallback": "branch_payment_mode"
},
"confirm_payment_cash": {
  "text": {
    "english": "Thank you. Ensure cash is paid at the branch. Would you like to know more about premium details, fund allocation and performance, growth values, switch to safe funds, market fall, stop paying, emergency financial and medical needs, current returns, or new policy?",
    "hindi": "धन्यवाद। कृपया शाखा में नकद भुगतान सुनिश्चित करें। क्या आप प्रीमियम विवरण, फंड आवंटन और प्रदर्शन, ग्रोथ वैल्यू, सुरक्षित फंड में स्विच, मार्केट गिरावट, भुगतान रोकना, आपातकालीन वित्तीय और चिकित्सा आवश्यकताओं, वर्तमान रिटर्न या नई पॉलिसी के बारे में अधिक जानना चाहेंगे?",
    "marathi": "धन्यवाद. कृपया शाखेत रोखीचा भरणा पूर्ण झाल्याची खात्री करा. तुम्हाला प्रीमियम तपशील, फंड वाटप आणि कामगिरी, वाढीचे मूल्य, सुरक्षित फंडमध्ये स्विच, मार्केट घसरण, भरणा थांबवणे, आपत्कालीन आर्थिक आणि वैद्यकीय गरजा, सध्याचे परतावे किंवा नवीन पॉलिसी याबद्दल अधिक जाणून घ्यायचं आहे का?",
   "gujarati": "આભાર. ખાતરી કરો કે શાખામાં રોકડ ચુકવણી કરવામાં આવી છે. શું તમે પ્રીમિયમ વિગતો, ફંડ ફાળવણી અને કાર્યક્ષમતા, વૃદ્ધિ મૂલ્ય, સુરક્ષિત ફંડમાં સ્વિચ, માર્કેટ પતન, ચુકવણી અટકાવવી, તાત્કાલિક નાણાકીય અને તબીબી જરૂરિયાતો, વર્તમાન વળતરો અથવા નવી પોલિસી વિશે વધુ જાણવામાં રસ ધરાવો છો?",
  },
  "options": {
    "english": {
      "yes": "faq_offer_more_info",
      "premium details": "faq_premium_answer",
      "premium detail": "faq_premium_answer",
      "fund": "faq_fund_answer",
      "fund allocation": "faq_fund_answer",
      "performance": "faq_fund_answer",
      "growth": "faq_growth_answer",
      "values": "faq_growth_answer",
      "safe": "faq_safe_fund_answer",
      "safe funds": "faq_safe_fund_answer",
      "safe fund": "faq_safe_fund_answer",
      "save funds": "faq_safe_fund_answer",
      "market": "faq_market_wait_answer",
      "fall": "faq_market_wait_answer",
      "market fall": "faq_market_wait_answer",
      "single": "faq_single_premium_answer",
      "stop paying": "faq_single_premium_answer",
      "emergency": "faq_emergency_answer",
      "financial": "faq_emergency_answer",
      "financial and medical needs": "faq_emergency_answer",
      "new policy": "faq_new_policy_answer",
      "mutual fund": "faq_mutual_fund_answer",
      "mutual": "faq_mutual_fund_answer",
      "returns": "faq_low_return_answer",
      "current returns": "faq_low_return_answer",
      "no": "faq_end",
      "i don't want": "faq_end",
    },
    "hindi": {
      "हाँ": "faq_offer_more_info",
      "प्रीमियम विवरण": "faq_premium_answer",
      "प्रीमियम डिटेल": "faq_premium_answer",
      "फंड": "faq_fund_answer",
      "फंड आवंटन": "faq_fund_answer",
      "प्रदर्शन": "faq_fund_answer",
      "ग्रोथ": "faq_growth_answer",
      "मूल्य": "faq_growth_answer",
      "सुरक्षित": "faq_safe_fund_answer",
      "सुरक्षित फंड": "faq_safe_fund_answer",
      "बाजार": "faq_market_wait_answer",
      "गिरावट": "faq_market_wait_answer",
      "पतन": "faq_market_wait_answer",
      "एकल": "faq_single_premium_answer",
      "भुगतान बंद करें": "faq_single_premium_answer",
      "आपातकालीन": "faq_emergency_answer",
      "वित्तीय": "faq_emergency_answer",
      "मुझे नहीं चाहिए": "faq_end",
      "नई पॉलिसी": "faq_new_policy_answer",
      "म्यूचुअल फंड": "faq_mutual_fund_answer",
      "रिटर्न्स": "faq_low_return_answer",
      "नहीं": "faq_end",
    },
    "marathi": {
      "हा": "faq_offer_more_info",
      "प्रीमियम तपशील": "faq_premium_answer",
      "फंड वाटप": "faq_fund_answer",
      "कामगिरी": "faq_fund_answer",
      "वाढ": "faq_growth_answer",
      "मूल्य": "faq_growth_answer",
      "सुरक्षित निधी": "faq_safe_fund_answer",
      "मार्केट": "faq_market_wait_answer",
      "बाजार पडझड": "faq_market_wait_answer",
      "भरणा थांबवा": "faq_single_premium_answer",
      "आपत्कालीन": "faq_emergency_answer",
      "आर्थिक गरजा": "faq_emergency_answer",
      "सध्याचे परतावे": "faq_low_return_answer",
      "नको": "faq_end",
      "नवीन पॉलिसी": "faq_new_policy_answer",
    },
   "gujarati": {
      "હા": "faq_offer_more_info",
      "પ્રીમિયમ વિગતો": "faq_premium_answer",
      "ફંડ ફાળવણી": "faq_fund_answer",
      "કાર્યક્ષમતા": "faq_fund_answer",
      "મૂલ્ય": "faq_growth_answer",
      "સુરક્ષિત": "faq_safe_fund_answer",
      "બજાર": "faq_market_wait_answer",
      "પતન": "faq_market_wait_answer",
      "ચુકવણી બંધ કરો": "faq_single_premium_answer",
      "તાત્કાલિક": "faq_emergency_answer",
      "મને નથી જોઈએ": "faq_end",
      "નવી પોલિસી": "faq_new_policy_answer",
      "મ્યુચ્યુઅલ ફંડ": "faq_mutual_fund_answer",
      "વર્તમાન વળતરો": "faq_low_return_answer",
    },
  },
  "fallback": "faq_offer_more_info"
},
 "faq_premium_answer": {
  "text": {
    "english": "Premium – ₹1L\nFrequency – Yearly\nSum Assured – ₹10L\nTerm – 10Y\nPPT – 7Y\nDue – 25 Sep 2024\nFund – ₹5.53L\nPaid – ₹4L\nReturns – 11.47%\nCharges – 3.89%\nLoyalty – ₹22K",
    "hindi": "प्रीमियम – ₹1 लाख\nआवृत्ति – वार्षिक\nबीमा राशि – ₹10 लाख\nमीयाद – 10 वर्ष\nभुगतान अवधि – 7 वर्ष\nअगली तिथि – 25 सितम्बर 2024\nफंड – ₹5.53 लाख\nभुगतान – ₹4 लाख\nरिटर्न – 11.47%\nशुल्क – 3.89%\nलॉयल्टी – ₹22 हजार",
    "marathi": "प्रीमियम – ₹1 लाख\nवारंवारता – वार्षिक\nहमी रक्कम – ₹10 लाख\nकालावधी – 10 वर्षे\nप्रिमियम पेमेंट कालावधी – 7 वर्षे\nदेय तारीख – 25 सप्टेंबर 2024\nफंड – ₹5.53 लाख\nभरलेले – ₹4 लाख\nपरतावा – 11.47%\nशुल्क – 3.89%\nनिष्ठा बोनस – ₹22 हजार",
   "gujarati": "પ્રિમિયમ – ₹1 લાખ\nવાર્ષિકતા – વર્ષમાં એક વખત\nસમ આશ્વાસન – ₹10 લાખ\nઅવધિ – 10 વર્ષ\nપેમેન્ટ પીરિયડ – 7 વર્ષ\nડ્યૂ તારીખ – 25 સપ્ટેમ્બર 2024\nફંડ – ₹5.53 લાખ\nચૂકવણી – ₹4 લાખ\nરિટર્ન – 11.47%\nચાર્જેસ – 3.89%\nલોયલ્ટી – ₹22 હજાર",
  },
  "next": "faq_end"
},
"faq_fund_answer": {
  "text": {
    "english": "Your current fund value is ₹5.53 lakhs. Fund performance is regularly updated on our website.",
    "hindi": "आपकी वर्तमान फंड वैल्यू ₹5.53 लाख है। फंड की परफॉर्मेंस नियमित रूप से हमारी वेबसाइट पर अपडेट होती है।",
    "marathi": "आपली वर्तमान फंड व्हॅल्यू ₹5.53 लाख आहे. फंडचे कामगिरी नियमितपणे आमच्या वेबसाइटवर अपडेट केली जाते.",
   "gujarati": "તમારું હાલનું ફંડ મૂલ્ય ₹5.53 લાખ છે. ફંડની કામગીરી અમારી વેબસાઈટ પર નિયમિતપણે અપડેટ થાય છે.",
  },
  "next": "faq_end"
},
"faq_growth_answer": {
  "text": {
    "english": "You’ve gained 11.47% effective annual returns after all charges. You can switch funds anytime based on your goals.",
    "hindi": "आपको सभी शुल्कों के बाद 11.47% की वार्षिक रिटर्न प्राप्त हुई है। आप अपनी जरूरतों के अनुसार कभी भी फंड बदल सकते हैं।",
    "marathi": "सर्व शुल्कानंतर आपल्याला 11.47% वार्षिक परतावा मिळाला आहे. आपण आपल्या उद्दिष्टांनुसार कधीही फंड बदलू शकता.",
   "gujarati": "તમને તમામ શુલ્કો પછી 11.47% વાર્ષિક રિટર્ન મળ્યું છે. તમે તમારા લક્ષ્યાંક મુજબ કોઈપણ સમયે ફંડ બદલી શકો છો.",
  },
  "next": "faq_end"
},
 "faq_market_wait_answer": {
  "text": {
    "english": "Markets are currently volatile. You may stay invested or shift to a safe fund to protect your capital.",
    "hindi": "फिलहाल बाजार अस्थिर हैं। आप निवेशित रह सकते हैं या अपनी पूंजी की सुरक्षा के लिए सुरक्षित फंड में स्थानांतरित कर सकते हैं।",
    "marathi": "सध्या बाजारात अस्थिरता आहे. आपण गुंतवणूक सुरू ठेवू शकता किंवा आपल्या भांडवलाच्या सुरक्षेसाठी सुरक्षित फंडमध्ये स्थलांतर करू शकता.",
   "gujarati": "હાલમાં બજાર અસ્થિર છે. તમે રોકાણ ચાલુ રાખી શકો છો અથવા તમારા મૂડીની સુરક્ષા માટે સલામત ફંડમાં બદલાવી શકો છો.",
  },
  "next": "faq_end"
},
"faq_safe_fund_answer": {
  "text": {
    "english": "The safe fund helps protect capital with minimal risk. You can switch to it anytime at no extra cost.",
    "hindi": "सेफ फंड न्यूनतम जोखिम के साथ पूंजी की सुरक्षा में मदद करता है। आप किसी भी समय बिना अतिरिक्त लागत के इसमें स्विच कर सकते हैं।",
    "marathi": "सेफ फंड किमान जोखमीसह भांडवलाचे संरक्षण करण्यास मदत करतो. आपण कधीही अतिरिक्त खर्च न करता यामध्ये स्विच करू शकता.",
   "gujarati": "સેફ ફંડ ઓછી જોખમ સાથે મૂડીની સુરક્ષા કરવામાં મદદ કરે છે. તમે કોઈ વધારાના ખર્ચ વિના ક્યારે પણ તેમાં સ્વિચ કરી શકો છો.",
  },
  "next": "faq_end"
},
"faq_single_premium_answer": {
  "text": {
    "english": "In a single premium policy, you pay only once. Your current policy offers flexible payments and loyalty benefits.",
    "hindi": "सिंगल प्रीमियम पॉलिसी में आपको एक बार में भुगतान करना होता है। आपकी मौजूदा पॉलिसी में फ्लेक्सिबल पेमेंट और लॉयल्टी जैसे फायदे मिलते हैं।",
    "marathi": "सिंगल प्रीमियम पॉलिसीमध्ये एकदाच पेमेंट करावे लागते. तुमच्या विद्यमान पॉलिसीत लवचिक पेमेंट आणि लॉयल्टीचे फायदे आहेत.",
   "gujarati": "સિંગલ પ્રીમીયમ પોલિસીમાં તમને માત્ર એકવાર ચુકવણી કરવાની હોય છે. તમારી હાલની પોલિસી લવચીક પેમેન્ટ અને લોયલ્ટી જેવા લાભ આપે છે.",
  },
  "next": "faq_end"
},
"faq_emergency_answer": {
  "text": {
    "english": "In emergencies, you can apply for partial withdrawal or loan based on your fund value.",
    "hindi": "आप इमरजेंसी में अपने फंड वैल्यू के आधार पर आंशिक निकासी या लोन के लिए आवेदन कर सकते हैं।",
    "marathi": "आपत्कालीन स्थितीत तुम्ही तुमच्या फंड व्हॅल्यूवर आधारित अंशतः पैसे काढू शकता किंवा कर्जासाठी अर्ज करू शकता.",
   "gujarati": "એમરજન્સી દરમિયાન તમે ફંડ મૂલ્યના આધારે અંશતઃ વિથડ્રોઅલ અથવા લોન માટે અરજી કરી શકો છો.",
  },
  "next": "faq_end"
},
"faq_new_policy_answer": {
  "text": {
    "english": "New ULIP policies have higher initial charges. Your current policy has only 1.61% charges and includes loyalty benefits.",
    "hindi": "नई ULIP पॉलिसियों में शुरूआती चार्जेस ज़्यादा होते हैं। आपकी मौजूदा पॉलिसी में चार्ज सिर्फ 1.61% है और इसमें लॉयल्टी बेनिफिट्स भी मिलते हैं।",
    "marathi": "नवीन ULIP पॉलिसींमध्ये सुरुवातीचे शुल्क जास्त असते. तुमच्या सध्याच्या पॉलिसीमध्ये केवळ 1.61% शुल्क आहे आणि लॉयल्टी फायदे मिळतात.",
   "gujarati": "નવી ULIP પોલિસીઓમાં પ્રારંભિક ચાર્જ વધુ હોય છે. તમારી હાલની પોલિસીમાં ફક્ત 1.61% ચાર્જ છે અને તેમાં લોયલ્ટી લાભો પણ શામેલ છે.",
  },
  "next": "faq_end"
},
"faq_mutual_fund_answer": {
  "text": {
    "english": "Mutual funds cost about 2% and offer no life cover. Your policy has only 1.61% charge, ₹10 lakh life cover, and ₹22,000 loyalty benefit.",
    "hindi": "म्यूचुअल फंड्स में लगभग 2% खर्च होता है और कोई लाइफ कवर नहीं होता। आपकी पॉलिसी में सिर्फ 1.61% चार्ज है, ₹10 लाख लाइफ कवर और ₹22,000 लॉयल्टी बेनिफिट है।",
    "marathi": "म्युच्युअल फंडमध्ये सुमारे 2% खर्च येतो आणि कोणतेही लाईफ कव्हर मिळत नाही. तुमच्या पॉलिसीमध्ये फक्त 1.61% शुल्क आहे, ₹10 लाखांचे लाईफ कव्हर आणि ₹22,000 लॉयल्टी लाभ आहेत.",
   "gujarati": "મ્યુચ્યુઅલ ફંડમાં આશરે 2% ખર્ચ થાય છે અને કોઈ લાઇફ કવર મળતું નથી. તમારી પોલિસીમાં ફક્ત 1.61% ચાર્જ, ₹10 લાખ લાઇફ કવર અને ₹22,000 લોયલ્ટી લાભ છે.",
  },
  "next": "faq_end"
},
"faq_low_return_answer": {
  "text": {
    "english": "You’re getting 11.47% annual return after all charges. Later, your charges will reduce to 1.61%. If not satisfied, you can switch funds.",
    "hindi": "आपको सभी चार्ज के बाद 11.47% सालाना रिटर्न मिल रहा है। आगे चलकर आपके चार्ज कम होकर 1.61% हो जाएंगे। अगर संतुष्ट नहीं हैं, तो फंड स्विच कर सकते हैं।",
    "marathi": "सर्व शुल्क वजा जाता, तुम्हाला 11.47% वार्षिक परतावा मिळत आहे. पुढे तुमचे शुल्क 1.61% पर्यंत कमी होतील. समाधान नसेल तर तुम्ही फंड स्विच करू शकता.",
   "gujarati": "તમને બધા ચાર્જ બાદ 11.47% વાર્ષિક રિટર્ન મળી રહ્યો છે. આગળ ચાલીને તમારા ચાર્જ 1.61% પર આવી જશે. જો સંતોષ ન હોય, તો ફંડ સ્વીચ કરી શકો છો.",
  },
  "next": "faq_end"
},
"faq_offer_more_info": {
  "text": {
    "english": "Do you want to know more about premium details, fund allocation and performance, growth values, switch to safe funds, market fall, single premium, emergency financial and medical needs, current returns, or new policy?",
    "hindi": "क्या आप प्रीमियम डिटेल्स, फंड अलोकेशन और प्रदर्शन, ग्रोथ वैल्यू, सुरक्षित फंड में बदलाव, मार्केट गिरावट, सिंगल प्रीमियम, इमरजेंसी जरूरतें, वर्तमान रिटर्न या नई पॉलिसी के बारे में और जानना चाहेंगे?",
    "marathi": "तुम्हाला प्रीमियम तपशील, फंड वाटप आणि कामगिरी, ग्रोथ व्हॅल्यूज, सुरक्षित फंडमध्ये बदल, मार्केट घसरण, सिंगल प्रीमियम, आपत्कालीन गरजा, सध्याचे रिटर्न्स किंवा नवीन पॉलिसीबद्दल अधिक जाणून घ्यायचं आहे का?",
   "gujarati": "શું તમે પ્રીમિયમ વિગતો, ફંડ ફાળવણી અને કાર્યક્ષમતા, વૃદ્ધિ મૂલ્ય, સુરક્ષિત ફંડમાં સ્વિચ, માર્કેટ ઘટી જવું, સિંગલ પ્રીમિયમ, તાત્કાલિક આવશ્યકતાઓ, વર્તમાન રિટર્ન્સ અથવા નવી પોલિસી વિશે વધુ જાણવા માંગો છો?",
  },
  "options": {
    "english": {
      "yes": "faq_offer_more_info",
      "premium": "faq_premium_answer",
      "premium detail": "faq_premium_answer",
      "fund": "faq_fund_answer",
      "fund allocation": "faq_fund_answer",
      "performance": "faq_fund_answer",
      "perfomance": "faq_fund_answer",
      "growth": "faq_growth_answer",
      "growth values": "faq_growth_answer",
      "values": "faq_growth_answer",
      "safe": "faq_safe_fund_answer",
      "safe funds": "faq_safe_fund_answer",
      "market": "faq_market_wait_answer",
      "market fall": "faq_market_wait_answer",
      "single": "faq_single_premium_answer",
      "stop paying": "faq_single_premium_answer",
      "single premium policy": "faq_single_premium_answer",
      "emergency": "faq_emergency_answer",
      "financial": "faq_emergency_answer",
      "financial and medical needs": "faq_emergency_answer",
      "new policy": "faq_new_policy_answer",
      "mutual fund": "faq_mutual_fund_answer",
      "mutual": "faq_mutual_fund_answer",
      "returns": "faq_low_return_answer",
      "current return": "faq_low_return_answer",
      "no": "branch_closure",
      "i dont want": "branch_closure",
    },
    "hindi": {
      "हाँ": "faq_offer_more_info",
      "प्रीमियम": "faq_premium_answer",
      "प्रीमियम डिटेल": "faq_premium_answer",
      "फंड": "faq_fund_answer",
      "फंड अलोकेशन": "faq_fund_answer",
      "प्रदर्शन": "faq_fund_answer",
      "ग्रोथ": "faq_growth_answer",
      "वाढीचे मूल्य": "faq_growth_answer",
      "सुरक्षित फंड": "faq_safe_fund_answer",
      "सुरक्षित": "faq_safe_fund_answer",
      "मार्केट": "faq_market_wait_answer",
      "बाजार": "faq_market_wait_answer",
      "सिंगल": "faq_single_premium_answer",
      "सिंगल प्रीमियम": "faq_single_premium_answer",
      "एकरकमी": "faq_single_premium_answer",
      "आपातकाल": "faq_emergency_answer",
      "नई पॉलिसी": "faq_new_policy_answer",
      "म्यूचुअल": "faq_mutual_fund_answer",
      "म्युच्युअल फंड": "faq_mutual_fund_answer",
      "रिटर्न": "faq_low_return_answer",
      "वर्तमान रिटर्न": "faq_low_return_answer",
      "नहीं": "branch_closure",
      "नही चाहता": "branch_closure",
    },
    "marathi": {
      "हो": "faq_offer_more_info",
      "प्रीमियम तपशील": "faq_premium_answer",
      "फंड वाटप": "faq_fund_answer",
      "कामगिरी": "faq_fund_answer",
      "वाढीचे मूल्य": "faq_growth_answer",
      "सुरक्षित फंड": "faq_safe_fund_answer",
      "मार्केट": "faq_market_wait_answer",
      "सिंगल": "faq_single_premium_answer",
      "एकरकमी": "faq_single_premium_answer",
      "आपत्कालीन गरजा": "faq_emergency_answer",
      "नवीन पॉलिसी": "faq_new_policy_answer",
      "म्युच्युअल फंड": "faq_mutual_fund_answer",
      "परतावा": "faq_low_return_answer",
      "नको": "branch_closure",
    },
   "gujarati": {
      "હા": "faq_offer_more_info",
      "પ્રીમિયમ": "faq_premium_answer",
      "ફંડ ફાળવણી": "faq_fund_answer",
      "કાર્યક્ષમતા": "faq_fund_answer",
      "વૃદ્ધિ મૂલ્ય": "faq_growth_answer",
      "સુરક્ષિત": "faq_safe_fund_answer",
      "માર્કેટ": "faq_market_wait_answer",
      "એકમૂશત": "faq_single_premium_answer",
      "સિંગલ પ્રીમિયમ": "faq_single_premium_answer",
      "તાત્કાલિક જરૂરિયાતો": "faq_emergency_answer",
      "નવી પોલિસી": "faq_new_policy_answer",
      "મ્યુચ્યુઅલ ફંડ": "faq_mutual_fund_answer",
      "વર્તમાન રિટર્ન": "faq_low_return_answer",
      "ના": "branch_closure",
    },
  },
  "fallback": "faq_offer_more_info"
},
 "faq_end": {
  "english": {
    "english": "That's all. Do you want to replay the questions?",
    "hindi": "बस इतना ही। क्या आप प्रश्नों को फिर से सुनना चाहेंगे?",
    "marathi": "एवढंच. तुम्हाला प्रश्न पुन्हा ऐकायचे आहेत का?",
   "gujarati": "અટલૂં જ. શું તમે પ્રશ્નો ફરી સાંભળવા ઈચ્છો છો?",
  },
  "options": {
    "english": ["yes", "replay", "again", "ok", "no", "bye"],
    "hindi": ["हाँ", "हां", "फिर से", "ठीक है", "नहीं", "अलविदा"],
    "marathi": ["हो", "परत", "बरं", "नको", "बाय"],
   "gujarati": ["હા", "ફરીથી", "બરાબર", "ના", "બાય"]
  },
  "map": {
    "faq_offer_more_info": ["yes", "replay", "again", "ok", "हाँ", "हां", "फिर से", "ठीक है", "हो", "परत", "बरं", "હા", "ફરીથી", "બરાબર"],
    "branch_closure": ["no", "bye", "नहीं", "अलविदा", "नको", "बाय", "ના", "બાય"]
  },
  "fallback": "faq_end"
},
"branch_payment_confirmation": {
  "text": {
    "english": "Thanks for the payment. Could you share when and how you made the payment, and the transaction ID or cheque number?",
    "hindi": "भुगतान के लिए धन्यवाद। कृपया बताएं कि आपने भुगतान कब और कैसे किया, और लेनदेन आईडी या चेक नंबर क्या है?",
    "marathi": "भरणा केल्याबद्दल धन्यवाद. कृपया सांगा की तुम्ही भरणा कधी आणि कसा केला, आणि व्यवहार आयडी किंवा चेक क्रमांक काय आहे?",
   "gujarati": "ચુકવણી માટે આભાર. તમે ક્યારે અને કેવી રીતે ચુકવણી કરી અને ટ્રાન્ઝેક્શન આઈડી અથવા ચેક નંબર શું છે કૃપા કરીને જણાવો?",
  },
  "options": {
    "english": ["done", "paid", "submitted", "yes"],
    "hindi": ["हाँ", "हां", "कर दिया", "भेज दिया"],
    "marathi": ["होय", "भरले", "पैसे दिले"],
   "gujarati": ["હા", "ચૂકવણી કરી", "પેઇડ"],
  },
  "map": {
    "faq_offer_more_info": ["done", "paid", "submitted", "yes", "हाँ", "हां", "कर दिया", "भेज दिया", "होय", "भरले", "पैसे दिले", "હા", "ચૂકવણી કરી", "પેઇડ"]
  },
  "next": "faq_offer_more_info",
  "fallback": "branch_closure"
},
"branch_payment_online": {
  "text": {
    "english": "We will send you a link. Please pay today to retain your benefits. Would you like to know more about your policy?",
    "hindi": "हम आपको एक लिंक भेजेंगे। कृपया आज ही भुगतान करें ताकि आपके लाभ बने रहें। क्या आप अपनी पॉलिसी के बारे में और जानना चाहेंगे?",
    "marathi": "आम्ही तुम्हाला एक लिंक पाठवू. कृपया आजच भरणा करा जेणेकरून तुमचे फायदे चालू राहतील. तुम्हाला पॉलिसीबद्दल अधिक माहिती हवी आहे का?",
   "gujarati": "અમે તમને એક લિંક મોકલશું. કૃપા કરીને આજે જ ચૂકવણી કરો જેથી કરીને તમારા ફાયદા ચાલુ રહે. શું તમે તમારા પૉલિસી વિશે વધુ જાણવા માંગો છો?",
  },
  "options": {
    "english": {
      "yes": "faq_offer_more_info",
      "no": "faq_end"
    },
    "hindi": {
      "हाँ": "faq_offer_more_info",
      "हां": "faq_offer_more_info",
      "नहीं": "faq_end",
      "ना": "faq_end"
    },
    "marathi": {
      "होय": "faq_offer_more_info",
      "नाही": "faq_end"
    },
   "gujarati": {
      "હા": "faq_offer_more_info",
      "ના": "faq_end"
    },
  },
  "fallback": "faq_offer_more_info"
},
"branch_offline_option": {
  "text": {
    "english": "You can also pay by visiting the branch. But online payment is easier. Want to know more about your policy?",
    "hindi": "आप शाखा में जाकर भी भुगतान कर सकते हैं, लेकिन ऑनलाइन भुगतान करना आसान है। क्या आप अपनी पॉलिसी के बारे में और जानना चाहेंगे?",
    "marathi": "आपण शाखेत जाऊनही पैसे भरू शकता, पण ऑनलाइन पेमेंट सोपे आहे. तुम्हाला पॉलिसीबद्दल अधिक माहिती हवी आहे का?",
   "gujarati": "તમે શાખા પર જઈને પણ ચુકવણી કરી શકો છો, પરંતુ ઑનલાઇન પેમેન્ટ સરળ છે. શું તમે તમારી પૉલિસી વિશે વધુ જાણવા માંગો છો?",
  },
  "options": {
    "english": {
      "yes": "faq_offer_more_info",
      "no": "faq_end"
    },
    "hindi": {
      "हाँ": "faq_offer_more_info",
      "हां": "faq_offer_more_info",
      "नहीं": "faq_end",
      "ना": "faq_end"
    },
    "marathi": {
      "होय": "faq_offer_more_info",
      "नाही": "faq_end"
    },
   "gujarati": {
      "હા": "faq_offer_more_info",
      "ના": "faq_end"
    }
  },
  "fallback": "faq_offer_more_info"
},
"branch_closure": {
  "text": {
    "english": "Alright, no problem at all. But don’t miss the valuable benefits in your policy. If you need any help or have questions, call us anytime at 1800-258-0000. Take care and have a lovely day!",
    "hindi": "अगर आपको और सहायता चाहिए, तो 1800 209 7272 पर कॉल करें या 8806727272 पर WhatsApp करें। आपका दिन शुभ हो!",
    "marathi": "अधिक मदतीसाठी कृपया 1800 209 7272 वर कॉल करा किंवा 8806727272 वर WhatsApp करा. आपला दिवस आनंददायी जावो!",
   "gujarati": "અગર તમને વધુ સહાયની જરૂર હોય, તો 1800 209 7272 પર કોલ કરો અથવા 8806727272 પર WhatsApp કરો. તમારો દિવસ શુભ રહે!",
  },
},
"convince_short": {
  "text": {
    "english": "It’ll just take 2 minutes. Please let me explain your benefits before you decide. Is that okay?",
    "hindi": "बस 2 मिनट लगेंगे। कृपया निर्णय लेने से पहले मैं आपके लाभ समझा दूं। क्या यह ठीक है?",
    "marathi": "फक्त 2 मिनिट लागतील. कृपया निर्णय घेण्यापूर्वी मी तुमचे फायदे समजावून सांगू दे. ठीक आहे का?",
    "gujarati": "માત્ર 2 મિનિટ લાગશે. કૃપા કરીને તમે નિર્ણય લો તે પહેલા હું તમારા ફાયદા સમજાવું. ઠીક છે?",
  },
  "options": {
    "english": {
      "yes": "policy_benefits",
      "ok": "policy_benefits",
      "no": "not_interested_branch",
      "no i dont want":"not_interested_branch",
      "not":"not_interested_branch",
      "ok tell me":"policy_benefits",
    },
    "hindi": {
      "हाँ": "policy_benefits",
      "ठीक है": "policy_benefits",
      "नहीं": "not_interested_branch",
    },
    "marathi": {
      "हो": "policy_benefits",
      "ठीक आहे": "policy_benefits",
      "नको": "not_interested_branch",
    },
    "gujarati": {
      "હા": "policy_benefits",
      "બરાબર": "policy_benefits",
      "ના": "not_interested_branch",
    }
  },
  "fallback": "convince_short"
},
"not_interested_branch": {
  "text": {
    "english": "This won’t take long—just 2 minutes. It’s about protecting your policy and avoiding future complications. May I explain once before you decide?",
    "hindi": "मैं समझता हूँ, लेकिन यह सिर्फ 2 मिनट का समय है और यह आपको बड़ा नुकसान होने से बचा सकता है। क्या मैं एक बार समझा दूँ?",
    "marathi": "माझं समजतंय, पण फक्त 2 मिनिट लागतील आणि यामुळे तुमचा मोठा तोटा टळू शकतो. मी एकदा समजावून सांगू का?",
    "gujarati": "હું સમજું છું, પરંતુ માત્ર 2 મિનિટ લાગશે અને તમે મોટું નુકસાન ટાળી શકો છો. શું હું એક વાર સમજાવું?",
  },
  "options": {
    "english": {
      "yes": "policy_benefits",
      "ok": "policy_benefits",
      "no": "branch_callback_offer",
      "no dont call": "branch_callback_offer",
      "no i dont want":"branch_callback_offer",
      "not":"branch_callback_offer",
    },
    "hindi": {
      "हाँ": "policy_benefits",
      "ठीक है": "policy_benefits",
      "नहीं": "branch_callback_offer",
    },
    "marathi": {
      "हो": "policy_benefits",
      "ठीक आहे": "policy_benefits",
      "नको": "branch_callback_offer",
    },
    "gujarati": {
      "હા": "policy_benefits",
      "બરાબર": "policy_benefits",
      "ના": "branch_callback_offer",
    },
  },
  "fallback": "not_interested_branch"
}
}
