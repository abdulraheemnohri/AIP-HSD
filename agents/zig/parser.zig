const std = @import("std");

pub const Packet = struct {
    src_ip: [4]u8,
    dst_ip: [4]u8,
    src_port: u16,
    dst_port: u16,
    protocol: u8,
};

pub fn parsePacket(raw: []const u8) !Packet {
    if (raw.len < 12) return error.IncompletePacket;

    return Packet{
        .src_ip = raw[0..4].*,
        .dst_ip = raw[4..8].*,
        .src_port = std.mem.readInt(u16, raw[8..10], .big),
        .dst_port = std.mem.readInt(u16, raw[10..12], .big),
        .protocol = 6, // TCP
    };
}

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    try stdout.print("AIP-HSD Zig Packet Parser: Starting ultra-fast analysis...\n", .{});

    const mock_raw = [_]u8{ 192, 168, 1, 100, 104, 22, 10, 5, 0, 80, 1, 187 };
    const p = try parsePacket(&mock_raw);

    try stdout.print("Parsed Packet: {d}.{d}.{d}.{d} -> {d}.{d}.{d}.{d} PORT: {d}\n",
        .{p.src_ip[0], p.src_ip[1], p.src_ip[2], p.src_ip[3],
          p.dst_ip[0], p.dst_ip[1], p.dst_ip[2], p.dst_ip[3], p.src_port});
}
