import FWCore.ParameterSet.Config as cms

def EcalMixingModuleValidation(**kwargs):
  mod = cms.EDProducer('EcalMixingModuleValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
