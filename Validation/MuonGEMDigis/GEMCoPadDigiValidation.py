import FWCore.ParameterSet.Config as cms

def GEMCoPadDigiValidation(**kwargs):
  mod = cms.EDProducer('GEMCoPadDigiValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
