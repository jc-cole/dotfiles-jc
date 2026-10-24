function fish_prompt --description 'Nothing to fear — monochrome and neon glitch'
    set -l last_status $status
    set -l normal (set_color normal)
    set -l muted (set_color 85858f)
    set -l pink (set_color ff38dc)
    set -l cyan (set_color 36c9dc)
    set -l violet (set_color 9b87ff)

    printf '\n%s┌─ %s%s' $muted $cyan (prompt_pwd)
    if set -q SSH_TTY; or set -q SSH_CONNECTION
        printf ' %s@%s' $muted $hostname
    end
    if functions -q fish_git_prompt
        set -l git_info (fish_git_prompt '%s')
        if test -n "$git_info"
            printf ' %s// %s%s' $muted $violet $git_info
        end
    end
    if test $last_status -ne 0
        printf ' %s× %s' (set_color ff615b) $last_status
    end
    if fish_is_root_user
        printf ' %s[root]' (set_color ff615b)
    end
    printf '\n%s└─%s ❯ %s' $muted $pink $normal
end
