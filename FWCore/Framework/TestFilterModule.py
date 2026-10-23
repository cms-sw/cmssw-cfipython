import FWCore.ParameterSet.Config as cms

def TestFilterModule(*args, **kwargs):
  mod = cms.EDFilter('TestFilterModule',
    acceptValue = cms.untracked.int32(1),
    onlyOne = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
