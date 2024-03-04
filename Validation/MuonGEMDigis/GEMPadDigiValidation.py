import FWCore.ParameterSet.Config as cms

def GEMPadDigiValidation(**kwargs):
  mod = cms.EDProducer('GEMPadDigiValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
