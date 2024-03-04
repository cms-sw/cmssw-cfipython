import FWCore.ParameterSet.Config as cms

def L1RCTParametersTester(**kwargs):
  mod = cms.EDAnalyzer('L1RCTParametersTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
