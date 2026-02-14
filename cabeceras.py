import sys
from robot import Robot
def validate_args(args: list[str]):
    if len(args) < 2:
        print("Usage: python3 robot.py <url>")
        sys.exit(1)

def main():
    args: list[str] = sys.argv
    validate_args(args)

    robots: list[Robot] = []
    for i in range(1,len(args)):
        print(f"Robot {i}")
        robots.append(Robot(args[i]))
        robots[i-1].retrieve()
        robots[i-1].headers()
        robots[i-1].show()
        print()

if __name__ == "__main__":
    main()