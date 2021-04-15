import FWCore.ParameterSet.Config as cms

lowPtGsfElectronCores = cms.EDProducer('LowPtGsfElectronCoreProducer',
  gsfPfRecTracks = cms.InputTag('lowPtGsfElePfGsfTracks'),
  ctfTracks = cms.InputTag('generalTracks'),
  superClusters = cms.InputTag('lowPtGsfElectronSuperClusters'),
  mightGet = cms.optional.untracked.vstring
)
