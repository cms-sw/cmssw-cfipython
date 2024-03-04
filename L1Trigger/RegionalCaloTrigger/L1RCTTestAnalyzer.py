import FWCore.ParameterSet.Config as cms

def L1RCTTestAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('L1RCTTestAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
