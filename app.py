from web3 import Web3
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
import random
from werkzeug.utils import secure_filename
import os
from flask import g
import string





app = Flask(__name__)
# rpc_url = "https://rpc.open-campus-codex.gelato.digital"
# web3 = Web3(Web3.HTTPProvider(rpc_url))
# nft_contract_address = "0xb7687e9e5cB584520350b489AcF6dB82F81f5290"
# nft_abi = [{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_eduTokenAddress","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"address","name":"owner","type":"address"}],"name":"ERC721IncorrectOwner","type":"error"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ERC721InsufficientApproval","type":"error"},{"inputs":[{"internalType":"address","name":"approver","type":"address"}],"name":"ERC721InvalidApprover","type":"error"},{"inputs":[{"internalType":"address","name":"operator","type":"address"}],"name":"ERC721InvalidOperator","type":"error"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"ERC721InvalidOwner","type":"error"},{"inputs":[{"internalType":"address","name":"receiver","type":"address"}],"name":"ERC721InvalidReceiver","type":"error"},{"inputs":[{"internalType":"address","name":"sender","type":"address"}],"name":"ERC721InvalidSender","type":"error"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ERC721NonexistentToken","type":"error"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"OwnableInvalidOwner","type":"error"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"OwnableUnauthorizedAccount","type":"error"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"owner","type":"address"},{"indexed":True,"internalType":"address","name":"approved","type":"address"},{"indexed":True,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"owner","type":"address"},{"indexed":True,"internalType":"address","name":"operator","type":"address"},{"indexed":False,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint256","name":"_fromTokenId","type":"uint256"},{"indexed":False,"internalType":"uint256","name":"_toTokenId","type":"uint256"}],"name":"BatchMetadataUpdate","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"internalType":"uint256","name":"_tokenId","type":"uint256"}],"name":"MetadataUpdate","type":"event"},{"inputs":[{"internalType":"string","name":"tokenURI","type":"string"}],"name":"mintNFT","outputs":[],"stateMutability":"nonpayable","type":"function"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":True,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"},{"indexed":True,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferNFT","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"eduTokenAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"hasEnoughGas","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"MIN_GAS_FEE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"}]
# nft_contract = web3.eth.contract(address=nft_contract_address, abi=nft_abi)

# # # Wallet details
# owner_address = "0x118eE37bDDc669a7cBe6d662a11dEFd87584fb23" #my address
# private_key = "017ed39ed53bc9c23f657c3e5cb9cef13eb5aa1f9ee37ddae1c715ca18fd0012"  # My private key

#         # # Metadata URL (Replace with actual URL)
# metadata_url = "https://www.pythonanywhere.com/user/collegebaazar4/shares/74150d42eb814c3897b70b5a1968d728/"

#         # # Get nonce
# nonce = web3.eth.get_transaction_count(owner_address)

app.secret_key = "waeiuuhid"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///usersdb.sqlite3'
app.config['SQLALCHEMY_BINDS'] = {
    'prods_db': 'sqlite:///prodsdb.sqlite3',
    'users_db': 'sqlite:///usersdb.sqlite3',
    'transacs_db': 'sqlite:///transacsdb.sqlite3',
    'fgot_pass_db': 'sqlite:///fgot_pass_db.sqlite3',
    'historyBC' : 'sqlite:///historyBC_db.sqlite3'
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'ruis.id9@gmail.com'
app.config['MAIL_PASSWORD'] = 'jjazhprflkncdlqf'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)
temp_username=""
temp_pass=""
global icon
icon = "&#x2705;"

# def check_email_domain(email):
#     parts = email.split('@')
#     return len(parts) == 2 and parts[1] == "heritageit.edu.in"
def check_email_domain(email):
    parts = email.split('@')
    is_clg_mail=parts[1]=="heritageit.edu.in" or parts[1]=='heritageit.edu'
    # return len(parts) == 2 and parts[1] == "heritageit.edu.in"
    return len(parts) == 2 and is_clg_mail

