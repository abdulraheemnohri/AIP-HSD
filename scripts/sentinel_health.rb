require 'json'
require 'net/http'

class SentinelHealthCheck
  def initialize(backend_url = "http://localhost:8000")
    @url = backend_url
  end

  def check_module(name, path)
    print "Checking #{name}... "
    if File.exist?(path)
      puts "[OK]"
      true
    else
      puts "[MISSING]"
      false
    end
  end

  def run_full_diagnostic
    puts "--- AIP-HSD // SENTINEL CORE DIAGNOSTIC ---"

    results = {
      python_core: check_module("Python Backend", "backend/python/main.py"),
      node_core: check_module("Node.js Backend", "backend/nodejs/src/index.js"),
      rust_core: check_module("Rust Scorer", "rust_module/src/lib.rs"),
      julia_engine: check_module("Julia Forecaster", "ai_module/forecaster.jl"),
      zig_agent: check_module("Zig Parser", "agents/zig/parser.zig"),
      cobol_legacy: check_module("COBOL Monitor", "integrations/cobol/security_monitor.cbl")
    }

    healthy = results.values.all?
    puts "-------------------------------------------"
    puts "OVERALL STATUS: #{healthy ? 'SYSTEM_STABLE' : 'DEGRADED_MODE'}"
    puts "-------------------------------------------"
  end
end

if __FILE__ == $0
  checker = SentinelHealthCheck.new
  checker.run_full_diagnostic
end
