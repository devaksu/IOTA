use iota_client::Client;
use rust_gpiozero::*;
use std::thread::sleep;
use std::time::Duration;

"""Program to monitor specific IOTA wallet 
and blink a led if payment is detected"""

#[tokio::main]
async fn main() {
    
    // Create a client instance and other variables
    let mut response = iota.get_address().balance(wallet).await.unwrap();
    let mut balance = response.balance;
    let wallet = "atoi1qpwvhlfyrelmme9cz5kuje70dqrf8nexcshzgs9nryz362h0d6ctkxjz2tp";
    let blink_price = 1000000;
    let led = LED::new(18);
    let iota = Client::builder()
        .with_node("https://api.lb-0.h.chrysalis-devnet.iota.cafe")
        .unwrap().with_node_sync_disabled().finish().await.unwrap();

    // Testing led working
    led.on();
    sleep(Duration::from_secs(3));
    led.off();

    println!("Connected to wallet {:?}", wallet);
    println!("Current balance: {:?} Miota", balance/1000000);

    //Loop for purchase process
    loop {
        println!("Ready for a purchase");
        response = iota.get_address().balance(wallet).await.unwrap();
        if response.balance == balance + blink_price {
            println!("Payment received. Lights ON!\nWallet balance is {:?} Miota", response.balance/1000000);
            led.on();
            sleep(Duration::from_secs(10));
            led.off();
            println!("Thank you for your order!");
            balance = response.balance;
        }
        sleep(Duration::from_secs(10));
    }
}
