import os # libs are in ls /usr/lib/python3.5

ls = os.listdir()

print(ls)

# All functions in os lib -- fairly familiar
# 'abort', 'access', 'altsep', 'chdir', 'chmod', 'chown', 'chroot', 'close',
# 'closerange', 'confstr', 'confstr_names', 'cpu_count', 'ctermid', 'curdir',
# 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ',
# 'environb', 'errno', 'error', 'execl', 'execle', 'execlp', 'execlpe',
# 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fchdir', 'fchmod',
# 'fchown', 'fdatasync', 'fdopen', 'fork', 'forkpty', 'fpathconf', 'fsdecode',
# 'fs', 'encode', 'fstat', 'fstatvfs', 'fsync', 'ftruncate', 'fwalk',
# 'get_blocking', 'get_exec_path', 'get_inheritable', 'get_terminal_size',
# 'getcwd', 'getcwdb', 'getegid', 'getenv', 'getenvb', 'geteuid', 'getgid',
# 'getgrouplist', 'getgroups', 'getloadavg', 'getlogin', 'getpgid', 'getpgrp',
# 'getpid', 'getppid', 'getpriority', 'getresgid', 'getresuid', 'getsid',
# 'getuid', 'getxattr', 'initgroups', 'isatty', 'kill', 'killpg', 'lchown',
# 'linesep', 'link', 'listdir', 'listxattr', 'lockf', 'lseek', 'lstat', 'major',
# 'makedev', 'makedirs', 'minor', 'mkdir', 'mkfifo', 'mknod', 'name', 'nice',
# 'open', 'openpty', 'pardir', 'path', 'pathconf', 'pathconf_names', 'pathsep',
# 'pipe', 'pipe2', 'popen', 'posix_fadvise', 'posix_fallocate', 'pread',
# 'putenv', 'pwrite', 'read', 'readlink', 'readv', 'remove', 'removedirs',
# 'removexattr', 'rename', 'renames', 'replace', 'rmdir', 'scandir',
# 'sched_get_priority_max', 'sched_get_priority_min', 'sched_getaffinity',
# 'sched_getparam', 'sched_getscheduler', 'sched_param',
# 'sched_rr_get_interval', 'sched_setaffinity', 'sched_setparam',
# 'sched_setscheduler', 'sched_yield', 'sendfile', 'sep', 'set_blocking',
# 'set_inheritable', 'setegid', 'seteuid', 'setgid', 'setgroups', 'setpgid',
# 'setpgrp', 'setpriority', 'setregid', 'setresgid', 'setresuid', 'setreuid',
# 'setsid', 'setuid', 'setxattr', 'spawnl', 'spawnle', 'spawnlp', 'spawnlpe',
# 'spawnv', 'spawnve', 'spawnvp', 'spawnvpe', 'st', 'stat', 'stat_float_times',
# 'stat_result', 'statvfs', 'statvfs_result', 'strerror',
# 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids',
# 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sync', 'sys',
#  'sysconf', 'sysconf_names', 'system', 'tcgetpgrp', 'tcsetpgrp',
# 'terminal_size', 'times', 'times_result', 'truncate', 'ttyname', 'umask',
# 'uname', 'uname_result', 'unlink', 'unsetenv', 'urandom', 'utime', 'wait',
# 'wait3', 'wait4', 'waitid', 'waitid_result', 'waitpid', 'walk', 'write',
# 'writev'
