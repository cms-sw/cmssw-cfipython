import FWCore.ParameterSet.Config as cms

def L1TCaloLayer1Validator(**kwargs):
  mod = cms.EDAnalyzer('L1TCaloLayer1Validator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
