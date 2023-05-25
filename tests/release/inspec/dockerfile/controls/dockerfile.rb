control 'dockerfile' do
  title "🐳 Dockerfile inspection to check the image is based on python 3.9 slim and exposes port 8000"

  describe file("Dockerfile") do
    its('content') { should match (%r{python:3.9-slim}) }
    its('content') { should match (%r{PORT_DEFAULT=8000}) }
    its('content') { should match (%r{HOST_ACCEPT_CONNECTION_FROM_OUTSIDE=0.0.0.0}) }
    its('content') { should match (%r{WORKDIR /app}) }
    its('content') { should match (%r{RUN mkdir modules}) }
    its('content') { should match (%r{pip install --no-cache-dir pipenv}) }
    its('content') { should match (%r{pipenv install --system --deploy}) }
    its('content') { should match (%r{COPY Pipfile Pipfile.lock .launch_api_server ./}) }
    its('content') { should match (%r{COPY modules /app/modules/}) }
    its('content') { should match (%r{EXPOSE .PORT}) }
    its('content') { should match (%r{uvicorn modules.api.berlin_clock:app --host .{HOST} --port .{PORT}}) }
    its('content') { should match (%r{chmod 755 /app/start_api_server}) }
  end
end