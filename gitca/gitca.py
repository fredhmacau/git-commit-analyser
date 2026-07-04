from git.exc import NoSuchPathError, InvalidGitRepositoryError
import sys
from analyser import analyse_commits

def main():
    try:
        if len(sys.argv) < 2:
            sys.exit("list of argument invalid")
        counts = analyse_commits(sys.argv[1])
        print(counts)
    except (NoSuchPathError, InvalidGitRepositoryError) as exc:
        sys.exit(f"Error reading repository: {exc}")
        
if __name__ == "__main__":
    main()