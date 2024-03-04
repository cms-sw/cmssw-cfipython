import FWCore.ParameterSet.Config as cms

def HcalDigisValidation(**kwargs):
  mod = cms.EDProducer('HcalDigisValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
