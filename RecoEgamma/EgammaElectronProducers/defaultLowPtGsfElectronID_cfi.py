import FWCore.ParameterSet.Config as cms

defaultLowPtGsfElectronID = cms.EDProducer('LowPtGsfElectronIDProducer',
  electrons = cms.InputTag('lowPtGsfElectrons'),
  unbiased = cms.InputTag('lowPtGsfElectronSeedValueMaps', 'unbiased'),
  rho = cms.InputTag('fixedGridRhoFastjetAll'),
  ModelNames = cms.vstring(''),
  ModelWeights = cms.vstring('RecoEgamma/ElectronIdentification/data/LowPtElectrons/LowPtElectrons_ID_2020Nov28.root'),
  ModelThresholds = cms.vdouble(-99),
  PassThrough = cms.bool(False),
  MinPtThreshold = cms.double(0.5),
  MaxPtThreshold = cms.double(15),
  Version = cms.string('V1'),
  mightGet = cms.optional.untracked.vstring
)
