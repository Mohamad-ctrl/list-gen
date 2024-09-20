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

    switchar = [
        "تغيير باقتي",
        "تحسين باقتي",
        "ترقية باقتي",
        "تخفيض باقتي",
        "الانتقال إلى باقة أخرى",
        "تحويل باقتي إلى باقة أخرى",
        "ترقية - تخفيض",
        "أغير باقتي",
        "غير اشتراكي",
        "انقل خطي"
    ]


    switchTypear = [
        "تحويل رقمي إلى دو",
        "الانتقال إلى du",
        "نقل رقمي إلى دو",
        "أنتقل إلى du",
        "أنقل رقمي إلى du",
        "غير رقمي لدو",
        "انقل رقمي لعندكم",
        "تغيير باقة هاتفي",
        "تبديل باقة هاتفي المتحرك",
        "تحسين باقة هاتفي المتحرك",
        "ترقية باقتي",
        "تخفيض باقة",
        "أبدل باقة هاتفي الحالية بباقة ثانية",
        "تغيير خطي",
        "غير خط جوالي",
        "تعيير اشتراك الجوال",
        "تغيير باقة الإنترنت المنزلي",
        "تحويل باقتي المنزلية إلى باقة ثابتة غيرها",
        "تبديل باقة الخدمات المنزلية",
        "أغير باقة المنزل",
        "تغيير باقتي الثابتة إلى باقة ثانية",
        "الانتقال من باقة du Home إلى باقة المنزل اللاسلكية",
        "أبدل باقتي المنزلية بباقة ثانية غيرها",
        "الانتقال من الأعمال إلى الأفراد",
        "تحويل حسابي من باقة أعمال إلى باقة شخصية",
        "تبديل باقتي من الأعمال إلى باقة أفراد",
        "تحويل خطة الأعمال الحالية إلى خطة شخصية",
        "الانتقال من باقة المؤسسات إلى باقة شخصية",
        "تغيير اشتراكي من أعمال إلى اشتراك شخصي",
        "نقل اشتراكي من باقة مؤسسات إلى أفراد"
    ]

    switchMobileTypear = [
        "تغيير باقة الدفع المسبق",
        "تغيير باقتي الحالية المدفوعة مسبقاً",
        "تغيير خطي المدفوع مسبقاً",
        "غير خطي مسبق الدفع",
        "تغيير باقة الدفع الآجل",
        "تغيير باقتي الحالية المفوترة",
        "تبديل باقتي المفوترة",
        "غير خطي لاحق الدفع",
        "تغيير خطي الدفع الآجل",
        "استبدال باقة الدفع المسبق الخاصة بي بباقة دفع آجل",
        "تغيير باقة دفع مسبق إلى باقة دفع لاحق",
        "نقل باقتي من دفع مسبق إلى دفع آجل",
        "تغيير خطة الدفع المسبق الخاصة بي إلى خطة دفع آجل",
        "تغيير خطة الدفع المسبق إلى باقة فاتورة",
        "الانتقال من الدفع الآجل إلى الدفع المسبق",
        "ترقية باقتي الحالية من الدفع المسبق إلى الدفع الآجل",
        "تحسين باقتي من الدفع المسبق إلى الدفع الآجل",
        "مسبق الدفع إلى آجل الدفع",
        "آجل الدفع إلى مسبق الدفع",
        "آجل إلى مسبق",
        "غير خطي من مسبق للاحق",
        "تغيير الخط من مسبق الدفع لآجل الدفع",
        "تغيير شريحتي من آجل الدفع لمسبق الدفع"
    ]


    # Define the utterance templates
    utterancesAR = [
        "{switchar}",
        "{switchTypear}",
        "{switchMobileTypear}",
        "{how_phrasesAR} {switchar} الحالية والإشتراك في باقة أخرى",
        "ساعدني في {switchar}",
        "{wantAr} {switchar}",
        "{wantAr} {switchTypear}",
        "{how_phrasesAR} {switchar} من {switchMobileTypear}",
        "{wantAr} مساعدة في {switchTypear}",
        "{how_phrasesAR} {switchMobileTypear}",
        "{how_phrasesAR} {switchTypear} {INTERROGATIVE_WORDSar} المساعدة"
    ]



    # Prepare a list of all lists for placeholders
    placeholder_listsAR = {
        "switchar": switchar, 
        "how_phrasesAR": how_phrasesAR,
        "wantAr": wantAr,
        "INTERROGATIVE_WORDSar": INTERROGATIVE_WORDSar,
        "switchMobileTypear": switchMobileTypear,
        "switchTypear": switchTypear
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
    file_name = f'maigration_ar_{formatted_date_time}.xlsx'
    df_ar.to_excel(file_name, index=False)

    print(f"Generated {len(all_combinations_ar)} unique Arabic questions and saved to {file_name}")
