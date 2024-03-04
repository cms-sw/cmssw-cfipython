import FWCore.ParameterSet.Config as cms

def CastorInvalidDataFilter(**kwargs):
  mod = cms.EDFilter('CastorInvalidDataFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
