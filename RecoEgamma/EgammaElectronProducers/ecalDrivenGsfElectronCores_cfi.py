import FWCore.ParameterSet.Config as cms

ecalDrivenGsfElectronCores = cms.EDProducer('GsfElectronCoreEcalDrivenProducer',
  gsfPfRecTracks = cms.InputTag('pfTrackElec'),
  gsfTracks = cms.InputTag('electronGsfTracks'),
  ctfTracks = cms.InputTag('generalTracks'),
  useGsfPfRecTracks = cms.bool(True),
  hgcalOnly = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
