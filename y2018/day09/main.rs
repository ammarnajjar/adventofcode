// I will leave this here as a proof to that
// the programming language does not
// matter as much as the algorithm!
use std::collections::HashMap;
use std::fs;

fn parse(filename: String) -> (u32, u32) {
    let contents = fs::read_to_string(filename)
        .expect("file not opened");
    let v: Vec<&str> = contents.split(' ').collect();
    let players: u32 = v[0].parse().expect("Not a number");
    let marbles: u32 = v[6].parse().expect("Not a number");
    (players, marbles)
}

fn inc_p(player: u32, ceiling: u32) -> u32 {
    let mut r = player + 1;
    if r > ceiling {
        r = 1;
    }
    r
}

fn calc(filename: String) -> u32 {
    let (players, marbles) = parse(filename);
    let mut scores = HashMap::new();
    scores.insert(0, 0);
    let mut g = vec![0, 1];
    let mut player = 1;
    let mut pos: usize = 1;

    for m in 2..(marbles + 1) {
        player = inc_p(player, players);
        if m % 23 == 0 {
            let posx: i32 = (pos as i32) - 7;
            if posx < 0 {
                pos = ((g.len() as i32) + posx) as usize;
            } else {
                pos = posx as usize;
            }
            let mut score = m + g.remove(pos);
            match scores.get(&player) {
                Some(current_score) => score += current_score,
                _ => (),
            }
            scores.insert(player, score);
            println!("marble: {} / {}", m.to_string(), marbles.to_string());
            continue;
        }
        else if (m - 1) % 23 == 0 {
            let posx: i32 = (g.iter().position(|&r| r == (m - 2)).unwrap()) as i32 - 4;
            if posx < 0 {
                pos = ((g.len() as i32) + posx) as usize;
            } else {
                pos = posx as usize;
            }
        }
        else {
            pos = g.iter().position(|&r| r == (m - 1)).unwrap() + 2;
        }
        let len_g = g.len();
        if pos > len_g {
            pos = pos - len_g;
        }
        g.insert(pos, m);
    }
    println!("scores: {:?}", scores);
    let mut max_score: u32 = 0;
    for &s in scores.values() {
        if s > max_score {
            max_score = s;
        }
    }
    max_score
}

fn main() {
    let v = calc("input09".to_string());
    println!("max = {:?}", v);
}
