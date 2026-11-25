from . import encoder                     # ایمپورت کردن ماژول encoder.py از همین پوشه (noral_net)


def statuss():                           # تعریف تابع statuss برای نمایش پیام وضعیت
    print("success")                     # چاپ کلمه success در خروجی


# what does __main__ do?                 # کامنت یادآوری درباره کاربرد __main__
if __name__ == "__main__":                # فقط وقتی خودِ __init__.py مستقیم اجرا شود، داخلش اجرا می‌شود
    statuss()                            # اجرای تابع statuss در حالت اجرای مستقیم این فایل
    print(encoder)                       # چاپ اطلاعات ماژول encoder در حالت اجرای مستقیم این فایل