class User(db.Model):
    __bind_key__ = 'users_db'
    id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column("username", db.String(100), nullable=False, unique=True)
    password = db.Column("password", db.String(100), nullable=False)
    email_verified = db.Column("email_verified", db.Boolean, default=False)
    wall_addr=db.Column("wallet_address", db.String(100), default="NA")
    wall_pk=db.Column("wallet_priv_key", db.String(100), default="NA")
class Prod(db.Model):
    __bind_key__ = 'prods_db'
    id=db.Column("id", db.Integer, primary_key=True)
    prod_name=db.Column("prod_name", db.String(100), nullable=False, unique=False)
    prod_price=db.Column("prod_price", db.Float, nullable=False)
    seller_id=db.Column("seller_id", db.Integer, nullable=False)
    image_name=db.Column("image_name", db.String(100), nullable=False, unique=False)
class History(db.Model):
    __bind_key__ = 'historyBC'
    id=db.Column("id", db.Integer, primary_key=True)
    prod_id=db.Column("prod_id", db.Integer, nullable=False, unique=False)
    prev_owner = db.Column("prev_owner", db.String(100), nullable=False)
    curr_owner = db.Column("curr_owner", db.String(100), nullable=False)
    tnx1 = db.Column("tnx1", db.String(100), nullable=False)#transaction 1:minting NFT
    tnx2 = db.Column("tnx2", db.String(100), nullable=False)
class Transac(db.Model):
    __bind_key__ = 'transacs_db'
    id=db.Column("id", db.Integer, primary_key=True)
    prod_id=db.Column("prod_id", db.Integer, nullable=False, unique=False)
    seller_id=db.Column("seller_id", db.Integer, nullable=False)
    buyer_id=db.Column("buyer_id", db.Integer, nullable=False)
    prod_price=db.Column("prod_price", db.Float, nullable=False)
    date=db.Column("date", db.String, nullable=False)
    time=db.Column("time", db.String, nullable=False)
    location=db.Column("location", db.String(50), nullable=False)
    seller_conf=db.Column("seller_conf", db.Integer, nullable=False)
    buyer_conf=db.Column("buyer_conf", db.Integer, nullable=False)
    completion=db.Column("completion", db.Integer, nullable=False)
class Fgot_pass(db.Model):
    __bind_key__ = 'fgot_pass_db'
    id = db.Column("id", db.Integer, primary_key=True)
    user_id = db.Column("User_id", db.Integer, nullable=False, unique=True)
    code = db.Column("Code", db.String(100), nullable=False)
