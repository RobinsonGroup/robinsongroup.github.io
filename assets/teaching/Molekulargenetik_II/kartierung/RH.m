%
loci = {'16' '48' '46' '4' '52' '11' '1' '18' '8' 'AP' '12' ...
    '111' '47' 'SOD'};

chr21marker = { 
{ '0' '0' '0' '0' '0' '1' '0' '0' '0' '0' '0' '0' '1' '1' }
{ '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' }
{ '1' '1' '?' '1' '?' '0' '0' '1' '?' '?' '1' '?' '?' '?' }
{ '0' '0' '1' '1' '1' '1' '0' '0' '0' '0' '0' '?' '0' '0' }
{ '0' '0' '0' '0' '0' '0' '0' '0' '0' '0' '0' '0' '0' '0' }
{ '1' '1' '1' '1' '?' '0' '0' '0' '0' '0' '0' '?' '0' '?' }
{ '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '0' }
{ '1' '1' '1' '1' '0' '0' '0' '0' '0' '0' '0' '0' '0' '0' }
{ '1' '1' '1' '1' '1' '1' '?' '0' '0' '0' '0' '0' '0' '?' }
{ '1' '1' '1' '0' '0' '1' '1' '1' '1' '1' '0' '0' '0' '0' }
{ '1' '1' '?' '1' '?' '1' '1' '0' '?' '?' '0' '0' '?' '?' }
{ '1' '1' '?' '1' '?' '1' '1' '1' '?' '?' '1' '1' '1' '?' }
{ '1' '1' '1' '0' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' }
{ '1' '1' '1' '1' '1' '0' '0' '1' '1' '1' '1' '1' '0' '0' }
{ '1' '1' '1' '0' '0' '1' '1' '1' '0' '0' '0' '0' '0' '?' }
{ '0' '0' '0' '0' '0' '1' '?' '0' '0' '0' '0' '0' '0' '0' }
{ '0' '0' '0' '0' '0' '1' '1' '0' '0' '0' '0' '0' '0' '0' }
{ '0' '0' '?' '0' '?' '0' '0' '0' '?' '?' '0' '0' '1' '?' }
{ '1' '1' '?' '1' '?' '1' '1' '0' '?' '?' '1' '1' '1' '?' }
{ '1' '1' '?' '0' '?' '0' '0' '0' '?' '?' '0' '0' '?' '?' }
{ '1' '1' '1' '1' '1' '0' '0' '0' '0' '0' '0' '0' '1' '1' }
{ '1' '1' '1' '1' '0' '0' '0' '1' '1' '0' '1' '1' '?' '1' }
{ '?' '0' '?' '0' '?' '0' '0' '0' '?' '?' '0' '?' '?' '?' }
{ '?' '0' '?' '0' '?' '1' '1' '0' '?' '?' '0' '0' '?' '?' }
{ '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '0' '0' '1' '1' }
{ '0' '0' '?' '0' '0' '1' '1' '?' '0' '0' '0' '0' '1' '1' }
{ '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '?' '?' }
{ '0' '0' '0' '0' '0' '1' '1' '0' '0' '0' '0' '0' '?' '?' }
{ '1' '1' '1' '1' '?' '?' '?' '0' '0' '0' '0' '?' '0' '0' }
{ '1' '1' '1' '1' '1' '1' '1' '1' '0' '0' '0' '0' '0' '1' }
{ '1' '1' '1' '1' '1' '1' '1' '0' '1' '1' '1' '1' '1' '?' }
{ '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '0' '0' }
{ '0' '1' '1' '0' '1' '0' '0' '0' '0' '0' '0' '0' '0' '0' }
{ '0' '0' '0' '0' '0' '0' '0' '1' '1' '1' '1' '1' '1' '1' }
{ '1' '1' '1' '1' '1' '1' '1' '0' '0' '0' '0' '?' '0' '0' }
{ '1' '1' '?' '1' '?' '0' '0' '0' '?' '?' '0' '?' '?' '?' }
{ '1' '1' '1' '1' '1' '1' '1' '0' '1' '1' '1' '1' '0' '0' }
{ '0' '0' '0' '0' '0' '0' '0' '0' '0' '0' '0' '0' '0' '1' }
{ '0' '0' '0' '0' '0' '0' '0' '0' '0' '0' '0' '0' '0' '?' }
{ '0' '0' '0' '0' '?' '1' '0' '0' '?' '0' '1' '1' '0' '0' }
{ '0' '0' '0' '0' '0' '1' '0' '0' '0' '0' '0' '?' '0' '0' }
{ '1' '1' '1' '1' '1' '1' '1' '1' '0' '0' '0' '?' '0' '0' }
{ '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '?' '1' '1' }
{ '1' '1' '1' '1' '1' '1' '1' '0' '0' '0' '0' '0' '0' '1' }
{ '1' '1' '?' '0' '?' '0' '0' '0' '?' '?' '?' '?' '?' '0' }
{ '0' '0' '0' '0' '0' '1' '1' '0' '1' '0' '0' '0' '0' '0' }
{ '0' '0' '0' '0' '1' '1' '0' '0' '1' '1' '0' '0' '0' '1' }
{ '1' '0' '0' '0' '0' '1' '0' '0' '1' '0' '0' '0' '0' '0' }
{ '1' '1' '1' '1' '1' '1' '1' '1' '1' '0' '0' '?' '0' '1' }
{ '1' '1' '1' '1' '0' '1' '0' '0' '0' '0' '0' '0' '0' '0' }
{ '1' '1' '1' '1' '0' '0' '0' '0' '0' '0' '0' '0' '1' '1' }
{ '0' '0' '0' '0' '0' '0' '0' '0' '0' '0' '0' '0' '1' '1' }
{ '1' '1' '0' '0' '0' '0' '0' '0' '0' '0' '0' '0' '0' '0' }
{ '0' '0' '0' '1' '1' '0' '0' '1' '1' '1' '1' '1' '1' '1' }
{ '1' '1' '0' '0' '0' '0' '0' '0' '1' '1' '0' '0' '0' '0' }
{ '?' '0' '?' '0' '?' '0' '0' '0' '?' '?' '?' '0' '?' '?' }
{ '?' '0' '?' '0' '?' '0' '0' '0' '?' '?' '1' '?' '1' '?' }
{ '?' '0' '?' '0' '?' '0' '0' '0' '?' '?' '0' '?' '0' '?' }
{ '0' '0' '0' '0' '0' '1' '1' '1' '1' '1' '1' '?' '1' '1' }
{ '?' '1' '?' '1' '?' '0' '0' '0' '?' '?' '0' '?' '0' '?' }
{ '1' '0' '0' '0' '?' '0' '0' '0' '0' '0' '0' '?' '0' '?' }
{ '?' '1' '?' '1' '?' '1' '1' '1' '?' '?' '1' '?' '1' '?' }
{ '?' '1' '?' '1' '?' '1' '?' '0' '?' '?' '0' '?' '0' '?' }
{ '0' '0' '0' '0' '0' '0' '0' '0' '0' '0' '0' '?' '0' '0' }
{ '?' '1' '?' '1' '?' '0' '0' '0' '?' '?' '1' '?' '1' '?' }
{ '?' '1' '?' '1' '?' '1' '1' '0' '?' '?' '1' '1' '1' '?' }
{ '?' '?' '?' '?' '?' '?' '?' '?' '?' '?' '?' '?' '?' '?' }
{ '?' '0' '?' '0' '?' '1' '1' '1' '?' '?' '1' '?' '1' '?' }
{ '1' '1' '1' '0' '?' '?' '?' '0' '0' '0' '0' '?' '0' '?' }
{ '1' '1' '1' '1' '1' '1' '1' '1' '0' '0' '0' '0' '0' '0' }
{ '1' '1' '1' '1' '1' '1' '1' '0' '1' '?' '1' '1' '1' '1' }
}

%% This number of markers is too large to solve by brute
%% force. Therefore, take a subset of 8 markers.

BCperm = [ 10 7 4 9 6 1 12 14];
BCloci = loci(BCperm);


loci =  {'AP'    '1'    '4'    '8'    '11'    '16'    '111'    'SOD' }
chr21 = { 
{ '0' '0' '0' '0' '1' '0' '1' '1' }
{ '1' '1' '1' '1' '1' '1' '1' '1' }
{ '?' '0' '1' '?' '0' '1' '?' '?' }
{ '0' '0' '1' '0' '1' '0' '0' '0' }
{ '0' '0' '0' '0' '0' '0' '0' '0' }
{ '0' '0' '1' '0' '0' '1' '0' '?' }
{ '1' '1' '1' '1' '1' '1' '1' '0' }
{ '0' '0' '1' '0' '0' '1' '0' '0' }
{ '0' '?' '1' '0' '1' '1' '0' '?' }
{ '1' '1' '0' '1' '1' '1' '0' '0' }
{ '?' '1' '1' '?' '1' '1' '?' '?' }
{ '?' '1' '1' '?' '1' '1' '1' '?' }
{ '1' '1' '0' '1' '1' '1' '1' '1' }
{ '1' '0' '1' '1' '0' '1' '0' '0' }
{ '0' '1' '0' '0' '1' '1' '0' '?' }
{ '0' '?' '0' '0' '1' '0' '0' '0' }
{ '0' '1' '0' '0' '1' '0' '0' '0' }
{ '?' '0' '0' '?' '0' '0' '1' '?' }
{ '?' '1' '1' '?' '1' '1' '1' '?' }
{ '?' '0' '0' '?' '0' '1' '?' '?' }
{ '0' '0' '1' '0' '0' '1' '1' '1' }
{ '0' '0' '1' '1' '0' '1' '?' '1' }
{ '?' '0' '0' '?' '0' '?' '?' '?' }
{ '?' '1' '0' '?' '1' '?' '?' '?' }
{ '1' '1' '1' '1' '1' '1' '1' '1' }
{ '0' '1' '0' '0' '1' '0' '1' '1' }
{ '1' '1' '1' '1' '1' '1' '?' '?' }
{ '0' '1' '0' '0' '1' '0' '?' '?' }
{ '0' '?' '1' '0' '?' '1' '0' '0' }
{ '0' '1' '1' '0' '1' '1' '0' '1' }
{ '1' '1' '1' '1' '1' '1' '1' '?' }
{ '1' '1' '1' '1' '1' '1' '0' '0' }
{ '0' '0' '0' '0' '0' '0' '0' '0' }
{ '1' '0' '0' '1' '0' '0' '1' '1' }
{ '0' '1' '1' '0' '1' '1' '0' '0' }
{ '?' '0' '1' '?' '0' '1' '?' '?' }
{ '1' '1' '1' '1' '1' '1' '0' '0' }
{ '0' '0' '0' '0' '0' '0' '0' '1' }
{ '0' '0' '0' '0' '0' '0' '0' '?' }
{ '0' '0' '0' '?' '1' '0' '0' '0' }
{ '0' '0' '0' '0' '1' '0' '0' '0' }
{ '0' '1' '1' '0' '1' '1' '0' '0' }
{ '1' '1' '1' '1' '1' '1' '1' '1' }
{ '0' '1' '1' '0' '1' '1' '0' '1' }
{ '?' '0' '0' '?' '0' '1' '?' '0' }
{ '0' '1' '0' '1' '1' '0' '0' '0' }
{ '1' '0' '0' '1' '1' '0' '0' '1' }
{ '0' '0' '0' '1' '1' '1' '0' '0' }
{ '0' '1' '1' '1' '1' '1' '0' '1' }
{ '0' '0' '1' '0' '1' '1' '0' '0' }
{ '0' '0' '1' '0' '0' '1' '1' '1' }
{ '0' '0' '0' '0' '0' '0' '1' '1' }
{ '0' '0' '0' '0' '0' '1' '0' '0' }
{ '1' '0' '1' '1' '0' '0' '1' '1' }
{ '1' '0' '0' '1' '0' '1' '0' '0' }
{ '?' '0' '0' '?' '0' '?' '?' '?' }
{ '?' '0' '0' '?' '0' '?' '1' '?' }
{ '?' '0' '0' '?' '0' '?' '0' '?' }
{ '1' '1' '0' '1' '1' '0' '1' '1' }
{ '?' '0' '1' '?' '0' '?' '0' '?' }
{ '0' '0' '0' '0' '0' '1' '0' '?' }
{ '?' '1' '1' '?' '1' '?' '1' '?' }
{ '?' '?' '1' '?' '1' '?' '0' '?' }
{ '0' '0' '0' '0' '0' '0' '0' '0' }
{ '?' '0' '1' '?' '0' '?' '1' '?' }
{ '?' '1' '1' '?' '1' '?' '1' '?' }
{ '?' '?' '?' '?' '?' '?' '?' '?' }
{ '?' '1' '0' '?' '1' '?' '1' '?' }
{ '0' '?' '0' '0' '?' '1' '0' '?' }
{ '0' '1' '1' '0' '1' '1' '0' '0' }
{ '?' '1' '1' '1' '1' '1' '1' '1' }
}

