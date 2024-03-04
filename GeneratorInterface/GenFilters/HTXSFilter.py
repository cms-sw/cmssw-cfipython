import FWCore.ParameterSet.Config as cms

def HTXSFilter(**kwargs):
  mod = cms.EDFilter('HTXSFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
