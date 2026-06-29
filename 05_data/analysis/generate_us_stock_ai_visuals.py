from math import cos, radians, sin
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT_DIR = Path("/Users/liuqiyu/Desktop/qveris/05_data/outputs/visuals")
MATRIX_OUT = OUT_DIR / "2026-06-29_us_stock_ai_data_capability_landscape.png"
UNIVERSE_OUT = OUT_DIR / "2026-06-29_us_stock_ai_data_capability_universe.png"

FONT_CJK = "/System/Library/Fonts/PingFang.ttc"
FONT_CJK_ALT = "/System/Library/Fonts/Hiragino Sans GB.ttc"
FONT_EN = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"

INK = "#111827"
MUTED = "#5B6472"
LINE = "#DDE3EA"
LINE_LIGHT = "#EDF1F5"
GREEN = "#0F8A64"
GREEN_FILL = "#E8F7F0"
BLUE = "#1F6FEB"
BLUE_FILL = "#EAF3FF"
GRAY = "#7A7F8A"
GRAY_FILL = "#F0F2F5"
GOLD = "#C58B16"
GOLD_FILL = "#FFF7DA"
TEAL = "#0E8F7E"
NAVY = "#173B63"


def font(size, bold=False):
    path = FONT_CJK if Path(FONT_CJK).exists() else FONT_CJK_ALT
    try:
        return ImageFont.truetype(path, size=size, index=8 if bold else 0)
    except Exception:
        return ImageFont.truetype(FONT_EN, size=size)


def text_size(draw, text, f):
    box = draw.textbbox((0, 0), text, font=f)
    return box[2] - box[0], box[3] - box[1]


def centered_text(draw, box, text, f, fill=INK, anchor_y_adjust=0):
    x1, y1, x2, y2 = box
    w, h = text_size(draw, text, f)
    draw.text((x1 + (x2 - x1 - w) / 2, y1 + (y2 - y1 - h) / 2 + anchor_y_adjust), text, font=f, fill=fill)


