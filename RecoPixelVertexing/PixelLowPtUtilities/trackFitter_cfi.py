import FWCore.ParameterSet.Config as cms

trackFitter = cms.EDProducer('TrackFitterProducer',
  TTRHBuilder = cms.string('')
)
