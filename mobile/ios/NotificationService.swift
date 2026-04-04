import Foundation
import UserNotifications

class AIPHSDNotificationService: UNNotificationServiceExtension {
    var contentHandler: ((UNNotificationContent) -> Void)?
    var bestAttemptContent: UNMutableNotificationContent?

    override func didReceive(_ request: UNNotificationRequest, withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void) {
        self.contentHandler = contentHandler
        bestAttemptContent = (request.content.mutableCopy() as? UNMutableNotificationContent)

        if let bestAttemptContent = bestAttemptContent {
            // AIP-HSD specific threat alert formatting
            bestAttemptContent.title = "[AIP-HSD] CRITICAL THREAT DETECTED"
            bestAttemptContent.body = "A new ransomware variant has been identified in the EMEA region."
            bestAttemptContent.sound = UNNotificationSound.defaultCritical
            contentHandler(bestAttemptContent)
        }
    }
}
