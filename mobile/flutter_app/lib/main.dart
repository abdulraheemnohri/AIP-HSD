import 'package:flutter/material.dart';

void main() {
  runApp(AIPHSDMobile());
}

class AIPHSDMobile extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'AIP-HSD Mobile',
      theme: ThemeData.dark(),
      home: DashboardScreen(),
    );
  }
}

class DashboardScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('AIP-HSD // SENTINEL MOBILE')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('GLOBAL THREAT LEVEL: CRITICAL', style: TextStyle(color: Colors.red, fontSize: 24)),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {},
              child: Text('TRIGGER EMERGENCY ISOLATION'),
              style: ElevatedButton.styleFrom(backgroundColor: Colors.blueAccent),
            )
          ],
        ),
      ),
    );
  }
}
