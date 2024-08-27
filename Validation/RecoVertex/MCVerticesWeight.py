import FWCore.ParameterSet.Config as cms

def MCVerticesWeight(**kwargs):
  mod = cms.EDFilter('MCVerticesWeight',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
