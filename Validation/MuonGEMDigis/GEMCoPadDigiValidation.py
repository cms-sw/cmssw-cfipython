import FWCore.ParameterSet.Config as cms

def GEMCoPadDigiValidation(*args, **kwargs):
  mod = cms.EDProducer('GEMCoPadDigiValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
