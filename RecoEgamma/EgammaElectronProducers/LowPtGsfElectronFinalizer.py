import FWCore.ParameterSet.Config as cms

def LowPtGsfElectronFinalizer(**kwargs):
  mod = cms.EDProducer('LowPtGsfElectronFinalizer',
    previousGsfElectronsTag = cms.InputTag(''),
    regressionConfig = cms.PSet(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
