import FWCore.ParameterSet.Config as cms

def EcalPreshowerDigisValidation(**kwargs):
  mod = cms.EDProducer('EcalPreshowerDigisValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod