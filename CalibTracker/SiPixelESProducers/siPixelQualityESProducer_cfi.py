import FWCore.ParameterSet.Config as cms

siPixelQualityESProducer = cms.ESProducer('SiPixelQualityESProducer',
  siPixelQualityLabel = cms.string(''),
  siPixelQualityLabel_RawToDigi = cms.string(''),
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
