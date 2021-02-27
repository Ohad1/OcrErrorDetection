# OcrErrorDetection
<p dir="rtl">
<strong><span style="text-decoration:underline;">איתור חשדות לשגיאות במסמך שעבר ocr </span></strong></p>


<p dir="rtl">
<strong>מגישים:</strong> אוהד גבאי ושני סמסון</p>


<p dir="rtl">
<strong>רקע:</strong></p>


<p dir="rtl">
קיימים ברשותנו מסמכי חקיקה היסטוריים רבים בפורמטים סרוקים שעברו OCR.</p>


<p dir="rtl">
לצערנו, סריקת OCR איננה מושלמת וקיימים מקרים בהם מתבצעות שגיאות בהמרה באמצעות OCR. כלומר, תוצרי ה-OCR שמתקבלים אינם נאמנים למקור, ומצויים בהם טעויות שונות. נציין לדוגמא מספר טעויות שנחשפנו אליהם במהלך המשימה.</p>




*   שגיאות כתיב
    *   החלפה בין כ' ל - ב': כולה -> בולה
    *   החלפה בין ס' ל - 0: הסבר -> בולה
    *   אותיות במקום מספרים: 21983 -> ג98ו2, 1 -> ו
    *   החלפה בין נ' ל - 'ב: המדינה -> המדיבה
*   שגיאות ברישום הערות שוליים: התשכ"ג-11963 -> התשכ"ג-1963 1
*   בלבל בין "(מרכאות) לבין זוג גרשיים (' ')

<p dir="rtl">
<strong>הנחיות שימוש בתכנית:</strong></p>




1. הורידו ספריית קוד [ocrErrorDetection](https://github.com/Ohad1/OcrErrorDetection) מהgithub.
2. הריצו את התוכנית הראשית OcrErrorDetector.py אשר מקבלת כקלט מחרוזת של הנתיב לתיקייה בה נמצאים קבצי ה-PDF וקבצי ה- DOCX התואמים להם. 

    <p dir="rtl">
<span style="text-decoration:underline;">דוגמא להרצה:</span> "python OcrErrorDetector.py "/home/username/OcrFolder</p>


3. בסיום הריצה, יווצרו קבצי txt בעלי שם זהה לקבצי ה-PDF וה-DOCX. קבצים אלו יכילו את תוכן כל אחד מהחוקים בצירוף תגית &lt;ש> לכל מילה החשודה כשגיאה.

<p dir="rtl">
הערות: הרצנו את התכנית על גבי מערכת הפעלה של Linux.</p>


<p dir="rtl">
<strong><span style="text-decoration:underline;">מטרת הפרויקט:</span></strong></p>


<p dir="rtl">
<span style="text-decoration:underline;">מטרת העל:</span> איתור שגיאות במסמכים שעברו סריקה של OCR.</p>


<p dir="rtl">
<span style="text-decoration:underline;">פירוט על שיטת העבודה:</span> על מנת לאתר את השגיאות במסמכים השונים ביצענו את הצעדים הבאים על מנת לאתר את החשדות בצורה המקיפה ביותר:</p>




*   סריקת קורפוס קבצי XML המכילים את כל החקיקה התקפה בנוסח מלא ויצירת <span style="text-decoration:underline;">מילון המכיל מילים מתוך קבצים אלו.</span> חשוב לציין שנתנו דגש למילים בעלות משמעות להיכנס למילון שלנו ומילים המהוות סעיפים לא נכנסו. התבצע שימוש בביטויים רגולרים שונים על מנת לזהות מילים בצורה מדויקת, למשל - חילוץ מילים מתוך מרכאות וסוגריים וזיהוי תאריכים.
*   Bigram - מעבר על המילים בזוגות. כך יכולנו לזהות מקרים בהם רצף מילים שכנות אינן תקינות
*   שימוש ב - hunspell: ספרייה ב-python המשמשת כמילון עברי-עברי חיצוני אשר מאתר שגיאות כתיב במילים.
*   שימוש ב- pytesseract: ספרייה ב-python המשמשת כ- OCR. השתמשנו בקבצי ה-PDF המקוריים, המרנו אותם לתמונות והרצנו את ה OCR הנ"ל, על מנת להשוות לתוצרים שקיבלנו.

<p dir="rtl">
<strong><span style="text-decoration:underline;">תיאור הפרויקט במונחים של מדעי הרוח הדיגיטליים :</span></strong></p>


<p dir="rtl">
תוכן - זיהוי שגיאות במסמך החקיקה.</p>


<p dir="rtl">
Semi structured - קבצי XML </p>


<p dir="rtl">
מאחר וקבצי הXML מכילים תיוגים - התבססנו על תיוגי &lt;p> שמכילים את תוכן החקיקה.</p>


<p dir="rtl">
<strong><span style="text-decoration:underline;">פתרון הבעיה + סיכום</span></strong></p>


<p dir="rtl">
<strong><span style="text-decoration:underline;">הערכת התוצאות:</span></strong></p>


<p dir="rtl">
הדרך בה נמדוד את טיב התוצאות היא באמצעות מעבר מדגמי על מספר מסמכים שעברו OCR, והרצת התוכנית שלנו עליהם. לאחר ניתוח של 10 קבצים שונים, להלן התוצאות:</p>




*   89 True Positive
*   18 False Positive
*   3 False Negative

<p dir="rtl">
מסקנות:</p>




*   83% מתוך כלל השגיאות שהתוכנה זיהתה, הן אכן שגיאות אמיתיות
*   מעל ל - 90% מסך השגיאות שקיימות בקבצים זוהו ע"י התוכנה 

<p dir="rtl">
 </p>


<p dir="rtl">
<strong><span style="text-decoration:underline;"> </span></strong></p>


<p dir="rtl">
 </p>
