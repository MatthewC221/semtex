#!/usr/bin/perl -w

# Shuffle

open (my $fh, "<", "file.txt") 
    or die "Can't open!\n";

while (my $line = <$fh>) {
    if ($line =~ /::(\d+)::/) {
        $value = $1;
        @array[$value] = $line;
    }
}

foreach $temp (@array) {
    $temp =~ s/::(\d+):://g;
    print $temp;
}
