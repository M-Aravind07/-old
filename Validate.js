    function ValidateSignupForm()
                    {
                        var uname=document.forms["signupform"]["uname_signup"].value;
                        if (uname=="" || uname==null)
                            {
                                alert("Please enter username");
                                return false;
                            }

                        var useremail=document.forms["signupform"]["email_signup"].value;
                        if (useremail=="" || useremail==null)
                            {
                                alert("Please enter email");
                                return false;
                            }

                        var pwd=document.forms["signupform"]["pwd_signup"].value;
                            if (pwd=="" || pwd==null)
                                {
                                    alert("Please enter password");
                                    return false;
                                }

                        var confirmpwd=document.forms["signupform"]["confirmpwd_signup"].value;
                            if (confirmpwd=="" || confirmpwd==null)
                                {
                                    alert("Please enter confirmation password");
                                    return false;
                                }

                            if (pwd!==confirmpwd)
                                {
                                    adddlert("Passwords do not match");
                                    return false;
                                }
            
                            if (length(pwd)<=8)
                                {
                                    alert("Password should be atleast 5 characters");
                                    return false;
                                }
                            
                            else if (length(pwd)>20)
                                {
                                    alert("Password is too large. Enter >8 and <20 characters")
                                    return false;
                                }
                    }