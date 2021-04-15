import FWCore.ParameterSet.Config as cms

SiStripClusterizerConditionsESProducer = cms.ESProducer('SiStripClusterizerConditionsESProducer',
  QualityLabel = cms.string(''),
  Label = cms.string(''),
  appendToDataLabel = cms.string('')
)
