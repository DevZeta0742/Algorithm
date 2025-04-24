use std::io::{stdin, stdout, Result, Write};

const P: i64 = 998244353;

fn mod_pow(mut base: i64, mut exp: i64, modulus: i64) -> i64 {
    let mut result = 1;
    base %= modulus;
    while exp > 0 {
        if exp & 1 > 0 {
            result = result * base % modulus;
        }
        exp >>= 1;
        base = base * base % modulus;
    }
    result
}

fn fft(a: &mut Vec<i64>, inv: bool) {
    let n = a.len();
    let mut j = 0;

    for i in 1..n {
        let mut rev = n / 2;
        while j >= rev {
            j -= rev;
            rev /= 2
        }
        j += rev;
        if i < j {
            a.swap(i, j);
        }
    }

    let mut step = 2;
    while step <= n {
        let half = step / 2;
        let u = mod_pow(3, (P - 1) / step as i64, P);
        let u = if inv { mod_pow(u, P - 2, P) } else { u };

        for i in (0..n).step_by(step) {
            let mut w = 1;
            for j in i..i+half {
                let v = a[j + half] * w % P;
                a[j + half] = (a[j] - v + P) % P;
                a[j] = (a[j] + v) % P;
                w = w * u % P;
            }
        }
        step *= 2;
    }

    if inv {
        let num = mod_pow(n as i64, P - 2, P);
        for i in 0..n {
            a[i] = a[i] * num % P;
        }
    }
}

fn multiply(a: &[i64], b: &[i64]) -> String {
    let mut n: i64 = 1;
    let total_length: usize = a.len() + b.len();
    while n < total_length as i64 {
        n *= 2;
    }

    let mut a_reversed: Vec<i64> = a.iter().rev().cloned().collect();
    a_reversed.resize(n as usize, 0);

    let mut b_reversed: Vec<i64> = b.iter().rev().cloned().collect();
    b_reversed.resize(n as usize, 0);

    fft(&mut a_reversed, false);
    fft(&mut b_reversed, false);

    let mut c: Vec<i64> = vec![0; n as usize];
    for i in 0..n as usize {
        c[i] = (a_reversed[i] * b_reversed[i]) % P;
    }

    fft(&mut c, true);

    let mut carry: i64 = 0;
    for i in 0..c.len() {
        carry += c[i];
        c[i] = carry % 10;
        carry /= 10;
    }

    while carry > 0 {
        c.push(carry % 10);
        carry /= 10;
    }

    let result: String = c.iter().rev().map(|&digit| digit.to_string()).collect();

    let result = result.trim_start_matches('0');
    if result.is_empty() {
        "0".to_string()
    } else {
        result.to_string()
    }
}

fn parse_digits(s: &str) -> Vec<i64> {
    s.chars().map(|c| c.to_digit(10).unwrap() as i64).collect()
}

fn main() -> Result<()> {
    let mut input = String::new();
    stdin().read_line(&mut input)?;
    let arr: Vec<&str> = input.trim().split(' ').collect();


    let a = parse_digits(arr[0].trim());
    let b = parse_digits(arr[1].trim());

    let res = multiply(&a, &b);

    writeln!(stdout(), "{}", res)?;

    Ok(())
}
