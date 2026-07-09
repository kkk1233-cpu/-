from pathlib import Path
import shutil
from .rules import HOMEWORK_KEYWORDS, EXTENSION_RULES, DEFAULT_CATEGORY


def get_file_category(file_path: Path) -> str:
    filename = file_path.name
    for keyword in HOMEWORK_KEYWORDS:
        if keyword in filename:
            return "homework"
    suffix = file_path.suffix.lower()
    return EXTENSION_RULES.get(suffix, DEFAULT_CATEGORY)


def get_unique_target_path(target_dir: Path, filename: str) -> Path:
    target_path = target_dir / filename
    counter = 1
    while target_path.exists():
        name, ext = Path(filename).stem, Path(filename).suffix
        target_path = target_dir / f"{name}_{counter}{ext}"
        counter += 1
    return target_path


def generate_organize_plan(source_dir: Path, recursive: bool = False) -> list:
    plan = []
    files = source_dir.rglob("*") if recursive else source_dir.glob("*")
    for file in files:
        if file.is_file():
            category = get_file_category(file)
            plan.append({
                "source": file,
                "category": category
            })
    return plan


def execute_organize(
    plan: list,
    target_root: Path,
    dry_run: bool = False,
    move_mode: bool = False
) -> dict:
    stats = {
        "total": 0,
        "categories": {},
        "operations": [],
        "mode": "移动" if move_mode else "复制"
    }

    if dry_run:
        print("\n===== 整理计划预览（Dry Run）=====")
        for item in plan:
            src = item["source"]
            cat = item["category"]
            print(f"【{cat}】{src.name} → {target_root / cat}")
        print(f"\n总计文件：{len(plan)} 个")
        return stats

    target_root.mkdir(exist_ok=True)

    for item in plan:
        src_file = item["source"]
        category = item["category"]
        target_dir = target_root / category
        target_dir.mkdir(exist_ok=True)
        dest_file = get_unique_target_path(target_dir, src_file.name)

        if move_mode:
            shutil.move(str(src_file), str(dest_file))
        else:
            shutil.copy2(src_file, dest_file)

        stats["total"] += 1
        stats["categories"][category] = stats["categories"].get(category, 0) + 1
        stats["operations"].append({
            "from": str(src_file),
            "to": str(dest_file),
            "category": category
        })

    return stats


def generate_report(stats: dict, target_root: Path):
    if stats["total"] == 0:
        return
    report_path = target_root / "整理报告.txt"
    lines = []
    lines.append("=" * 30 + " 课程资料整理报告 " + "=" * 30)
    lines.append(f"操作模式：{stats['mode']}")
    lines.append(f"整理总文件数：{stats['total']} 个")
    lines.append("\n【分类统计】")
    for cat, count in stats["categories"].items():
        lines.append(f"- {cat}：{count} 个")
    lines.append("\n【文件操作详情】")
    for op in stats["operations"]:
        lines.append(f"[{op['category']}] {op['from']} → {op['to']}")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
