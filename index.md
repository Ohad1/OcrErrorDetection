<!-- Output copied to clipboard! -->

<!-----
NEW: Check the "Suppress top comment" option to remove this info from the output.

Conversion time: 1.25 seconds.


Using this HTML file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β29
* Sun Feb 28 2021 09:10:06 GMT-0800 (PST)
* Source doc: README
* Tables are currently converted to HTML tables.
* This document has images: check for >>>>>  gd2md-html alert:  inline image link in generated source and store images to your server. NOTE: Images in exported zip file from Google Docs may not appear in  the same order as they do in your doc. Please check the images!

----->


<p style="color: red; font-weight: bold">>>>>>  gd2md-html alert:  ERRORs: 0; WARNINGs: 0; ALERTS: 2.</p>
<ul style="color: red; font-weight: bold"><li>See top comment block for details on ERRORs and WARNINGs. <li>In the converted Markdown or HTML, search for inline alerts that start with >>>>>  gd2md-html alert:  for specific instances that need correction.</ul>

<p style="color: red; font-weight: bold">Links to alert messages:</p><a href="#gdcalert1">alert1</a>
<a href="#gdcalert2">alert2</a>

<p>
<p dir="rtl">
<strong><span style="text-decoration:underline;">איתור ותיקון שגיאות במסמך שעבר OCR</span></strong></p>

</p>
<p>
<p dir="rtl">
<strong>מגישים:</strong> אוהד גבאי ושני סמסון</p>

</p>
<p>
<p dir="rtl">
<strong>רקע:</strong></p>

</p>
<p>
<p dir="rtl">
קיימים ברשותנו מסמכי חקיקה היסטוריים רבים בפורמטים סרוקים שעברו OCR.</p>

</p>
<p>
<p dir="rtl">
לצערנו, סריקת OCR אינה מושלמת וקיימים מקרים בהם מתבצעות שגיאות בהמרה באמצעות OCR. כלומר, תוצרי ה-OCR שמתקבלים אינם נאמנים למקור, ומצויים בהם טעויות שונות. נציין לדוגמא מספר טעויות שנחשפנו אליהן במהלך המשימה.</p>

</p>
<ol>

<li>שגיאות כתיב 
<ol>
 
<li>החלפה בין כ' ל - ב': כולה -> בולה
 
<li>החלפה בין ס' ל - 0: הסבר -> בולה
 
<li>אותיות במקום מספרים: 

<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


<img src="images/image1.png" width="" alt="alt_text" title="image_tooltip">
 -> ג98ו2, 1 -> ו
 
<li>החלפה בין נ' ל - 'ב: המדינה -> המדיבה
</li> 
</ol>

<li>שגיאות ברישום הערות שוליים: 

<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


<img src="images/image2.png" width="" alt="alt_text" title="image_tooltip">
 -> התשכ"ג-1963 1 או התשכ"ג-11963 

<li>בלבול בין "(מרכאות) לבין זוג גרשיים (' ')
</li>
</ol>
<p>
<p dir="rtl">
<strong>הנחיות שימוש בתכנית:</strong></p>

</p>
<ol>

<li>הורידו ספריית קוד <a href="https://github.com/Ohad1/OcrErrorDetection">ocrErrorDetection</a> מהgithub.

<li>הריצו את התוכנית הראשית OcrErrorDetector.py אשר מקבלת כקלט מחרוזת של הנתיב לתיקייה בה נמצאים קבצי ה-PDF וקבצי ה- DOCX התואמים להם. 
<p>

    <p dir="rtl">
<span style="text-decoration:underline;">דוגמא להרצה:</span> "python OcrErrorDetector.py "/home/username/OcrFolder</p>

</p>
<ol>

<li>בסיום הריצה, יווצרו קבצי txt בעלי שם זהה לקבצי ה-PDF וה-DOCX. קבצים אלו יכילו את תוכן כל אחד מהחוקים בצירוף תגית &lt;ש> לכל מילה החשודה כשגיאה.
</li>
</ol>
</li>
</ol>
<p>
<p dir="rtl">
הערה: הרצנו את התכנית על גבי מערכת הפעלה של Linux.</p>

