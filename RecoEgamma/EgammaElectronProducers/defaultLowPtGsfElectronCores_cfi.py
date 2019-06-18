import FWCore.ParameterSet.Config as cms

defaultLowPtGsfElectronCores = cms.EDProducer('LowPtGsfElectronCoreProducer',
  gsfPfRecTracks = cms.InputTag('pfTrackElec'),
  gsfTracks = cms.InputTag('electronGsfTracks'),
  ctfTracks = cms.InputTag('generalTracks'),
  useGsfPfRecTracks = cms.bool(True),
  superClusters = cms.InputTag('lowPtGsfElectronSuperClusters'),
  mightGet = cms.optional.untracked.vstring
)
