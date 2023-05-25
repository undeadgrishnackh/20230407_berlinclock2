control 'dockercompose' do
  title "🐳🧩 Docker-Compose inspection to check the container runner is setup properly to work from Docker Hub"

  describe file("docker-compose.yml") do
    its('content') { should match (%r{berlin_clock:}) }
    its('content') { should match (%r{image: "undeadgrishnackh/berlin_clock:latest"}) }
    its('content') { should match (%r{stdin_open: true}) }
    its('content') { should match (%r{tty: true}) }
    its('content') { should match (%r{container_name: "berlin_clock"}) }
    its('content') { should match (%r{ports:}) }
    its('content') { should match (%r{- "8000:8000"}) }
    its('content') { should match (%r{extra_hosts:}) }
    its('content') { should match (%r{"host.docker.internal:host-gateway"}) }
  end
end