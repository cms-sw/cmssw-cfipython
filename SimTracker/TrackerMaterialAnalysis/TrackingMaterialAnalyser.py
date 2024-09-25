import FWCore.ParameterSet.Config as cms

def TrackingMaterialAnalyser(*args, **kwargs):
  mod = cms.EDAnalyzer('TrackingMaterialAnalyser',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
