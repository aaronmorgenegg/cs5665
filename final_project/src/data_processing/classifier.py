from slippi.id import ActionState


CLASSIFIER_LOG_FILE = "logs/classifier_misc_states.txt"


# State Classfiers
STATE_CLASSIFIER_NEUTRAL       = 1
STATE_CLASSIFIER_LEDGE         = 2
STATE_CLASSIFIER_DOWNED_GROUND = 3
STATE_CLASSIFIER_DOWNED_AIR    = 4
STATE_CLASSIFIER_DEAD          = 5
STATE_CLASSIFIER_MOVING_GROUND = 6
STATE_CLASSIFIER_MOVING_AIR    = 7
STATE_CLASSIFIER_ATTACK_GROUND = 8
STATE_CLASSIFIER_ATTACK_AIR    = 9
STATE_CLASSIFIER_SHIELD        = 10
STATE_CLASSIFIER_DODGE         = 11
STATE_CLASSIFIER_MISC          = 12

STATE_NAMES = {
    STATE_CLASSIFIER_NEUTRAL: 'neutral',
    STATE_CLASSIFIER_LEDGE: 'ledge',
    STATE_CLASSIFIER_DOWNED_GROUND: 'downed_ground',
    STATE_CLASSIFIER_DOWNED_AIR: 'downed_air',
    STATE_CLASSIFIER_DEAD: 'dead',
    STATE_CLASSIFIER_MOVING_GROUND: 'moving_ground',
    STATE_CLASSIFIER_MOVING_AIR: 'moving_air',
    STATE_CLASSIFIER_ATTACK_GROUND: 'attack_ground',
    STATE_CLASSIFIER_ATTACK_AIR: 'attack_air',
    STATE_CLASSIFIER_SHIELD: 'shield',
    STATE_CLASSIFIER_DODGE: 'dodge',
    STATE_CLASSIFIER_MISC: 'misc'
}

