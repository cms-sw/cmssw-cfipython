import FWCore.ParameterSet.Config as cms

defaultLowPtGsfElectronID = cms.EDProducer('LowPtGsfElectronIDProducer',
  useGsfToTrack = cms.bool(False),
  usePAT = cms.bool(False),
  electrons = cms.InputTag('lowPtGsfElectrons'),
  gsfToTrack = cms.InputTag('lowPtGsfToTrackLinks'),
  unbiased = cms.InputTag('lowPtGsfElectronSeedValueMaps', 'unbiased'),
  rho = cms.InputTag('fixedGridRhoFastjetAllTmp'),
  ModelNames = cms.vstring(),
  ModelWeights = cms.vstring(),
  ModelThresholds = cms.vdouble(),
  PassThrough = cms.bool(False),
  MinPtThreshold = cms.double(0.5),
  MaxPtThreshold = cms.double(15),
  Version = cms.string('')
)
