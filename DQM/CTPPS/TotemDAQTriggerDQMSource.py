import FWCore.ParameterSet.Config as cms

def TotemDAQTriggerDQMSource(*args, **kwargs):
  mod = cms.EDProducer('TotemDAQTriggerDQMSource',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
