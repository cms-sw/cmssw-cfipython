import FWCore.ParameterSet.Config as cms

def PythiaFilterIsolatedTrack(*args, **kwargs):
  mod = cms.EDFilter('PythiaFilterIsolatedTrack',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
