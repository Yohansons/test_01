import random
import time

from utils import Web3Utils, file_to_list, logger
from inputs.config import BONUS_CODE, DELAY
from fake_useragent import UserAgent

import requests

url = "https://api.rabby.io/v1/points/claim_snapshot"

headers = {
    "Host": "api.rabby.io",
    "Connection": "keep-alive",
    "Content-Length": "224",
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="130", "Google Chrome";v="130"',
    "X-Version": "0.92.48",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": UserAgent().random,
    "x-api-ts": str(int(time.time())),
    "Content-Type": "application/json",
    "x-api-ver": "v2",
    "Accept": "application/json, text/plain, */*",
    "X-Client": "Rabby",
    "sec-ch-ua-platform": '"Windows"',
    "Origin": "chrome-extension://acmacodkjb dgmoleebolmdjonilkdbch",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7",
}


wallets = file_to_list("inputs/wallets.txt")
proxy_list = file_to_list("inputs/proxies.txt")
