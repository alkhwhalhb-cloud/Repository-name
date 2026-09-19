from flask import Flask, render_template_string

app = Flask(__name__)

# بيانات الشركة في سوريا
OWNER_1 = "مصطفى أبو بكر"
OWNER_2 = "محمد علو"
LOCATION_TEXT = "سوريا - محافظة إدلب - أرمناز"
PHONE_NUMBER = "+963941784954"
PHONE_DISPLAY = "+963 941 784 954"
WHATSAPP_NUMBER = "963941784954"

# بيانات مطور وصانع الموقع
DEV_NAME = "Aziz S Hussein"
DEV_WHATSAPP = "9647716001163"
DEV_PHONE_DISPLAY = "+964 771 600 1163"

HTML_CODE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>شركة العلو وأبو بكر | تصنيع مناشر الحجر والروافع الجسرية - أرمناز</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
        body { background-color: #0d1117; color: #e6edf3; line-height: 1.6; padding-bottom: 40px; }
        .container { max-width: 920px; margin: 0 auto; padding: 15px; }

        .top-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 8px 12px;
            background: #161b22;
            border: 1px solid #30363d;
            border-radius: 12px;
            margin-bottom: 15px;
        }
        .top-bar-title { font-size: 0.9rem; color: #94a3b8; font-weight: 500; }
        .menu-dots-btn {
            background: #21262d;
            border: 1px solid #30363d;
            color: #f59e0b;
            font-size: 1.6rem;
            width: 42px;
            height: 42px;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: 0.2s;
            line-height: 1;
        }
        .menu-dots-btn:hover { background: #30363d; color: #fff; transform: scale(1.05); }

        .modal-overlay {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.75);
            backdrop-filter: blur(4px);
            z-index: 9999;
            align-items: center;
            justify-content: center;
            padding: 15px;
        }
        .modal-box {
            background: linear-gradient(145deg, #161b22, #0f141c);
            border: 2px solid #38bdf8;
            border-radius: 18px;
            max-width: 440px;
            width: 100%;
            padding: 25px 20px;
            text-align: center;
            position: relative;
            box-shadow: 0 10px 35px rgba(56, 189, 248, 0.25);
            animation: popIn 0.3s ease-out;
        }
        @keyframes popIn { from { transform: scale(0.85); opacity: 0; } to { transform: scale(1); opacity: 1; } }
        .modal-close {
            position: absolute;
            top: 12px;
            left: 14px;
            background: #21262d;
            border: 1px solid #30363d;
            color: #94a3b8;
            font-size: 1.3rem;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .modal-close:hover { color: #fff; background: #e11d48; }

        .dev-badge {
            display: inline-block;
            background: rgba(56, 189, 248, 0.15);
            color: #38bdf8;
            border: 1px solid #38bdf8;
            padding: 4px 14px;
            border-radius: 20px;
            font-size: 0.82rem;
            font-weight: bold;
            margin-bottom: 12px;
        }
        .dev-name { color: #ffb703; font-size: 1.5rem; font-weight: 800; margin-bottom: 4px; }
        .dev-role { color: #cbd5e1; font-size: 0.95rem; font-weight: 500; margin-bottom: 14px; }
        .dev-phone-box {
            background: #0d1117;
            border: 1px solid #30363d;
            border-radius: 10px;
            padding: 8px 14px;
            display: inline-block;
            direction: ltr;
            color: #38bdf8;
            font-weight: bold;
            font-size: 1.15rem;
            letter-spacing: 1px;
            margin-bottom: 15px;
        }
        .dev-about { color: #94a3b8; font-size: 0.88rem; line-height: 1.6; margin-bottom: 20px; }
        .btn-dev-wa {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            background: #25d366;
            color: white;
            padding: 12px 20px;
            border-radius: 10px;
            text-decoration: none;
            font-weight: bold;
            font-size: 1rem;
            transition: 0.2s;
            box-shadow: 0 4px 15px rgba(37, 211, 102, 0.4);
            width: 100%;
        }
        .btn-dev-wa:hover { background: #1ebe5d; transform: translateY(-2px); }

        header {
            background: linear-gradient(135deg, #161b22, #0a0d12);
            border: 1px solid #30363d;
            border-top: 4px solid #f59e0b;
            border-radius: 16px;
            padding: 30px 20px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.6);
            margin-bottom: 25px;
        }
        .badge-loc {
            display: inline-block;
            background: rgba(245, 158, 11, 0.15);
            color: #f59e0b;
            border: 1px solid #f59e0b;
            padding: 5px 16px;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: bold;
            margin-bottom: 12px;
        }
        h1 { color: #f8fafc; font-size: 2.1rem; margin-bottom: 6px; font-weight: 800; }
        .subtitle { color: #38bdf8; font-size: 1.15rem; font-weight: bold; margin-bottom: 12px; }
        
        .owners-box {
            display: inline-flex;
            gap: 15px;
            background: #21262d;
            border: 1px solid #30363d;
            padding: 8px 18px;
            border-radius: 10px;
            margin-bottom: 16px;
            flex-wrap: wrap;
            justify-content: center;
        }
        .owner-item { color: #f0f6fc; font-size: 0.95rem; }
        .owner-item b { color: #f59e0b; }

        .bio { color: #8b949e; font-size: 0.95rem; max-width: 720px; margin: 0 auto 18px; }

        .phone-highlight {
            background: #161b22;
            border: 1px solid #30363d;
            display: inline-block;
            padding: 8px 22px;
            border-radius: 10px;
            margin-bottom: 18px;
            direction: ltr;
            font-size: 1.3rem;
            font-weight: bold;
            color: #38bdf8;
            letter-spacing: 1px;
        }

        .cta-buttons { display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; }
        .btn-call, .btn-wa {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            padding: 13px 25px;
            border-radius: 10px;
            text-decoration: none;
            font-weight: bold;
            font-size: 1.05rem;
            transition: 0.3s;
            flex: 1;
            min-width: 220px;
            max-width: 280px;
        }
        .btn-wa { background: #238636; color: #fff; box-shadow: 0 4px 15px rgba(35, 134, 54, 0.4); }
        .btn-wa:hover { background: #2ea043; transform: translateY(-2px); }
        .btn-call { background: #f59e0b; color: #000; box-shadow: 0 4px 15px rgba(245, 158, 11, 0.4); }
        .btn-call:hover { background: #d97706; transform: translateY(-2px); }

        .section-title {
            color: #f59e0b;
            font-size: 1.35rem;
            font-weight: bold;
            margin: 30px 0 18px;
            display: flex;
            align-items: center;
            gap: 10px;
            border-right: 4px solid #f59e0b;
            padding-right: 12px;
        }

        .gallery-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; }
        .gallery-card {
            background: #161b22;
            border: 1px solid #30363d;
            border-radius: 14px;
            overflow: hidden;
            box-shadow: 0 6px 20px rgba(0,0,0,0.4);
            display: flex;
            flex-direction: column;
            transition: 0.3s;
        }
        .gallery-card:hover { border-color: #f59e0b; transform: translateY(-4px); }
        
        .img-container {
            width: 100%;
            height: 210px;
            background: #090c10;
            display: flex;
            align-items: center;
            justify-content: center;
            border-bottom: 1px solid #30363d;
        }
        .img-container svg { width: 100%; height: 100%; }

        .gallery-info { padding: 18px; flex: 1; display: flex; flex-direction: column; justify-content: space-between; }
        .gallery-info h3 { color: #f0f6fc; font-size: 1.15rem; margin-bottom: 8px; }
        .gallery-info p { color: #8b949e; font-size: 0.9rem; line-height: 1.6; margin-bottom: 12px; }
        .spec-badge {
            display: inline-block;
            background: rgba(56, 189, 248, 0.12);
            color: #38bdf8;
            border: 1px solid rgba(56, 189, 248, 0.3);
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 0.8rem;
            align-self: flex-start;
            font-weight: 500;
        }

        .info-box {
            background: #161b22;
            border: 1px solid #30363d;
            border-radius: 14px;
            padding: 24px;
            margin-top: 35px;
            text-align: center;
        }
        .info-title { color: #f59e0b; font-size: 1.25rem; font-weight: bold; margin-bottom: 12px; }
        .info-details { color: #c9d1d9; font-size: 0.98rem; line-height: 2; }
        .owners-tag { color: #38bdf8; font-weight: bold; font-size: 1.1rem; }

        footer { text-align: center; color: #6e7681; font-size: 0.85rem; margin-top: 40px; }
        footer b { color: #f59e0b; }
    </style>
</head>
<body>

<div class="container">

    <div class="top-bar">
        <span class="top-bar-title">🏢 شركة العلو وأبو بكر للصناعات الثقيلة</span>
        <button class="menu-dots-btn" onclick="openDevModal()" title="صانع ومطور الموقع">⋮</button>
    </div>

    <div id="devModal" class="modal-overlay" onclick="closeOnOutside(event)">
        <div class="modal-box">
            <button class="modal-close" onclick="closeDevModal()">&times;</button>
            <div class="dev-badge">💻 صانع ومطور الموقع</div>
            <div class="dev-name">{{ dev_name }}</div>
            <div class="dev-role">Digital Creator & Web Developer</div>
            <div class="dev-phone-box">📱 {{ dev_phone }}</div>
            <p class="dev-about">
                تمت برمجة وتصميم وتطوير هذا الموقع بواسطة المطور <b>{{ dev_name }}</b>.<br>
                هل ترغب بإنشاء وتصميم موقع احترافي لشركتك أو عملك؟ تواصل معي مباشرة عبر واتساب.
            </p>
            <a href="https://wa.me/{{ dev_wa }}?text=مرحباً عزيز، رأيت موقع شركة العلو وأبو بكر وأود تصميم وبرمجة موقع لعملي" target="_blank" class="btn-dev-wa">
                💬 تواصل مع عزيز عبر واتساب
            </a>
        </div>
    </div>

    <header>
        <div class="badge-loc">📍 {{ location }}</div>
        <h1>شركة العلو وأبو بكر</h1>
        <div class="subtitle">لتصنيع وتفصيل مناشر الحجر، الروافع الجسرية والمعدات الثقيلة</div>
        
        <div class="owners-box">
            <div class="owner-item">إدارة وتصنيع: <b>السيد {{ owner1 }}</b></div>
            <div class="owner-item">& <b>السيد {{ owner2 }}</b></div>
        </div>

        <p class="bio">
            خبرة متقدمة وجودة صناعية في تصنيع مناشر الحجر الكبيرة، الروافع الجسرية للمقالع والمعامل، خطوط الجلي والتلميع الأوتوماتيكية، ومشارح الديسك بأعلى معايير المتانة.
        </p>

        <div>
            <span class="phone-highlight">📱 {{ phone_display }}</span>
        </div>

        <div class="cta-buttons">
            <a href="https://wa.me/{{ wa_num }}?text=السلام عليكم، أود الاستفسار وطلب تفصيل معدات من المعلمين مصطفى أبو بكر ومحمد علو" target="_blank" class="btn-wa">
                💬 مراسلة عبر واتساب
            </a>
            <a href="tel:{{ phone_num }}" class="btn-call">
                📞 اتصال مباشر
            </a>
        </div>
    </header>

    <div class="section-title">⚙️ معرض الآليات والمعدات المصنعة في ورشتنا</div>
    
    <div class="gallery-grid">
        
        <!-- 1. جلاية متعددة الرؤوس -->
        <div class="gallery-card">
            <div class="img-container">
                <svg viewBox="0 0 400 220" xmlns="http://www.w3.org/2000/svg">
                    <rect width="400" height="220" fill="#11161f"/>
                    <rect x="30" y="90" width="340" height="40" rx="4" fill="#e2e8f0" stroke="#94a3b8" stroke-width="2"/>
                    <rect x="40" y="100" width="320" height="15" fill="#f8fafc"/>
                    <g fill="#f97316" stroke="#c2410c" stroke-width="1.5">
                        <rect x="50" y="45" width="22" height="45" rx="3"/><rect x="80" y="45" width="22" height="45" rx="3"/>
                        <rect x="110" y="45" width="22" height="45" rx="3"/><rect x="140" y="45" width="22" height="45" rx="3"/>
                        <rect x="170" y="45" width="22" height="45" rx="3"/><rect x="200" y="45" width="22" height="45" rx="3"/>
                        <rect x="230" y="45" width="22" height="45" rx="3"/><rect x="260" y="45" width="22" height="45" rx="3"/>
                        <rect x="290" y="45" width="22" height="45" rx="3"/><rect x="320" y="45" width="22" height="45" rx="3"/>
                    </g>
                    <g fill="#1e293b">
                        <rect x="52" y="38" width="18" height="7" rx="2"/><rect x="82" y="38" width="18" height="7" rx="2"/>
                        <rect x="112" y="38" width="18" height="7" rx="2"/><rect x="142" y="38" width="18" height="7" rx="2"/>
                        <rect x="172" y="38" width="18" height="7" rx="2"/><rect x="202" y="38" width="18" height="7" rx="2"/>
                        <rect x="232" y="38" width="18" height="7" rx="2"/><rect x="262" y="38" width="18" height="7" rx="2"/>
                        <rect x="292" y="38" width="18" height="7" rx="2"/><rect x="322" y="38" width="18" height="7" rx="2"/>
                    </g>
                    <rect x="30" y="130" width="340" height="20" fill="#334155"/>
                    <g fill="#0284c7">
                        <circle cx="61" cy="160" r="10"/><circle cx="121" cy="160" r="10"/>
                        <circle cx="181" cy="160" r="10"/><circle cx="241" cy="160" r="10"/><circle cx="301" cy="160" r="10"/>
                    </g>
                    <rect x="20" y="175" width="360" height="15" fill="#1e293b" stroke="#475569"/>
                    <text x="200" y="205" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">جلاية أوتوماتيكية متعددة الرؤوس</text>
                </svg>
            </div>
            <div class="gallery-info">
                <div>
                    <h3>جلاية رخام وحجر متعددة الرؤوس</h3>
                    <p>خط جلي وتلميع آلي بمحركات متتالية عالية القدرة، يضمن استواء سطح الحجر والرخام وسرعة فائقة في الإنتاج.</p>
                </div>
                <span class="spec-badge">تحكم كهربائي وهيدروليكي متكامل</span>
            </div>
        </div>

        <!-- 2. رافعة جسرية صفراء -->
        <div class="gallery-card">
            <div class="img-container">
                <svg viewBox="0 0 400 220" xmlns="http://www.w3.org/2000/svg">
                    <rect width="400" height="220" fill="#11161f"/>
                    <rect x="30" y="70" width="340" height="45" rx="5" fill="#eab308" stroke="#ca8a04" stroke-width="2"/>
                    <line x1="40" y1="50" x2="360" y2="50" stroke="#0f172a" stroke-width="3"/>
                    <line x1="60" y1="50" x2="60" y2="70" stroke="#0f172a" stroke-width="2"/>
                    <line x1="120" y1="50" x2="120" y2="70" stroke="#0f172a" stroke-width="2"/>
                    <line x1="180" y1="50" x2="180" y2="70" stroke="#0f172a" stroke-width="2"/>
                    <line x1="240" y1="50" x2="240" y2="70" stroke="#0f172a" stroke-width="2"/>
                    <line x1="300" y1="50" x2="300" y2="70" stroke="#0f172a" stroke-width="2"/>
                    <line x1="340" y1="50" x2="340" y2="70" stroke="#0f172a" stroke-width="2"/>
                    <text x="200" y="98" fill="#1e3a8a" font-size="14" font-weight="900" text-anchor="middle">ما شاء الله - رافعة مقالع ثقيلة</text>
                    <rect x="175" y="115" width="50" height="22" rx="3" fill="#1e293b" stroke="#64748b"/>
                    <line x1="200" y1="137" x2="200" y2="165" stroke="#f1f5f9" stroke-width="3" stroke-dasharray="3,2"/>
                    <path d="M195,165 Q200,180 205,165" fill="none" stroke="#f59e0b" stroke-width="4"/>
                    <rect x="25" y="60" width="16" height="110" fill="#ca8a04"/>
                    <rect x="359" y="60" width="16" height="110" fill="#ca8a04"/>
                    <rect x="15" y="170" width="370" height="12" fill="#334155"/>
                    <text x="200" y="205" fill="#f59e0b" font-size="12" font-weight="bold" text-anchor="middle">رافعة جسرية (Overhead Crane) حمولات عالية</text>
                </svg>
            </div>
            <div class="gallery-info">
                <div>
                    <h3>رافعة جسرية ثقيلة للمقالع</h3>
                    <p>جسر رافعة فولاذي مصمم للأوزان الثقيلة وكتل البلوك الكبيرة، مع نظام سحب وتدوير هيدروليكي آمن وسلس.</p>
                </div>
                <span class="spec-badge">تحمل أطنان وأوزان مقالع عالية</span>
            </div>
        </div>

        <!-- 3. مقص ومفرزة ديسك مع رولات -->
        <div class="gallery-card">
            <div class="img-container">
                <svg viewBox="0 0 400 220" xmlns="http://www.w3.org/2000/svg">
                    <rect width="400" height="220" fill="#11161f"/>
                    <rect x="40" y="120" width="320" height="25" fill="#e2e8f0" stroke="#2563eb" stroke-width="2"/>
                    <g stroke="#64748b" stroke-width="3">
                        <line x1="60" y1="120" x2="60" y2="145"/><line x1="90" y1="120" x2="90" y2="145"/>
                        <line x1="120" y1="120" x2="120" y2="145"/><line x1="150" y1="120" x2="150" y2="145"/>
                        <line x1="250" y1="120" x2="250" y2="145"/><line x1="280" y1="120" x2="280" y2="145"/>
                        <line x1="310" y1="120" x2="310" y2="145"/><line x1="340" y1="120" x2="340" y2="145"/>
                    </g>
                    <rect x="170" y="45" width="60" height="50" fill="#f8fafc" stroke="#2563eb" stroke-width="2"/>
                    <rect x="185" y="25" width="30" height="20" rx="3" fill="#2563eb"/>
                    <circle cx="200" cy="115" r="28" fill="#1d4ed8" stroke="#60a5fa" stroke-width="2"/>
                    <circle cx="200" cy="115" r="8" fill="#ffffff"/>
                    <polygon points="160,145 240,145 215,185 185,185" fill="#1e3a8a"/>
                    <text x="200" y="208" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">مقص ومفرزة ديسك مع طاولة رولات</text>
                </svg>
            </div>
            <div class="gallery-info">
                <div>
                    <h3>مقص ومفرزة ديسك مع طاولة رولات</h3>
                    <p>تشريح وقص دقيق لألواح وواجهات الحجر والرخام، مزودة بسكة رولات حديدية لسهولة تدوير وسحب الكتل.</p>
                </div>
                <span class="spec-badge">قص وتشريح عالي الدقة</span>
            </div>
        </div>

        <!-- 4. هيكل منشرة جسرية زرقاء -->
        <div class="gallery-card">
            <div class="img-container">
                <svg viewBox="0 0 400 220" xmlns="http://www.w3.org/2000/svg">
                    <rect width="400" height="220" fill="#11161f"/>
                    <rect x="60" y="45" width="35" height="135" fill="#1e40af" stroke="#60a5fa" stroke-width="2"/>
                    <rect x="305" y="45" width="35" height="135" fill="#1e40af" stroke="#60a5fa" stroke-width="2"/>
                    <rect x="312" y="25" width="22" height="20" rx="2" fill="#2563eb"/>
                    <rect x="50" y="95" width="300" height="35" rx="3" fill="#1d4ed8" stroke="#93c5fd" stroke-width="2"/>
                    <line x1="75" y1="112" x2="325" y2="112" stroke="#ffffff" stroke-width="2"/>
                    <rect x="40" y="175" width="320" height="15" fill="#0f172a" stroke="#334155" stroke-width="2"/>
                    <text x="200" y="208" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">هيكل منشرة كتل وبلوك حجر متين</text>
                </svg>
            </div>
            <div class="gallery-info">
                <div>
                    <h3>هيكل منشرة كتل وبلوك حجر</h3>
                    <p>أعمدة وقواعد حديدية ضخمة مصممة لامتصاص الاهتزاز والرجفان أثناء قص الكتل الحجرية الكبيرة في المقالع.</p>
                </div>
                <span class="spec-badge">فولاذ معالج ضد الاهتزاز</span>
            </div>
        </div>

        <!-- 5. جسر وقاعدة منشرة أبيض وأحمر -->
        <div class="gallery-card">
            <div class="img-container">
                <svg viewBox="0 0 400 220" xmlns="http://www.w3.org/2000/svg">
                    <rect width="400" height="220" fill="#11161f"/>
                    <rect x="35" y="65" width="330" height="55" rx="4" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
                    <g fill="#0f172a">
                        <circle cx="80" cy="80" r="10"/><circle cx="130" cy="80" r="10"/><circle cx="180" cy="80" r="10"/>
                        <circle cx="230" cy="80" r="10"/><circle cx="280" cy="80" r="10"/><circle cx="320" cy="80" r="10"/>
                    </g>
                    <rect x="40" y="90" width="30" height="25" fill="#b91c1c"/>
                    <rect x="330" y="90" width="30" height="25" fill="#b91c1c"/>
                    <rect x="25" y="125" width="350" height="30" fill="#b91c1c"/>
                    <polygon points="120,125 145,125 135,155 110,155" fill="#ffffff"/>
                    <polygon points="170,125 195,125 185,155 160,155" fill="#ffffff"/>
                    <polygon points="220,125 245,125 235,155 210,155" fill="#ffffff"/>
                    <polygon points="270,125 295,125 285,155 260,155" fill="#ffffff"/>
                    <rect x="75" y="155" width="30" height="30" fill="#f8fafc"/><rect x="185" y="155" width="30" height="30" fill="#f8fafc"/><rect x="295" y="155" width="30" height="30" fill="#f8fafc"/>
                    <text x="200" y="208" fill="#f87171" font-size="12" font-weight="bold" text-anchor="middle">جسر وقاعدة منشرة تفصيل خاص</text>
                </svg>
            </div>
            <div class="gallery-info">
                <div>
                    <h3>جسر وقاعدة منشرة تفصيل خاص</h3>
                    <p>تصنيع وتفصيل جسور وقواعد المناشر حسب المقاسات المطلوبة وسماكة الكتل للورش والمعامل والمقالع.</p>
                </div>
                <span class="spec-badge">تفصيل وتعديل حسب الطلب</span>
            </div>
        </div>

        <!-- 6. تجهيز وشحن المعدات بالونش -->
        <div class="gallery-card">
            <div class="img-container">
                <svg viewBox="0 0 400 220" xmlns="http://www.w3.org/2000/svg">
                    <rect width="400" height="220" fill="#11161f"/>
                    <rect x="0" y="0" width="400" height="130" fill="#1e293b"/>
                    <rect x="0" y="130" width="400" height="90" fill="#0f172a"/>
                    <rect x="30" y="135" width="340" height="40" rx="3" fill="#1e3a8a"/>
                    <circle cx="80" cy="180" r="16" fill="#000000" stroke="#475569" stroke-width="4"/>
                    <circle cx="130" cy="180" r="16" fill="#000000" stroke="#475569" stroke-width="4"/>
                    <circle cx="280" cy="180" r="16" fill="#000000" stroke="#475569" stroke-width="4"/>
                    <circle cx="330" cy="180" r="16" fill="#000000" stroke="#475569" stroke-width="4"/>
                    <polygon points="50,140 70,60 85,65 65,140" fill="#dc2626"/>
                    <polygon points="70,60 180,30 185,45 80,70" fill="#ef4444"/>
                    <line x1="180" y1="40" x2="180" y2="70" stroke="#e2e8f0" stroke-width="2" stroke-dasharray="3,2"/>
                    <rect x="140" y="70" width="130" height="45" rx="3" fill="#f97316" stroke="#ffffff" stroke-width="2"/>
                    <text x="205" y="97" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">تحميل الماكينة</text>
                    <text x="200" y="210" fill="#f59e0b" font-size="12" font-weight="bold" text-anchor="middle">تجهيز وشحن وتركيب في المقالع</text>
                </svg>
            </div>
            <div class="gallery-info">
                <div>
                    <h3>تجهيز وشحن وتركيب في المقالع</h3>
                    <p>متابعة كاملة لعمليات التحميل الميداني، النقل بالرافعات، التركيب في مقلع الزبون وتشغيل الآلية لتسليمها جاهزة للإنتاج.</p>
                </div>
                <span class="spec-badge">تسليم وتشغيل ميداني متكامل</span>
            </div>
        </div>

    </div>

    <div class="info-box">
        <div class="info-title">📍 مقر الورشة والإدارة الرسمية</div>
        <div class="info-details">
            الموقع: <b>{{ location }}</b><br>
            أصحاب الشركة والإدارة: <span class="owners-tag">{{ owner1 }} & {{ owner2 }}</span><br>
            رقم التواصل المباشر / واتساب المعمل: <b>{{ phone_display }}</b><br>
            لتفصيل الآليات والمناشر، الصيانة، وطلب عروض الأسعار: نسعد باتصالكم أو مراسلتنا واتساب مباشرة.
        </div>
    </div>

    <footer>
        جميع الحقوق محفوظة &copy; 2026 | شركة <b>{{ owner1 }} & {{ owner2 }}</b> - مناشر حجر وروافع جسرية
    </footer>

</div>

<script>
    function openDevModal() { document.getElementById('devModal').style.display = 'flex'; }
    function closeDevModal() { document.getElementById('devModal').style.display = 'none'; }
    function closeOnOutside(e) { if (e.target.id === 'devModal') { closeDevModal(); } }
</script>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(
        HTML_CODE,
        phone_num=PHONE_NUMBER,
        phone_display=PHONE_DISPLAY,
        wa_num=WHATSAPP_NUMBER,
        owner1=OWNER_1,
        owner2=OWNER_2,
        location=LOCATION_TEXT,
        dev_name=DEV_NAME,
        dev_phone=DEV_PHONE_DISPLAY,
        dev_wa=DEV_WHATSAPP
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
