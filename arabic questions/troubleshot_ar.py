import pandas as pd
import itertools
from datetime import datetime

def generate_list():
    # Define the lists provided

    artroubleshooting = [
        "استكشاف الأخطاء",
        "حل المشكلة",
        "إصلاح الأخطاء",
        "إصلاح المشاكل",
        "إصلاح",
        "حل مشكلتي",
        "معالجة المشكلة",
        "معالجة المشكلات التقنية"
    ]



    how_phrasesAR = ["كيف يمكنني", "كيف", "ممكن أعرف كيف", "شلون", "كيفية"]

    wantAr = ["أبغى", "أبي", "أريد", "أبا", "بدي", "ريد", "ودي", "أود", "أحتاج"]

    INTERROGATIVE_WORDSar = [
        "هل يمكنني", "هل يمكنك", "هل", "ما هي", "ما هو", "وش", "وش هي", "إيش", "ما هو", 
        "شنو", "شو هو", "شو هي", "شو", "قديش", "كم", "ماذا", "لماذا", "ليش"
    ]


    PayChargeIssuear = [
        "مشاكل في الدفع وإعادة التعبئة",
        "مشكلة الدفع/إعادة التعبئة",
        "مشاكل في الدفع وإعادة الشحن",
        "مشكلة في الدفع",
        "لم تتم عملية الدفع",
        "الدفع أونلاين لا يعمل",
        "الدفع عن طريق الإنترنت لا يعمل",
        "غير قادر على إتمام الدفع",
        "لم أتمكن من إتمام عملية الدفع السريع",
        "فشلت عملية الدفع",
        "مشكلة في إعادة التعبئة",
        "مشكلة في إعادة الشحن",
        "لم تتم عملية إعادة الشحن",
        "إعادة الشحن أونلاين لا تعمل",
        "غير قادر على إتمام إعادة تعبئة حسابي",
        "لم أتمكن من إتمام عملية إعادة الشحن السريع",
        "فشلت عملية إعادة الشحن لخطي"
    ]


    # Define the utterance templates
    utterancesAR = [
        "لدي مشكلة",
        "ساعدني في حل مشكلتي",
        "لدي مشكلة في خدمة من خدماتكم",
        "{troubleshootingTypear} وبحاجة إلى مساعدة",
        "{troubleshootingTypear}",
        "{artroubleshooting}",
        "{troubleshootingTypear} {how_phrasesAR} {artroubleshooting}",
        "{PayChargeIssuear}",
        "{how_phrasesAR} {artroubleshooting} عندي {PayChargeIssuear}",
        "أواجه {PayChargeIssuear} {INTERROGATIVE_WORDSar} مساعدتي في حلها",
        "{INTERROGATIVE_WORDSar} {troubleshootingTypear}"
    ]


    # Prepare a list of all lists for placeholders
    placeholder_listsAR = {
        "artroubleshooting": artroubleshooting, 
        "how_phrasesAR": how_phrasesAR,
        "wantAr": wantAr,
        "INTERROGATIVE_WORDSar": INTERROGATIVE_WORDSar,
        "PayChargeIssuear": PayChargeIssuear
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
    file_name = f'troubleshot_ar_{formatted_date_time}.xlsx'
    df_ar.to_excel(file_name, index=False)

    print(f"Generated {len(all_combinations_ar)} unique Arabic questions and saved to {file_name}")
