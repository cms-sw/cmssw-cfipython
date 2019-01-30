import FWCore.ParameterSet.Config as cms

produceEcalDrivenGsfElectronCores = cms.EDProducer('GEDGsfElectronCoreProducer',
  gsfPfRecTracks = cms.InputTag('pfTrackElec'),
  gsfTracks = cms.InputTag('electronGsfTracks'),
  ctfTracks = cms.InputTag('generalTracks'),
  useGsfPfRecTracks = cms.bool(True),
  GEDEMUnbiased = cms.InputTag('GEDPFCandidates')
)
