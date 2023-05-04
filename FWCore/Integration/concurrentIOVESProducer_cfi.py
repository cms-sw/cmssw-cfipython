import FWCore.ParameterSet.Config as cms

concurrentIOVESProducer = cms.ESProducer('ConcurrentIOVESProducer',
  appendToDataLabel = cms.string('')
)
