import FWCore.ParameterSet.Config as cms

def GE0TriggerPseudoProducer(*args, **kwargs):
  mod = cms.EDProducer('GE0TriggerPseudoProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
