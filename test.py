import pstats

p = pstats.Stats("selection_1.stats")
p.sort_stats("cumulative")
p.print_stats()