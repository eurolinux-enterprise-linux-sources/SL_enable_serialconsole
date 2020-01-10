#!/usr/bin/perl
# Modified by S. Timm to support both LILO and GRUB under 7.3
# Feb 20 2004
# This version will only modify the active boot loader,
# either LILO or GRUB, not both
# Can't use grubby here because the functionality needed isn't 
# available in grubby 3.3.10
# arguments will take the same form as the serialconsole 2.0 
# in 7.3
# Modified by Troy Dawson and David Kinnvall to fix the $Num
# and /boot bugs.
# May, 6, 2004
# Modified by Troy Dawson to work with RHEL6
#   This version only works with grub, not lilo
#   This version only edits the grub file since
#     that is all you have to do for RHEL6
# Aug. 23, 2010
# serialconsole.pl [-h] [-q] [-d <device>] [-s <speed>]
$Device='/dev/ttyS0';
$Speed=9600;
$Num=0;
while ($#ARGV >= 0 )
{
$test=$ARGV[0];
if ( $test eq '-h' ) 
	{ 
	  print "serialconsole.pl [ -h ] [ -q ] [ -d <device> ] [ -s <speed> ]\n \n";
	  print "-h help      Display this help file \n";
	  print "-q quiet     Only send errors to the screen \n";
	  print "-d device    The serial device --default is /dev/ttyS0 \n ";
	  print "-s speed     Speed of the serial device --default is 9600 \n";
	  exit;
        }
elsif ( $test eq '-q' ) 
        {
	  $quiet="Y";
          shift @ARGV;
	}
elsif ( $test eq '-d' )
        {
	$Device=$ARGV[1];
	unless (($Num) = ($Device =~ /\/dev\/ttyS(.)/)) 
        {
   	die "Device must be in the form /dev/ttyS?\n";
        }
	shift @ARGV;
	shift @ARGV;
        }
elsif ( $test eq '-s' ) 
        {
	$Speed=$ARGV[1];
	shift @ARGV;
	shift @ARGV;
# hack--test to see if this is numeric by taking the integer value
# a string will return zero)
        $intspeed=int($Speed);
}

else
{       die "Invalid parameters"; }
}


##################################################
#Determine if we are running LILO or GRUB as default boot loader
#(grubby doesn't tell us that under 7.3)
#Boot sector will contain GRUB if it is grub,
#won't if it isn't.
# TJD I am leaving this code in incase we need 
#  something similar to see if we are doing
#  grub or efi
##################################################
$grubbootdrive="";
$lilobootdrive="";
if ( -r "/boot/grub/grub.conf" )
{
        $grubbootline=`grep 'boot=' /boot/grub/grub.conf`;
        chop $grubbootline;
        ($grubtext,$grubbootdrive)=split("=",$grubbootline);
}
if ( -r "/etc/lilo.conf" )
{
        $lilobootline=`grep 'boot=' /etc/lilo.conf`;
        chop $lilobootline;
        ($lilotext,$lilobootdrive)=split('=',$lilobootline);
}
$bootsect="";
if ($grubbootdrive ne "")
{
        $grubbootsect=`dd if=$grubbootdrive count=1 bs=512 2>/dev/null | grep GRUB`;
	if ( $grubbootsect ne "")
        {
            $bloader="GRUB";
	}
}

if (($grubbootsect eq "") && ($lilobootdrive ne ""))
{
        $lilobootsect=`dd if=$lilobootdrive count=1 bs=512 2>/dev/null | grep LILO`;
        if ($lilobootsect ne "")
        {
                $bloader="LILO";
        }
}

if ($bloader eq "GRUB")
{
$SerialLineDone = 0;
$TerminalLineDone = 0;
$Sconline="console=tty0 console=ttyS$Num,$Speed";
#should allow for the fact that /boot/grub/grub.conf can
#be a symlink, also save a copy of previous file.
chdir ("/boot/grub");
$grubfile="grub.conf";
if ( -l $grubfile)
{
$grublink=$grubfile;
$grubfile=readlink($grublink);
}
system "cp -p $grubfile $grubfile.serialconsole.sav";
open (GRUB, "$grubfile");
while ($ThisLine = <GRUB>)
{
   # If there is already a 'serial=' line, change it...
   if ($ThisLine =~ s/^[    ]*serial .*$/serial --unit=$Num --speed=$Speed /) {
      print "Modifying serial line in grub.conf...\n";
      $SerialLineDone = 1;
   }
   # If there is already a 'terminal' line, change it...
   if ($ThisLine =~ s/^terminal\s*.*$/terminal --timeout=10 serial console/) {
      print "Modifying terminal line in grub.conf...\n";
      $TerminalLineDone = 1;
}
   # Append correct console speed to all kernel lines
   if ($ThisLine =~ /kernel .*\/vmlinuz/)
{
       $ThisLine =~ s/console\s*=\s*.*$//;
       chop $ThisLine;
       $ThisLine = "$ThisLine $Sconline \n";
  }


   # Store grub line
     push @grub,$ThisLine;
}
close (GRUB);
# open $grubfile  for writing
open (GRUB,">$grubfile");

if ($SerialLineDone == 0) 
{ 
print GRUB "serial --unit=$Num --speed=$Speed\n";
}
if ($TerminalLineDone == 0)
{
print GRUB "terminal --timeout=10 serial console\n";
}
# Write file...
foreach $ThisLine (@grub) {
   print GRUB $ThisLine;

}
close (GRUB);

}


