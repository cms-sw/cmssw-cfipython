import FWCore.ParameterSet.Config as cms

def HcalTBTriggerFilter(*args, **kwargs):
  mod = cms.EDFilter('HcalTBTriggerFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
