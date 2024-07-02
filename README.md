# Fibonacci API

This project is a REST API that computes and returns the nth number in the Fibonacci sequence.


### Prerequisites

- Python 3.9
- Flask

# Clone the repository:


git clone https://github.com/Achimek/bentley.git
cd fibonacci_api

# Create and Run virtual envrionment 
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install requirements
pip install -r requirements.txt

# Run the application
python task.py


# To run docker Build the docket container
docker build -t fibonacci_api

# run container

docker run -p 4000:4000 fibonacci_api

# Production Deployment and Scaling
For production deployment, I would use Azure. I can use Docker to containerize the application and Kubernetes for orchestration. I would implement CI/CD pipelines using tools like Azure Devops, GitHub Actions, Jenkins, or Travis CI. Add monitoring using tools like Container insights, Azure Monitor managed service for Prometheus, Azure Managed Grafana, Prometheus and Grafana, and logging using ELK stack (Elasticsearch, Logstash, and Kibana).
To handle high traffic, use load balancers and auto-scaling features provided by cloud services. I will ensure the application is stateless to allow horizontal scaling.

Second options is use Container instance with azure traffic manager which providing DNS traffic manager with load balancing, also it's providing autoscalling without any need of cluster configuration for API and without cost of VM scale set.