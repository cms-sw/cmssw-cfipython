import FWCore.ParameterSet.Config as cms

def EcalDigisValidation(**kwargs):
  mod = cms.EDProducer('EcalDigisValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
