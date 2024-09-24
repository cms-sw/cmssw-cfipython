import FWCore.ParameterSet.Config as cms

def HGCalTriggerGeomTesterV9Imp3(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalTriggerGeomTesterV9Imp3',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
