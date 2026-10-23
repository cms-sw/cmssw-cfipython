import FWCore.ParameterSet.Config as cms

def GenPUProtonProducer(*args, **kwargs):
  mod = cms.EDProducer('GenPUProtonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
