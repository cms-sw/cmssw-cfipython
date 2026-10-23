import FWCore.ParameterSet.Config as cms

def TrackingParticleCategoriesAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TrackingParticleCategoriesAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
