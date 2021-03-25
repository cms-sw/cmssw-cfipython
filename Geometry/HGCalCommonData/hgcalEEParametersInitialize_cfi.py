import FWCore.ParameterSet.Config as cms

hgcalEEParametersInitialize = cms.ESProducer('HGCalParametersESModule',
  name = cms.string('HGCalEESensitive'),
  name2 = cms.string('HGCalEE'),
  nameW = cms.string('HGCalEEWafer'),
  nameC = cms.string('HGCalEECell'),
  nameT = cms.string('HGCal'),
  nameX = cms.string('HGCalEESensitive'),
  fromDD4Hep = cms.bool(False),
  appendToDataLabel = cms.string('')
)
