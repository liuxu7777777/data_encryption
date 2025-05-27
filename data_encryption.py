from Crypto.PublicKey import RSA
from sympy import factorint
import base64
#依赖pycryptodome库（RSA处理）和sympy库（数学计算）。
# ==========【输入公钥】==========
pem_public_key = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC1BZATh+py9fCfVCYy2cUCSNQ2
qpYMKK1t+JWSl/wU4BBUjSBs5yqzMzMU0/4PL7VADNtiRcaU3XqbjP1tzCRoCKPR
QU6VtUEkj/lC1ojp1mMgEpKe23HF/EJ3GXI8OV1SpugSB2FVfOeLQ+1jEYOtNbRZ
0ZxtZmaJdLq8HVRZTwIDAQAB
-----END PUBLIC KEY-----"""

# ==========【输入明文和密文】==========
plaintext = "张三"
ciphertext_b64 = "O4M6RmIR8ZngiqfnrVtioOpne5K6c+y3cMUQDt8XUajCKcubG9EOKS3O2KfQvBKy3AxENWRqoqmr0O97xq3BnS9enHKf/r1MbNP6KC3z88XAY2j3o3ugEoVEF3x7rH74aWkWlb41Ayr+/KW2aNvRb8InoP7/M8De3gkDVNwN1ao="  # 你知道的密文（Base64 编码）

# ==========【解析公钥】==========
key = RSA.importKey(pem_public_key)
n = key.n# 模数（两个大素数的乘积）
e = key.e# 公开指数（通常为65537）
#公钥中提取n和e，这是RSA加密的核心参数。
print("[+] 公钥参数解析成功")
print(f"n = {n}")
print(f"e = {e}")

# ==========【解码密文】==========
ciphertext = base64.b64decode(ciphertext_b64)
ciphertext_int = int.from_bytes(ciphertext, byteorder="big")

# ==========【尝试分解 n】==========
#使用sympy的factorint函数分解n，若成功得到两个素数p和q，即可计算私钥参数d。
factors = factorint(n)  # 使用 sympy 进行因子分解
if len(factors) == 2:
    p, q = list(factors.keys())
    print(f"[+] 成功分解: p = {p}")
    print(f"[+] 成功分解: q = {q}")
else:
    print("[!] 失败: n 过大，无法因子分解")

