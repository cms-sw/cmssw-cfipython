import FWCore.ParameterSet.Config as cms

def TotemDAQTriggerDQMSource(**kwargs):
  mod = cms.EDProducer('TotemDAQTriggerDQMSource',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
