import FWCore.ParameterSet.Config as cms

def APVCyclePhaseDebuggerFromL1TS(*args, **kwargs):
  mod = cms.EDAnalyzer('APVCyclePhaseDebuggerFromL1TS',
    l1TSCollection = cms.InputTag('scalersRawToDigi'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