def round_rect(draw, box, radius=12, fill="white", outline=LINE, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def badge(draw, center, text, status):
    colors = {
        "Full": (GREEN, GREEN_FILL),
        "Partial": (BLUE, BLUE_FILL),
        "TBD": (GRAY, GRAY_FILL),
        "Gap": (GOLD, GOLD_FILL),
    }
    fg, bg = colors[status]
    f = font(18, bold=True)
    tw, th = text_size(draw, text, f)
    x, y = center
    box = (x - tw / 2 - 18, y - th / 2 - 9, x + tw / 2 + 18, y + th / 2 + 9)
    draw.rounded_rectangle(box, radius=13, fill=bg)
    draw.text((x - tw / 2, y - th / 2 - 1), text, font=f, fill=fg)


def icon_line(draw, x, y, color=TEAL):
    draw.line([(x, y + 24), (x + 14, y + 12), (x + 27, y + 18), (x + 42, y)], fill=color, width=4)
    draw.ellipse((x - 3, y + 21, x + 5, y + 29), fill=color)
    draw.ellipse((x + 11, y + 9, x + 19, y + 17), fill=color)
    draw.ellipse((x + 24, y + 15, x + 32, y + 23), fill=color)
    draw.ellipse((x + 39, y - 3, x + 47, y + 5), fill=color)


def icon_doc(draw, x, y, color=NAVY):
    draw.rounded_rectangle((x, y, x + 38, y + 48), radius=5, outline=color, width=3, fill=None)
    for i in range(3):
        draw.line((x + 9, y + 14 + i * 10, x + 29, y + 14 + i * 10), fill=color, width=2)


def icon_shield(draw, x, y, color=TEAL):
    pts = [(x + 24, y), (x + 44, y + 9), (x + 39, y + 38), (x + 24, y + 50), (x + 9, y + 38), (x + 4, y + 9)]
    draw.polygon(pts, outline=color, fill=None)
    draw.line((x + 15, y + 25, x + 22, y + 33, x + 35, y + 17), fill=color, width=3)


def icon_bars(draw, x, y, color=BLUE):
    for i, h in enumerate([18, 30, 42]):
        draw.rounded_rectangle((x + i * 14, y + 48 - h, x + i * 14 + 8, y + 48), radius=3, fill=None, outline=color, width=3)


def draw_title(draw, title, subtitle, x=80, y=42, centered=False, canvas_w=1600):
    title_f = font(54, bold=True)
    sub_f = font(24)
    if centered:
        tw, _ = text_size(draw, title, title_f)
        sw, _ = text_size(draw, subtitle, sub_f)
        draw.text(((canvas_w - tw) / 2, y), title, font=title_f, fill=INK)
        draw.text(((canvas_w - sw) / 2, y + 72), subtitle, font=sub_f, fill=MUTED)
    else:
        draw.text((x, y), title, font=title_f, fill=INK)
        draw.text((x, y + 70), subtitle, font=sub_f, fill=MUTED)
        draw.line((x, y + 120, x + 110, y + 120), fill=TEAL, width=3)


def generate_matrix():
    W, H = 2000, 1240
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)
    draw_title(draw, "美股 AI 数据能力全景图", "从数据类型、QVeris 公开覆盖到 Agent 工作流的全景映射", centered=True, canvas_w=W)

    rows = [
        ("行情监控", "Market Monitor", ["Full", "Partial", "Partial", "TBD", "TBD", "TBD", "TBD", "Full", "TBD", "Partial", "TBD", "TBD", "TBD"], icon_line, GREEN),
        ("公司研究", "Company Research", ["Partial", "TBD", "TBD", "Full", "Full", "TBD", "TBD", "Full", "TBD", "TBD", "TBD", "TBD", "Gap"], icon_doc, NAVY),
        ("财报披露", "Filings & Earnings", ["TBD", "TBD", "TBD", "Full", "Full", "TBD", "TBD", "Partial", "TBD", "TBD", "TBD", "TBD", "TBD"], icon_doc, NAVY),
        ("估值判断", "Valuation", ["Partial", "TBD", "TBD", "Partial", "Partial", "TBD", "Gap", "TBD", "TBD", "TBD", "TBD", "TBD", "TBD"], icon_bars, BLUE),
        ("预期差", "Consensus Gap", ["TBD", "TBD", "TBD", "Partial", "Partial", "TBD", "Gap", "Partial", "TBD", "TBD", "TBD", "TBD", "TBD"], icon_bars, BLUE),
        ("风险监控", "Risk Monitor", ["Partial", "Partial", "Partial", "TBD", "Partial", "TBD", "TBD", "Partial", "TBD", "Partial", "TBD", "Gap", "Gap"], icon_shield, GOLD),
        ("AI 供应链", "AI Supply Chain", ["TBD", "TBD", "TBD", "Partial", "Partial", "TBD", "TBD", "Partial", "TBD", "TBD", "TBD", "TBD", "Gap"], icon_line, TEAL),
    ]
    cols = [
        ("行情", "Market"),
        ("微观结构", "Micro"),
        ("流动性", "Liquidity"),
        ("基本面", "Fund."),
        ("披露", "Filings"),
        ("估值", "Val."),
        ("预期", "Est."),
        ("新闻事件", "News"),
        ("宏观", "Macro"),
        ("期权", "Options"),
        ("资金持仓", "Flow"),
        ("做空", "Short"),
        ("差异化", "Alt."),
    ]

    table_x, table_y = 210, 205
    row_h, col_w = 70, 112
    left_w = 250
    table_w = left_w + col_w * len(cols)
    table_h = 96 + row_h * len(rows)
    round_rect(draw, (table_x, table_y, table_x + table_w, table_y + table_h), radius=12, fill="white", outline="#CCD4DD")

    # Header
    draw.rectangle((table_x, table_y, table_x + table_w, table_y + 96), fill="white")
    centered_text(draw, (table_x, table_y, table_x + left_w, table_y + 96), "产品场景\nWorkflows", font(22, True), fill=INK)
    for i, (zh, en) in enumerate(cols):
        x1 = table_x + left_w + i * col_w
        draw.line((x1, table_y, x1, table_y + table_h), fill=LINE_LIGHT, width=1)
        centered_text(draw, (x1, table_y + 18, x1 + col_w, table_y + 48), zh, font(18, True), fill=INK)
        centered_text(draw, (x1, table_y + 50, x1 + col_w, table_y + 78), en, font(13), fill=MUTED)
    draw.line((table_x, table_y + 96, table_x + table_w, table_y + 96), fill=LINE, width=1)

    for r_idx, (zh, en, statuses, icon_fn, icon_color) in enumerate(rows):
        y1 = table_y + 96 + r_idx * row_h
        draw.line((table_x, y1, table_x + table_w, y1), fill=LINE_LIGHT, width=1)
        icon_fn(draw, table_x + 28, y1 + 16, icon_color)
        draw.text((table_x + 92, y1 + 14), zh, font=font(19, True), fill=INK)
        draw.text((table_x + 92, y1 + 41), en, font=font(14), fill=MUTED)
        for c_idx, status in enumerate(statuses):
            cx = table_x + left_w + c_idx * col_w + col_w / 2
            cy = y1 + row_h / 2
            label = {"Full": "Full", "Partial": "Part.", "TBD": "TBD", "Gap": "Gap"}[status]
            badge(draw, (cx, cy), label, status)

    # Legend
    legend_x, legend_y = 1660, 80
    for i, (label, st) in enumerate([("已公开确认 Full", "Full"), ("部分确认 Partial", "Partial"), ("需 Inspect / TBD", "TBD"), ("公开缺口 Gap", "Gap")]):
        y = legend_y + i * 34
        badge(draw, (legend_x, y), label.split()[0], st)
        draw.text((legend_x + 70, y - 12), " ".join(label.split()[1:]), font=font(15), fill=MUTED)

    # Trust infrastructure
    infra_y = 845
    draw.line((90, infra_y - 18, 780, infra_y - 18), fill=LINE, width=1)
    draw.line((1220, infra_y - 18, 1910, infra_y - 18), fill=LINE, width=1)
    centered_text(draw, (790, infra_y - 44, 1210, infra_y - 4), "可信基础设施  Trust Infrastructure", font(26, True), fill=INK)
    round_rect(draw, (90, infra_y, 1910, infra_y + 96), radius=12, fill="white", outline="#CCD4DD")
    infra = ["Security Master", "Symbology Mapping", "Exchange Calendar", "Data Freshness", "Provider Reconciliation", "Data Lineage", "Credit Ledger"]
    for i, label in enumerate(infra):
        x = 130 + i * 255
        draw.ellipse((x, infra_y + 28, x + 38, infra_y + 66), outline=NAVY, width=3)
        draw.text((x + 52, infra_y + 28), label, font=font(17), fill=INK)

    # Agent workflows
    flow_y = 1000
    draw.line((90, flow_y - 18, 780, flow_y - 18), fill=LINE, width=1)
    draw.line((1220, flow_y - 18, 1910, flow_y - 18), fill=LINE, width=1)
    centered_text(draw, (790, flow_y - 44, 1210, flow_y - 4), "Agent 工作流  Agent Workflows", font(26, True), fill=INK)
    workflows = [
        ("投资研究", "Research", TEAL),
        ("财报监控", "Earnings", BLUE),
        ("估值助手", "Valuation", NAVY),
        ("风险预警", "Risk", GOLD),
        ("AI 供应链", "AI Chain", TEAL),
        ("报告生成", "Reports", BLUE),
    ]
    for i, (zh, en, color) in enumerate(workflows):
        x = 120 + i * 310
        round_rect(draw, (x, flow_y + 12, x + 240, flow_y + 86), radius=10, fill="white", outline=LINE)
        draw.ellipse((x + 24, flow_y + 29, x + 68, flow_y + 73), outline=color, width=3)
        draw.text((x + 86, flow_y + 26), zh, font=font(20, True), fill=INK)
        draw.text((x + 86, flow_y + 53), en, font=font(14), fill=MUTED)

    draw.text((620, 1168), "核心价值：不只是接入数据，而是让 AI Agent 理解数据路径、质量、覆盖与适用场景。", font=font(18), fill=MUTED)
    img.save(MATRIX_OUT, quality=95)


