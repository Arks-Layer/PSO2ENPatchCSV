#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
MATTERBOARD_DIR = REPO_ROOT / "Story" / "Matterboard"
ACTOR_TSV = REPO_ROOT / "_local" / "classic" / "actor_name_classic_npc_name_and_title_ko_jp.tsv"
REGION_TSV = REPO_ROOT / "_local" / "classic" / "ui_craft_name_classic_region_like_ko_jp.tsv"
PLACE_TSV = REPO_ROOT / "_local" / "classic" / "matterboard_place_label_ko_jp.tsv"
CHAR_ALIAS_TSV = REPO_ROOT / "_local" / "classic" / "matterboard_character_alias_ko_jp.tsv"
TITLE_TSV = REPO_ROOT / "_local" / "classic" / "matterboard_title_like_ko_jp.tsv"
EP1_QUEST_TITLE_TSV = REPO_ROOT / "_local" / "classic" / "episode1_quest_title_ko_jp.tsv"


TARGET_TEMPLATE_MAP = {
    "該当のクエスト中、何処かに出現する<br>イベントフィールドを発見し<br>イベントを閲覧してくること。":
        "해당 퀘스트 중 어딘가에 출현하는<br>이벤트 필드를 발견해<br>이벤트를 확인해 올 것.",
    "下記のクエスト中、何処かに出現する<br>イベントフィールドを発見し<br>イベントを閲覧してくること。":
        "아래 퀘스트 중 어딘가에 출현하는<br>이벤트 필드를 발견해<br>이벤트를 확인해 올 것.",
    "アークスシップ内にいる<br>該当のキャラクターに話しかけ<br>イベントを閲覧してくること。":
        "아크스 쉽 내부에 있는<br>해당 캐릭터에게 말을 걸어<br>이벤트를 확인해 올 것.",
    "該当のストーリークエストを<br>クリアしてくること。":
        "해당 스토리 퀘스트를<br>클리어해 올 것.",
}

EXPLANATION_EXACT_MAP = {
    "わたしとわたしたちが指定するエネミーを<br>倒し、残留物を回収してきてもらいたい。<br>わたしとわたしたちが願うのは、それだけ。":
        "나와 우리들이 지정한 에너미를<br>쓰러뜨리고 잔류물을 회수해 오길 바란다.<br>나와 우리들이 바라는 것은 그것뿐.",
    "指定されたエネミーを倒し、残留物を<br>回収することで、可能性は紡がれる。<br>それは、君にしかできないことだ。":
        "지정된 에너미를 쓰러뜨리고 잔류물을<br>회수하면 가능성은 이어진다.<br>그건 너만이 할 수 있는 일이다.",
}

YELLOW_SUFFIX_MAP = {
    "達成で捜索完了": "달성하면 수색 완료",
    "目標達成で捜索完了": "목표를 달성하면 수색 완료",
    "報告完了でイベント発生": "보고를 완료하면 이벤트 발생",
}


