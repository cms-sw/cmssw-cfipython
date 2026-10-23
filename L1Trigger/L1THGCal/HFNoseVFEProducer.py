import FWCore.ParameterSet.Config as cms

def HFNoseVFEProducer(*args, **kwargs):
  mod = cms.EDProducer('HFNoseVFEProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
