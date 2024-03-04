import FWCore.ParameterSet.Config as cms

def L1TBasicDemo(**kwargs):
  mod = cms.EDAnalyzer('L1TBasicDemo',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
