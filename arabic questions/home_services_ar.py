import pandas as pd
import itertools
from datetime import datetime

def generate_list():
    # Define the Arabic lists
    homepackagesAR = [
        "قنوات تلفزيونية", "القنوات والتلفزيون", "خدمات التلفزيون المنزلي", "باقات التلفزيون المنزلي",
        "القنوات التلفزيونية", "خدمة التلفزيون", "تلفزيون دو", "تلفزيون", "خطط التلفزيون", 
        "إدارة باقات التلفزيون المنزلي", "تعديل حزمة التلفزيون المنزلي", "تخصيص باقة التلفزيون الخاصة بي", 
        "إضافة قنوات جديدة إلى باقة التلفزيون الخاصة بي", "إضافة قنوات رياضية إلى باقة التلفزيون الخاصة بي",
        "إزالة بعض القنوات من اشتراك التلفزيون الحالي", "ترقية باقة التلفزيون الخاصة بي"
    ]

    subscribear = ["شراء", "اشتراك", "تفعيل", "تشغيل"]

    relocateAR = [
        "الانتقال إلى منزل جديد", "تغيير منزلي", "الانتقال إلى موقع جديد", "لدي عنوان جديد",
        "نقل خدماتي المنزلية إلى مكان جديد", "الانتقال إلى بيت جديد", "نقل الخدمة المنزلية لموقع آخر",
        "منزل جديد", "عنواني الجديد", "نقل خدمة دو هوم", "نقل خدمة الانترنت المنزلي", "تغيير مكان السكن"
    ]

    how_phrasesAR = ["كيف يمكنني", "كيف", "ممكن أعرف كيف", "شلون", "كيفية"]

    wantAr = ["أبغى", "أبي", "أريد", "أبا", "بدي", "ريد", "ودي", "أود", "أحتاج"]

    INTERROGATIVE_WORDSar = [
        "هل يمكنني", "هل يمكنك", "هل", "ما هي", "ما هو", "وش", "وش هي", "إيش", "ما هو", 
        "شنو", "شو هو", "شو هي", "شو", "قديش", "كم", "ماذا", "لماذا", "ليش"
    ]

    StreamingSerTypeAR = ["ديزني بلس", "ديزني+", "خدمة OSN", "او اس ان", "أمازون برايم"]

    StreamingServicesInquiryAR = [
        "أفعل", "أشترك في", "الاشتراك", "تفعيل", "أفعل اشتراك", "تنشيط", "ألغي اشتراكي", 
        "ألغي الاشتراك", "إلغاء اشتراك", "إيقاف الاشتراك", "حذف اشتراكي", "إلغاء التفعيل في",
        "لدي مشكلة في", "عندي مشكلة باشتراكي في", "أواجه مشكلة مع"
    ]

    # Define the Arabic utterance templates
    utterancesAR = [
        "{homepackagesAR}",
        "{how_phrasesAR} {subscribear} في {homepackagesAR}",
        "{wantAr} اختيار باقة جديدة من أجل {homepackagesAR}",
        "{wantAr} إضافة {homepackagesAR} على اشتراكي الحالي",
        "{wantAr} تساعدني من فضلك في {homepackagesAR}",
        "أعرض لي {homepackagesAR} السنوية",
        "{INTERROGATIVE_WORDSar} {homepackagesAR}",
        "أخبريني عن عروض {homepackagesAR}",
        "الخيارات المتاحة لي {subscribear} في {homepackagesAR}",
        "{INTERROGATIVE_WORDSar} القنوات المتوفرة مع خدمة {homepackagesAR}؟",
        "{StreamingSerTypeAR}",
        "أسعار {StreamingSerTypeAR}",
        "خدمات البث",
        "{INTERROGATIVE_WORDSar} عرض {StreamingSerTypeAR}؟",
        "{how_phrasesAR} {StreamingServicesInquiryAR} خدمة {StreamingSerTypeAR}؟",
        "عروض {StreamingSerTypeAR}",
        "{wantAr} أستفسر عن خدمات {StreamingSerTypeAR} المتاحة",
        "{StreamingServicesInquiryAR} {StreamingSerTypeAR}",
        "{how_phrasesAR} أتواصل من أجل {StreamingSerTypeAR} في حال أردت المساعدة؟",
        "{wantAr} تساعدني من فضلك في {StreamingServicesInquiryAR} خدمة {StreamingSerTypeAR}",
        "مزايا ورسوم {StreamingSerTypeAR}",
        "{wantAr} {StreamingSerTypeAR}",
        "{INTERROGATIVE_WORDSar} خدمات البث",
        "{relocateAR}",
        "{how_phrasesAR} {relocateAR}",
        "{wantAr} {relocateAR}",
        "طلب {relocateAR}",
        "{how_phrasesAR}  أقدم طلب من أجل {relocateAR}",
        "{wantAr} نقل خدمات دو الثابتة إلى مكان آخر",
        "أخطط للانتقال إلى {relocateAR} {INTERROGATIVE_WORDSar} مساعدتي في بعض التفاصيل",
        "{wantAr} أغير مكان إقامتي ساعدني في تقديم طلب {relocateAR}",
        "{INTERROGATIVE_WORDSar} {relocateAR}"
    ]

    # Prepare a list of all lists for placeholders
    placeholder_listsAR = {
        "homepackagesAR": homepackagesAR,
        "subscribear": subscribear,
        "relocateAR": relocateAR,
        "how_phrasesAR": how_phrasesAR,
        "wantAr": wantAr,
        "INTERROGATIVE_WORDSar": INTERROGATIVE_WORDSar,
        "StreamingSerTypeAR": StreamingSerTypeAR,
        "StreamingServicesInquiryAR": StreamingServicesInquiryAR
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
    file_name = f'home_services_ar_{formatted_date_time}.xlsx'
    df_ar.to_excel(file_name, index=False)

    print(f"Generated {len(all_combinations_ar)} unique Arabic questions and saved to {file_name}")
