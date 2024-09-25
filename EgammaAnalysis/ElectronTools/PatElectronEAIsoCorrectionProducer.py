import FWCore.ParameterSet.Config as cms

def PatElectronEAIsoCorrectionProducer(*args, **kwargs):
  mod = cms.EDProducer('PatElectronEAIsoCorrectionProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
