<!-- Output copied to clipboard! -->

<!-----
NEW: Check the "Suppress top comment" option to remove this info from the output.

Conversion time: 0.903 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β29
* Sun Feb 28 2021 09:20:03 GMT-0800 (PST)
* Source doc: Copy of README
* Tables are currently converted to HTML tables.
----->


<p dir="rtl">
<strong><span style="text-decoration:underline;">איתור ותיקון שגיאות במסמך שעבר OCR</span></strong></p>


<p dir="rtl">
<strong>מגישים:</strong> אוהד גבאי ושני סמסון</p>


<p dir="rtl">
<strong>רקע:</strong></p>


<p dir="rtl">
קיימים ברשותנו מסמכי חקיקה היסטוריים רבים בפורמטים סרוקים שעברו OCR.</p>


<p dir="rtl">
לצערנו, סריקת OCR אינה מושלמת וקיימים מקרים בהם מתבצעות שגיאות בהמרה באמצעות OCR. כלומר, תוצרי ה-OCR שמתקבלים אינם נאמנים למקור, ומצויים בהם טעויות שונות. נציין לדוגמא מספר טעויות שנחשפנו אליהן במהלך המשימה.</p>


<p dir="rtl">
<strong>הנחיות שימוש בתכנית:</strong></p>


<p dir="rtl">
הערה: הרצנו את התכנית על גבי מערכת הפעלה של Linux.</p>


<p dir="rtl">
<strong><span style="text-decoration:underline;">מטרת הפרויקט:</span></strong></p>


<p dir="rtl">
<span style="text-decoration:underline;">מטרת העל:</span> איתור שגיאות במסמכים שעברו סריקה של OCR.</p>


<p dir="rtl">
<span style="text-decoration:underline;">פירוט על שיטת העבודה:</span> על מנת לאתר את השגיאות במסמכים השונים ביצענו את הצעדים הבאים על מנת לאתר את החשדות בצורה המקיפה ביותר:</p>




*   סריקת קורפוס קבצי XML המכילים את כל החקיקה התקפה בנוסח מלא ויצירת <span style="text-decoration:underline;">מילון המכיל מילים מתוך קבצים אלו.</span> חשוב לציין שנתנו דגש למילים בעלות משמעות להיכנס למילון שלנו ומילים המהוות סעיפים לא נכנסו. התבצע שימוש בביטויים רגולרים שונים על מנת לזהות מילים בצורה מדויקת, למשל - חילוץ מילים מתוך מרכאות וסוגריים וזיהוי תאריכים.
*   Bigram - מעבר על המילים בזוגות. כך יכולנו לזהות מקרים בהם רצף מילים שכנות אינן תקינות
*   שימוש ב - hunspell: ספרייה ב-python המשמשת כמילון עברי חיצוני אשר מאתר שגיאות כתיב במילים.
*   שימוש ב- pytesseract: ספרייה ב-python המשמשת כ- OCR. השתמשנו בקבצי ה-PDF המקוריים, המרנו אותם לתמונות והרצנו את ה OCR הנ"ל, על מנת להשוות לקבצי ה - DOCX שקיבלנו כקלט.

<p dir="rtl">
<strong><span style="text-decoration:underline;">תיאור הפרויקט במונחים של מדעי הרוח הדיגיטליים :</span></strong></p>


<p dir="rtl">
מעבר על תוצרים של סריקות OCR מהווה פעולה ראשונית במשימה, שבה אנו קולטים את התוכן המצוי במסמכי החקיקה השונים. המשימה מתרכזת ב<span style="text-decoration:underline;">תוכן</span> המסמכים ומנסה לאתר שגיאות הקיימות בחקיקה.</p>


<p dir="rtl">
בנוסף, שימוש ב<span style="text-decoration:underline;">מסמכים חצי מובנים</span> - קבצי XML. קבצים אלו מכילים ברובם תיוגים המסייעים לנו במציאת תוכן ספציפי שאותו נרצה לנתח, כאן כאמור התרכזנו בתוכן החוקים ועל כן חילצנו את המשפטים הכלואים בתגיות &lt;p>, אשר מסמלות פסקאות.</p>


