html_email = """\
        <html>
          <body style ="font-family: Arial, Helvetica, sans-serif; text-align: center; 
          background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(138,61,81,1) 35%, rgba(0,212,255,1) 100%);
          padding: 3%; max-width: 600px;">
          <div style = "position: relative; display:grid; background: rgba(255,255,255,0.94);
    border-radius: 5px; box-shadow: 0px 0px 11px -1px rgba(46,46,46,1); width: 600px;">
           <h2 style=" padding:40px; font-weight:lighter; text-transform:uppercase; color:#414141;"
            >Hi admin</h2>
            <p>List of today's events:<br> </p>
            <p>
               {}
            </p>
            <p style="padding:40px;">Have a nice day!</p>
            <br>
            </div>
          </body>
        </html>
        """

text_email = """\
        Hi! 
        List of today's events:
        {}
        Have a nice day!
        """
