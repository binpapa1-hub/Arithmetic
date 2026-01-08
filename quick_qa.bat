@echo off
echo ========================================
echo QA 실행 시작
echo ========================================
echo.

echo [1/3] 단위 테스트 실행...
pytest tests/ -v
if %errorlevel% neq 0 (
    echo [오류] 테스트 실패
    pause
    exit /b 1
)
echo.

echo [2/3] 코드 커버리지 확인...
pytest --cov=src --cov-report=term-missing tests/
if %errorlevel% neq 0 (
    echo [오류] 커버리지 확인 실패
    pause
    exit /b 1
)
echo.

echo [3/3] 코드 품질 검사...
echo - pylint 실행 중...
pylint src/ --score=y --disable=import-error 2>nul
echo - flake8 실행 중...
flake8 src/ --max-line-length=100 --count 2>nul
echo.

echo ========================================
echo QA 완료
echo ========================================
echo.
echo 다음 단계:
echo 1. GUI 테스트: python main.py
echo 2. 콘솔 테스트: python src/console_app.py
echo.
pause

