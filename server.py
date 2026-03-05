class Server:
    def __init__(self, hostname: str, ip: str, environment: str, status: str) -> None:
        """Instantiates a server object

        Args:
            hostname: Server Hostname
            ip: Server IP Address
            environment: Server Environment
            status: Server Status

        Returns:
            None."""
        self.hostname = hostname
        self.ip = ip
        self.environment = environment
        self.status = status

    def is_healthy(self) -> bool:
        """Returns server status if healthy

        Args:
            None.

        Returns:
            True if server is healthy"""
        return self.status == "healthy"

    def summary(self) -> str:
        """Returns server attributes

        Args:
            None.

        Returns:
            Server Hostname, IP, Environment, Status"""
        return f"Server Hostname: {self.hostname} IP: {self.ip} Environment: {self.environment} Status: {self.status}"


if __name__ == "__main__":
    server = Server("web-01", "192.168.1.10", "production", "healthy")
    print(server.summary())
    print(server.is_healthy())

    server2 = Server("web-02", "192.168.1.11", "production", "unhealthy")
    print(server2.summary())
    print(server2.is_healthy())
