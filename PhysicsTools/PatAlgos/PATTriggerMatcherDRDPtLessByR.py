import FWCore.ParameterSet.Config as cms

def PATTriggerMatcherDRDPtLessByR(*args, **kwargs):
  mod = cms.EDProducer('PATTriggerMatcherDRDPtLessByR',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
