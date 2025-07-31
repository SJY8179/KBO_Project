
'''
    Args:
        (dict) 추가 header로 넣을 값

    Returns:
        (dict) header 반환
'''
def get_request_header(headers:dict = None):

    default_headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
    }

    if headers:
        default_headers.update(headers)  # 전달받은 headers로 덮어씀
    
    return default_headers


