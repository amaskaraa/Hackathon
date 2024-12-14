import streamlit as st

from src.services.process import extract_text,generate_user_stories_and_criteria_specific


def main():
    st.title("BRD Automation System")

    st.sidebar.header("Inputs")
    brd_file = st.sidebar.file_uploader("Upload BRD Document", type=["pdf", "docx", "txt"])
    # app_link = st.sidebar.text_input("Application Link")
    # setup_file = st.sidebar.file_uploader("Upload Setup Guidelines", type=["txt"])

    if st.sidebar.button("Generate Test Cases"):
        if brd_file is None:
            st.sidebar.error("Please upload a BRD document before generating test cases.")
        else:
            st.subheader("Extracted BRD Requirements")
            text = extract_text(brd_file)

            st.subheader("Text Evaluation")
            with st.spinner("Executing test cases..."):
                # user_stories_and_criteria = generate_user_stories_and_criteria(text)
                user_stories_and_criteria_specific= generate_user_stories_and_criteria_specific(text)
                st.write(user_stories_and_criteria_specific)
# ------------------------------------------------------------------------------------------------#
#         validation_result = validate_test_case(user_stories_and_criteria)
        #
        # st.subheader("Test Execution Results")
        # st.write(validation_result)
        # if st.button("Generate User Stories and Acceptance Criteria"):
        #     with st.spinner("Generating user stories and acceptance criteria..."):
        #         user_stories_and_criteria = generate_user_stories_and_criteria(text)
        #     st.subheader("Generated User Stories and Acceptance Criteria")
        #     st.write(user_stories_and_criteria)
        # print(user_stories_and_criteria)
        # if setup_file:
        #     setup_instructions = setup_file.read().decode("utf-8")
        #     if st.button("Automate Environment Setup"):
        #         setup_environment(setup_instructions)
        #         st.success("Environment setup completed successfully!")

        # Generate and Execute Test Cases
#         if st.button("Generate and Execute Test Cases"):
#             with st.spinner("Executing test cases..."):
#                 test_cases = [f"Test case for: {line}" for line in user_stories_and_criteria.splitlines() if line.strip()]
#                 print(test_cases)
#                 results = []
#                 for test_case in test_cases:
#                     acceptance_criteria = """
# 1. The platform must integrate all HR functions (Recruitment, Onboarding, Employee Management, Attendance, Leave, PMS, Payroll View, Assets, Offboarding, Helpdesk).
# 2. Employees must be able to apply for leaves, view/download payslips, regularize attendance, and raise helpdesk tickets.
# 3. Administrators must configure holidays, leave types, and payroll policies, upload payslips, and define access controls.
# 4. The setup process for the system must follow guidelines and be automated.
# 5. The platform must ensure secure, role-based access to data and workflows.
# """
#                     validation_result = validate_test_case(test_case, acceptance_criteria)
#                     status, explanation = validation_result.split("\n", 1)
#                     results.append({"test_case": test_case, "status": status, "explanation": explanation})
#             st.subheader("Test Execution Results")
#             st.write(results)
#
#             report_path = generate_report(results)
#             st.download_button(
#                 label="Download Test Report",
#                 data=open(report_path, "rb").read(),
#                 file_name="test_report.csv",
#             )




if __name__ == "__main__":
    main()
