import FWCore.ParameterSet.Config as cms

def GEMPadDigiValidation(*args, **kwargs):
  mod = cms.EDProducer('GEMPadDigiValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
