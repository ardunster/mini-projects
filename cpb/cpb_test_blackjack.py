#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 17:36:49 2020

@author: adunster
"""
'''
Unit testing applications for Blackjack game
'''

import unittest
import cpb_blackjack

class TestBlackjack(unittest.TestCase):
    
    def setUp(self):
        self.deck_test = cpb_blackjack.Deck()
        self.dtest = cpb_blackjack.Dealer()
        self.ptest = cpb_blackjack.Player()

    def test_deck_shuffle(self):
        self.deck_test.shuffle()
        result = self.deck_test.shuffled
        self.assertEqual(set(result), set(self.deck_test.fresh))
        self.assertNotEqual(result, self.deck_test.fresh)

    def test_player_rec_deal(self):
        hand = ['AS', '2S']
        self.ptest.rec_deal(hand[0])
        self.ptest.rec_deal(hand[1])
        result = self.ptest.hand
        self.assertEqual(result, hand)

    def test_player_discard(self):
        hand = ['AS', '2S']
        self.ptest.rec_deal(hand[0])
        self.ptest.rec_deal(hand[1])
        self.ptest.discard()
        result = self.ptest.hand
        self.assertEqual(result, [])
    
    def test_player_bet(self):
        self.ptest.balance = 200
        bet = 100
        self.ptest.bet(bet)
        result = self.ptest.balance
        self.assertEqual(result, 100)
        
    def test_player_win(self):
        self.ptest.balance = 200
        winnings = 200
        self.ptest.win(winnings)
        result = self.ptest.balance
        self.assertEqual(result, 400)
        
    def test_player_over99k(self):
        self.ptest.balance = 98999
        winnings = 2000
        self.ptest.win(winnings)
        result = self.ptest.balance
        self.assertEqual(result, 99999)


    def test_dealer_rec_deal(self):
        hand = ['AS', '2S']
        visible_hand = ['*', '2S']
        self.dtest.rec_deal(hand[0])
        self.dtest.rec_deal(hand[1])
        result = (self.dtest.hand, self.dtest.visible_hand)
        self.assertEqual(result, (hand, visible_hand))

    def test_dealer_discard(self):
        hand = ['AS', '2S']
        self.dtest.rec_deal(hand[0])
        self.dtest.rec_deal(hand[1])
        self.dtest.discard()
        result = self.dtest.hand
        self.assertEqual(result, [])
        
        
    def test_draw_out(self):
        draw_out = []
        for i in range(6):
            draw_out.append(draw_card(i,['AS']))
        result = [' _____ ', '|A .  |', '| /.\\ |', '|(_^_)|', '|  ^  |', '|____A|']
        self.assertEqual(result, draw_out)


if __name__ == '__main__':
    unittest.main()
