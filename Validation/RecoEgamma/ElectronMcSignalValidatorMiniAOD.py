import FWCore.ParameterSet.Config as cms

def ElectronMcSignalValidatorMiniAOD(**kwargs):
  mod = cms.EDProducer('ElectronMcSignalValidatorMiniAOD',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
