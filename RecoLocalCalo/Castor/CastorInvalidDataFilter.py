import FWCore.ParameterSet.Config as cms

def CastorInvalidDataFilter(*args, **kwargs):
  mod = cms.EDFilter('CastorInvalidDataFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
