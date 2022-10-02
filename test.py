import pstats

p = pstats.Stats("insertion_1.stats")
p.sort_stats("cumulative")
p.print_stats()