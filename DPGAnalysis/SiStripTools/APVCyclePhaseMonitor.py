import FWCore.ParameterSet.Config as cms

def APVCyclePhaseMonitor(*args, **kwargs):
  mod = cms.EDAnalyzer('APVCyclePhaseMonitor',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
