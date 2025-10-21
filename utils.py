#!/usr/bin/env python3

import git
import tempfile
import shutil
import urllib.parse
from typing import Dict, Optional, Tuple

from clients import get_secret_data

async def clone_git_repo(git_url: str, credentials_ref: Optional[Dict] = None, 
                       namespace: str = "default") -> Tuple[str, str]:
    """Клонировать Git репозиторий и вернуть путь и хеш коммита"""
    temp_dir = tempfile.mkdtemp(prefix="nixos-operator-")
    
    try:
        # Подготовка credentials если есть
        git_kwargs = {}
        if credentials_ref:
            secret_data = await get_secret_data(credentials_ref["name"], namespace)
            # Предполагаем, что в secret есть ssh-privatekey или token
            if "ssh-privatekey" in secret_data:
                ssh_key = secret_data["ssh-privatekey"]
                git_kwargs["env"] = {"GIT_SSH_COMMAND": f"ssh -i {ssh_key}"}
            elif "token" in secret_data:
                # Для HTTPS с токеном
                parsed_url = urllib.parse.urlparse(git_url)
                auth_url = f"{parsed_url.scheme}://token:{secret_data['token']}@{parsed_url.netloc}{parsed_url.path}"
                git_url = auth_url
        
        # Клонирование репозитория
        repo = git.Repo.clone_from(git_url, temp_dir, **git_kwargs)
        commit_hash = repo.head.commit.hexsha
        
        return temp_dir, commit_hash
        
    except Exception as e:
        shutil.rmtree(temp_dir, ignore_errors=True)
        raise
