import FWCore.ParameterSet.Config as cms

def TestFilterModule(**kwargs):
  mod = cms.EDFilter('TestFilterModule',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
