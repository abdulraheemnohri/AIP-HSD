package com.aiphsd.mobile

import android.app.NotificationManager
import android.content.Context
import androidx.core.app.NotificationCompat

class AIPHSDNotificationHandler(private val context: Context) {
    fun sendSecurityAlert(title: String, message: String) {
        val builder = NotificationCompat.Builder(context, "aiphsd_alerts")
            .setSmallIcon(android.R.drawable.ic_dialog_alert)
            .setContentTitle("[AIP-HSD] $title")
            .setContentText(message)
            .setPriority(NotificationCompat.PRIORITY_HIGH)

        val notificationManager = context.getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
        notificationManager.notify(1, builder.build())
    }
}
