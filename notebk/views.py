from django.http import HttpResponse
from django.shortcuts import render
from message import wechatpy
# Create your views here.


def connect(request):
    if request.method == "GET":
        args_dict = request.GET
        signature = args_dict["signature"]
        token = "L0121709361809"
        timestamp = args_dict["timestamp"]
        nonce = args_dict["nonce"]
        echo_str = args_dict["echo_str"]
        try:
            wechatpy.check_signature(signature, token, timestamp, nonce)
            return HttpResponse(content=echo_str, status=200)
        except Exception:
            pass
    return HttpResponse(status=200)


