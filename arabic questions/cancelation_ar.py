import pandas as pd
import itertools
from datetime import datetime

def generate_list():
    # Define the lists provided

    canceltypear = [
        "باقتي المسبقة الدفع",
        "باقتي الآجلة الدفع",
        "باقة الهاتف المتحرك",
        "باقة الدفع المسبق الخاصة بي",
        "باقة الدفع الآجل الخاصة بي",
        "خطي",
        "خطي مسبق الدفع",
        "خطي لاحق الدفع",
        "باقتي المنزلية",
        "باقة المنزل",
        "باقة المنزل اللاسلكية 5G",
        "باقة المنزل اللاسلكية 4G",
        "الانترنت المنزلي اللاسلكي 4G",
        "الانترنت المنزلي اللاسلكي 5G",
        "خدماتي المنزلية",
        "باقة المنزل السلكية",
        "انترنت البيت",
        "باقتي",
        "باقاتي",
        "باقتي الحالية",
        "حزمي الفعالة",
        "إلغاء خدمة القيمة المضافة",
        "خدمة القيمة المضافة VAS",
        "إلغاء القيمة المضافة",
        "الغاء اشتراك خدمات القيم المضافة"
    ]


    how_phrasesAR = ["كيف يمكنني", "كيف", "ممكن أعرف كيف", "شلون", "كيفية"]

    wantAr = ["أبغى", "أبي", "أريد", "أبا", "بدي", "ريد", "ودي", "أود", "أحتاج"]

    INTERROGATIVE_WORDSar = [
        "هل يمكنني", "هل يمكنك", "هل", "ما هي", "ما هو", "وش", "وش هي", "إيش", "ما هو", 
        "شنو", "شو هو", "شو هي", "شو", "قديش", "كم", "ماذا", "لماذا", "ليش"
    ]


    cancelBundleTypear = [
        "باقة البيانات",
        "حزمة البيانات",
        "باقة النت",
        "باقة المكالمات",
        "باقة الدقائق",
        "العرض الخاص بي",
        "العروض",
        "عرضي الفعال",
        "العروض الفعالة",
        "باقة الاتصال عبر الانترنت"
    ]


    cancelar = [
        "ألغي",
        "إلغاء",
        "حذف",
        "إلغاء الاشتراك",
        "إلغاء التفعيل",
        "إيقاف",
        "إنهاء اشتراك",
        "إلغاء التنشيط",
        "إلغاء خدمة",
        "إنهاء العقد",
        "ألغي اشتراكي",
        "حذف اشتراكي",
        "كنسل الاشتراك",
        "إغلاق حسابي"
    ]


    cancellationreasonar = [
        "الباقة غالية",
        "السعر مرتفع",
        "السعر عالي جداً",
        "الرسوم الشهرية غالية",
        "سأسافر",
        "سأنتقل إلى خارج الدولة",
        "أرغب بالسفر",
        "أبي أسافر",
        "وجدت عرض أفضل",
        "أبحث عن عرض أفضل",
        "أبحث عن مزايا أكثر",
        "غير راض عن الخدمة",
        "أنا لست سعيد بمزايا باقتي الحالية",
        "الخدمة ليست كالمتوقع",
        "لم أعد بحاجة إلى باقتي الحالية"
    ]


    # Define the utterance templates
    utterancesAR = [
        "{cancelar}",
        "{wantAr} {cancelar} {canceltypear}",
        "{cancellationreasonar} و {wantAr} إلغائها الآن",
        "{cancelar} {cancelBundleTypear} الخاصة بي من فضلك",
        "ساعدني من فضلك في {cancelar} {canceltypear} {cancellationreasonar}",
        "{how_phrasesAR} {cancelar} {cancelBundleTypear} الخاصة بي",
        "{INTERROGATIVE_WORDSar} {cancelar} {cancelBundleTypear}",
        "{INTERROGATIVE_WORDSar} خطوات {cancelar} {canceltypear}؟",
        "{wantAr} {cancelar} خدمات الاتصال الخاصة بي",
        "{wantAr} بتقديم طلب {cancelar} {canceltypear}"
    ]

    # Prepare a list of all lists for placeholders
    placeholder_listsAR = {
        "canceltypear": canceltypear, 
        "how_phrasesAR": how_phrasesAR,
        "wantAr": wantAr,
        "INTERROGATIVE_WORDSar": INTERROGATIVE_WORDSar,
        "cancelBundleTypear": cancelBundleTypear,
        "cancelar": cancelar,
        "cancellationreasonar": cancellationreasonar
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
    file_name = f'cancelation_ar{formatted_date_time}.xlsx'
    df_ar.to_excel(file_name, index=False)

    print(f"Generated {len(all_combinations_ar)} unique Arabic questions and saved to {file_name}")
