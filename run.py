import os
from mediaflow_proxy.main import app as main_app

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "7860"))
    uvicorn.run("run:main_app", host="0.0.0.0", port=port)
