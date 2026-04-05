// AIP-HSD Big Data Ingestion Engine (Scala)
// Handles high-throughput security telemetry ingestion into a data lake.

import java.time.Instant

case class SecurityEvent(
  id: String,
  source: String,
  eventType: String,
  timestamp: Instant
)

object DataLakeIngestor {
  def ingestBatch(events: List[SecurityEvent]): Unit = {
    println(s"AIP-HSD Scala Engine: Ingesting batch of ${events.size} security events...")
    events.foreach { e =>
      println(s"[DATALAKE] Stored Event: ${e.eventType} from ${e.source}")
    }
  }

  def main(args: Array[String]): Unit = {
    val mockEvents = List(
      SecurityEvent("EVT-901", "Sensor-Alpha", "TRAFFIC_SPIKE", Instant.now()),
      SecurityEvent("EVT-902", "Sensor-Beta", "MALWARE_DETECTION", Instant.now())
    )
    ingestBatch(mockEvents)
    println("Ingestion cycle complete.")
  }
}
