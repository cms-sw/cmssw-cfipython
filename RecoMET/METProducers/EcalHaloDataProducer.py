import FWCore.ParameterSet.Config as cms

def EcalHaloDataProducer(*args, **kwargs):
  mod = cms.EDProducer('EcalHaloDataProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
