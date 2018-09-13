import FWCore.ParameterSet.Config as cms

HcalTrigTowerGeometryESProducer = cms.ESProducer('HcalTrigTowerGeometryESProducer',
  useFullGranularityHF = cms.bool(False),
  appendToDataLabel = cms.string('')
)
