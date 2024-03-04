import FWCore.ParameterSet.Config as cms

def GEMStripDigiValidation(**kwargs):
  mod = cms.EDProducer('GEMStripDigiValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
