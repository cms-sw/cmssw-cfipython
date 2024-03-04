import FWCore.ParameterSet.Config as cms

def EcalTBValidation(**kwargs):
  mod = cms.EDProducer('EcalTBValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