<p dir="rtl">
יתר על כן, שימוש ב<span style="text-decoration:underline;">מסמכים לא מובנים</span> - קבצי ה-DOCX המהווים את תוצרי ה-OCR וקבצי ה-PDF המקוריים, שאותם אף הפכנו לתמונות, על מנת להשתמש ב- pytesseract, ספריית ה-OCR בפייתון, שביצעה סריקה, נוסף על הקיים, של קבצים מתוך קורפוס החקיקה.</p>


<p dir="rtl">
בעזרת ביטויים רגולריים, מילון חיצוני והמילון המבוסס על קבצי ה-XML ביצענו <span style="text-decoration:underline;">תיוג</span> בינארי - חשד לשגיאה או לא, על כל אחת מהמילים שהופיעו בתוצרי ה-OCR.</p>


<p dir="rtl">
<strong><span style="text-decoration:underline;">פתרון הבעיה</span></strong></p>


<p dir="rtl">
כעת נסביר על תהליך העבודה שלנו וכיצד פעלנו על מנת למקסם את מציאת המילים החשודות כשגיאות.</p>


<p dir="rtl">
<span style="text-decoration:underline;">שלבים מקדימים לביצוע התוכנית הראשית:</span></p>


<p dir="rtl">
(הערה - הקבצים המבצעים זאת נמצאים בספריית הקוד)</p>




*   Doc2DOCX: המרת תוצרי ה-OCR בפורמט DOC לפורמט DOCX בשל התאמה עבור ספריות נוחות לשימוש בפייתון, שמסייעות בהמרת קבצים בפורמט DOCX לקבצי txt. אנחנו השתמשנו ב-docx2txt.
*   DictionaryCreator: יצירת מילון המורכב ממילים המצויות בקבצי ה-XML. פעולה זאת נחשבת ליקרה ועל ביצענו אותה פעם אחת, ייצאנו לקובץ json ובנינו באמצעותו את המילון שנמצא בשימוש בתוכנית הראשית. מילון זה משתמש בנוסף כמונה - סוכם עבור כל מילה כמה פעמים היא מופיעה.

<p dir="rtl">
<span style="text-decoration:underline;">שלבי התוכנית הראשית (OcrErrorDetector):</span></p>


<p dir="rtl">
<strong>קלט:</strong> נתיב לתיקייה המכילה קבצי PDF וקבצי DOCX.</p>


<p dir="rtl">
<strong>פלט:</strong> קבצי txt עבור כל חוק, אשר ימצא באותה תיקייה שניתנה כקלט.</p>


<p dir="rtl">
<strong><span style="text-decoration:underline;">הערכת התוצאות:</span></strong></p>


<p dir="rtl">
הדרך בה נמדוד את טיב התוצאות היא באמצעות מעבר מדגמי על מספר מסמכים שעברו OCR, והרצת התוכנית שלנו עליהם. בחרנו לנתח 10 קבצים שונים וקיבלנו את התוצאות להלן:</p>



<table>
  <tr>
   <td><strong>False</strong>
   </td>
   <td><strong>True</strong>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td><p dir="rtl">
18</p>

   </td>
   <td><p dir="rtl">
89</p>

   </td>
   <td><strong>Positive</strong>
   </td>
  </tr>
  <tr>
   <td><p dir="rtl">
3</p>

   </td>
   <td>
   </td>
   <td><strong>Negative</strong>
   </td>
  </tr>
</table>


<p dir="rtl">
כעת נסביר מה כל תא בטבלה מסמל:</p>




*   True Positive - מספר השגיאות שהתוכנה זיהתה שהן אכן שגיאות אמיתיות.
*   False Positive - מספר השגיאות שהתוכנה זיהתה אך הן לא באמת שגיאות.
*   False Negative - מספר השגיאות שקיימות בקבצים אך התוכנה לא זיהתה.

<p dir="rtl">
תא אחד נותר ריק מאחר והוא מייצג את רוב המילים (מספר המילים התקינות שהן אכן מילים תקינות)</p>


<p dir="rtl">
<strong>דוגמאות:</strong></p>


<table>
  <tr>
   <td><p dir="rtl">
<strong>מקור</strong></p>

   </td>
   <td><p dir="rtl">
<strong>תוצר</strong></p>

   </td>
   <td><p dir="rtl">
<strong>האם השגיאה אותרה?</strong></p>

   </td>
  </tr>
  <tr>
   <td><p dir="rtl">
נשיא המדינה</p>

   </td>
   <td><p dir="rtl">