</p>
<p>
<p dir="rtl">
<strong><span style="text-decoration:underline;">מטרת הפרויקט:</span></strong></p>

</p>
<p>
<p dir="rtl">
<span style="text-decoration:underline;">מטרת העל:</span> איתור שגיאות במסמכים שעברו סריקה של OCR.</p>

</p>
<p>
<p dir="rtl">
<span style="text-decoration:underline;">פירוט על שיטת העבודה:</span> על מנת לאתר את השגיאות במסמכים השונים ביצענו את הצעדים הבאים על מנת לאתר את החשדות בצורה המקיפה ביותר:</p>

</p>
<ul>

<li>סריקת קורפוס קבצי XML המכילים את כל החקיקה התקפה בנוסח מלא ויצירת <span style="text-decoration:underline;">מילון המכיל מילים מתוך קבצים אלו.</span> חשוב לציין שנתנו דגש למילים בעלות משמעות להיכנס למילון שלנו ומילים המהוות סעיפים לא נכנסו. התבצע שימוש בביטויים רגולרים שונים על מנת לזהות מילים בצורה מדויקת, למשל - חילוץ מילים מתוך מרכאות וסוגריים וזיהוי תאריכים.

<li>Bigram - מעבר על המילים בזוגות. כך יכולנו לזהות מקרים בהם רצף מילים שכנות אינן תקינות

<li>שימוש ב - hunspell: ספרייה ב-python המשמשת כמילון עברי חיצוני אשר מאתר שגיאות כתיב במילים.

<li>שימוש ב- pytesseract: ספרייה ב-python המשמשת כ- OCR. השתמשנו בקבצי ה-PDF המקוריים, המרנו אותם לתמונות והרצנו את ה OCR הנ"ל, על מנת להשוות לקבצי ה - DOCX שקיבלנו כקלט.
</li>
</ul>
<p>
<p dir="rtl">
<strong><span style="text-decoration:underline;">תיאור הפרויקט במונחים של מדעי הרוח הדיגיטליים :</span></strong></p>

</p>
<p>
<p dir="rtl">
מעבר על תוצרים של סריקות OCR מהווה פעולה ראשונית במשימה, שבה אנו קולטים את התוכן המצוי במסמכי החקיקה השונים. המשימה מתרכזת ב<span style="text-decoration:underline;">תוכן</span> המסמכים ומנסה לאתר שגיאות הקיימות בחקיקה.</p>

</p>
<p>
<p dir="rtl">
בנוסף, שימוש ב<span style="text-decoration:underline;">מסמכים חצי מובנים</span> - קבצי XML. קבצים אלו מכילים ברובם תיוגים המסייעים לנו במציאת תוכן ספציפי שאותו נרצה לנתח, כאן כאמור התרכזנו בתוכן החוקים ועל כן חילצנו את המשפטים הכלואים בתגיות &lt;p>, אשר מסמלות פסקאות.</p>

</p>
<p>
<p dir="rtl">
יתר על כן, שימוש ב<span style="text-decoration:underline;">מסמכים לא מובנים</span> - קבצי ה-DOCX המהווים את תוצרי ה-OCR וקבצי ה-PDF המקוריים, שאותם אף הפכנו לתמונות, על מנת להשתמש ב- pytesseract, ספריית ה-OCR בפייתון, שביצעה סריקה, נוסף על הקיים, של קבצים מתוך קורפוס החקיקה.</p>

</p>
<p>
<p dir="rtl">
בעזרת ביטויים רגולריים, מילון חיצוני והמילון המבוסס על קבצי ה-XML ביצענו <span style="text-decoration:underline;">תיוג</span> בינארי - חשד לשגיאה או לא, על כל אחת מהמילים שהופיעו בתוצרי ה-OCR.</p>

</p>
<p>
<p dir="rtl">
<strong><span style="text-decoration:underline;">פתרון הבעיה</span></strong></p>

</p>
<p>
<p dir="rtl">
כעת נסביר על תהליך העבודה שלנו וכיצד פעלנו על מנת למקסם את מציאת המילים החשודות כשגיאות.</p>

</p>
<p>
<p dir="rtl">
<span style="text-decoration:underline;">שלבים מקדימים לביצוע התוכנית הראשית:</span></p>

