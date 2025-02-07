import FWCore.ParameterSet.Config as cms

def SwitchProducer(*args, **kwargs):
  mod = cms.EDProducer('SwitchProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
