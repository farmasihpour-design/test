# how to import status from neue+ral network library
from noral_net import statuss


# how to import encoder from neue+ral network library
from noral_net import encoder

def main():                              # تعریف تابع اصلی برنامه؛ همه کارهای اصلی اینجا جمع می‌شوند
    statuss()                            # صدا زدن تابع statuss  تا پیام وضعیت چاپ شود

    enc = encoder.Encoder()              # ساخت یک نمونه (شیء) از کلاس Encoder و ذخیره در متغیر enc
    child = encoder.Encoder_child()      # ساخت یک نمونه از کلاس فرزند Encoder_child و ذخیره در child

    print(enc)                           # چاپ اطلاعات شیء enc  خروجی
    print(child)                         # چاپ اطلاعات شیء child در خروجی


if __name__ == "__main__":                # شرط بررسی اینکه آیا فایل مستقیماً اجرا شده یا ایمپورت شده است
    main()                               # اگر مستقیم اجرا شده باشد، تابع main() را راه می‌اندازد