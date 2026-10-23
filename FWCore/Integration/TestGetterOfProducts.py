import FWCore.ParameterSet.Config as cms

def TestGetterOfProducts(*args, **kwargs):
  mod = cms.EDFilter('TestGetterOfProducts',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
