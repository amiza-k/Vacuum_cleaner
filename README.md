# Vacuum Cleaner Agent

[English](#english) | [فارسی](#فارسی)

---

## English

A simple console simulation of an automatic vacuum cleaner agent, based on the classic Vacuum World example from the Intelligent Agents chapter of an AI course.

The environment has two rooms, **A** and **B**. The agent can perform three actions:

- **Suck** (clean the current room)
- **Right** (move from A to B)
- **Left** (move from B to A)

### How it works

The logic follows the mind map included in this repository (`Vacuum_cleaner.xmind`):

1. Ask which room the agent is in (A or B).
2. Check whether the current room is dirty.
   - If dirty: clean it (7 seconds).
   - If clean: do nothing.
3. Move to the other room (3 seconds): from A go right, from B go left.
4. Repeat. The loop ends after both rooms have been visited.

At the end, the program prints the recorded state of each room.

### Requirements

- Python 3

No external libraries are needed.

### Usage

```bash
python Untitled-1.py
```

Example session:

```
start
Where am I? A or B? A
Is it clean? Y or N? N
Cleaning. 7 seconds
Cleaning done
Moving to room B
Moving. 3 seconds.
I'm in room B
Is it clean? Y or N? Y
Room B was clean
Moving to room A
Moving. 3 seconds.
I'm in room A
finished cleaning. Room A: ['Dirty'], Room B: ['Clean']
```

### Files

| File | Description |
|---|---|
| `Untitled-1.py` | The agent simulation |
| `Vacuum_cleaner.xmind` | Mind map of the agent's decision logic |

---

## فارسی

یک شبیه‌سازی ساده‌ی کنسولی از یک عامل جاروبرقی خودکار (automatic vacuum cleaner agent)، بر اساس مثال معروف Vacuum World (دنیای جاروبرقی) از فصل Intelligent Agents (عامل‌های هوشمند) درس هوش مصنوعی.

محیط شامل دو خانه‌ی **A** و **B** است. عامل سه کار می‌تواند انجام دهد:

- **Suck** (جارو کردن خانه‌ی فعلی)
- **Right** (رفتن از A به B)
- **Left** (رفتن از B به A)

### نحوه‌ی کار

منطق برنامه از روی نقشه‌ی ذهنی (mind map) موجود در این مخزن (`Vacuum_cleaner.xmind`) پیاده‌سازی شده است:

1. پرسیدن اینکه عامل در کدام خانه است (A یا B).
2. بررسی اینکه خانه‌ی فعلی کثیف است یا نه.
   - اگر کثیف باشد: جارو می‌کند (۷ ثانیه).
   - اگر تمیز باشد: کاری نمی‌کند.
3. رفتن به خانه‌ی دیگر (۳ ثانیه): از A به راست و از B به چپ.
4. تکرار. حلقه پس از بازدید هر دو خانه پایان می‌یابد.

در پایان، برنامه وضعیت ثبت‌شده‌ی هر خانه را چاپ می‌کند.

### پیش‌نیازها

- Python 3 (پایتون ۳)

به هیچ کتابخانه‌ی خارجی (external library) نیاز نیست.

### نحوه‌ی اجرا

```bash
python Untitled-1.py
```

نمونه‌ی اجرا همان نمونه‌ی بخش انگلیسی بالا است.

### فایل‌ها

| فایل | توضیح |
|---|---|
| `Untitled-1.py` | شبیه‌سازی عامل |
| `Vacuum_cleaner.xmind` | نقشه‌ی ذهنی (mind map) منطق تصمیم‌گیری عامل |
