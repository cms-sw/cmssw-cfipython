import FWCore.ParameterSet.Config as cms

def HcalTBTriggerFilter(**kwargs):
  mod = cms.EDFilter('HcalTBTriggerFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