@app.route("/", methods=['GET', 'POST'])
def home():
    allProds=Prod.query.all()

    status=0
    if 'username' in session:
        status=1
    # return render_template('new_dashboard.html')
    if request.method=='POST':
        query=request.form['query']
        if query:
            results=Prod.query.filter(Prod.prod_name.ilike(f"%{query}%")).all()
        return render_template('test.html', allProds=results, status=status)
    return render_template('test.html', allProds=allProds, status=status)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            #flash('Login successful!', 'success')
            session['username'] = username
            session['user_id'] = user.id
            # return redirect(url_for('new_dashboard'))
            # earlier: return redirect(url_for('dashboard', username=username))
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials', 'error')

    return render_template("wahidlogin.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conf_password = request.form['conf_password']

        if not username or not password:
            flash('Username and password required')
            return redirect(url_for('signup'))

        #if not check_email_domain(username):
            #flash('Enter your college email ID')
            #return redirect(url_for('signup'))

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists', 'error')
        elif password!=conf_password:
            flash('Both the passwords need to be the same', 'error')
        else:
            hashed_pass = generate_password_hash(password)
            global temp_username
            global temp_pass
            temp_username=username
            temp_pass=hashed_pass
            return redirect(url_for('otppage'))
            session['user_id'] = temp_row.id
            flash('Sign up successful')
            return redirect(url_for('home'))
    # return render_template('signup.html')
    return render_template('wahidsignup.html')

#@app.route("/meta_mask")
#def meta_mask():
    #return render_template("meta_mask.html")

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")


@app.route("/dashboard")
def dashboard():
    if "username" in session:
        username = session["username"]
        row = User.query.filter_by(username=username).first()
        email_verified = row.email_verified
        return render_template('dashboard.html', username=username, email_verified=email_verified, icon=icon)
    return redirect(url_for('login'))
@app.route("/verification", methods=['POST', 'GET'])
def otppage():
    username=temp_username
    if 'otp' not in session:
        session['otp']=random.randint(1000, 9999)
        print(f"Gen: {session['otp']}")
        msg = Message(
            subject="OTP for College Baazar",
            sender=("College Baazar support", app.config['MAIL_USERNAME']),
            recipients=[username]
        )
        msg.body = f"{session['otp']} is your OTP for College Baazar Account Creation, dont share with anyone.\nIf you did not request the otp, kindly ignore this message."
        try:
            mail.send(msg)
        except Exception as e:
            print(f'Error sending email: {str(e)}')

    if request.method == 'POST':
        n=int(request.form['n1'])*1000+int(request.form['n2'])*100+int(request.form['n3'])*10+int(request.form['n4'])
        # entered_otp = int(request.form.get("otp_from_form"))
        entered_otp = n
        print(f"Entered otp is: {n} and session otp: {int(session['otp'])}\n")
        print("Class 1: ", type(entered_otp))
        print(" Class 2: ", type(int(session['otp'])))
        if entered_otp == int(session['otp']):
            print("Entered if")
            # username = temp_username
            # password=temp_pass
            new_user = User(username=username, password=temp_pass, wall_addr="NA", wall_pk="NA")
            db.session.add(new_user)
            db.session.commit()
            session['username'] = username
            temp_row=User.query.filter_by(username=session['username']).first()
            session['user_id'] = temp_row.id
            return redirect(url_for('home'))
    return render_template('otppage.html')
@app.route("/logout")
def logout():
    session.clear()
    flash('Logged out successfully!')
    return redirect(url_for('login'))
def is_allowed_extension(filename):
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'svg'}  # Example set of extensions
    # Extract the file extension
    file_extension = filename.split('.')[-1].lower()

    # Check if the file extension is in the allowed set
    return file_extension in allowed_extensions


@app.route("/meta_mask", methods=['GET', 'POST'])
def meta_mask():
    if 'username' not in session:
        flash('You need to be logged in first.')
        return redirect(url_for('login'))
    if  request.method=='POST':
        wallet=request.form['wallet']
        privateKey=request.form['privateKey']
        if not wallet or not privateKey:
            flash('Both fields need to be filled')
            return redirect(url_for('meta_mask'))
        m_user=User.query.filter_by(id=session['user_id']).first()
        m_user.wall_addr=wallet
        m_user.wall_pk=privateKey
        db.session.add(m_user)
        db.session.commit()
        flash('Meta Mask Linked!')
        return redirect(url_for('home'))
    return render_template("meta_mask.html")
