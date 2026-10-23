import FWCore.ParameterSet.Config as cms

def EcalFEDWithCRCErrorProducer(*args, **kwargs):
  mod = cms.EDProducer('EcalFEDWithCRCErrorProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
