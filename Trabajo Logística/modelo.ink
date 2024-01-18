inkling "2.0"
using Goal
using Math

# Numero de trabajos por batch
const MaxJobCount = 10

# Numero de maquinas que recorre cada trabajo
const StepCount = 4

type LearningState {
    # Tabla con los trabajos que no han comenzado
    JobTimes: number<0 .. 60>[StepCount][MaxJobCount],

    # Steps no completados para trabajos en progreso
    WIPTimes: number<0 .. 60>[(StepCount - 1) * StepCount / 2],
    BlockTime: number,
}

type SimState extends LearningState {
    NextJobMask: number<0, 1, >[MaxJobCount],
}

type SimAction {
    NextJob: number<J1 = 1, J2 = 2, J3 = 3, J4 = 4, J5 = 5, J6 = 6, J7 = 7, J8 = 8, J9 = 9, J10 = 10>,
}

simulator FlexSimSimulator(action: SimAction): SimState {
}

function ApplyJobMask(s: SimState) {
    return constraint SimAction {
        NextJob: number<mask s.NextJobMask>
    }
}

graph (input: SimState) {
    concept RemoveMask(input): LearningState {
        programmed function (s: SimState): LearningState {
            return LearningState(s)
        }
    }
    output concept MinimizeBlockTime(RemoveMask): SimAction {
        curriculum {

            source FlexSimSimulator
            mask ApplyJobMask

            training {
                EpisodeIterationLimit: 800,
                NoProgressIterationLimit: 1000000,
            }

            goal (State: SimState) {
                minimize BlockTime:
                    State.BlockTime
                    in Goal.RangeBelow(20)
            }
        }
    }
}