בשיא המדיבה</p>

   </td>
   <td><p dir="rtl">
<strong>בשיא </strong>- לא זוהתה כשגיאה, מאחר ומילה זו קיימת במילון ה-XML.</p>

<p>
<p dir="rtl">
<strong>המדיבה </strong>- זוהתה כשגיאה</p>

   </td>
  </tr>
  <tr>
   <td><p dir="rtl">
"על אף האמור בכל <span style="text-decoration:underline;">חיקוק</span> לא יינתן.."</p>

   </td>
   <td><p dir="rtl">
"על אף האמור בכל <span style="text-decoration:underline;">וירקרק</span> לא יינתן.."</p>

   </td>
   <td><p dir="rtl">
<strong>וירקרק </strong>- זוהתה כשגיאה באמצעות המילון החיצוני, לא הופיעה במילון ה- XML.</p>

   </td>
  </tr>
  <tr>
   <td><p dir="rtl">
"..דגלים וסמלים דומים.."</p>

   </td>
   <td><p dir="rtl">
"..דגלים וסמלים דומים.."</p>

   </td>
   <td><p dir="rtl">
<strong>דגלים</strong>- מילה תקינה שזוהתה כשגיאה.</p>

   </td>
  </tr>
</table>

<p dir="rtl">
המילים "המדיבה", "וירקרק" הן שגיאות שהצלחנו לאתר (True Positive)</p>


<p dir="rtl">
המילה "דגלים" הינה מילה תקינה שזוהתה כשגיאה (False Positive)</p>


<p dir="rtl">
המילה "בשיא" הינה שגיאה שלא זוהתה (False Negative)</p>


<p dir="rtl">
<strong>מסקנות:</strong></p>




*   83% מתוך כלל השגיאות שהתוכנה זיהתה, הן אכן שגיאות אמיתיות
*   קרוב ל - 90% מסך השגיאות שקיימות בקבצים זוהו ע"י התוכנה 

<p dir="rtl">
להערכנו, התוצאות שלנו בעיקר טובות כאשר מדובר במילים בעלות שגיאות כתיב, מילים שהשתבשו עם סימן פיסוק שונה מן המקור. בנוסף, ברוב המקרים אנחנו מצליחים לתפוס את השגיאה הנפוצה של הערות השוליים.</p>


<p dir="rtl">
התוצאות שלנו פחות טובות עבור מילים שמספר המופעים שלהם גבוה במילון ה-XML, אך בפועל הן מהוות שגיאה במסמכים מסוימים ("בשיא"). מאחר וחסר לנו הניתוח הלוגי והתחבירי של המשפטים בחקיקה, לא נצליח לאתר שגיאות מהסוג הנ"ל.</p>


<p dir="rtl">
<strong><span style="text-decoration:underline;">סיכום:</span></strong></p>


<p dir="rtl">
בפרויקט זה בחרנו לעבוד עם OCR על מנת למצוא חשדות לשגיאות במסמכי חקיקה. בחרנו לשלב כמה שיטות עבודה שונות על מנת למקסם את מציאת המילים שנפגמו: שימוש במילון חיצוני, בניית מילון פנימי המבוסס על קורפוס קבצי 	ה- XML וסריקה נוספת באמצעות OCR אחר. למדנו מה זה OCR וכיצד כלי זה עובד, הכרנו ועבדנו עם ספריות שונות בפייתון כגון- docx2txt, hunspell. למדנו להשתמש בביטויים רגולרים ועל כך שהם יכולים לסייע לנו במציאת טעויות רבות בחקיקה. ובעיקר יצא לנו לחוות מקרוב את החשיבות של שימוש ב-OCR בהקשר של מדעי הרוח הדיגיטליים.</p>


<p dir="rtl">
אנחנו סבורים שעמדנו במשימה עבור סוג מסוים של שגיאות, כמו שפירטנו בהערכת התוצאות, ומודעים לכך שיש גם שגיאות שלא הצלחנו לעלות עליהן.</p>


<p dir="rtl">
סה"כ שמחנו לקחת חלק בקורס ולהכיר את התחומים השונים של מדעי הרוח הדיגיטליים. העבודה עם OCR הייתה מאתגרת והיינו צריכים ללמוד לזהות שגיאות שונות שלא תמיד חזרו על עצמן בין מסמכי החקיקה השונים.</p>


<p dir="rtl">
 </p>