# TODO: Clean up the Misc category, figure out what each of those states should be
STATE_CLASSIFIERS = {
    STATE_CLASSIFIER_NEUTRAL: [
                        ActionState.WAIT,
                        ActionState.PASS,
                        ActionState.OTTOTTO,
                        ActionState.OTTOTTO_WAIT,
                        ActionState.APPEAL_R,
                        ActionState.APPEAL_L,
                        ActionState.ITEM_HAMMER_MOVE,
                        ActionState.WAIT_2,
                        ActionState.WAIT_3,
                        ActionState.WAIT_1,
                        ActionState.WAIT_4
    ],
    STATE_CLASSIFIER_LEDGE: [
                        ActionState.CLIFF_CATCH,
                        ActionState.CLIFF_WAIT,
                        ActionState.CLIFF_CLIMB_SLOW,
                        ActionState.CLIFF_CLIMB_QUICK,
                        ActionState.CLIFF_ESCAPE_SLOW,
                        ActionState.CLIFF_ESCAPE_QUICK,
                        ActionState.CLIFF_JUMP_SLOW_1,
                        ActionState.CLIFF_JUMP_SLOW_2,
                        ActionState.CLIFF_JUMP_QUICK_1,
                        ActionState.CLIFF_JUMP_QUICK_2,
                        ActionState.CLIFF_ATTACK_SLOW,
                        ActionState.CLIFF_ATTACK_QUICK,
                        ActionState.CLIFF_WAIT_1
    ],
    STATE_CLASSIFIER_DOWNED_GROUND: [
                        ActionState.DOWN_BOUND_U,
                        ActionState.DOWN_WAIT_U,
                        ActionState.DOWN_DAMAGE_U,
                        ActionState.DOWN_STAND_U,
                        ActionState.DOWN_ATTACK_U,
                        ActionState.DOWN_FOWARD_U,
                        ActionState.DOWN_BACK_U,
                        ActionState.DOWN_SPOT_U,
                        ActionState.DOWN_BOUND_D,
                        ActionState.DOWN_WAIT_D,
                        ActionState.DOWN_DAMAGE_D,
                        ActionState.DOWN_STAND_D,
                        ActionState.DOWN_ATTACK_D,
                        ActionState.DOWN_FOWARD_D,
                        ActionState.DOWN_BACK_D,
                        ActionState.DOWN_SPOT_D,
                        ActionState.PASSIVE,
                        ActionState.PASSIVE_STAND_F,
                        ActionState.PASSIVE_STAND_B,
                        ActionState.SHIELD_BREAK_DOWN_U,
                        ActionState.SHIELD_BREAK_DOWN_D,
                        ActionState.SHIELD_BREAK_STAND_U,
                        ActionState.SHIELD_BREAK_STAND_D,
                        ActionState.FURA_FURA,
                        ActionState.CAPTURE_PULLED_HI,
                        ActionState.CAPTURE_WAIT_HI,
                        ActionState.CAPTURE_DAMAGE_HI,
                        ActionState.CAPTURE_PULLED_LW,
                        ActionState.CAPTURE_WAIT_LW,
                        ActionState.CAPTURE_DAMAGE_LW,
                        ActionState.CAPTURE_CUT,
                        ActionState.CAPTURE_JUMP,
                        ActionState.CAPTURE_NECK,
                        ActionState.CAPTURE_FOOT,
                        ActionState.DAMAGE_N_2,
                        ActionState.DAMAGE_N_3,
                        ActionState.SLIP,
                        ActionState.SLIP_STAND,
                        ActionState.MISS_FOOT,
                        ActionState.FURA_SLEEP_END,
                        ActionState.SLIP_DOWN,
                        ActionState.WAIT_ITEM,
                        ActionState.SQUAT_WAIT_ITEM,
                        ActionState.SQUAT_WAIT_1,
                        ActionState.SQUAT_WAIT_2,
                        ActionState.ITEM_HAMMER_WAIT,
                        ActionState.ITEM_BLIND,
                        ActionState.FURA_SLEEP_START,
                        ActionState.FURA_SLEEP_LOOP,
                        ActionState.ESCAPE_N,
                        ActionState.REBOUND_STOP,
                        ActionState.REBOUND
     ],
    STATE_CLASSIFIER_DOWNED_AIR: [
                        ActionState.FALL_SPECIAL,
                        ActionState.FALL_SPECIAL_F,
                        ActionState.FALL_SPECIAL_B,
                        ActionState.PASSIVE_WALL,
                        ActionState.PASSIVE_WALL_JUMP,
                        ActionState.PASSIVE_CEIL,
                        ActionState.SHIELD_BREAK_FLY,
                        ActionState.SHIELD_BREAK_FALL,
                        ActionState.THROWN_F,
                        ActionState.THROWN_B,
                        ActionState.THROWN_HI,
                        ActionState.THROWN_LW,
                        ActionState.THROWN_LW_WOMEN,
                        ActionState.WALL_DAMAGE,
                        ActionState.DAMAGE_FLY_TOP,
                        ActionState.DAMAGE_HI_2,
                        ActionState.DAMAGE_HI_1,
                        ActionState.DAMAGE_AIR_2,
                        ActionState.DAMAGE_LW_3,
                        ActionState.DAMAGE_FLY_N,
                        ActionState.DAMAGE_FLY_ROLL,
                        ActionState.DAMAGE_FALL,
                        ActionState.DAMAGE_AIR_3,
                        ActionState.DAMAGE_FLY_LW,
                        ActionState.DAMAGE_N_1,
                        ActionState.DAMAGE_FLY_HI,
                        ActionState.DAMAGE_HI_3
    ],
    STATE_CLASSIFIER_DEAD: [
                        ActionState.DEAD_DOWN,
                        ActionState.DEAD_LEFT,
                        ActionState.DEAD_RIGHT,
                        ActionState.DEAD_UP,
                        ActionState.DEAD_UP_STAR,
                        ActionState.DEAD_UP_STAR_ICE,
                        ActionState.DEAD_UP_FALL,
                        ActionState.DEAD_UP_FALL_HIT_CAMERA,
                        ActionState.DEAD_UP_FALL_HIT_CAMERA_FLAT,
                        ActionState.DEAD_UP_FALL_ICE,
                        ActionState.DEAD_UP_FALL_HIT_CAMERA_ICE,
                        ActionState.REBIRTH,
                        ActionState.REBIRTH_WAIT,
                        ActionState.ENTRY,
                        ActionState.ENTRY_START,
                        ActionState.ENTRY_END
    ],
    STATE_CLASSIFIER_MOVING_GROUND: [
                        ActionState.WALK_SLOW,
                        ActionState.WALK_MIDDLE,
                        ActionState.WALK_FAST,
                        ActionState.TURN,
                        ActionState.TURN_RUN,
                        ActionState.DASH,
                        ActionState.RUN,
                        ActionState.RUN_DIRECT,
                        ActionState.RUN_BRAKE,
                        ActionState.KNEE_BEND,
                        ActionState.SQUAT,
                        ActionState.SQUAT_WAIT,
                        ActionState.SQUAT_RV,
                        ActionState.LANDING,
                        ActionState.LANDING_FALL_SPECIAL,
                        ActionState.HEAVY_WALK_1
    ],
    STATE_CLASSIFIER_MOVING_AIR: [
                        ActionState.JUMP_F,
                        ActionState.JUMP_B,
                        ActionState.JUMP_AERIAL_F,
                        ActionState.JUMP_AERIAL_B,
                        ActionState.FALL,
                        ActionState.FALL_F,
                        ActionState.FALL_B,
                        ActionState.FALL_AERIAL,
                        ActionState.FALL_AERIAL_F,
                        ActionState.FALL_AERIAL_B
    ],
    STATE_CLASSIFIER_ATTACK_GROUND: [
                        ActionState.ATTACK_11,
                        ActionState.ATTACK_12,
                        ActionState.ATTACK_13,
                        ActionState.ATTACK_100_START,
                        ActionState.ATTACK_100_LOOP,
                        ActionState.ATTACK_100_END,
                        ActionState.ATTACK_DASH,
                        ActionState.ATTACK_S_3_HI,
                        ActionState.ATTACK_S_3_HI_S,
                        ActionState.ATTACK_S_3_S,
                        ActionState.ATTACK_S_3_LW_S,
                        ActionState.ATTACK_S_3_LW,
                        ActionState.ATTACK_HI_3,
                        ActionState.ATTACK_LW_3,
                        ActionState.ATTACK_S_4_HI,
                        ActionState.ATTACK_S_4_HI_S,
                        ActionState.ATTACK_S_4_S,
                        ActionState.ATTACK_S_4_LW_S,
                        ActionState.ATTACK_S_4_LW,
                        ActionState.ATTACK_HI_4,
                        ActionState.ATTACK_LW_4,
                        ActionState.CATCH,
                        ActionState.CATCH_PULL,
                        ActionState.CATCH_DASH,
                        ActionState.CATCH_DASH_PULL,
                        ActionState.CATCH_WAIT,
                        ActionState.CATCH_ATTACK,
                        ActionState.CATCH_CUT,
                        ActionState.THROW_F,
                        ActionState.THROW_B,
                        ActionState.THROW_HI,
                        ActionState.THROW_LW,
                        ActionState.ATTACK_S_4_HOLD
    ],
    STATE_CLASSIFIER_ATTACK_AIR: [
                        ActionState.ATTACK_AIR_N,
                        ActionState.ATTACK_AIR_F,
                        ActionState.ATTACK_AIR_B,
                        ActionState.ATTACK_AIR_HI,
                        ActionState.ATTACK_AIR_LW,
                        ActionState.LANDING_AIR_N,
                        ActionState.LANDING_AIR_F,
                        ActionState.LANDING_AIR_B,
                        ActionState.LANDING_AIR_HI,
                        ActionState.LANDING_AIR_LW
    ],
    STATE_CLASSIFIER_SHIELD: [
                        ActionState.GUARD_ON,
                        ActionState.GUARD,
                        ActionState.GUARD_OFF,
                        ActionState.GUARD_SET_OFF,
                        ActionState.GUARD_REFLECT
    ],
    STATE_CLASSIFIER_DODGE: [
                        ActionState.ESCAPE_F,
                        ActionState.ESCAPE_B,
                        ActionState.ESCAPE,
                        ActionState.ESCAPE_AIR
    ]
}

