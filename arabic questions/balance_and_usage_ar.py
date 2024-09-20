import pandas as pd
import itertools
from datetime import datetime

def generate_list():
    # Define the Arabic lists
    balance = [
        "رصيدي الحالي",
        "وحداتي المجانية",
        "رصيدي",
        "رصيد وحداتي المجانية",
        "رصيدي المتبقي",
        "الرصيد",
        "رصيد الوحدات المجانية المتبقي",
        "رصيدي المتاح",
        "رصيدي المتاح والوحدات المجانية المتبقية",
        "رصيد الحساب",
        "باقيلي رصيد",
        "متبقيلي رصيد",
        "رصيدي يلي ضايل",
        "معي رصيد",
        "رصيد البيانات الخاص بي",
        "البيانات المتبقية",
        "رصيد باقة البيانات",
        "رصيد البيانات على خطي المسبق الدفع",
        "رصيدي من البيانات",
        "رصيد بياناتي",
        "باقي في البيانات",
        "متبقي من باقة النت",
        "الرصيد المتبقي في باقة الإنترنت",
        "بقيانلي من باقة النت",
        "ضايلي رصيد من باقة البيانات",
        "اديش معي نت",
        "اديش معي بباقة البيانات",
        "رصيد باقة المكالمات",
        "رصيد المكالمات الصوتية",
        "الدقائق المتبقية في حسابي",
        "رصيدي من باقة المكالمات",
        "رصيدي من المكالمات الصوتية",
        "رصيد الدقائق",
        "بقيانلي مكالمات",
        "كم دقيقة معي"
    ]

    PayChargeNow = [
        "دفع فاتورة",
        "دفع فاتورة صديق",
        "دفع فاتورتي",
        "خاصية الدفع السريع",
        "ادفع الآن",
        "الدفع لصديق",
        "دفع فاتورة خطي",
        "ادفع فاتورة هاتفي",
        "الدفع لباقة الاتصال المنزلي",
        "ادفع الحين",
        "ادفع فاتورتي الحين",
        "دفع الفواتير المعلقة",
        "ادفع فواتيري المستحقة الحين",
        "ادفع فواتيري المتراكمة",
        "تعبئة الرصيد السريعة",
        "إعادة التعبئة الآن",
        "إعادة الشحن الآن",
        "تعبئة الرصيد لصديق",
        "إعادة الشحن السريع",
        "إعادة تعبئة باقة الدفع المسبق الخاصة بي",
        "إعادة شحن باقتي",
        "شراء رصيد",
        "إضافة رصيد",
        "شحن الرصيد",
        "إضافة رصيد لحسابي الآن",
        "إعادة شحن رصيد هاتفي",
        "إعادة شحن الرصيد لصديق",
        "إضافة رصيد للآخرين",
        "إعادة شحن خطي المدفوع مسبقاً الآن",
        "أعبي رصيد",
        "إعادة تعبئة الرصيد الآن لرقمي",
        "اشحن خطي"
    ]

    PayChargeHistory = [
        "آخر دفعة قمت بها",
        "دفعاتي الأخيرة",
        "تفاصيل دفعاتي السابقة",
        "سجل الفواتير",
        "سجلات الدفع الخاصة بي",
        "قائمة معاملات الدفع السابقة الخاصة بي",
        "تفاصيل الدفع لخدمة الانترنت المنزلي",
        "دفعاتي لخط الدفع الآجل الخاص بي",
        "تتبع سجل الدفع الخاص بي",
        "سجل الدفع",
        "معاملات الدفع الأخيرة لحسابي",
        "كشف حساب",
        "الدفعات السابقة",
        "تواريخ الدفعات الأخيرة",
        "قائمة معاملات إعادة شحن خطي المدفوع مسبقاً",
        "سجل إعادة الشحن الخاص بي",
        "سجل إعادة التعبئة",
        "سجل إعادة تعبئة الرصيد الخاص بي",
        "تاريخ إعادة الشحن",
        "تواريخ الشحن الأخيرة لخطي"
    ]

    how_phrasesAR = ["كيف يمكنني", "كيف", "ممكن أعرف كيف", "شلون", "كيفية"]

    wantAr = ["أبغى", "أبي", "أريد", "أبا", "بدي", "ريد", "ودي", "أود", "أحتاج"]

    INTERROGATIVE_WORDSar = [
        "هل يمكنني", "هل يمكنك", "هل", "ما هي", "ما هو", "وش", "وش هي", "إيش", "ما هو", 
        "شنو", "شو هو", "شو هي", "شو", "قديش", "كم", "ماذا", "لماذا", "ليش"
    ]

    usageBreakdown = [
        "تفاصيل عن الاستخدام اليومي",
        "تفاصيل الاستخدام الخاص بي",
        "تفاصيل استخدام باقاتي",
        "سجل الاستخدام",
        "عرض تفاصيل الاستخدام",
        "معلومات الاستخدام",
        "ملخص الاستخدام",
        "ملخص استخدام باقتي",
        "تفاصيل الاستهلاك",
        "تفاصيل متعلقة باستهلاكي",
        "تحليل تفاصيل الاستخدام",
        "تحليل استهلاك الرصيد",
        "تفاصيل الفاتورة"
    ]

    TopUsageReasonsAR = [
        "أسباب الاستخدام العالي",
        "أسباب زيادة الاستخدام",
        "زيادة رسوم الاستخدام",
        "زيادة في رسوم الاستخدام",
        "ارتفاع استهلاك البيانات",
        "أسباب ارتفاع الاستهلاك",
        "ارتفع استهلاكي كثيراً",
        "استهلاكي مؤخراً مرتفع جداً",
        "استهلاك أكثر بكثير من المعتاد",
        "الاستهلاك السريع",
        "أسباب زيادة السعر"
    ]
    # Define the Arabic utterance templates
    utterancesAR = [
        "الرصيد والاستخدام",
        "{wantAr} تفاصيل عن الرصيد والاستخدام",
        "أحتاج مساعدة في معرفة رصيدي وتفاصيل الاستخدام",
        "التحقق من تاريخ المعاملات",
        "الاستهلاك والفوائد",
        "{balance}",
        "{how_phrasesAR} معرفة {balance}",
        "{INTERROGATIVE_WORDSar} {balance}",
        "{wantAr} أستفسر عن {balance}",
        "التحقق من {balance} من فضلك.",
        "{wantAr} أعرف {INTERROGATIVE_WORDSar} باقي في {balance}",
        "الاستعلام والكشف عن {balance}",
        "معرفة كم {balance}",
        "{wantAr} {balance}",
        "الدفع و إعادة التعبئة",
        "الدفع",
        "إعادة التعبئة",
        "إعادة الشحن",
        "{PayChargeNow}",
        "{how_phrasesAR} {PayChargeNow}",
        "ساعدني من فضلك , {wantAr} {PayChargeNow}",
        "{wantAr} تساعدني {PayChargeNow}",
        "ليس لدي رصيد ساعدني في {PayChargeNow}",
        "رصيدي على وشك الإنتهاء و {wantAr} {PayChargeNow}",
        "{INTERROGATIVE_WORDSar} {PayChargeNow}",
        "{wantAr} {PayChargeNow}",
        "{PayChargeHistory}",
        "{wantAr} معرفة {PayChargeHistory}",
        "{how_phrasesAR} الاستعلام عن {PayChargeHistory}",
        "{wantAr} مساعدة في الكشف عن {PayChargeHistory}",
        "عرض {PayChargeHistory}",
        "{wantAr} {PayChargeHistory}",
        "الرجاء إظهار {PayChargeHistory}",
        "الاطلاع على تواريخ {PayChargeHistory}",
        "{usageBreakdown}",
        "{wantAr} تعرض لي {usageBreakdown}",
        "لدي استفسار عن {usageBreakdown}",
        "ساعدني من فضلك {how_phrasesAR} تتبع {usageBreakdown}",
        "{INTERROGATIVE_WORDSar} إرسال {usageBreakdown}",
        "عندي سؤال عن {usageBreakdown} للباقات",
        "{usageBreakdown} للشهر الماضي كامل",
        "أظهر لي لو سمحت {usageBreakdown}",
        "{how_phrasesAR} {usageBreakdown}",
        "{INTERROGATIVE_WORDSar} {usageBreakdown}",
        "{wantAr} {usageBreakdown}",
        "استعلام عن الاستهلاك",
        "{TopUsageReasonsAR}",
        "{INTERROGATIVE_WORDSar} {TopUsageReasonsAR}",
        "في الشهر الماضي {TopUsageReasonsAR} للدقائق والبيانات {INTERROGATIVE_WORDSar} السبب؟",
        "{wantAr} أعرف {TopUsageReasonsAR}",
        "وصلني إشعار {TopUsageReasonsAR} لهذا الشهر أخبرني {INTERROGATIVE_WORDSar} الذي يسبب {TopUsageReasonsAR} لبيانات باقات الهاتف المتحرك الخاص بي",
        "{how_phrasesAR} معرفة {TopUsageReasonsAR}",
        "{wantAr} {TopUsageReasonsAR}"
    ]

    # Prepare a list of all lists for placeholders
    placeholder_listsAR = {
        "balance": balance,
        "PayChargeNow": PayChargeNow,
        "PayChargeHistory": PayChargeHistory,
        "how_phrasesAR": how_phrasesAR,
        "wantAr": wantAr,
        "INTERROGATIVE_WORDSar": INTERROGATIVE_WORDSar,
        "usageBreakdown": usageBreakdown,
        "TopUsageReasonsAR": TopUsageReasonsAR
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
    file_name = f'balance&usage_ar_{formatted_date_time}.xlsx'
    df_ar.to_excel(file_name, index=False)

    print(f"Generated {len(all_combinations_ar)} unique Arabic questions and saved to {file_name}")
