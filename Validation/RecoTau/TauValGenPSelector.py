import FWCore.ParameterSet.Config as cms

def TauValGenPSelector(**kwargs):
  mod = cms.EDFilter('TauValGenPSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
