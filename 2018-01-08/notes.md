# Notes - Jan 01, 2018

1. Data Structures
2. Algorithms
3. Complexity
    *   2^N
    *   N^3
    *   N^2
    *   N
    *   log(N)
    *   1

4. Math

## Maximum Subsequence Problem

At 10^9 calculations per second (optimistic) a problem with n=10^6 the complexity of:

* `n^3 = (10^6)^3 / 10^9 / 60 / 60 / 24 / 365 = 31.7` years to complete
* `n^2 = (10^6)^2 / 10^9 / 60 / 60 = 16.7` minutes to complete
* `n = 10^6 / 10^9 / 60 = 0.001` seconds to complete

## Powers of 2

&nbsp;      | 10s        | 20s        | 30s        | 40s         
------------|------------|------------|------------|------------
2^0 = 1     | 2^10 = 1K  | 2^20 = 1M  | 2^30 = 1B  | 2^40 = 1T
2^1 = 2     |            |            |            | 
2^2 = 4     |            |            | 2^32 = 4B  | 
2^3 = 8     |            |            |            | 
2^4 = 16    |            | 2^24 = 16M |            | 
2^5 = 32    |            |            |            | 
2^6 = 64    |            |            |            | 
2^7 = 128   |            |            |            | 2^47 = 128T
2^8 = 256   |            |            |            | 
2^9 = 512   |            |            |            | 
