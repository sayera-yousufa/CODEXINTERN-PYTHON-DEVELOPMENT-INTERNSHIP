import streamlit as st
import numpy as np

st.set_page_config(page_title="Matrix Operations Tool", layout="centered")
st.title("🧮 Matrix Operations Tool using NumPy")

# Helper function to convert input string to matrix
def parse_matrix(text):
    try:
        return np.array([[float(num) for num in row.split()] for row in text.strip().split('\n')])
    except:
        st.error("Invalid matrix format. Please check your input.")
        return None

st.markdown("### ✍️ Enter Matrix A:")
matrix_a_text = st.text_area("Matrix A (use space between elements and newline between rows)", height=100)
st.markdown("### ✍️ Enter Matrix B:")
matrix_b_text = st.text_area("Matrix B (only needed for binary operations)", height=100)

operation = st.selectbox("📌 Select Operation", [
    "Addition (A + B)",
    "Subtraction (A - B)",
    "Multiplication (A × B)",
    "Transpose (A)",
    "Transpose (B)",
    "Determinant (A)",
    "Determinant (B)"
])

if st.button("🔄 Compute"):
    A = parse_matrix(matrix_a_text)
    B = parse_matrix(matrix_b_text) if matrix_b_text.strip() else None

    if A is None:
        st.stop()

    if "B" in operation and B is None:
        st.error("Matrix B is required for this operation.")
        st.stop()

    try:
        if operation == "Addition (A + B)":
            result = A + B
        elif operation == "Subtraction (A - B)":
            result = A - B
        elif operation == "Multiplication (A × B)":
            result = A @ B
        elif operation == "Transpose (A)":
            result = A.T
        elif operation == "Transpose (B)":
            result = B.T
        elif operation == "Determinant (A)":
            if A.shape[0] == A.shape[1]:
                result = np.linalg.det(A)
            else:
                st.error("Matrix A must be square to calculate determinant.")
                st.stop()
        elif operation == "Determinant (B)":
            if B.shape[0] == B.shape[1]:
                result = np.linalg.det(B)
            else:
                st.error("Matrix B must be square to calculate determinant.")
                st.stop()

        st.success("✅ Result:")
        st.code(str(result))

    except Exception as e:
        st.error(f"❌ Error: {e}")
