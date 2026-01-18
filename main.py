import multiprocessing
import subprocess
import time
from src.utils.logger import setup_logger

# --- CONFIGURATION ---
BACKEND_PORT = 8081

logger = setup_logger("DQ_RULE_CONFIG_API_LAUNCHER")

# Run the FastAPI Backend
def run_fastapi():
    logger.info(f"[API] Starting CONFIG API on port {BACKEND_PORT}...")
    cmd = [
        "uv", "run", "python", "-m", "uvicorn", 
        "src.api.config_api:app",
        "--reload", 
        "--host", "127.0.0.1", 
        "--port", str(BACKEND_PORT)
    ]
    subprocess.run(cmd)

if __name__ == "__main__":
  
    api_p = multiprocessing.Process(target=run_fastapi)

    try:
        api_p.start()
        time.sleep(3)
        
        logger.info("\n DQ RULE CONFIG API IS FULLY OPERATIONAL")
        logger.info(f"Access the API at: http://localhost:{BACKEND_PORT}")
        
        # Keep main process alive
        api_p.join() 

    except KeyboardInterrupt:
        logger.info("\n Shutting down DQ RULE CONFIG API...")
        api_p.terminate()
        logger.info("Shutdown complete.")