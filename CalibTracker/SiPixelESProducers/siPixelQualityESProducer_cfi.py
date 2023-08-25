import FWCore.ParameterSet.Config as cms

siPixelQualityESProducer = cms.ESProducer('SiPixelQualityESProducer',
  siPixelQualityFromDbLabel = cms.string(''),
  ListOfRecordToMerge = cms.VPSet(
    cms.PSet(
      record = cms.string('SiPixelQualityFromDbRcd'),
      tag = cms.string('')
    ),
    cms.PSet(
      record = cms.string('SiPixelDetVOffRcd'),
      tag = cms.string('')
    )
  ),
  appendToDataLabel = cms.string('')
)
