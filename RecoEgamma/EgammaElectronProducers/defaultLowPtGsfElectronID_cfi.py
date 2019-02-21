import FWCore.ParameterSet.Config as cms

defaultLowPtGsfElectronID = cms.EDProducer('LowPtGsfElectronIDProducer',
  electrons = cms.InputTag('lowPtGsfElectrons'),
  rho = cms.InputTag('fixedGridRhoFastjetAllTmp'),
  ModelNames = cms.vstring(''),
  ModelWeights = cms.vstring('RecoEgamma/ElectronIdentification/data/LowPtElectrons/RunII_Fall17_LowPtElectrons_mva_id.xml.gz'),
  ModelThresholds = cms.vdouble(-1),
  PassThrough = cms.bool(False),
  MinPtThreshold = cms.double(0.5),
  MaxPtThreshold = cms.double(15)
)
