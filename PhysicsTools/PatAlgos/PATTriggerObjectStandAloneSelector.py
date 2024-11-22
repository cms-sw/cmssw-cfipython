import FWCore.ParameterSet.Config as cms

def PATTriggerObjectStandAloneSelector(*args, **kwargs):
  mod = cms.EDFilter('PATTriggerObjectStandAloneSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