@app.route('/add_product', methods=['GET', 'POST'])
def addprod():
    if 'username' not in session:
        flash('You need to be logged in first.')
        return redirect(url_for('login'))
    if  request.method=='POST':
        prod_name=request.form['prod_name'].capitalize()
        prod_price=request.form['prod_price']
        seller_id= session['user_id']
        max_id = db.session.query(func.max(Prod.id)).scalar()
        next_id= (max_id or 0) + 1
        #product_id_for_image=
        # new_prod=Prod(prod_name=prod_name, prod_price=prod_price, seller_id=seller_id)
        #image integration
        if int(prod_price)>50000:
            return 'Price can not be higher than 50, 000 rupees.'
        if len(prod_name)> 20:
            return 'Product name cannot be greater than 20 characters.'
        if 'image' not in request.files:
            return 'No file part'
        file = request.files['image']
        if file.filename == '':
            return 'No selected file'
        # if file and allowed_file(file.filename):
        file_temp=file.filename.split('.')[-1].lower()
        if not file or file_temp not in ALLOWED_EXTENSIONS:
            return 'Enter a valid file.'
            #filename.split('.')[-1].lower()
            # Sanitize the original filename
            original_filename = secure_filename(file.filename)

            # Rename the file (example: prefix with 'new_' or use a timestamp)
        new_filename = f"image_{next_id}.{file.filename.rsplit('.', 1)[1].lower()}"

            # Alternatively, use a timestamp or UUID for unique filenames
            # from datetime import datetime
            # new_filename = datetime.now().strftime("%Y%m%d%H%M%S") + '_' + original_filename

            # Save the file with the new name
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_filename))

        new_prod=Prod(prod_name=prod_name, prod_price=prod_price, seller_id=seller_id, image_name=new_filename)
        db.session.add(new_prod)
        db.session.commit()
        #new starts 04:45
        # last_prod_id=Prod.query.order_by(Prod.id.desc()).first().id
        # print(f"last id of prod is: {last_prod_id}")
        # seller_wall=User.query.filter_by(id=session['user_id']).first().wall_addr
        # seller_wall=seller_.wall_addr if seller_ else None


        # #minting starts


        # # Connect to the testnet


        # # NFT contract address and ABI

        # # Connect to the contract


        # # Estimate gas
        # try:
        #     estimated_gas = nft_contract.functions.mintNFT(metadata_url).estimate_gas({"from": owner_address})
        #     estimated_gas = int(estimated_gas * 1.2)  # Increase gas limit by 20%
        # except Exception as e:
        #     print(f"Gas estimation failed: {e}")
        #     exit()

        # # Build the minting transaction
        # txn = nft_contract.functions.mintNFT(metadata_url).build_transaction({
        #     "from": owner_address,
        #     "gas": estimated_gas,
        #     "gasPrice": web3.to_wei("10", "gwei"),
        #     "nonce": nonce
        # })

        # # Sign and send the transaction
        # signed_txn = web3.eth.account.sign_transaction(txn, private_key)
        # tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
        # #minting ends

        # new_hist=History(prod_id=last_prod_id, prev_owner="NULL", curr_owner=seller_wall, tnx1=tx_hash, tnx2="NULL")
        # db.session.add(new_hist)
        db.session.commit()
        #new ends 04:45


        #------------
        # db.session.add(new_prod)
        # db.session.commit()


        """global otp
        otp=random.randint(1000,9999)
        msg=Message('routineMaker Email Verification.', sender='wahidurr661@outlook.com', recipients=[username])
        msg.body="Hi your otp for routineMaker is: "+str(otp)
        mail.send(msg)"""

        flash('Product added succesfully!')
        return redirect(url_for('addprod'))
    return render_template('addprod.html')#addprod2 for newPage
@app.route('/all_products', methods=['GET', 'POST'])
def allprods():
    allProds=Prod.query.all()
    # if request.method=='GET':
    #     if 'username' not in session:
    #         flash('You need to log in first!')
    #         return render_template('harshlogin.html')

    return render_template('test.html', allProds=allProds)
