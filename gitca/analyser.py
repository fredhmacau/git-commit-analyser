from git import Repo
from git.exc import NoSuchPathError, InvalidGitRepositoryError
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime, timedelta,timezone


@dataclass
class CommitStats:
    commits_by_author: Counter =field(default_factory= Counter)
    commits_by_file: Counter =field(default_factory= Counter)


def analyse_commits(repo_path: str, days: int = 90) -> CommitStats:
    repo = Repo(repo_path)
    stats = CommitStats()
    limit = datetime.now(timezone.utc) - timedelta(days=days)
    for commit in repo.iter_commits():
        if commit.committed_datetime < limit:
            break
        else:
            stats.commits_by_author[commit.author.name] += 1
            try:
                for file_path in commit.stats.files.keys():
                    root = file_path.split('/')
                    stats.commits_by_file[root[0]] += 1
            except Exception:
                pass
        

    return stats