def getStateData(game):
    """

    :param game: slippi game
    :return: list of frames containing discrete states
    [[port1, port2],...,[port1, port2]]
    """
    state_data = []
    misc_states = []

    for frame in game.frames:
        frame_state = []
        for port in frame.ports:
            if port is None:
                pass
            else:
                data = port.leader
                try:
                    state = classify(data.post.state)
                except Exception as e:
                    state = STATE_CLASSIFIER_MISC
                    if data.post.state not in misc_states:
                        misc_states.append(data.post.state)
                # TODO: need to check for wavedashes
                # TODO: check if clasification of special moves in air works correctly
                frame_state.append(state)
        state_data.append(frame_state)

    try:
        with open(CLASSIFIER_LOG_FILE, "w") as myfile:
            for item in misc_states:
                myfile.write("{},\n".format(str(item)))
    except FileNotFoundError:
        print("Warning: Classifier Log file {} not found".format(CLASSIFIER_LOG_FILE))

    return state_data

def classify(state):
    """

    :param state: slippi game state
    :return: classified state
    :seealso: https://py-slippi.readthedocs.io/en/latest/source/slippi.html#module-slippi.id
    """
    for key, value in STATE_CLASSIFIERS.items():
        if state in value:
            return key
    raise Exception("Error: Could not classify game state: {}".format(str(state)))

