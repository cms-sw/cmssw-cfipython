import FWCore.ParameterSet.Config as cms

def HGCalTriggerGeomTesterV9Imp2(**kwargs):
  mod = cms.EDAnalyzer('HGCalTriggerGeomTesterV9Imp2',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
