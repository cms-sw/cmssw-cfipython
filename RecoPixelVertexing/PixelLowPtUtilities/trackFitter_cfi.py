import FWCore.ParameterSet.Config as cms

trackFitter = cms.EDProducer('TrackFitterProducer',
  TTRHBuilder = cms.string(''),
  mightGet = cms.optional.untracked.vstring
)
