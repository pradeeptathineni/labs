#!/usr/bin/env bash
# Compose Linux's collectors without installing a monitoring service
set -euo pipefail
export LC_ALL=C

usage() {
    printf 'Usage: %s [--interval SECONDS] [--help]\n' "${0##*/}"
    printf 'Report Linux CPU, memory, local filesystems, and top five processes.\n'
    printf 'SECONDS must be an integer from 1 to 60 (default: 1).\n'
}

fail() {
    printf 'server-stats: %s\n' "$1" >&2
    exit 1
}

interval=1
case "${1:-}" in
    --help|-h) [[ $# == 1 ]] || fail 'Help takes no additional arguments'; usage; exit 0 ;;
    --interval)
        [[ $# == 2 ]] || fail 'Use --interval SECONDS'
        [[ $2 =~ ^([1-9]|[1-5][0-9]|60)$ ]] || fail 'Interval must be an integer from 1 to 60'
        interval=$2 ;;
    '') [[ $# == 0 ]] || fail 'Unexpected empty argument' ;;
    *) fail 'Unknown argument; use --help' ;;
esac

[[ $(uname -s) == Linux ]] || fail 'Linux is required (procps and GNU coreutils)'
for tool in vmstat free df ps awk; do
    command -v "$tool" >/dev/null || fail "Required command is missing: $tool"
done

cpu_report() {
    # The first row is since boot. Only the second row covers our interval.
    vmstat -n "$interval" 2 | awk '
        $1 == "r" {
            for (i = 1; i <= NF; i++) column[$i] = i
            next
        }
        $1 ~ /^[0-9]+$/ {
            rows++
            if (rows == 2) {
                split("us sy id wa st", fields, " ")
                for (i = 1; i <= 5; i++) {
                    name = fields[i]
                    if (!column[name]) exit 1
                    value = $(column[name])
                    if (value !~ /^[0-9]+([.][0-9]+)?$/ || value > 100) exit 1
                    metric[name] = value
                }
                valid = 1
            }
        }
        END {
            if (!valid) exit 1
            printf "Non-idle: %.1f%% (includes wait and stolen time)\n", 100 - metric["id"]
            printf "User: %.1f%% | System: %.1f%% | I/O wait: %.1f%% | Stolen: %.1f%%\n", metric["us"], metric["sy"], metric["wa"], metric["st"]
        }
    '
}

memory_report() {
    # Available includes reclaimable cache. The used column varies by version.
    free --bytes | awk '
        $1 == "Mem:" {
            if (NF < 7) exit 1
            for (i = 2; i <= 7; i++) if ($i !~ /^[0-9]+$/) exit 1
            total = $2; unallocated = $4; available = $7
            if (total <= 0 || available > total || unallocated > total) exit 1
            valid = 1
        }
        END {
            if (!valid) exit 1
            printf "Total: %.1f MiB | Used: %.1f MiB (%.1f%%) | Available: %.1f MiB | Free: %.1f MiB\n", total / 1048576, (total - available) / 1048576, 100 * (total - available) / total, available / 1048576, unallocated / 1048576
        }
    '
}

process_report() {
    # Consume every row to avoid breaking ps with SIGPIPE under pipefail.
    ps -eo pid=PID,comm=COMMAND,pcpu=CPU%,pmem=MEM%,rss=RSS_KiB \
        --sort="$1" | awk 'NR <= 6'
}

# Collect everything before printing so a failed collector cannot look complete.
cpu=$(cpu_report) || fail 'Could not collect CPU statistics with vmstat'
memory=$(memory_report) || fail 'Could not collect memory statistics with free'
# An overlay and its backing device can appear together. Do not sum them.
disk=$(df -h --local --exclude-type=tmpfs --exclude-type=devtmpfs) \
    || fail 'Could not collect local filesystem statistics with df'
cpu_processes=$(process_report '-pcpu,-rss,pid') || fail 'Could not list CPU processes with ps'
memory_processes=$(process_report '-rss,-pcpu,pid') || fail 'Could not list memory processes with ps'

printf 'CPU (sample: %s second(s))\n%s\n\n' "$interval" "$cpu"
printf 'Memory (used = total - available)\n%s\n\n' "$memory"
printf 'Disk (mounted local filesystems; excludes tmpfs and devtmpfs)\n%s\n\n' "$disk"
printf 'Top 5 processes by CPU (lifetime average)\n%s\n\n' "$cpu_processes"
printf 'Top 5 processes by memory (resident size)\n%s\n' "$memory_processes"
