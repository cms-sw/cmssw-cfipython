import FWCore.ParameterSet.Config as cms

def TauValidationMiniAOD(*args, **kwargs):
  mod = cms.EDProducer('TauValidationMiniAOD',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
