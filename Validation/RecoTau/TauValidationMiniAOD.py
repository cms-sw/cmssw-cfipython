import FWCore.ParameterSet.Config as cms

def TauValidationMiniAOD(**kwargs):
  mod = cms.EDProducer('TauValidationMiniAOD',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