@app.route('/prod_info/<int:sno>', methods=['GET', 'POST'])
def prodinfo(sno):
    if 'username' not in session:
        flash("You need to be logged in first.")
        return redirect(url_for('login'))
    if  request.method=='POST':
        row_Prod=Prod.query.filter_by(id=sno).first()
        prod_id=row_Prod.id
        seller_id=row_Prod.seller_id
        buyer_id=session['user_id']
        if ownProduct(prod_id, buyer_id):
            flash('You can not buy your own product!')
            return redirect(url_for('home'))
        if alreadyBought(prod_id, buyer_id):
            flash('This exact item is already pending in your Pending Purchases!')
            allProds=Prod.query.all()
            return render_template('test.html', allProds=allProds)
        prod_price=row_Prod.prod_price
        date=request.form['date']
        time=request.form['time']
        location=request.form['location']


        new_transac=Transac(prod_id=prod_id, seller_id=seller_id, buyer_id=buyer_id, prod_price=prod_price, date=date, time=time, location=location, seller_conf=0, buyer_conf=1, completion=0)
        db.session.add(new_transac)
        db.session.commit()

        flash('Product purchase in process, check Pending Purchases for more details.')
        return redirect(url_for('home'))
    row_val=Prod.query.filter_by(id=sno).first()
    return render_template('productinfo.html', row_val=row_val)
@app.route('/buy_dashboard')
def buydash():#working
    if 'username' not in session:
        flash("You need to be logged in first.")
        return redirect(url_for('login'))
    pending_buys=Transac.query.filter_by( buyer_id=session['user_id'], completion=0).all()
    names=[]

    for pending_buy in pending_buys:
        names.append(Prod.query.filter_by(id=pending_buy.prod_id).first())



    return render_template('buy_dashboard.html', names=names, pending_buys=pending_buys)
@app.route('/buy_dashboard_confirmed')
def buydashconfirmed():
    if 'username' not in session:
        flash("You need to be logged in first.")
        return redirect(url_for('login'))
    confirmed_buys=Transac.query.filter_by( buyer_id=session['user_id'], completion=1).all()
    names=[]

    for confirmed_buy in confirmed_buys:
        names.append(Prod.query.filter_by(id=confirmed_buy.prod_id).first())


    return render_template('buy_dashboard_confirmed.html', names=names, confirmed_buys=confirmed_buys)
@app.route('/sell_dashboard')
# def selldash():#working
#     if 'username' not in session:
#         flash("You need to be logged in first.")
#         return redirect(url_for('login'))
#     pending_sells=Transac.query.filter_by(completion=0, seller_id=session['user_id']).all()
#     names=[]
#     for pending_sell in pending_sells:
#         names.append(Prod.query.filter_by(id=pending_sell.prod_id).first())
#     return render_template('sell_dashboard.html', names=names)
def selldash():#trial
    if 'username' not in session:
        flash("You need to be logged in first.")
        return redirect(url_for('login'))
    pending_sells=Transac.query.filter_by( seller_id=session['user_id'], completion=0).all()
    names=[]
    for pending_sell in pending_sells:
        names.append(Prod.query.filter_by(id=pending_sell.prod_id).first())
    return render_template('sell_dashboard.html', names=names, pending_sells=pending_sells)
# @app.route('/sell_dashboard')
# def selldash():
#     pending_sells=Transac.query.filter_by(completion=0, seller_id=session['user_id']).all()
#     pending_sells_names=[]
#     for pending_sell in pending_sells:
#         product=Prod.query.filter_by(id=pending_sell.id).first()
#         product_name=product.prod_name
#         pending_sells_names.append(product_name)
#     return render_template('buy_dashboard.html', names=pending_sells_names)
#Configuring upload folder
#UPLOAD_FOLDER = 'uploads/'
@app.route('/sell_dashboard_confirmed')
def selldashconfirmed():
    if 'username' not in session:
        flash("You need to be logged in first.")
        return redirect(url_for('login'))
    confirmed_sales=Transac.query.filter_by( seller_id=session['user_id'], completion=1).all()
    names=[]

    for confirmed_sell in confirmed_sales:
        names.append(Prod.query.filter_by(id=confirmed_sell.prod_id).first())


    return render_template('sell_dashboard_confirmed.html', names=names, confirmed_sales=confirmed_sales)
@app.route('/buyer_order_info/<int:sno>')
def buyerorderinfo(sno):
    # transac_row=Transac.query.filter_by(prod_id=sno, buyer_id=session['user_id']).first()
    transac_row=Transac.query.filter_by(id=sno, buyer_id=session['user_id']).first()

    return render_template('buyer_order_info.html', transac_row=transac_row)


