#!/usr/bin/perl
# AIP-HSD Legacy Log Forensic Tool (Perl)
# Specialized string processing for ancient corporate log formats.

use strict;
use warnings;
use Time::Piece;

sub extract_anomalies {
    my ($log_data) = @_;
    print "AIP-HSD Perl Forensics: Scanning legacy stream...\n";

    my @lines = split('\n', $log_data);
    foreach my $line (@lines) {
        if ($line =~ /FAIL|ERROR|UNAUTHORIZED/i) {
            my $timestamp = localtime->strftime('%Y-%m-%d %H:%M:%S');
            print "[ANOMALY] [$timestamp] Found: $line\n";
        }
    }
}

my $mock_log = "2023-01-01 Login Success\n2023-01-02 UNAUTHORIZED ACCESS ATTEMPT SECTOR 7\n2023-01-03 System Reboot\n";
extract_anomalies($mock_log);
