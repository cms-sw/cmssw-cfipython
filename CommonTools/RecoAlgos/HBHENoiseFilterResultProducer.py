import FWCore.ParameterSet.Config as cms

def HBHENoiseFilterResultProducer(*args, **kwargs):
  mod = cms.EDProducer('HBHENoiseFilterResultProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
