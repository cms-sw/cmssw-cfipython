import FWCore.ParameterSet.Config as cms

lowPtGsfElectronID = cms.EDProducer('LowPtGsfElectronIDProducer',
  electrons = cms.InputTag('lowPtGsfElectrons'),
  unbiased = cms.InputTag('lowPtGsfElectronSeedValueMaps', 'unbiased'),
  rho = cms.InputTag('fixedGridRhoFastjetAllTmp'),
  ModelNames = cms.vstring(''),
  ModelWeights = cms.vstring('RecoEgamma/ElectronIdentification/data/LowPtElectrons/RunII_Autumn18_LowPtElectrons_mva_id.xml.gz'),
  ModelThresholds = cms.vdouble(-10),
  PassThrough = cms.bool(False),
  MinPtThreshold = cms.double(0.5),
  MaxPtThreshold = cms.double(15),
  mightGet = cms.optional.untracked.vstring
)
