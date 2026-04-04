#include <iostream>
#include <string>
#include <vector>
#include <chrono>
#include <ctime>

struct PacketInfo {
    std::string source;
    std::string destination;
    int port;
    std::string protocol;
    long timestamp;
};

class NetworkSniffer {
public:
    void startSniffing() {
        std::cout << "AIP-HSD C++ Packet Sniffer starting on eth0..." << std::endl;
        // Mock packet capture logic
        for (int i = 0; i < 5; ++i) {
            PacketInfo p = capturePacket();
            logPacket(p);
        }
    }

private:
    PacketInfo capturePacket() {
        return {"192.168.1.100", "104.22.10.5", 443, "HTTPS",
                std::chrono::system_clock::to_time_t(std::chrono::system_clock::now())};
    }

    void logPacket(const PacketInfo& p) {
        std::cout << "[PACKET] SRC: " << p.source << " -> DST: " << p.destination
                  << " PORT: " << p.port << " PROT: " << p.protocol << std::endl;
    }
};

int main() {
    NetworkSniffer sniffer;
    sniffer.startSniffing();
    return 0;
}
