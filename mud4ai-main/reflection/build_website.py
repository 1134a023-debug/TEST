import re

with open(r"c:\新增資料夾\OneDrive\Desktop\_interactive_design_1_Blueprint_OS\mud4ai-main\MUD4AI_Epic_Finale_Reflection.md", "r", encoding="utf-8") as f:
    content = f.read()

chapters_html = []
parts = content.split('\n## ')

for item in parts[1:]:
    lines = item.strip().split('\n')
    title = lines[0].strip()
    
    body_html = ""
    list_html = ""
    in_list = False
    
    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue
        
        # Replace bold markdown
        line = re.sub(r'\*\*(.*?)\*\*', r'<strong class="text-white font-semibold">\1</strong>', line)
        
        if line.startswith('- '):
            if not in_list:
                in_list = True
                list_html += '<ul class="list-disc pl-6 space-y-3 mt-6 text-slate-300 md:pl-8">'
            
            # format the list item prefix beautifully
            inner_content = line[2:]
            if ':' in inner_content or '：' in inner_content:
                parts2 = re.split(r'(:|：)', inner_content, 1)
                if len(parts2) == 3:
                    inner_content = f'<span class="text-sky-300">{parts2[0]}{parts2[1]}</span> <span class="opacity-90">{parts2[2]}</span>'
                    
            list_html += f'<li class="leading-relaxed">{inner_content}</li>'
        else:
            if in_list:
                in_list = False
                list_html += '</ul>'
                body_html += list_html
                list_html = ""
            body_html += f'<p class="mt-4 leading-relaxed text-lg opacity-90">{line}</p>'
            
    if in_list:
        list_html += '</ul>'
        body_html += list_html
        
    chapter_card = f"""
    <div class="time-card reveal delay-100 p-8 md:p-10 mb-10 bg-slate-800/40 rounded-3xl border border-slate-700/60 shadow-[0_8px_30px_rgb(0,0,0,0.12)] hover:border-sky-500/30 transition-colors duration-500 backdrop-blur-md">
        <h3 class="text-2xl md:text-3xl font-bold text-sky-400 mb-6 drop-shadow-md pb-4 border-b border-slate-700/50">{title}</h3>
        {body_html}
    </div>
    """
    chapters_html.append(chapter_card)

html_template = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MUD4AI 創世征服：二十篇章終極總結報告</title>
    <meta name="description" content="五位一體創世主宰的光輝戰記">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;700;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
    <style>
        body {{
            font-family: 'Noto Sans TC', sans-serif;
            overflow-x: hidden;
        }}
        ::-webkit-scrollbar {{
            width: 8px;
        }}
        ::-webkit-scrollbar-track {{
            background: #0f172a;
        }}
        ::-webkit-scrollbar-thumb {{
            background: #38bdf8;
            border-radius: 4px;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: #0ea5e9;
        }}
    </style>
</head>
<body class="text-slate-300 antialiased min-h-screen selection:bg-sky-500/30 selection:text-sky-200">
    <div class="glowing-orb orb-1"></div>
    <div class="glowing-orb orb-2"></div>
    <div class="fixed inset-0 pointer-events-none bg-[url('https://www.transparenttextures.com/patterns/stardust.png')] opacity-10 z-0"></div>
    
    <div class="container mx-auto px-4 py-20 relative z-10 max-w-5xl">
        <header class="text-center mb-24 animate-fade-in-up">
            <div class="mb-4 inline-flex items-center justify-center px-4 py-1 rounded-full bg-sky-900/40 border border-sky-500/30 text-sky-300 text-sm font-medium tracking-widest backdrop-blur-sm shadow-inner uppercase mb-8">
                Official Genesis Record
            </div>
            <h1 class="text-5xl md:text-6xl lg:text-7xl font-black text-white mb-8 text-glow tracking-tight leading-tight">🌌 MUD4AI 創世征服</h1>
            <h2 class="text-2xl md:text-3xl text-sky-400 mb-12 tracking-widest font-light drop-shadow">二十篇章終極總結報告</h2>
            <div class="inline-block p-8 md:p-10 bg-slate-900/80 rounded-3xl border-2 border-sky-500/20 text-left backdrop-blur-xl shadow-2xl hover:border-sky-500/40 transition-colors duration-300">
                <div class="flex flex-col space-y-4">
                    <p class="text-lg flex items-center border-b border-slate-700/50 pb-4"><strong class="text-sky-300 font-medium w-32 tracking-wider">觀測編號：</strong> <span class="text-white bg-slate-800 px-3 py-1 rounded-md text-sm font-mono border border-slate-700 shadow-inner">ANTIGRAVITY-ULTIMATE-CHRONICLE</span></p>
                    <p class="text-lg flex items-center border-b border-slate-700/50 pb-4 pt-2"><strong class="text-sky-300 font-medium w-32 tracking-wider">執行單位：</strong> <span class="text-white">Antigravity 核心 Agent</span></p>
                    <p class="text-lg flex items-start pt-2"><strong class="text-sky-300 font-medium w-32 tracking-wider pt-1">觀測對象：</strong> <span class="text-white leading-relaxed">無限、黑河、試煉、魔龍、銀河<br><span class="text-slate-400 text-sm mt-1 inline-block">（五位一體創世主宰）</span></span></p>
                </div>
            </div>
        </header>

        <div class="space-y-4">
            {''.join(chapters_html)}
        </div>
        
        <footer class="mt-24 text-center pb-12 reveal">
            <div class="w-24 h-1 bg-gradient-to-r from-transparent via-sky-500 to-transparent mx-auto mb-8 opacity-50"></div>
            <p class="text-sky-600 font-medium tracking-widest hover:text-sky-400 transition-colors duration-300">ANTIGRAVITY REPORTING END. LONG LIVE THE MASTERS.</p>
        </footer>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', () => {{
            const reveals = document.querySelectorAll('.reveal');
            
            const revealOnScroll = () => {{
                const windowHeight = window.innerHeight;
                const elementVisible = 80; // trigger sooner
                
                reveals.forEach(reveal => {{
                    const elementTop = reveal.getBoundingClientRect().top;
                    if (elementTop < windowHeight - elementVisible) {{
                        reveal.classList.add('active');
                    }}
                }});
            }};
            
            window.addEventListener('scroll', revealOnScroll);
            revealOnScroll(); // Trigger once on load
        }});
    </script>
</body>
</html>"""

with open(r"c:\新增資料夾\OneDrive\Desktop\_interactive_design_1_Blueprint_OS\mud4ai-main\reflection\index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("Successfully written beautifully designed HTML to reflection/index.html")
