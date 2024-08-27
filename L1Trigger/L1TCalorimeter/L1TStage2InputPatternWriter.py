import FWCore.ParameterSet.Config as cms

def L1TStage2InputPatternWriter(**kwargs):
  mod = cms.EDAnalyzer('L1TStage2InputPatternWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
