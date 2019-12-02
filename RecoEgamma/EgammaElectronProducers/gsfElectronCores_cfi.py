import FWCore.ParameterSet.Config as cms

gsfElectronCores = cms.EDProducer('GsfElectronCoreProducer',
  gsfPfRecTracks = cms.InputTag('pfTrackElec'),
  gsfTracks = cms.InputTag('electronGsfTracks'),
  ctfTracks = cms.InputTag('generalTracks'),
  useGsfPfRecTracks = cms.bool(True),
  ecalDrivenGsfElectronCoresTag = cms.InputTag('ecalDrivenGsfElectronCores'),
  pflowGsfElectronCoresTag = cms.InputTag('pfElectronTranslator', 'pf'),
  pfSuperClusters = cms.InputTag('pfElectronTranslator', 'pf'),
  pfSuperClusterTrackMap = cms.InputTag('pfElectronTranslator', 'pf'),
  mightGet = cms.optional.untracked.vstring
)