</p>
<p>
<p dir="rtl">
(הערה - הקבצים המבצעים זאת נמצאים בספריית הקוד)</p>

</p>
<ul>

<li>Doc2DOCX: המרת תוצרי ה-OCR בפורמט DOC לפורמט DOCX בשל התאמה עבור ספריות נוחות לשימוש בפייתון, שמסייעות בהמרת קבצים בפורמט DOCX לקבצי txt. אנחנו השתמשנו ב-docx2txt.

<li>DictionaryCreator: יצירת מילון המורכב ממילים המצויות בקבצי ה-XML. פעולה זאת נחשבת ליקרה ועל ביצענו אותה פעם אחת, ייצאנו לקובץ json ובנינו באמצעותו את המילון שנמצא בשימוש בתוכנית הראשית. מילון זה משתמש בנוסף כמונה - סוכם עבור כל מילה כמה פעמים היא מופיעה.
</li>
</ul>
<p>
<p dir="rtl">
<span style="text-decoration:underline;">שלבי התוכנית הראשית (OcrErrorDetector):</span></p>

</p>
<p>
<p dir="rtl">
<strong>קלט:</strong> נתיב לתיקייה המכילה קבצי PDF וקבצי DOCX.</p>

</p>
<p>
<p dir="rtl">
<strong>פלט:</strong> קבצי txt עבור כל חוק, אשר ימצא באותה תיקייה שניתנה כקלט.</p>

</p>
<ul>

<li>יצירת רשימה המבוססת על המילים שנלקחו מתוך סריקת ה-OCR השני עבור חוק מתוך קורפוס החקיקה. 
<ul>
 
<li>המרת קובץ PDF לתמונה
 
<li>הפעלת הפונקציה image_to_string מתוך ספריית pytesseract לחילוץ מילים מתוך התמונה.
 
<li>בניית מילון המורכב ממילים רלוונטיות בלבד על סמך סינון באמצעות ביטויים רגולרים.
</li> 
</ul>

<li>המרת תוצר OCR מקובץ DOCX לקובץ txt.

<li>מעבר על כל שורה המופיעה בקובץ txt 
<ul>
 
<li>סינון מילים רלוונטיות על סמך ביטויים רגולרים.
 
<li>עבור כל מילה -  
<ul>
  
<li>נסביר את אופן החשיבה שלנו. מאחר והמילון המבוסס על קבצי ה-XML מכיל המון מילים, הוא מורכב ממילים רבות מקבצי חקיקה מתוך הקורפוס. ומנגד יש לנו את את המילון החיצוני 	(hunspell) ורשימת מילים שנקלטו מסריקה של ה- OCR האחר. על מנת שנוכל להיעזר בכולם, הגדרנו סף (THRESHOLD) שערכו שווה ל- 10, ומגדיר שאם המילה מופיעה למעלה מ- 10 פעמים (בערך מחצית מן המילים מתוך קבצי ה-XML מופיעות עד 10 פעמים) במילון - נתייג אותה כתקינה. אחרת, ניתן למילה "הזדמנות נוספת" להיווכח שהיא תקינה - אם המילה נכתבה ללא שגיאות כתיב ונמצאת ברשימה של ה-OCR האחר.
</li>  
</ul>
 
<li>יצירת רשימת bigrams המורכבת מזוגות מילים המופיעות באותה שורה, בדרך זו נוכל לדעת האם זוג מילים שכנות מהוות זוג מילים תקינות.
 
<li>כל מילה שחשודה כשגיאה - נעטוף אותה משני צידיה בתיוג &lt;ש> (ש- שגיאה) והיא תעותק באופן הנ"ל לקובץ הפלט.
</li> 
</ul>

<li>יצירת קובץ txt.
</li>
</ul>
<p>
<p dir="rtl">
<strong><span style="text-decoration:underline;">הערכת התוצאות:</span></strong></p>

</p>
<p>
<p dir="rtl">
הדרך בה נמדוד את טיב התוצאות היא באמצעות מעבר מדגמי על מספר מסמכים שעברו OCR, והרצת התוכנית שלנו עליהם. בחרנו לנתח 10 קבצים שונים וקיבלנו את התוצאות להלן:</p>

