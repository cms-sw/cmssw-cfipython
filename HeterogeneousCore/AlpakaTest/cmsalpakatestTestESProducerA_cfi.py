import FWCore.ParameterSet.Config as cms

cmsalpakatestTestESProducerA = cms.ESProducer('cms::alpakatest::TestESProducerA',
  value = cms.required.int32,
  appendToDataLabel = cms.string('')
)
