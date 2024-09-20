import pandas as pd
import itertools
from datetime import datetime

def generate_list():
    # Define the Arabic lists
    bundleTypear = [
        "باقات البيانات",
        "باقة إنترنت للجوال",
        "حزمة البيانات",
        "باقات إنترنت الهاتف المحمول",
        "باقات الإنترنت",
        "باقة بيانات",
        "باقات المكالمات الصوتية",
        "باقات الدقائق",
        "باقة صوت",
        "حزمة المكالمات الصوتية",
        "باقة تجوال",
        "باقة السفر",
        "باقات التجوال",
        "حزمة التجوال",
        "باقة الاتصال عبر الانترنت",
        "باقة بوتيم",
        "باقات مكالمات الصوت والفيديو",
        "باقة فويسو",
        "باقة داتا",
        "باقة انترنت",
        "باقة مكالمات",
        "باقة مكالمات دولية",
        "باقة مسجات",
        "باقة مجتمع",
        "باقة شباب",
        "باقة عائلية",
        "باقة أعمال",
        "باقة مخصصة"
    ]

    checkFixar = [
        "التحقق من المكالمات",
        "التحقق من/إصلاح المكالمات",
        "الاستعلام عن مكالماتي",
        "مشكلة في المكالمات",
        "التحقق من البيانات",
        "التحقق من /إصلاح البيانات",
        "الاستعلام عن بياناتي",
        "مشكلة في البيانات"
    ]

    voiceTypear = [
        "الدقائق المحلية",
        "الدقائق داخل الإمارات",
        "المكالمات المحلية",
        "الدقائق الدولية",
        "الدقائق خارج الإمارات",
        "مكالمات دولية",
        "مكالمات انترناشونال"
    ]

    how_phrasesAR = ["كيف يمكنني", "كيف", "ممكن أعرف كيف", "شلون", "كيفية"]

    wantAr = ["أبغى", "أبي", "أريد", "أبا", "بدي", "ريد", "ودي", "أود", "أحتاج"]

    INTERROGATIVE_WORDSar = [
        "هل يمكنني", "هل يمكنك", "هل", "ما هي", "ما هو", "وش", "وش هي", "إيش", "ما هو", 
        "شنو", "شو هو", "شو هي", "شو", "قديش", "كم", "ماذا", "لماذا", "ليش"
    ]

    buyar = [
        "شراء",
        "تقعيل",
        "اشتراك",
        "أحصل على",
        "أشترك",
        "الحصول على",
        "فعّل"
    ]


    specialdealsar = [
        "صفقات خاصة",
        "عروض خاصة وأسعار مخفضة",
        "العروض الحصرية",
        "العروض الشهرية المميزة",
        "عروض خاصة",
        "باقات بمزايا خاصة بي",
        "الباقات المخصصة",
        "عروضي"
    ]

    offersTypear = [
        "الأجهزة والباقات",
        "البيانات والمكالمات الصوتية",
        "باقات البيانات والصوت",
        "الباقات الصوتية",
        "الباقات",
        "البيانات والدقائق"
    ]

    PlanDevicesDealsar = [
        "عروض الباقات",
        "صفقات الباقات",
        "عروض الأجهزة",
        "صفقات الأجهزة",
        "أفضل العروض والصفقات"
    ]

    # Define the Arabic utterance templates
    utterancesAR = [
        "إدارة الباقات",
        "إدارة الخدمات المضافة",
        "{bundleTypear}",
        "{checkFixar}",
        "{voiceTypear}",
        "{buyar} {voiceTypear}",
        "{buyar}{bundleTypear}",
        "الاستعلام عن {bundleTypear}",
        "{INTERROGATIVE_WORDSar} {buyar} في باقات du",
        "أبحث عن {bundleTypear} ساعدني من فضلك",
        "ساعدني في اختيار {bundleTypear} مناسبة",
        "خيارات {bundleTypear} المتاحة أخبرني عنها",
        "أخطط للسفر و {wantAr} {buyar} في {bundleTypear}",
        "{INTERROGATIVE_WORDSar} {bundleTypear} المتوفرة ؟",
        "{wantAr} استفسر عن باقات {voiceTypear}؟",
        "{bundleTypear} مع الشرح بالتفصيل",
        "{wantAr} الاطلاع على قائمة {bundleTypear} المتوفرة",
        "الباقات المتوفرة",
        "الاستفسار عن حالة الباقة",
        "{specialdealsar}",
        "{offersTypear}",
        "{PlanDevicesDealsar}",
        "{INTERROGATIVE_WORDSar} يمكنني {buyar} {PlanDevicesDealsar}",
        "{wantAr} استفسر عن {PlanDevicesDealsar}",
        "{wantAr} اسأل عن {offersTypear}",
        "أعرض لي {offersTypear} المتاحة لي",
        "{INTERROGATIVE_WORDSar} يوجد {specialdealsar} لرقمي",
        "{buyar} {specialdealsar}",
        "قائمة {specialdealsar} الشهرية الموجودة",
        "{specialdealsar} متوفرة لي في الوقت الحالي",
        "{specialdealsar} {offersTypear}",
        "الاطلاع على {PlanDevicesDealsar}",
        "{wantAr} معرفة المزيد عن {specialdealsar} الجديدة",
        "{wantAr} {specialdealsar}"
    ]

    # Prepare a list of all lists for placeholders
    placeholder_listsAR = {
        "bundleTypear": bundleTypear,
        "checkFixar": checkFixar,
        "voiceTypear": voiceTypear,
        "how_phrasesAR": how_phrasesAR,
        "wantAr": wantAr,
        "INTERROGATIVE_WORDSar": INTERROGATIVE_WORDSar,
        "buyar": buyar,
        "specialdealsar": specialdealsar,
        "offersTypear": offersTypear,
        "PlanDevicesDealsar": PlanDevicesDealsar
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
    file_name = f'manage_bundles_ar{formatted_date_time}.xlsx'
    df_ar.to_excel(file_name, index=False)

    print(f"Generated {len(all_combinations_ar)} unique Arabic questions and saved to {file_name}")
