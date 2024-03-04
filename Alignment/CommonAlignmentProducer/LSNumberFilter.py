import FWCore.ParameterSet.Config as cms

def LSNumberFilter(**kwargs):
  mod = cms.EDFilter('LSNumberFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
