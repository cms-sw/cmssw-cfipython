import FWCore.ParameterSet.Config as cms

def HGCalTriggerGeoTesterManager(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalTriggerGeoTesterManager',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