</p>

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


<p>
<p dir="rtl">
כעת נסביר מה כל תא בטבלה מסמל:</p>

</p>
<ul>

<li>True Positive - מספר השגיאות שהתוכנה זיהתה שהן אכן שגיאות אמיתיות.

<li>False Positive - מספר השגיאות שהתוכנה זיהתה אך הן לא באמת שגיאות.

<li>False Negative - מספר השגיאות שקיימות בקבצים אך התוכנה לא זיהתה.
</li>
</ul>
<p>
<p dir="rtl">
תא אחד נותר ריק מאחר והוא מייצג את רוב המילים (מספר המילים התקינות שהן אכן מילים תקינות)</p>

</p>
<p>
<p dir="rtl">
<strong>דוגמאות:</strong></p>

</p>

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


<p>
<p dir="rtl">
המילים "המדיבה", "וירקרק" הן שגיאות שהצלחנו לאתר (True Positive)</p>

</p>
<p>
<p dir="rtl">
המילה "דגלים" הינה מילה תקינה שזוהתה כשגיאה (False Positive)</p>

</p>
<p>
<p dir="rtl">
המילה "בשיא" הינה שגיאה שלא זוהתה (False Negative)</p>

</p>
<p>
<p dir="rtl">
<strong>מסקנות:</strong></p>

</p>
<ul>

<li>83% מתוך כלל השגיאות שהתוכנה זיהתה, הן אכן שגיאות אמיתיות

<li>קרוב ל - 90% מסך השגיאות שקיימות בקבצים זוהו ע"י התוכנה 
</li>
</ul>
<p>
<p dir="rtl">
להערכנו, התוצאות שלנו בעיקר טובות כאשר מדובר במילים בעלות שגיאות כתיב, מילים שהשתבשו עם סימן פיסוק שונה מן המקור. בנוסף, ברוב המקרים אנחנו מצליחים לתפוס את השגיאה הנפוצה של הערות השוליים.</p>

</p>
<p>
<p dir="rtl">
התוצאות שלנו פחות טובות עבור מילים שמספר המופעים שלהם גבוה במילון ה-XML, אך בפועל הן מהוות שגיאה במסמכים מסוימים ("בשיא"). מאחר וחסר לנו הניתוח הלוגי והתחבירי של המשפטים בחקיקה, לא נצליח לאתר שגיאות מהסוג הנ"ל.</p>

</p>
<p>
<p dir="rtl">
<strong><span style="text-decoration:underline;">סיכום:</span></strong></p>

</p>
<p>
<p dir="rtl">
בפרויקט זה בחרנו לעבוד עם OCR על מנת למצוא חשדות לשגיאות במסמכי חקיקה. בחרנו לשלב כמה שיטות עבודה שונות על מנת למקסם את מציאת המילים שנפגמו: שימוש במילון חיצוני, בניית מילון פנימי המבוסס על קורפוס קבצי 	ה- XML וסריקה נוספת באמצעות OCR אחר. למדנו מה זה OCR וכיצד כלי זה עובד, הכרנו ועבדנו עם ספריות שונות בפייתון כגון- docx2txt, hunspell. למדנו להשתמש בביטויים רגולרים ועל כך שהם יכולים לסייע לנו במציאת טעויות רבות בחקיקה. ובעיקר יצא לנו לחוות מקרוב את החשיבות של שימוש ב-OCR בהקשר של מדעי הרוח הדיגיטליים.</p>

</p>
<p>
<p dir="rtl">
אנחנו סבורים שעמדנו במשימה עבור סוג מסוים של שגיאות, כמו שפירטנו בהערכת התוצאות, ומודעים לכך שיש גם שגיאות שלא הצלחנו לעלות עליהן.</p>

</p>
<p>
<p dir="rtl">
סה"כ שמחנו לקחת חלק בקורס ולהכיר את התחומים השונים של מדעי הרוח הדיגיטליים. העבודה עם OCR הייתה מאתגרת והיינו צריכים ללמוד לזהות שגיאות שונות שלא תמיד חזרו על עצמן בין מסמכי החקיקה השונים.</p>

</p>
<p>
<p dir="rtl">
 </p>

</p>
