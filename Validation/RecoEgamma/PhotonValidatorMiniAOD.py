import FWCore.ParameterSet.Config as cms

def PhotonValidatorMiniAOD(*args, **kwargs):
  mod = cms.EDProducer('PhotonValidatorMiniAOD',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
