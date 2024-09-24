import FWCore.ParameterSet.Config as cms

def L1KeyListWriter(**kwargs):
  mod = cms.EDAnalyzer('L1KeyListWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod