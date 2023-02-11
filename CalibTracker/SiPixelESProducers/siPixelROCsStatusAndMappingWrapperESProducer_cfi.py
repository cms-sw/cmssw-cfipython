import FWCore.ParameterSet.Config as cms

siPixelROCsStatusAndMappingWrapperESProducer = cms.ESProducer('SiPixelROCsStatusAndMappingWrapperESProducer',
  ComponentName = cms.string(''),
  CablingMapLabel = cms.string(''),
  UseQualityInfo = cms.bool(False),
  appendToDataLabel = cms.string('')
)
