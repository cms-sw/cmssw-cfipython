import FWCore.ParameterSet.Config as cms

trackExtraRekeyer = cms.EDProducer('TrackExtraRekeyer',
  src = cms.InputTag('generalTracks'),
  association = cms.InputTag('muonReducedTrackExtras')
)
