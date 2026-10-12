#!/usr/bin/env bash

# 01-server-performance-stats/server-stats.sh - Show Linux system use
# Usage: ./server-stats.sh [--interval SECONDS] [--help]
#
# Use existing Linux tools without adding a service
# Print the report only after every command succeeds

# Stop on command errors and keep Linux output in English
set -euo pipefail
export LC_ALL=C

# Show the accepted options and what the report includes
usage() {
    printf 'Usage: %s [--interval SECONDS] [--help]\n' "${0##*/}"
    printf 'Report Linux CPU, memory, local filesystems, and top five processes.\n'
    printf 'SECONDS must be an integer from 1 to 60 (default: 1).\n'
}

# Print an error and stop without a partial report
fail() {
    printf 'server-stats: %s\n' "$1" >&2
    exit 1
}

# Use one second unless a whole number from one to sixty is given
interval=1
case "${1:-}" in
    --help|-h)
        [[ $# == 1 ]] || fail 'Help takes no additional arguments'
        usage
        exit 0
        ;;
    --interval)
        [[ $# == 2 ]] || fail 'Use --interval SECONDS'
        [[ $2 =~ ^([1-9]|[1-5][0-9]|60)$ ]] \
            || fail 'Interval must be an integer from 1 to 60'
        interval=$2
        ;;
    '')
        [[ $# == 0 ]] || fail 'Unexpected empty argument'
        ;;
    *)
        fail 'Unknown argument; use --help'
        ;;
esac

# Check Linux and its tools after allowing help on any host
[[ $(uname -s) == Linux ]] \
    || fail 'Linux is required (procps and GNU coreutils)'
for tool in vmstat free df ps awk; do
    command -v "$tool" >/dev/null || fail "Required command is missing: $tool"
done

# Measure CPU use during the chosen seconds, rather than since startup
cpu_report() {
    vmstat -n "$interval" 2 | awk '
        # Find columns by name so their order can change
        $1 == "r" {
            for (i = 1; i <= NF; i++) column[$i] = i
            next
        }

        # The first row covers time since startup. Use the second row.
        $1 ~ /^[0-9]+$/ {
            rows++
            if (rows == 2) {
                split("us sy id wa st", fields, " ")

                # Require every CPU field and a percentage from zero to 100
                for (i = 1; i <= 5; i++) {
                    name = fields[i]
                    if (!column[name]) exit 1
                    value = $(column[name])
                    if (value !~ /^[0-9]+([.][0-9]+)?$/ || value > 100) {
                        exit 1
                    }
                    metric[name] = value
                }
                valid = 1
            }
        }

        # Reject missing data, then print the total and its parts
        END {
            if (!valid) exit 1
            printf "Non-idle: %.1f%% (includes wait and stolen time)\n", \
                100 - metric["id"]
            printf "User: %.1f%% | System: %.1f%% | " \
                "I/O wait: %.1f%% | Stolen: %.1f%%\n", \
                metric["us"], metric["sy"], metric["wa"], metric["st"]
        }
    '
}

# Count cached memory as available because Linux can free it
memory_report() {
    free --bytes | awk '
        # Require all fields to contain whole numbers
        $1 == "Mem:" {
            if (NF < 7) exit 1
            for (i = 2; i <= 7; i++) {
                if ($i !~ /^[0-9]+$/) exit 1
            }

            # Check the total and the two values used in the report
            total = $2
            unallocated = $4
            available = $7
            if (total <= 0 || available > total || unallocated > total) {
                exit 1
            }
            valid = 1
        }

        # Use available memory because the used column varies by tool version
        END {
            if (!valid) exit 1
            printf "Total: %.1f MiB | Used: %.1f MiB (%.1f%%) | " \
                "Available: %.1f MiB | Free: %.1f MiB\n", \
                total / 1048576, \
                (total - available) / 1048576, \
                100 * (total - available) / total, \
                available / 1048576, \
                unallocated / 1048576
        }
    '
}

# Sort by the given fields and print the header plus five process rows
process_report() {
    # Read all rows so stopping after five does not make ps fail
    ps -eo pid=PID,comm=COMMAND,pcpu=CPU%,pmem=MEM%,rss=RSS_KiB \
        --sort="$1" | awk 'NR <= 6'
}

# Collect CPU and memory before printing so failed output cannot look complete
cpu=$(cpu_report) || fail 'Could not collect CPU statistics with vmstat'
memory=$(memory_report) || fail 'Could not collect memory statistics with free'

# Docker can show the same disk twice, so do not add the rows together
disk=$(df -h --local --exclude-type=tmpfs --exclude-type=devtmpfs) \
    || fail 'Could not collect local filesystem statistics with df'

# Collect both process lists using a second field to break ties
cpu_processes=$(process_report '-pcpu,-rss,pid') \
    || fail 'Could not list CPU processes with ps'
memory_processes=$(process_report '-rss,-pcpu,pid') \
    || fail 'Could not list memory processes with ps'

# Print the full report after all five collections succeed
printf 'CPU (sample: %s second(s))\n%s\n\n' "$interval" "$cpu"
printf 'Memory (used = total - available)\n%s\n\n' "$memory"
printf 'Disk (mounted local filesystems; excludes tmpfs and devtmpfs)\n%s\n\n' \
    "$disk"
printf 'Top 5 processes by CPU (lifetime average)\n%s\n\n' "$cpu_processes"
printf 'Top 5 processes by memory (resident size)\n%s\n' "$memory_processes"
