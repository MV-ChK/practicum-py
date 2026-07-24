def parse_logs(logs):
    for log in logs:
        if "ERROR" in log:
            yield log

def count_errors(logs):
    return sum(1 for _ in parse_logs(logs))
    
    
    # cnt = 0
    # for i in parse_logs(logs):
    #     cnt += 1
    # return f"Количество логов с ошибкой: {cnt}"
    
    
    # log_obj = parse_logs(logs)
    # try:
    #     cnt = 0
    #     while True:
    #         next(log_obj)
    #         cnt += 1
    # except StopIteration:
    #     print(f"Количество логов с ошибкой: {cnt}")


mock_logs = [
    "INFO | User login",
    "ERROR | DB timeout",
    "INFO | Page loaded",
    "ERROR | File not found",
    "WARNING | Low memory"
]

print(f"Количество логов с ошибкой: {count_errors(mock_logs)}")