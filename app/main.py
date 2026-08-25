import os

from flask import Flask, jsonify, request

from app import config_secrets, report_runner, user_lookup

app = Flask(__name__)
app.secret_key = config_secrets.signing_key()


@app.get("/healthz")
def healthz():
    return jsonify({"status": "ok", "database": config_secrets.database_url()})


@app.get("/accounts")
def accounts():
    account_id = request.args.get("account_id", "")
    return jsonify(user_lookup.find_account(account_id))


@app.get("/accounts/search")
def accounts_search():
    holder = request.args.get("holder", "")
    return jsonify(user_lookup.search_accounts_by_holder(holder))


@app.post("/reports")
def reports():
    report_name = request.args.get("name", "daily")
    return jsonify({"path": report_runner.generate_report(report_name)})


def main():
    user_lookup.bootstrap()
    app.run(host="127.0.0.1", port=int(os.environ.get("PORT", "5001")))


if __name__ == "__main__":
    main()
