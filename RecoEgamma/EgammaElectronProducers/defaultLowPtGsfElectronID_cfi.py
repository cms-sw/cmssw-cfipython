import FWCore.ParameterSet.Config as cms

defaultLowPtGsfElectronID = cms.EDProducer('LowPtGsfElectronIDProducer',
  electrons = cms.InputTag('lowPtGsfElectrons'),
  rho = cms.InputTag('fixedGridRhoFastjetAllTmp'),
  ModelNames = cms.vstring(),
  ModelWeights = cms.vstring(),
  ModelThresholds = cms.vdouble(),
  PassThrough = cms.bool(False),
  MinPtThreshold = cms.double(0.5),
  MaxPtThreshold = cms.double(15)
)
