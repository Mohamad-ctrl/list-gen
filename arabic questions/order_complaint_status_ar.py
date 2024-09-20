import pandas as pd
import itertools
from datetime import datetime

def generate_list():
    # Define the lists provided

    OrderstatusAR = [
        "حالة طلب المنتج",
        "حالة طلبي للمنتجات",
        "حالة طلب الشراء الأخير الخاص بي",
        "طلب الشراء عبر الانترنت",
        "طلب الشراء",
        "حالة المنتج الذي طلبته",
        "حالة طلبي المقدم أونلاين",
        "حالة طلب مبيعات",
        "تركيب الخط الثابت",
        "حالة طلبي لتركيب الخط الثابت المنزلي",
        "حالة طلب تفعيل الخدمات الثابتة المنزلية",
        "تركيب الخدمات الثابتة المنزلية",
        "تركيب خدمات منزلية"
    ]

    how_phrasesAR = ["كيف يمكنني", "كيف", "ممكن أعرف كيف", "شلون", "كيفية"]

    wantAr = ["أبغى", "أبي", "أريد", "أبا", "بدي", "ريد", "ودي", "أود", "أحتاج"]

    INTERROGATIVE_WORDSar = [
        "هل يمكنني", "هل يمكنك", "هل", "ما هي", "ما هو", "وش", "وش هي", "إيش", "ما هو", 
        "شنو", "شو هو", "شو هي", "شو", "قديش", "كم", "ماذا", "لماذا", "ليش"
    ]


    checkstatusar = [
        "معرفة",
        "تتبع",
        "أعرف حالته",
        "أعرف تفاصيل عن",
        "التحقق",
        "متابعة",
        "التحقق من",
        "أتابع",
        "حالة",
        "تتبع حالة"
    ]

    trackWayAr = [
        "معرف الطلب",
        "رمز الطلب",
        "رقم جوالي",
        "رقم الموبايل"
    ]


    ComplaintStatusAR = [
        "حالة شكواي",
        "الشكاوي",
        "حالة الشكوى الخاصة بي",
        "حالة شكواي المقدمة",
        "الشكوى التي أرسلتها",
        "تفاصيل شكواي",
        "تفاصيل الشكوى الخاصة بي",
        "وضع شكواي",
        "حالة التيكيت اللي فتحتها",
        "شكوى",
        "مشكلتي",
        "المشكلة التي أبلغت عنها",
        "بلغت عن مشكلة من قبل",
        "رفعت شكوى"
    ]

    # Define the utterance templates
    utterancesAR = [
        "{OrderstatusAR}",
        "{checkstatusar} الطلب",
        "{how_phrasesAR} {checkstatusar} {OrderstatusAR}",
        "متى بتوصلون {OrderstatusAR}",
        "ساعدني في {checkstatusar} {OrderstatusAR}",
        "{INTERROGATIVE_WORDSar} صار في {OrderstatusAR} الخاص بي",
        "قدمت طلب و {wantAr} {checkstatusar} من فضلك",
        "{wantAr} {checkstatusar} {OrderstatusAR}",
        "متى موعدي من أجل {OrderstatusAR}",
        "{wantAr} أعرف {OrderstatusAR}",
        "طلبت جهاز أونلاين و {wantAr} أعرف {OrderstatusAR}",
        "لم استلم طلبي حتى الآن أخبرني متى موعد الاستلام؟",
        "أين طلبي",
        "{OrderstatusAR} باستخدام {trackWayAr}",
        "{ComplaintStatusAR}",
        "{how_phrasesAR} {checkstatusar} {ComplaintStatusAR}",
        "ساعدني في {checkstatusar} {ComplaintStatusAR}",
        "{INTERROGATIVE_WORDSar} صار في {ComplaintStatusAR}",
        "ماذا عن {ComplaintStatusAR} ؟ متى سيتم الرد عليها؟",
        "متى بتحلون {ComplaintStatusAR}؟",
        "{wantAr} {checkstatusar} {ComplaintStatusAR}",
        "{wantAr} معلومات عن {ComplaintStatusAR}",
        "{ComplaintStatusAR} {INTERROGATIVE_WORDSar} جار العمل عليها"
    ]

    # Prepare a list of all lists for placeholders
    placeholder_listsAR = {
        "OrderstatusAR": OrderstatusAR, 
        "how_phrasesAR": how_phrasesAR,
        "wantAr": wantAr,
        "INTERROGATIVE_WORDSar": INTERROGATIVE_WORDSar,
        "checkstatusar": checkstatusar,
        "trackWayAr": trackWayAr,
        "ComplaintStatusAR": ComplaintStatusAR
    }

    # Generate all combinations and remove duplicates using a set
    all_combinations_ar = set()

    for utterance in utterancesAR:
        placeholders = [f"{{{key}}}" for key in placeholder_listsAR if f"{{{key}}}" in utterance]
        if placeholders:
            combos = itertools.product(*(placeholder_listsAR[key.strip("{}")] for key in placeholders))
            for combo in combos:
                question = utterance
                for placeholder, value in zip(placeholders, combo):
                    question = question.replace(placeholder, value)
                all_combinations_ar.add(question)
        else:
            all_combinations_ar.add(utterance)

    # Save to Excel
    df_ar = pd.DataFrame(list(all_combinations_ar), columns=["Questions"])
    currentDate = datetime.now()

    # Format the date and time
    formatted_date_time = currentDate.strftime("%d-%m_%I.%M%p").lower()

    # Create the file name
    file_name = f'order_complaint_status_ar{formatted_date_time}.xlsx'
    df_ar.to_excel(file_name, index=False)

    print(f"Generated {len(all_combinations_ar)} unique Arabic questions and saved to {file_name}")
