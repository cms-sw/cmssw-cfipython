import FWCore.ParameterSet.Config as cms

zdcHardcodeGeometryEP = cms.ESProducer('ZdcHardcodeGeometryEP',
  applyAlignment = cms.bool(False),
  zdcAddRPD = cms.bool(False),
  appendToDataLabel = cms.string('')
)
