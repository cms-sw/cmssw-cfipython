import FWCore.ParameterSet.Config as cms

def EcalTBMCInfoProducer(*args, **kwargs):
  mod = cms.EDProducer('EcalTBMCInfoProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
