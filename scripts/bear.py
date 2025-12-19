#!/usr/bin/env python3
"""
Bear X-Callback-URL API Wrapper

Bear 노트앱과의 상호작용을 위한 Python API
X-Callback-URL 스킴을 통해 노트 생성, 검색, 수정 등을 지원합니다.
"""

import subprocess
import urllib.parse
import json
import os
from typing import Optional, Dict, List, Any


# xcall 도구 경로
XCALL_PATH = "/Applications/xcall.app/Contents/MacOS/xcall"
# Bear API 토큰
BEAR_TOKEN = os.environ.get("BEAR_API_TOKEN", "")


def has_xcall() -> bool:
    """xcall 설치 여부 확인"""
    return os.path.exists(XCALL_PATH)


def call_bear(
    action: str,
    params: Dict[str, str],
    need_response: bool = False
) -> Optional[Dict[str, Any]]:
    """
    Bear X-Callback-URL 호출

    Args:
        action: Bear 액션 이름 (create, search, add-text 등)
        params: URL 파라미터 딕셔너리
        need_response: 응답 필요 여부 (True면 xcall 사용, False면 open 사용)

    Returns:
        need_response=True일 때 JSON 응답, 아니면 None
    """
    # 토큰이 필요한 액션인 경우 추가
    if action in ["search", "tags", "open-tag", "todo", "today", "untagged", "locked"]:
        if BEAR_TOKEN:
            params["token"] = BEAR_TOKEN

    # URL 생성
    query = urllib.parse.urlencode(params)
    url = f"bear://x-callback-url/{action}"
    if query:
        url = f"{url}?{query}"

    if need_response:
        if has_xcall():
            # xcall로 응답 받기
            result = subprocess.run(
                [XCALL_PATH, "-url", url],
                capture_output=True,
                text=True,
                check=False
            )
            if result.stdout:
                try:
                    return json.loads(result.stdout)
                except json.JSONDecodeError:
                    return None
            return None
        else:
            # xcall이 없으면 앱만 열기 (응답 불가)
            subprocess.run(["open", url], check=False)
            return None
    else:
        # open 명령으로 실행 (응답 없음)
        subprocess.run(["open", url], check=False)
        return None


def create_note(
    title: str,
    text: str = "",
    tags: str = "",
    add_timestamp: bool = False,
    return_id: bool = False
) -> Optional[Dict[str, str]]:
    """
    새 노트 생성

    Args:
        title: 노트 제목
        text: 노트 내용
        tags: 쉼표로 구분된 태그 목록
        add_timestamp: 현재 날짜/시간 추가 여부
        return_id: 응답(노트 ID) 반환 여부

    Returns:
        return_id=True일 때 {identifier, title} 반환, 아니면 None
    """
    params = {}
    if title:
        params["title"] = title
    if text:
        params["text"] = text
    if tags:
        params["tags"] = tags
    if add_timestamp:
        params["timestamp"] = "yes"

    return call_bear("create", params, need_response=return_id)


def search_notes(
    term: str = "",
    tag: str = ""
) -> Optional[List[Dict[str, Any]]]:
    """
    노트 검색 (토큰 필요)

    Args:
        term: 검색어
        tag: 태그 필터 (선택사항)

    Returns:
        검색 결과 노트 목록
    """
    params = {}
    if term:
        params["term"] = term
    if tag:
        params["tag"] = tag

    result = call_bear("search", params, need_response=True)
    if isinstance(result, list):
        return result
    return None


def add_text(
    note_id: str = "",
    note_title: str = "",
    text: str = "",
    mode: str = "append",
    header: str = ""
) -> None:
    """
    기존 노트에 텍스트 추가 또는 변경

    Args:
        note_id: 노트 ID (note_title 없으면 필수)
        note_title: 노트 제목 (note_id 없으면 대신 사용)
        text: 추가할 텍스트
        mode: 모드 (append, prepend, replace_all, replace)
        header: 특정 헤더에만 적용 (선택사항)
    """
    params = {}
    if note_id:
        params["id"] = note_id
    elif note_title:
        params["title"] = note_title
    else:
        raise ValueError("note_id 또는 note_title 중 하나는 필수입니다")

    if text:
        params["text"] = text
    if mode:
        params["mode"] = mode
    if header:
        params["header"] = header

    call_bear("add-text", params, need_response=False)


def open_note(
    note_id: str = "",
    note_title: str = "",
    header: str = ""
) -> None:
    """
    노트 열기

    Args:
        note_id: 노트 ID (note_title 없으면 필수)
        note_title: 노트 제목 (note_id 없으면 대신 사용)
        header: 특정 헤더로 이동 (선택사항)
    """
    params = {}
    if note_id:
        params["id"] = note_id
    elif note_title:
        params["title"] = note_title
    else:
        raise ValueError("note_id 또는 note_title 중 하나는 필수입니다")

    if header:
        params["header"] = header

    call_bear("open-note", params, need_response=False)


def get_tags() -> Optional[List[Dict[str, str]]]:
    """
    모든 태그 조회 (토큰 필요)

    Returns:
        {name} 형식의 태그 목록
    """
    result = call_bear("tags", {}, need_response=True)
    if isinstance(result, list):
        return result
    return None


def open_tag(name: str) -> None:
    """
    특정 태그의 모든 노트 표시

    Args:
        name: 태그명 (쉼표로 여러 개 가능)
    """
    params = {"name": name}
    call_bear("open-tag", params, need_response=False)


def rename_tag(old_name: str, new_name: str) -> None:
    """
    태그 이름 변경

    Args:
        old_name: 현재 태그명
        new_name: 새 태그명
    """
    params = {
        "name": old_name,
        "new_name": new_name
    }
    call_bear("rename-tag", params, need_response=False)


def delete_tag(name: str) -> None:
    """
    태그 삭제

    Args:
        name: 태그명
    """
    params = {"name": name}
    call_bear("delete-tag", params, need_response=False)


def trash_note(note_id: str = "", note_title: str = "") -> None:
    """
    노트를 휴지통으로 이동

    Args:
        note_id: 노트 ID (note_title 없으면 필수)
        note_title: 노트 제목 (note_id 없으면 대신 사용)
    """
    params = {}
    if note_id:
        params["id"] = note_id
    elif note_title:
        params["title"] = note_title
    else:
        raise ValueError("note_id 또는 note_title 중 하나는 필수입니다")

    call_bear("trash", params, need_response=False)


def archive_note(note_id: str = "", note_title: str = "") -> None:
    """
    노트를 보관함으로 이동

    Args:
        note_id: 노트 ID (note_title 없으면 필수)
        note_title: 노트 제목 (note_id 없으면 대신 사용)
    """
    params = {}
    if note_id:
        params["id"] = note_id
    elif note_title:
        params["title"] = note_title
    else:
        raise ValueError("note_id 또는 note_title 중 하나는 필수입니다")

    call_bear("archive", params, need_response=False)


def grab_url(
    url: str,
    tags: str = "",
    return_id: bool = False
) -> Optional[Dict[str, str]]:
    """
    웹페이지를 새 노트로 캡처

    Args:
        url: 캡처할 URL
        tags: 태그 목록
        return_id: 응답(노트 ID) 반환 여부

    Returns:
        return_id=True일 때 {identifier, title} 반환, 아니면 None
    """
    params = {"url": url}
    if tags:
        params["tags"] = tags

    return call_bear("grab-url", params, need_response=return_id)
