# 목차
- 로그아웃 로직 구현 - `auth.py`
- 직접해보기

## 로그아웃 로직 구현 - `auth.py`
```python
@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.sign_in"))
```

## 직접해보기
- 현재 로그아웃 버튼을 만들지 않았으니, `/logout`을 하자
- 로그인 정보가 없을 때도 확인해보자. 의도한대로라면 `/sign-in`으로 이동한다.