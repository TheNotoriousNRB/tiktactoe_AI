from tictactoe_game_environment import TicTacToeGameEnvironment as gm
from une_ai.models import GraphNode

def minimax(node, player, depth):
    move_best = None
    game_state = node.get_state()
    player_turn = game_state['player-turn']
    is_maximizing = player_turn == player

    if is_maximizing:
        value = float('-inf')
    else:
        value = float('+inf')
    
    if depth <= 0 or gm.is_terminal(game_state):
        value = gm.payoff(game_state, player)
        return value, move_best
    
    legal_actions = gm.get_legal_actions(game_state)
    for action in legal_actions:
        new_state = gm.transition_result(game_state, action)
        child_node = GraphNode(new_state, node, action, 1)
        value_new, _ = minimax(child_node, player, depth-1)
        if(is_maximizing and value_new > value) or (not is_maximizing and value_new < value):
            value = value_new
            move_best = action
            
    return value, move_best

def minimax_alpha_beta(node, player, alpha, beta, depth):
    return 0, None

def optimised_minimax(node, player, tt, depth):
    return 0, None