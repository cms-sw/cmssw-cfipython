import FWCore.ParameterSet.Config as cms

trackProducerFromPatMuons = cms.EDProducer('TrackProducerFromPatMuons',
  src = cms.InputTag('slimmedMuons'),
  innerTrackOnly = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)
