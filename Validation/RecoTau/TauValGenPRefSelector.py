import FWCore.ParameterSet.Config as cms

def TauValGenPRefSelector(**kwargs):
  mod = cms.EDFilter('TauValGenPRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
