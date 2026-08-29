# backend

FROM python:3.13-slim

# everything in backend folder is copied to /app folder in the container
COPY backend/ /app/

# install uv
RUN pip install --no-cache-dir uv

#changes the working directory to /app
WORKDIR /app

# run uv sync to install dependencies in pyproject.toml without dev packages
RUN uv sync --no-dev

#changes the working directory to /app/src/backend
WORKDIR /app/src/backend

# run uv run uvicorn api:app --host. 0.0.0.0 binds the uvicorn server to all available IP addresses in the container, 
# allowing it to accept incoming requests from outside the container.   
CMD [ "uv" , "run", "uvicorn", "api:app", "--host", "0.0.0.0"]