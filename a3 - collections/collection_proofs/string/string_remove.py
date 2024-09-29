if __name__ == "__main__":
    st = "abcjj"
    print(st)

    st = st.replace("a","")
    print(st)
    st = st[:3]
    print(st)

    st = st.removeprefix("b")
    print(st)

    st = st.removesuffix("j")
    print(st)