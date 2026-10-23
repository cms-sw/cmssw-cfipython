import FWCore.ParameterSet.Config as cms

def PATTriggerMatcherDRLessByR(*args, **kwargs):
  mod = cms.EDProducer('PATTriggerMatcherDRLessByR',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
