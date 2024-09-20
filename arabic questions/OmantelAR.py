import pandas as pd
import itertools
from datetime import datetime

def generate_list():
    # Define the lists provided

    balancear = [
        "رصيد",
        "إظهار رصيدي",
        "الرصيد المتبقي",
        "مبلغ الرصيد المدفوع مسبقاً",
        "التحقق من رصيد هاتفي",
        "الاطلاع على رصيد الحساب",
        "رصيدي الحالي",
        "حالة رصيدي",
        "رصيدي المتاح"
    ]

    controlar = [
        "إدارة الرصيد",
        "التحكم في رصيدي",
        "إدارة استخدام الرصيد الخاص بي",
        "إدارة رصيدي بشكل أفضل",
        "أتحكم برصيدي",
        "إدارة البيانات",
        "التحكم في بياناتي",
        "إدارة بيانات هاتفي",
        "إدارة استخدام البيانات",
        "التحكم في استخدام بياناتي",
        "أتحكم ببياناتي"
    ]


    # Define the utterance templates
    utterancesAR = [
        "الرصيد",
        "{balancear}",
        "كم باقي في حسابي {balancear}",
        "{checkar} {balancear}",
        "{wantAr} {checkar} {balancear}، كم المتبقي؟",
        "{how_phrasesAR} {checkar} {balancear}",
        "{controlar}",
        "أحتاج مساعدة لمعرفة {controlar}",
        "أفضل حل من أجل {controlar}",
        "خيارات {controlar}",
        "{how_phrasesAR} {controlar} في موبايل {controlDataDevicear}",
        "جهازي {controlDataDevicear}، {how_phrasesAR} أقدر {controlar}",
        "باقتي",
        "خدمات باقتي",
        "تفاصيل عن {commitmentar} من فضلك",
        "{commitmentar}",
        "{commitmentar} في باقتي",
        "تفاصيل {commitmentar} المفعلة",
        "{checkar} {commitmentar}",
        "أخبرني عن تفاصيل {commitmentar} لاشتراكي الحالي",
        "{how_phrasesAR} معرفة تفاصيل {commitmentar} المسبق الدفع",
        "الفواتير",
        "{billingar}",
        "{INTERROGATIVE_WORDSar} لدي أي {billingar}",
        "{how_phrasesAR} {billingar}، ساعدني من فضلك",
        "{INTERROGATIVE_WORDSar} معرفة {billingar}",
        "{wantAr} {checkar} {billingar}",
        "اعرض لي {billingar}",
        "هدية باقتي",
        "اعرض لي هدايا باقتي من فضلك",
        "{wantAr} قائمة بهدايا باقتي",
        "{wantAr} {checkar} المزيد عن هدايا باقتي",
        "أخبرني {how_phrasesAR} الحصول على هدية باقتي",
        "{INTERROGATIVE_WORDSar} لدي أي هدية باقتي؟",
        "خدمات ومزايا إضافية",
        "{addOnsar}",
        "{wantAr} {checkar} {addOnsar}",
        "اعرض لي من فضلك {addOnsar}",
        "المتجر الإلكتروني",
        "{eshopar}",
        "أسأل عن جهاز {devicesar}، إذا كان {eshopar}",
        "{INTERROGATIVE_WORDSar} {eshopar}",
        "{wantAr} أسأل، {INTERROGATIVE_WORDSar} حسابي {eshopar}",
        "أجهزة {devicesar}، {INTERROGATIVE_WORDSar} {eshopar}",
        "{how_phrasesAR} {eshopar} جهاز {devicesar}",
        "مكاسب",
        "أخبرني من فضلك عن برنامج مكاسب",
        "{INTERROGATIVE_WORDSar} برنامج مكاسب",
        "{makasib}",
        "{how_phrasesAR} {makasib}، ساعدني من فضلك",
        "{INTERROGATIVE_WORDSar} خطوات {makasib}",
        "سمعت عن برنامج مكاسب، {how_phrasesAR} {makasib}",
        "الانضمام إلى عمانتل",
        "{joinOmantel}",
        "{wantAr} {joinOmantel} ساعدني من فضلك",
        "{how_phrasesAR} الانضام إلى عائلة عمانتل",
        "{how_phrasesAR} أقدر {joinOmantel}",
        "خطوات {joinOmantel}",
        "{how_phrasesAR} أصير من مستخدمي عمانتل",
        "خدمات شريحة الهاتف",
        "{buySIMar}",
        "{how_phrasesAR} {buySIMar}",
        "{wantAr} {buySIMar}، {INTERROGATIVE_WORDSar} الطريقة؟",
        "{replacementar}",
        "{how_phrasesAR}{replacementar}",
        "عندي {replacementar} و {wantAr} تبديلها",
        "تحديث بياناتي",
        "تحديث بيانات ملفي الشخصي",
        "{updateProfilear}",
        "{wantAr} {updateProfilear}",
        "ساعدني في {updateProfilear}",
        "{how_phrasesAR} {updateProfilear}",
        "{how_phrasesAR} أقدر {updateProfilear} في عمانتل",
        "ضريبة القيمة المضافة",
        "الضريبة",
        "{VATar}",
        "أخبرني عن {VATar} في عمانتل",
        "{INTERROGATIVE_WORDSar} {VATar}",
        "{INTERROGATIVE_WORDSar} معرفة تفاصيل عن {VATar}",
        "أقرب فرع لعمانتل",
        "أقرب صالة عمانتل",
        "صالات عمانتل",
        "فروع عمانتل القريبة مني",
        "أقرب منفذ"
    ]


    # Prepare a list of all lists for placeholders
    placeholder_listsAR = {
        "balancear": balancear,

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
    file_name = f'standalone_ar_{formatted_date_time}.xlsx'
    df_ar.to_excel(file_name, index=False)

    print(f"Generated {len(all_combinations_ar)} unique Arabic questions and saved to {file_name}")
