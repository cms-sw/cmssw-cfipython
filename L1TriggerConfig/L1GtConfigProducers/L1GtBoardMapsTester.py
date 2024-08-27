import FWCore.ParameterSet.Config as cms

def L1GtBoardMapsTester(**kwargs):
  mod = cms.EDAnalyzer('L1GtBoardMapsTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
