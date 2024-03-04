import FWCore.ParameterSet.Config as cms

def TriggerMatcherToHLTDebug(**kwargs):
  mod = cms.EDProducer('TriggerMatcherToHLTDebug',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
