import FWCore.ParameterSet.Config as cms

def EcalBarrelDigisValidation(**kwargs):
  mod = cms.EDProducer('EcalBarrelDigisValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
