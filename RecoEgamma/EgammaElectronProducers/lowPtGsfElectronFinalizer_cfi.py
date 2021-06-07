import FWCore.ParameterSet.Config as cms

lowPtGsfElectronFinalizer = cms.EDProducer('LowPtGsfElectronFinalizer',
  previousGsfElectronsTag = cms.InputTag(''),
  regressionConfig = cms.PSet()
)
