from django.shortcuts import redirect

kakao_id = "138ad70ec3835cf90b1fa2e481ca4f91"

# Create your views here.
def kakao_login(request):
    client_id = kakao_id
    REDIRECT_URI = "http://localhost:8000/accounts/kakao/login/callback/"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={REDIRECT_URI}&response_type=code"
    )


def kakao_login_callback(request):
    try:
        # (1)
        code = request.GET.get("code")
        client_id = os.environ.get("KAKAO_ID")
        REDIRECT_URI = "http://127.0.0.1:8000/users/login/kakao/callback"
        # (2)
        token_request = requests.get(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={REDIRECT_URI}&code={code}"
        )
        # (3)
        token_json = token_request.json()
        error = token_json.get("error", None)
        if error is not None:
            raise KakaoException()
        # (4)
        access_token = token_json.get("access_token")
        # (5)
        profile_request = requests.get(
            "https://kapi.kakao.com/v2/user/me",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        profile_json = profile_request.json()
        # (6)
        email = profile_json.get("kakao_account", None).get("email")
        if email is None:
            raise KakaoException()
        properties = profile_json.get("properties")
        nickname = properties.get("nickname")
        profile_image = properties.get("profile_image")
        # (7)
        try:
            user = models.User.objects.get(email=email)
            if user.login_method != models.User.LOGIN_KAKAO:
                raise KakaoException()
        except models.User.DoesNotExist:
            user = models.User.objects.create(
                email=email,
                username=email,
                first_name=nickname,
                login_method=models.User.LOGIN_KAKAO,
                email_verified=True,
            )
            user.set_unusable_password()
            user.save()
            # (8)
            if profile_image is not None:
                photo_request = requests.get(profile_image)
                user.avatar.save(
                    f"{nickname}-avatar", ContentFile(photo_request.content)
                )
        login(request, user)
        return redirect(reverse("core:home"))
    except KakaoException:
        return redirect(reverse("users:login"))
