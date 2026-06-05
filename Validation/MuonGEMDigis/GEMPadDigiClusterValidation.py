import FWCore.ParameterSet.Config as cms

def GEMPadDigiClusterValidation(*args, **kwargs):
  mod = cms.EDProducer('GEMPadDigiClusterValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
