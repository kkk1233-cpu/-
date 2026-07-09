import argparse
from pathlib import Path
from course_organizer.core import generate_organize_plan, execute_organize, generate_report

def main():
    parser = argparse.ArgumentParser(description="课程资料自动整理器")
    parser.add_argument("--source", required=True, type=str, help="源文件夹路径")
    parser.add_argument("--target", required=True, type=str, help="目标整理文件夹")
    parser.add_argument("--dry-run", action="store_true", help="预览整理计划")
    parser.add_argument("--mode", choices=["copy", "move"], default="copy", help="操作模式")
    parser.add_argument("--recursive", action="store_true", help="递归整理子目录")

    args = parser.parse_args()
    source_dir = Path(args.source).absolute()
    target_dir = Path(args.target).absolute()

    if not source_dir.exists() or not source_dir.is_dir():
        print(f"错误：源目录 {source_dir} 不存在")
        return

    print(f"源目录：{source_dir}")
    print(f"目标目录：{target_dir}")
    print(f"预览模式：{'是' if args.dry_run else '否'}")
    print(f"操作模式：{args.mode}")
    print(f"递归整理：{'是' if args.recursive else '否'}")

    plan = generate_organize_plan(source_dir, args.recursive)
    if not plan:
        print("未找到需要整理的文件")
        return

    move_mode = (args.mode == "move")
    stats = execute_organize(plan, target_dir, args.dry_run, move_mode)

    if not args.dry_run:
        generate_report(stats, target_dir)


if __name__ == "__main__":
    main()
