import pandas as pd
import itertools
from datetime import datetime

def generate_list():
    # Define the lists provided

    how_phrasesAR = ["كيف يمكنني", "كيف", "ممكن أعرف كيف", "شلون", "كيفية"]

    wantAr = ["أبغى", "أبي", "أريد", "أبا", "بدي", "ريد", "ودي", "أود", "أحتاج"]

    INTERROGATIVE_WORDSar = [
        "هل يمكنني", "هل يمكنك", "هل", "ما هي", "ما هو", "وش", "وش هي", "إيش", "ما هو", 
        "شنو", "شو هو", "شو هي", "شو", "قديش", "كم", "ماذا", "لماذا", "ليش"
    ]

    hometypeAR = [
        "باقة البيت اللاسلكية",
        "باقات دو اللاسلكية للمنزل",
        "الإنترنت المنزلي اللاسلكي",
        "باقات نت لاسلكية للبيت",
        "باقات الوايرلس",
        "الإنترنت المنزلي اللاسلكي الغير محدود 5G",
        "الباقات اللاسلكية",
        "شبكة فايبر",
        "شبكة فايير ثابتة",
        "الباقات السلكية"
    ]

    newProductAR = [
        "الباقات الثابتة",
        "الخط الثابت",
        "باقات المنزل",
        "باقات الدفع المسبق",
        "اشتراك مسبق الدفع",
        "خط الدفع المسبق",
        "باقات الدفع الآجل",
        "باقات مفوترة",
        "خط دفع آجل",
        "اشتراك دفع لاحق",
        "باقات الجوال للشركات",
        "باقة الهاتف المتحرك للشركات",
        "باقة الهاتف المتحرك للمؤسسات",
        "باقات مسبقة الدفع للشركات",
        "باقات مفوترة للشركات",
        "باقات دفع مسبق للمؤسسات",
        "باقات مفوترة للمؤسسات",
        "خطوط للشركات",
        "الباقات الثابتة للشركات",
        "الخدمات الثابتة للشركات",
        "خدمات ثابتة للمؤسسات",
        "خط ثابت للأعمال",
        "خدمات الإنترنت للأعمال",
        "خدمات الاتصال والإنترنت للمؤسسات",
        "باقات الإنترنت للشركات",
        "الخطوط الثابتة والإنترنت للشركات",
        "الأجهزة"
    ]

    subscribear = [
        "شراء",
        "اشتراك",
        "تفعيل",
        "تشغيل"
    ]

    devicesTypear = [
        "الهواتف",
        "هواتف متحركة",
        "أجهزة الهواتف المحمولة",
        "جوالات",
        "تلفونات",
        "موبايل",
        "أجهزة لوحية",
        "تابلت",
        "أيباد",
        "الساعات الذكية",
        "ساعة آبل",
        "ساعة سامسونج",
        "سمارت ووتش",
        "الألعاب",
        "بلاي ستيشن",
        "اكسسوارات الهاتف المتحرك",
        "اكسسوارات للجوال",
        "سماعات",
        "سماعة أبل",
        "ايربودز",
        "شاحن",
        "كيبل شاحن",
        "ملحقات"
    ]

    phoneTypear = [
        "آبل",
        "آيفون",
        "آيفون 15",
        "آيفون 15 برو ماكس",
        "سامسونج",
        "جالكسي",
        "جالكسي S24 ألترا",
        "جالكسي Z",
        "كل الهواتف",
        "جميع الأجهزة المحمولة",
        "اوبو",
        "شاومي",
        "كل الجوالات"
    ]

    # Define the utterance templates
    utterancesAR = [
        "{newProductAR}",
        "{hometypeAR}",
        "{wantAr} تفاصيل أكثر عن {newProductAR} المتاحة",
        "{newProductAR} الأكثر مبيعاً",
        "{how_phrasesAR} {subscribear} في {hometypeAR}",
        "{wantAr} {subscribear} في {newProductAR}, أبحث عن أفضل سعر",
        "{INTERROGATIVE_WORDSar} {hometypeAR}",
        "{how_phrasesAR} {subscribear} {hometypeAR} {INTERROGATIVE_WORDSar} الخطوات",
        "{INTERROGATIVE_WORDSar} توفرون خدمات للمنزل؟ انترنت وهاتف؟",
        "أنا مشترك جديد في دو, أبحث عن {newProductAR}",
        "{newProductAR} المقترحة",
        "{INTERROGATIVE_WORDSar} يوجد خصم على {newProductAR}",
        "أعرض لي من فضلك {newProductAR} المتوفرة حالياً",
        "{devicesTypear}",
        "{phonesTypear}",
        "أعرض لي أحدث إصدارات {phonesTypear}",
        "أبحث عن {devicesTypear}",
        "{wantAr} {subscribear} {devicesTypear} أعرض لي المتوفر من فضلك",
        "{subscribear} {devicesTypear}",
        "قائمة {phonesTypear} المتوفرة",
        "منتجات جديدة"
    ]


    # Prepare a list of all lists for placeholders
    placeholder_listsAR = {
        "newProductAR": newProductAR, 
        "how_phrasesAR": how_phrasesAR,
        "wantAr": wantAr,
        "INTERROGATIVE_WORDSar": INTERROGATIVE_WORDSar,
        "hometypeAR": hometypeAR,
        "subscribear": subscribear,
        "devicesTypear": devicesTypear,
        "phonesTypear": phoneTypear
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
    file_name = f'explour_products_ar_{formatted_date_time}.xlsx'
    df_ar.to_excel(file_name, index=False)

    print(f"Generated {len(all_combinations_ar)} unique Arabic questions and saved to {file_name}")
