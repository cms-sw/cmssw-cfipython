import FWCore.ParameterSet.Config as cms

def APVCyclePhaseDebuggerFromL1TS(**kwargs):
  mod = cms.EDAnalyzer('APVCyclePhaseDebuggerFromL1TS',
    l1TSCollection = cms.InputTag('scalersRawToDigi'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
