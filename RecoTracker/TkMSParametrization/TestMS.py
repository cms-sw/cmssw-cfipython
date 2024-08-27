import FWCore.ParameterSet.Config as cms

def TestMS(**kwargs):
  mod = cms.EDAnalyzer('TestMS',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
