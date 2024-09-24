import FWCore.ParameterSet.Config as cms

def PATMETSelector(*args, **kwargs):
  mod = cms.EDFilter('PATMETSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
