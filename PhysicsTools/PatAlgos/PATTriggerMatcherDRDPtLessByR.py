import FWCore.ParameterSet.Config as cms

def PATTriggerMatcherDRDPtLessByR(**kwargs):
  mod = cms.EDProducer('PATTriggerMatcherDRDPtLessByR',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
