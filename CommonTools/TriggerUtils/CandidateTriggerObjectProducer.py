import FWCore.ParameterSet.Config as cms

def CandidateTriggerObjectProducer(*args, **kwargs):
  mod = cms.EDProducer('CandidateTriggerObjectProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
