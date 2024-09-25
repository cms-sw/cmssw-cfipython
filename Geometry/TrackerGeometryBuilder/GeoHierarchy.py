import FWCore.ParameterSet.Config as cms

def GeoHierarchy(*args, **kwargs):
  mod = cms.EDAnalyzer('GeoHierarchy',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
