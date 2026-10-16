# Vacuum Cleaner Agent: 3 Rooms

[English](#english) | [فارسی](#فارسی)

---

## English

A console simulation of an automatic vacuum cleaner agent in a three-room environment (rooms **A**, **B** and **C**, arranged in a line), written in Python. It extends the classic two-room Vacuum World example from the Intelligent Agents chapter of an AI course.

The agent can perform three actions:

- **Suck** (clean the current room)
- **Right** (move one room to the right)
- **Left** (move one room to the left)

### How it works

1. Ask which room the agent starts in (A, B or C).
2. Check whether the current room is dirty (via user input, Y or N).
   - If dirty: clean it (7 seconds).
   - Either way, the room is recorded as clean.
3. Move to the next room according to the path table below (3 seconds per move).
4. Repeat until all three rooms have been recorded as clean.

At the end, the program prints the recorded state of each room.

### Movement table

`RL` is the step counter. Each column is the room the agent starts in, and the path is read from top to bottom.

| Step (`RL`) | Start in A | Start in B | Start in C |
|---|---|---|---|
| 0 | Right → B | Right → C | Left → B |
| 1 | Right → C | Left → B | Left → A |
| 2 | - | Left → A | - |

For example, starting in B the path is B → C → B → A.

In the code, the direction of the last move is stored in `lm`, so that the agent starting in A (or C) keeps going in the same direction when it passes through B.

### Requirements

- Python 3

No external libraries are needed.

### Usage

```bash
python 3room.py
```

### Files

| File | Description |
|---|---|
| `3room.py` | The agent simulation |

---

## فارسی

یک شبیه‌سازی کنسولی از یک عامل جاروبرقی خودکار (automatic vacuum cleaner agent) در محیط سه خانه‌ای (خانه‌های **A**، **B** و **C** که در یک خط قرار دارند)، نوشته‌شده با Python. این پروژه، مثال دو خانه‌ای Vacuum World (دنیای جاروبرقی) از فصل Intelligent Agents (عامل‌های هوشمند) درس هوش مصنوعی را گسترش می‌دهد.

عامل سه کار می‌تواند انجام دهد:

- **Suck** (جارو کردن خانه‌ی فعلی)
- **Right** (رفتن یک خانه به راست)
- **Left** (رفتن یک خانه به چپ)

### نحوه‌ی کار

1. پرسیدن اینکه عامل از کدام خانه شروع می‌کند (A، B یا C).
2. بررسی اینکه خانه‌ی فعلی کثیف است یا نه (از طریق ورودی کاربر، Y یا N).
   - اگر کثیف باشد: جارو می‌کند (۷ ثانیه).
   - در هر دو حالت، خانه به‌عنوان تمیز ثبت می‌شود.
3. رفتن به خانه‌ی بعدی طبق جدول مسیر زیر (۳ ثانیه برای هر حرکت).
4. تکرار تا زمانی که هر سه خانه تمیز ثبت شوند.

در پایان، برنامه وضعیت ثبت‌شده‌ی هر خانه را چاپ می‌کند.

### جدول حرکت

`RL` شمارنده‌ی مرحله (step counter) است. هر ستون، خانه‌ای است که عامل از آن شروع می‌کند و مسیر از بالا به پایین خوانده می‌شود.

| مرحله (`RL`) | شروع از A | شروع از B | شروع از C |
|---|---|---|---|
| ۰ | Right ← B | Right ← C | Left ← B |
| ۱ | Right ← C | Left ← B | Left ← A |
| ۲ | - | Left ← A | - |

مثلاً با شروع از B، مسیر به‌صورت B ← C ← B ← A است.

در کد، جهت آخرین حرکت در متغیر `lm` ذخیره می‌شود تا عاملی که از A (یا C) شروع کرده، هنگام عبور از B در همان جهت ادامه دهد.

### پیش‌نیازها

- Python 3 (پایتون ۳)

به هیچ کتابخانه‌ی خارجی (external library) نیاز نیست.

### نحوه‌ی اجرا

```bash
python 3room.py
```

### فایل‌ها

| فایل | توضیح |
|---|---|
| `3room.py` | شبیه‌سازی عامل |
