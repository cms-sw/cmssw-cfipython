import FWCore.ParameterSet.Config as cms

def GenHIEventProducer(*args, **kwargs):
  mod = cms.EDProducer('GenHIEventProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
