import FWCore.ParameterSet.Config as cms

def TestFindProduct(**kwargs):
  mod = cms.EDAnalyzer('TestFindProduct',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
