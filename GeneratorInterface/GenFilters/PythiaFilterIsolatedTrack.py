import FWCore.ParameterSet.Config as cms

def PythiaFilterIsolatedTrack(**kwargs):
  mod = cms.EDFilter('PythiaFilterIsolatedTrack',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
