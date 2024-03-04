import FWCore.ParameterSet.Config as cms

def PATTriggerObjectStandAloneSelector(**kwargs):
  mod = cms.EDFilter('PATTriggerObjectStandAloneSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
