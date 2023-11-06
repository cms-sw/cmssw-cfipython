import FWCore.ParameterSet.Config as cms

cmsalpakatestTestESProducerB = cms.ESProducer('cms::alpakatest::TestESProducerB',
  value = cms.required.int32,
  appendToDataLabel = cms.string('')
)
