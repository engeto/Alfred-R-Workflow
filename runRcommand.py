


import rpy2.robjects as robjects
import sys
import alfred


if __name__ == "__main__":
    try:
        val = str(sys.argv[1])
    except:
        sys.exit(1)

    icon = alfred.Icon(filepath="/Applications/R.app")

    r_item = alfred.Item(
        uid='hex',
        arg="",
        title=str(robjects.r(val)),
        subtitle="R Output",
        valid=False,
        icon=icon)


    print alfred.render([r_item])