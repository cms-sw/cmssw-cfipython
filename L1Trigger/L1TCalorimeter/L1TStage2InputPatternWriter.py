import FWCore.ParameterSet.Config as cms

def L1TStage2InputPatternWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('L1TStage2InputPatternWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