def load_actor_map(path: Path) -> dict[str, str]:
    mapping: dict[str, str] = {}
    with path.open(encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        next(reader, None)
        for row in reader:
            if len(row) >= 3:
                mapping[row[2]] = row[1]
    return mapping


def load_region_map(path: Path) -> dict[str, str]:
    mapping: dict[str, str] = {}
    with path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            jp = row["jp_region_label"]
            ko = row["ko_region_label"]
            mapping[jp] = ko
    return mapping


def load_simple_map(path: Path) -> dict[str, str]:
    mapping: dict[str, str] = {}
    with path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            mapping[row["jp"]] = row["ko"]
    return mapping


def load_title_map(title_tsv: Path, ep1_quest_tsv: Path) -> tuple[dict[str, str], dict[str, str]]:
    title_map: dict[str, str] = {}
    client_order_map: dict[str, str] = {}
    with title_tsv.open(encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            kind = row["kind"]
            jp = row["jp"]
            ko = row["ko"]
            if kind == "client_order":
                client_order_map[jp] = ko
            else:
                title_map[jp] = ko
    with ep1_quest_tsv.open(encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if len(row) >= 2:
                title_map[row[0]] = row[1]
    return title_map, client_order_map


def translate_character_expr(text: str, actor_map: dict[str, str], alias_map: dict[str, str]) -> str:
    text = text.strip()
    if text in alias_map:
        return alias_map[text]

    normalized = text.replace("&", "＆")
    if normalized in alias_map:
        return alias_map[normalized]

    parts = [p.strip() for p in normalized.split("＆")]
    translated_parts = []
    for part in parts:
        if part in alias_map:
            translated_parts.append(alias_map[part])
        elif part in actor_map:
            translated_parts.append(actor_map[part])
        else:
            translated_parts.append(part)
    return "＆".join(translated_parts)


def translate_area_label(jp_area_with_suffix: str, region_map: dict[str, str]) -> str:
    base = jp_area_with_suffix.removesuffix("エリア")
    ko_base = region_map.get(base, base)
    return f"{ko_base} 에리어"


def lookup_title_like(text: str, title_map: dict[str, str]) -> str:
    normalized = text.replace("\\u3000", "　")
    return title_map.get(text, title_map.get(normalized, text))


def translate_place_line(text: str, place_map: dict[str, str]) -> str:
    for jp, ko in sorted(place_map.items(), key=lambda x: len(x[0]), reverse=True):
        text = text.replace(jp, ko)
    text = text.replace("ショップエリア<br>\\u3000ゲートエリア行きテレポーター前", "쇼핑 구역<br>\\u3000게이트 에리어행 텔레포터 앞")
    return text


def translate_explanation(
    text: str,
    actor_map: dict[str, str],
    alias_map: dict[str, str],
    region_map: dict[str, str],
    place_map: dict[str, str],
    title_map: dict[str, str],
    client_order_map: dict[str, str],
) -> str:
    if text in EXPLANATION_EXACT_MAP:
        return EXPLANATION_EXACT_MAP[text]

    translated = text
    translated = translated.replace("【出現ポイント】", "【출현 포인트】")
    translated = translated.replace("【場所】", "【장소】")
    translated = translated.replace("【キャラクター】", "【캐릭터】")
    translated = translated.replace("【イベント】", "【이벤트】")
    translated = translated.replace("【クエスト】", "【퀘스트】")

    translated = re.sub(
        r"(\\u3000| )?(.+?)が対象となる",
        lambda m: f"{m.group(1) or ''}{translate_area_label(m.group(2), region_map)}가 대상이 되는",
        translated,
    )
    translated = re.sub(
        r"(\\u3000| )?(.+?エリア)のアークスクエスト",
        lambda m: f"{m.group(1) or ''}{translate_area_label(m.group(2), region_map)}의 아크스 퀘스트",
        translated,
    )
    translated = re.sub(
        r"(\\u3000| )?(.+?エリア)の(<br>)",
        lambda m: f"{m.group(1) or ''}{translate_area_label(m.group(2), region_map)}의{m.group(3)}",
        translated,
    )
    translated = translated.replace("アークスクエストおよびフリーフィールドの", "아크스 퀘스트 및 프리 필드의")
    translated = translated.replace("シングルパーティーエリア内", "싱글 파티 에리어 내")

    for jp, ko in sorted(region_map.items(), key=lambda x: len(x[0]), reverse=True):
        translated = translated.replace(f"{jp} 에리어", f"{ko} 에리어")

    translated = translate_place_line(translated, place_map)

    translated = re.sub(
        r"(【캐릭터】<br>)(?:\\u3000| )?(.+?)(?=(<br>|$))",
        lambda m: m.group(1) + translate_character_expr(m.group(2), actor_map, alias_map),
        translated,
    )

    translated = re.sub(
        r"(【이벤트】<br>)(?:\\u3000| )?(.+?)(?=(<br>|$))",
        lambda m: m.group(1) + lookup_title_like(m.group(2), title_map),
        translated,
    )
    translated = re.sub(
        r"(【퀘스트】<br>)(?:\\u3000| )?(.+?)(?=(<br>|$))",
        lambda m: m.group(1) + lookup_title_like(m.group(2), title_map),
        translated,
    )

    translated = translated.replace("マターの捜索中にクエストを", "마타를 수색하는 동안 퀘스트를")
    translated = translated.replace("マターの捜索中に分岐ルートを", "마타를 수색하는 동안 분기 루트를")
    translated = translated.replace("クリアすることで捜索完了", "클리어하면 수색 완료")

    def replace_client_order(match: re.Match[str]) -> str:
        speaker = translate_character_expr(match.group(1), actor_map, alias_map)
        order_title = client_order_map.get(match.group(2), match.group(2))
        suffix = YELLOW_SUFFIX_MAP.get(match.group(3), match.group(3))
        return f"<yellow>{speaker}의 클라이언트 오더<br>\\u3000『{order_title}』를<br>\\u3000{suffix}<c>"

    translated = re.sub(
        r"<yellow>(.+?)のクライアントオーダー<br>\\u3000『(.+?)』の<br>\\u3000(.+?)<c>",
        replace_client_order,
        translated,
    )

    # Normalize literal ideographic space escapes in translated text.
    translated = translated.replace("\\u3000", " ")
    translated = translated.replace("　", " ")
    translated = translated.replace("<br> ", "<br>")
    translated = re.sub(r" {2,}", " ", translated)

    return translated


def main() -> None:
    actor_map = load_actor_map(ACTOR_TSV)
    region_map = load_region_map(REGION_TSV)
    place_map = load_simple_map(PLACE_TSV)
    alias_map = load_simple_map(CHAR_ALIAS_TSV)
    title_map, client_order_map = load_title_map(TITLE_TSV, EP1_QUEST_TITLE_TSV)

    changed_files = 0
    changed_rows = 0

    for path in sorted(MATTERBOARD_DIR.glob("mb*.csv")):
        with path.open(encoding="utf-8", newline="") as f:
            rows = list(csv.reader(f))

        file_changed = False
        for row in rows:
            if len(row) < 2:
                continue
            current = row[1]
            if not (current.startswith('"') and current.endswith('"')):
                continue
            inner = current[1:-1]

            if row[0] == "TargetName_Errand#0":
                updated = TARGET_TEMPLATE_MAP.get(inner, inner)
            elif row[0] == "Explanation#0":
                updated = translate_explanation(
                    inner,
                    actor_map=actor_map,
                    alias_map=alias_map,
                    region_map=region_map,
                    place_map=place_map,
                    title_map=title_map,
                    client_order_map=client_order_map,
                )
            else:
                continue

            if updated != inner:
                row[1] = f'"{updated}"'
                changed_rows += 1
                file_changed = True

        if file_changed:
            with path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f, lineterminator="\n")
                writer.writerows(rows)
            changed_files += 1

    print(f"changed_files={changed_files}")
    print(f"changed_rows={changed_rows}")


if __name__ == "__main__":
    main()
