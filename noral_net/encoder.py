class Encoder:                             # تعریف کلاس پایه Encoder برای ساخت شیءهای انکودر
    def __init__(self):                    # سازنده کلاس؛ وقتی Encoder() ساخته شود، خودکار اجرا می‌شود
        pass                               # فعلاً مقداردهی خاصی انجام نمی‌دهد و رد می‌شود

    def __getitem__(self, key):            # متد خاص برای دسترسی با براکت مثل obj[key]
        pass                               # فعلاً چیزی برنمی‌گرداند و رد می‌شود


class Encoder_child(Encoder):              # تعریف زیرکلاس Encoder_child که از Encoder ارث می‌برد
    def __getitem__(self, key):            # بازنویسی (override) متد __getitem__ مخصوص کلاس فرزند
        pass                               # فعلاً رفتار اختصاصی خاصی ندارد و رد می‌شود