import FWCore.ParameterSet.Config as cms

def LowPtGsfElectronFinalizer(*args, **kwargs):
  mod = cms.EDProducer('LowPtGsfElectronFinalizer',
    previousGsfElectronsTag = cms.InputTag(''),
    regressionConfig = cms.PSet(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
