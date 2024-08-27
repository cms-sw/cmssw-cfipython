import FWCore.ParameterSet.Config as cms

def L1GtStableParametersTester(**kwargs):
  mod = cms.EDAnalyzer('L1GtStableParametersTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
