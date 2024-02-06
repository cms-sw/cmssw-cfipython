import FWCore.ParameterSet.Config as cms

hgcalTBEEParametersInitialize = cms.ESProducer('HGCalTBParametersESModule',
  name = cms.string('HGCalEESensitive'),
  name2 = cms.string('HGCalEE'),
  nameW = cms.string('HGCalEEWafer'),
  nameC = cms.string('HGCalEECell'),
  nameT = cms.string('HGCal'),
  nameX = cms.string('HGCalEESensitive'),
  fromDD4hep = cms.bool(False),
  appendToDataLabel = cms.string('')
)