@app.route('/seller_order_info/<int:sno>')
# def sellerorderinfo(sno):#working
#     transac_row=Transac.query.filter_by(prod_id=sno, seller_id=session['user_id']).first()
#     return render_template('seller_order_info.html', transac_row=transac_row)

def sellerorderinfo(sno):#trial
    transac_row=Transac.query.filter_by(id=sno).first()
    return render_template('seller_order_info.html', transac_row=transac_row)


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/harsh_login')
def harshlogin():
    return render_template('harshlogin.html')
@app.route('/read/<status>')
def read(status):
    stat=status[-4:]
    print(f"stat: {stat}")
    id=status[:-4]
    print(f"id: {id}")
    if 'username' not in session:
        return redirect(url_for('home'))
    row=Transac.query.filter_by(id=id).first()
    if stat=='conf':
        sendMailConfirmation(row)
        if row.buyer_conf==1:
            row.seller_conf=1
            row.completion=1
            db.session.add(row)
            db.session.commit()
            print("entered: accepted")
            return redirect(url_for('home'))
        else:
            row.buyer_conf=1
            row.completion=1
            db.session.add(row)
            db.session.commit()
            print("entered: accepted")
            return redirect(url_for('home'))
    elif stat=='edit':
        # if row.buyer_conf==1:
        #     row.buyer_conf=0
        # else:
        #     row.seller_conf=0
        # db.session.add(row)
        # db.session.commit()
        print("entered: edit")
        return redirect(f'/edit/{id}')
    else: #rejected
        if row.buyer_conf==1:
            row.buyer_conf=0
        row.seller_conf=0
        db.session.add(row)
        db.session.commit()
        print("entered: rejected")
        return redirect(url_for('home'))
@app.route('/edit/<int:sno>', methods=['POST', 'GET'])
def edit(sno):
    if request.method=='POST':
        row=Transac.query.filter_by(id=sno).first()
        row.date=request.form['date']
        row.time=request.form['time']
        row.location=request.form['location']
        if row.buyer_conf==1:
            print("row.buyer_conf==1 triggered")
            row.buyer_conf=0
            row.seller_conf=1
        else:
            row.seller_conf=0
            row.buyer_conf=1
        db.session.add(row)
        db.session.commit()
        return redirect(url_for('home'))
    row=Transac.query.filter_by(id=sno).first()
    return render_template('edit.html', row=row)

def sendMailConfirmation(row):
    buyer_id=row.buyer_id
    seller_id=row.seller_id
    buyer=User.query.filter_by(id=buyer_id).first()
    seller=User.query.filter_by(id=seller_id).first()
    mail_list=[buyer.username, seller.username]
    product=Prod.query.filter_by(id=row.prod_id).first()
    product_name=product.prod_name

    msg = Message(
        subject="Order Confirmed",
        sender=("College Baazar Support", app.config['MAIL_USERNAME']),
        recipients=[buyer.username]
    )
    msg.body = f"Hi,  your order for {product_name} on College Baazar is Confirmed!\nKindly meet up at the following location at {row.time}.\nDate: {row.date}\nLocation: {row.location}"
    try:
        mail.send(msg)
        print("mail sent")
    except Exception as e:
        print(f'Error sending email: {str(e)}')




    msg = Message(
            subject="Order Confirmed",
            sender=("College Baazar Support", app.config['MAIL_USERNAME']),
            recipients=[seller.username]
        )
    msg.body = f"Hi,  your order for {product_name} on College Baazar is Confirmed!\nKindly meet up at the following location at {row.time}.\nDate: {row.date}\nLocation: {row.location}"
    try:
        mail.send(msg)
    except Exception as e:
        print(f'Error sending email: {str(e)}')
@app.route('/wahid_login', methods=['POST', 'GET'])
def wahidlogin():
    return render_template('wahidlogin.html')
