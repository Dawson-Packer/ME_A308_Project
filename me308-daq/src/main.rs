use esp_idf_svc::hal::peripherals::Peripherals;
use esp_idf_svc::hal::adc::*;
// use esp_idf_svc::hal::adc::attenuation::adc_atten_t;

fn main() -> Result<()> {

    let peripherals = Peripherals::take()?;

    let mut adc = AdcDriver::new(peripherals.adc1, &Config::new().calibration(true))?;

    // const ATTENUATION: adc_atten_t = attenuation::DB_6;

    // It is necessary to call this function once. Otherwise some patches to the runtime
    // implemented by esp-idf-sys might not link properly. See https://github.com/esp-rs/esp-idf-template/issues/71
    esp_idf_svc::sys::link_patches();

    // Bind the log crate to the ESP Logging facilities
    esp_idf_svc::log::EspLogger::initialize_default();

    log::info!("Hello, world!");

    Ok(())
}
