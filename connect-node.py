from flask import Flask, jsonify
from web3 import Web3

app = Flask(__name__)

# เชื่อมต่อกับ Ethereum node (เช่น Infura หรือ Ganache)
infura_url = "https://mainnet.infura.io/v3/6f0684eb75964a5aa5ae8cf10562294c"
web3 = Web3(Web3.HTTPProvider(infura_url))

# ตรวจสอบการเชื่อมต่อ
if web3.is_connected():
    print("Connected to Ethereum node")
else:
    print("Failed to connect")

@app.route('/')
def index():
    # ตัวอย่างการดึงข้อมูลจาก blockchain
    latest_block = web3.eth.block_number
    return jsonify({"latest_block": latest_block})

if __name__ == "__main__":
    app.run(debug=True)
