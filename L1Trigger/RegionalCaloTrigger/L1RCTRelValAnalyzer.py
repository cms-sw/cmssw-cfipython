import FWCore.ParameterSet.Config as cms

def L1RCTRelValAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('L1RCTRelValAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
