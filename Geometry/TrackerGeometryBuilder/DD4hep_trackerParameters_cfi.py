import FWCore.ParameterSet.Config as cms

DD4hep_trackerParameters = cms.ESProducer('TrackerParametersESProducer',
  appendToDataLabel = cms.string('')
)
