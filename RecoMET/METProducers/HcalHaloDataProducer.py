import FWCore.ParameterSet.Config as cms

def HcalHaloDataProducer(*args, **kwargs):
  mod = cms.EDProducer('HcalHaloDataProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