def alreadyBought(prod_id, buyer_id):
    row=Transac.query.filter_by(completion=0, buyer_id=buyer_id, prod_id=prod_id).first()
    if row:
        return True
    return False
def ownProduct(prod_id, buyer_id):
    row=Prod.query.filter_by(id=prod_id).first()
    if row.seller_id==buyer_id:
        return True
    return False
@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method=='POST':
        f_name=request.form['fullname']
        e_address='wahidurr661@outlook.com'
        sub=request.form['subject']
        message=request.form['message']
        msg = Message(
        subject=sub,
        sender=("College Baazar support", app.config['MAIL_USERNAME']),
        recipients=[e_address]
        )
        msg.body = f"{f_name}\n{e_address}\n{message}"
        try:
            mail.send(msg)
            print("mail sent")
        except Exception as e:
            print(f'Error sending email: {str(e)}')
        return redirect(url_for('contact'))
    return render_template('contact_form2.html')
@app.route('/search', methods=['GET'])
def search():
    query=request.args.get('query')
    if query:
        results=Prod.query.filter(Prod.prod_name.ilike(f"%{query}%")).all()
        return render_template('search_results.html', results=results)
    return render_template('')

def generate_random_string(length=20):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@app.route('/forgot_password_phase1', methods=['GET', 'POST'])
def forgot_password_phase1():
    if request.method=='POST':
        email=request.form['username']
        email_in_db=User.query.filter_by(username=email).first()
        if not email_in_db:
            flash('No account found linked to thsi email')
            return redirect(url_for('forgot_password_phase1'))
        user_id=email_in_db.id
        print(f"User id is : {user_id}")
        code=generate_random_string()
        print(f"code is; {code}")
        fgot_pass_row=Fgot_pass(user_id=user_id, code=str(code))
        db.session.add(fgot_pass_row)
        db.session.commit()
        #send mail
        msg = Message(
            subject="Password reset link",
            sender=("College Baazar Support", app.config['MAIL_USERNAME']),
            recipients=[email]
        )
        msg.body = f"Your password reset link is: \nhttps://collegebaazar.pythonanywhere.com//forgot_password_phase2/{code} \nGo to the above link and follow the instructions.\nDo not share with anyone."
        try:
            mail.send(msg)
            print("mail sent for password reset")
        except Exception as e:
            print(f'Error sending email: {str(e)}')
        flash('Check your mail box, a link has been sent to help you change your password')
    return render_template('forgot_password_phase1.html')

@app.route('/forgot_password_phase2/<string:sno>', methods=['GET', 'POST'])
def forgot_password_phase2(sno=''):
    fgot_pass_row=Fgot_pass.query.filter_by(code=sno).first()
    if not fgot_pass_row:
        return '<h1>404 No Page found :-(</h1>'
    if request.method=='POST':
        new_pass=request.form['new_pass']
        conf_new_pass=request.form['conf_new_pass']
        if new_pass!=conf_new_pass:
            flash('Both the passwords need to be same')
            return redirect(f'/forgot_password_phase2/{sno}')
        user_id=fgot_pass_row.user_id
        print(f'user_id is: {user_id}')
        user_row=User.query.filter_by(id=user_id).first()
        user_row.password=generate_password_hash(str(new_pass))
        print(f'new pass is: {new_pass}')
        db.session.add(user_row)
        db.session.commit()
        #delete the link
        db.session.delete(fgot_pass_row)
        db.session.commit()
        flash('Login with your new password')
        return redirect(url_for('login'))

    return render_template('forgot_password_phase2.html')


@app.before_request
def load_user():
    if 'username' not in session: # Function to retrieve the current user
        g.user = None
        return
    u_txt=session['username']
    position = u_txt.find('.')
    g.user=u_txt[:position].capitalize()
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # db.create_all(bind='users_db')  # Create tables for the users_db
        # db.create_all(bind='prods_db')  # Create tables for the prods_db
    app.run(debug=False)
