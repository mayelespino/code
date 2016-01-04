#
#http://ss64.com/bash/syntax-prompt.html
export PS1='\[\e[33m\][\u | \h | \w]\[\e[0m\]\n>'
#export PS1='[\u@\h:\w]\n\[\e[33m\]>\[\e[0m\]'
export PS2="> "
export PATH=$PATH:~/bin
export HISTTIMEFORMAT="%d/%m/%y %T "
#
alias l='ls -hF'
alias ll='ls -htAFl'
alias lc='ls -Fm'
alias l1='ls -1'
alias la='ls -aF'
alias L='ls -F | grep /'
alias c='clear'
alias gh='cd /x/local/maespino/githome/gimp'
alias ldr='ls -AF *|grep \/'
alias mp='ps -alumaespino | grep -v tcs| grep -v bash | grep -v ssh | grep -v grep'
alias d='history | grep -w cd  | grep -v history | cut -c 26- | sort -u'
alias e='open -a TextMate'

#
#

# List like
#
function lk
{
    ls | grep -i $1
}


# Bookmark files and/or list them out.
#
function BM {
    if [[ ! -e ~/.scratch ]]
    then
        mkdir ~/.scratch
    fi

    case $1 in
    '')
        echo ">================<"
        cat ~/.scratch/bm.txt
        echo ">================<"
        ;;
    e)
        vim ~/.scratch/bm.txt
        ;;
    *)
        sort ~/.scratch/bm.txt | uniq -u > ~/.scratch/bm.tmp
        mv ~/.scratch/bm.txt ~/.scratch/bm.old
	mv ~/.scratch/bm.tmp ~/.scratch/bm.txt
	for file in $@
	do 
	    echo `pwd`\/$file >> ~/.scratch/bm.txt
	done
	;;
    esac
}

# TAR file from  ~/.scratch/bm.txt in to ~/TAR.tar
#
function TBM
{
    if [ -x ~/TBM.tar ]
    then
        rm ~/TBM.tar
    fi
    tar -cPf ~/TBM.tar `cat ~/.scratch/bm.txt`
    tar -tf ~/TBM.tar
    ll ~/TBM.tar
}

#Back up to ~/back/$file.$RANDOM.BACK 
#
function BK
{
    for file in $@
    do 
        cp $file ~/back/$file.$RANDOM.BK 
    done  
}


# Create the VIMRC file
#
function createVimrcFile
{
cat > ~/.vimrc << EOF
" expand tabs
set tabstop=4
set shiftwidth=4
set expandtab
"highlighting
syntax  off
"Show menu with possible tab completions
set wildmenu
"matches are highlighted
set nohls

EOF
}

function H
{
    history | grep -w $1  | grep -v history | cut -c 26- | sort -u
}

function K
{
    for output in $(ps aux | grep $1 | grep -v grep | awk '{print $2}'); do kill -9 $output; done 
}


function C
{
    echo $1 | bc -q
}


#http://amix.dk/vim/vimrc.html
function vimrc()
{
cat > ~/.vimrc << EOF
" Ignore case when searching
set ignorecase
" Highlight search results
set hlsearch
" Show matching brackets when text indicator is over them
set showmatch
" No annoying sound on errors
set noerrorbells
set novisualbell
set t_vb=
set tm=500
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Colors and Fonts
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Enable syntax highlighting
syntax enable

colorscheme desert
set background=dark

" Set extra options when running in GUI mode
if has("gui_running")
    set guioptions-=T
    set guioptions+=e
    set t_Co=256
    set guitablabel=%M\ %t
endif

" Set utf8 as standard encoding and en_US as the standard language
set encoding=utf8

" Use Unix as the standard file type
set ffs=unix,dos,mac
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Files, backups and undo
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Turn backup off, since most stuff is in SVN, git et.c anyway...
set nobackup
set nowb
set noswapfile


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Text, tab and indent related
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Use spaces instead of tabs
set expandtab

" Be smart when using tabs ;)
set smarttab

" 1 tab == 4 spaces
set shiftwidth=4
set tabstop=4

" Linebreak on 500 characters
set lbr
set tw=500

"Auto indent
set ai
"Smart indent
set si
"Wrap lines	
set wrap 

EOF
}

#
# main()
#
# <><
