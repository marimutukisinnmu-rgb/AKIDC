"""AKIDC: a tiny CLI tool for tracking anka targets."""

from __future__ import annotations

import argparse
import random


def parse_target(raw: str) -> int:
    """Parse a positive target post number."""
    try:
        target = int(raw.lstrip(">"))
    except ValueError as exc:
        raise argparse.ArgumentTypeError("番号は整数で指定してください") from exc
    if target < 1:
        raise argparse.ArgumentTypeError("番号は1以上で指定してください")
    return target


def main() -> None:
    parser = argparse.ArgumentParser(description="安価ターゲットを決める・管理するツール")
    parser.add_argument("--target", type=parse_target, help="安価の目標レス番号（例: --target 200）")
    parser.add_argument("--current", type=int, default=1, help="現在のレス番号（既定: 1）")
    parser.add_argument("--random", action="store_true", help="目標番号をランダムに決める")
    parser.add_argument("--max", type=int, default=300, help="ランダム時の上限（既定: 300）")
    args = parser.parse_args()

    if args.current < 1:
        parser.error("--current は1以上で指定してください")

    target = args.target
    if args.random:
        if args.max < args.current:
            parser.error("--max は --current 以上にしてください")
        target = random.randint(args.current, args.max)
    elif target is None:
        parser.error("--target または --random を指定してください")

    print(f"🎯 安価ターゲット: >>{target}")
    if target < args.current:
        print("この番号はすでに通過しています。過去レス安価です！")
    elif target == args.current:
        print("今が安価成立のタイミング！")
    else:
        print(f"あと {target - args.current} レスで到達します。")


if __name__ == "__main__":
    main()
