#!/usr/bin/perl

# Incomplete login_leaks

my $filename = "text.txt";

@array;
@last_letter;
$count = 0;

open(my $fh, '<:encoding(UTF-8)', $filename)
or die "Could not open file '$filename' $!";
while (my $row = <$fh>) {
    if ($row =~ /(.).(.)/) {
        $first = $1;
        $last = $2;
        print $last;
        $array[ord($first)]++;
        $last_letter[ord($last)]++;
        $count++;
    }
}

$i = 0;
$total = 0;
for ($i = 0; $i < scalar @array; $i++) {
    if ($array[$i] ne "") {
        $char = chr($i);
        print("begins: $char = $array[$i]\n");
    }
}

print "Ending array\n\n\n";

$i = 0;

for ($i = 0; $i < scalar @last_letter; $i++) {
    if ($last_letter[$i] ne "") {
        $char = chr($i);
        print("ends: $char = $last_letter[$i]\n");
    }
}
