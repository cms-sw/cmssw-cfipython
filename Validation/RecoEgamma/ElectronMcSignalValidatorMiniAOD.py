import FWCore.ParameterSet.Config as cms

def ElectronMcSignalValidatorMiniAOD(*args, **kwargs):
  mod = cms.EDProducer('ElectronMcSignalValidatorMiniAOD',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
