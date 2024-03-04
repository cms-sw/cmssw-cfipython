import FWCore.ParameterSet.Config as cms

def L1GctTest(**kwargs):
  mod = cms.EDAnalyzer('L1GctTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
