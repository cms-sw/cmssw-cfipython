import FWCore.ParameterSet.Config as cms

trackAlgoPriorityOrderDefault = cms.ESProducer('TrackAlgoPriorityOrderESProducer',
  ComponentName = cms.string('trackAlgoPriorityOrder'),
  algoOrder = cms.vstring(),
  appendToDataLabel = cms.string('')
)