def arc_polygon(cx, cy, r1, r2, a1, a2, steps=40):
    pts = []
    for i in range(steps + 1):
        a = radians(a1 + (a2 - a1) * i / steps)
        pts.append((cx + r2 * cos(a), cy + r2 * sin(a)))
    for i in range(steps, -1, -1):
        a = radians(a1 + (a2 - a1) * i / steps)
        pts.append((cx + r1 * cos(a), cy + r1 * sin(a)))
    return pts


def generate_universe():
    W, H = 1800, 1120
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)
    draw_title(draw, "美股 AI 数据能力宇宙图", "从可信基础设施，到数据类型、具体能力与 Agent 工作流的全景预览", x=70, y=60)
    cx, cy = 900, 570

    # soft rings
    for r, color in [(520, "#F7FAFC"), (430, "#F2F8FB"), (335, "#EEF8F5"), (238, "#F8FBFF")]:
        draw.ellipse((cx - r, cy - r, cx + r, cy + r), outline=LINE, width=1, fill=None)
        draw.ellipse((cx - r + 8, cy - r + 8, cx + r - 8, cy + r - 8), outline="#F4F6F9", width=1)

    sectors = [
        ("行情\nMarket", "#A6D8FF", 240, 300),
        ("基本面\nFund.", "#BDEDD7", 300, 360),
        ("披露\nFilings", "#BFEFE7", 0, 55),
        ("新闻\nNews", "#D6F5EC", 55, 105),
        ("估值\nValuation", "#EAF2FF", 105, 155),
        ("宏观\nMacro", "#D9ECFF", 155, 210),
        ("期权\nOptions", "#FFE1C7", 210, 240),
    ]
    for label, color, a1, a2 in sectors:
        pts = arc_polygon(cx, cy, 145, 285, a1, a2)
        draw.polygon(pts, fill=color, outline="white")
        ma = radians((a1 + a2) / 2)
        tx, ty = cx + 210 * cos(ma), cy + 210 * sin(ma)
        centered_text(draw, (tx - 78, ty - 34, tx + 78, ty + 34), label, font(22, True), fill=INK)

    draw.ellipse((cx - 142, cy - 142, cx + 142, cy + 142), fill="white", outline=LINE, width=2)
    draw.rounded_rectangle((cx - 116, cy - 96, cx + 116, cy - 50), radius=14, fill="#173B63")
    centered_text(draw, (cx - 116, cy - 96, cx + 116, cy - 50), "1. Trust Core 可信基础设施", font(15, True), fill="white")
    core_items = ["Security Master", "Symbology", "Exchange Calendar", "Provider Reconciliation", "Data Freshness", "Credit Ledger"]
    for i, item in enumerate(core_items):
        x = cx - 105 + (i % 2) * 118
        y = cy - 25 + (i // 2) * 36
        draw.ellipse((x, y, x + 13, y + 13), outline=NAVY, width=2)
        draw.text((x + 19, y - 3), item, font=font(11), fill=INK)

    # Ring labels
    draw.rounded_rectangle((cx - 170, cy - 330, cx + 170, cy - 290), radius=14, fill="white", outline=LINE)
    centered_text(draw, (cx - 170, cy - 330, cx + 170, cy - 290), "2. 数据类型 Data Types", font(20, True), fill=INK)
    draw.rounded_rectangle((cx - 155, cy - 455, cx + 155, cy - 415), radius=14, fill="#111827")
    centered_text(draw, (cx - 155, cy - 455, cx + 155, cy - 415), "3. Agent Workflows 工作流", font(18, True), fill="white")

    points = [
        ("Real-time\nQuote", 250, 415, "Full"),
        ("Historical\nOHLCV", 275, 460, "Full"),
        ("Bid/Ask\nSpread", 310, 420, "Partial"),
        ("SEC\nFilings", 20, 365, "Full"),
        ("Earnings\nRelease", 45, 430, "Full"),
        ("News\nEvents", 70, 390, "Full"),
        ("Valuation\nRatios", 115, 390, "TBD"),
        ("Consensus\nEstimates", 135, 470, "Gap"),
        ("Treasury\nYields", 165, 420, "TBD"),
        ("Options\nIV/OI", 215, 420, "Partial"),
        ("Fund\nFlow", 145, 500, "TBD"),
        ("Short\nInterest", 105, 500, "Gap"),
        ("Supply\nChain", 82, 505, "Gap"),
        ("Dark Pool\nATS/TRF", 60, 505, "Gap"),
    ]
    color_map = {"Full": GREEN, "Partial": BLUE, "TBD": GRAY, "Gap": GOLD}
    for label, angle, radius, st in points:
        a = radians(angle)
        x, y = cx + radius * cos(a), cy + radius * sin(a)
        draw.ellipse((x - 5, y - 5, x + 5, y + 5), fill=color_map[st])
        draw.text((x + 12, y - 16), label, font=font(14), fill=INK)

    # Side workflow cards
    cards = [
        (110, 260, "投资研究", "Investment\nResearch", BLUE),
        (90, 480, "财报监控", "Earnings\nMonitor", TEAL),
        (105, 700, "风险合规", "Risk\nControl", GOLD),
        (1450, 260, "宏观监控", "Macro\nMonitor", GREEN),
        (1480, 500, "报告预警", "Reports\nAlerts", BLUE),
        (1400, 730, "Agent 调用", "Tool\nCalling", "#6F4DBF"),
    ]
    for x, y, zh, en, color in cards:
        round_rect(draw, (x, y, x + 230, y + 96), radius=12, fill="white", outline=LINE)
        draw.ellipse((x + 26, y + 24, x + 74, y + 72), outline=color, width=4)
        draw.text((x + 96, y + 22), zh, font=font(20, True), fill=INK)
        draw.text((x + 96, y + 50), en, font=font(14), fill=MUTED)
        # connector to orbit
        end_x = cx - 520 if x < cx else cx + 520
        draw.line((x + (230 if x < cx else 0), y + 48, end_x, y + 48), fill=LINE, width=1)
        draw.ellipse((end_x - 4, y + 44, end_x + 4, y + 52), fill=color)

    # Legend and note
    legend_x, legend_y = 1535, 90
    for i, (label, st) in enumerate([("Full", "Full"), ("Partial", "Partial"), ("TBD / Inspect", "TBD"), ("Gap", "Gap")]):
        y = legend_y + i * 36
        draw.ellipse((legend_x, y, legend_x + 20, y + 20), fill=color_map[st])
        draw.text((legend_x + 32, y - 2), label, font=font(16), fill=INK)

    round_rect(draw, (1360, 930, 1720, 1035), radius=12, fill="white", outline=LINE)
    draw.text((1390, 955), "关键：", font=font(18, True), fill=BLUE)
    draw.text((1450, 955), "全景不是展示 API 数量，", font=font(18), fill=INK)
    draw.text((1390, 987), "而是展示 AI Agent 能否理解数据路径、", font=font(18), fill=INK)
    draw.text((1390, 1019), "来源、质量与适用场景。", font=font(18), fill=INK)

    img.save(UNIVERSE_OUT, quality=95)


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    generate_matrix()
    generate_universe()
    print(MATRIX_OUT)
    print(UNIVERSE_OUT)


if __name__ == "__main__":
    main()
