import FWCore.ParameterSet.Config as cms

TrackerAdditionalParametersPerDet = cms.ESProducer('TrackerAdditionalParametersPerDetESModule',
  appendToDataLabel = cms.string('')
)
