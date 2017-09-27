sl()
{
#mac dont have usleep (to make ls -t work)
#so Im ordering these by size (ls -S)

    mkdir rick-astley
    cd rick-astley

    mkdir never
    zip -r gonna.zip never > /dev/null
    ln -s up.txt give
    ln -s up.sh you
    touch up.sh
    chmod 755 up.sh

    ls -S #sort by size
    cd ..

    rm -rf rick-astley
}
