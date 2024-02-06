import FWCore.ParameterSet.Config as cms

cmsalpakatestTestESProducerC = cms.ESProducer('cms::alpakatest::TestESProducerC',
  value = cms.required.int32,
  appendToDataLabel = cms.string('')
)
