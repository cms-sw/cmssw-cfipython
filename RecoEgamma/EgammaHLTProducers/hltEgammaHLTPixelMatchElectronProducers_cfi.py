import FWCore.ParameterSet.Config as cms

hltEgammaHLTPixelMatchElectronProducers = cms.EDProducer('EgammaHLTPixelMatchElectronProducers',
  TrackProducer = cms.InputTag('hltEleAnyWP80CleanMergedTracks'),
  GsfTrackProducer = cms.InputTag(''),
  UseGsfTracks = cms.bool(False),
  BSProducer = cms.InputTag('hltOnlineBeamSpot'),
  mightGet = cms.optional.untracked.vstring
)
