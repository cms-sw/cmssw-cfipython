import FWCore.ParameterSet.Config as cms

totemGeometryESModule = cms.ESProducer('TotemGeometryESModule',
  useDDL = cms.bool(True),
  useDD4hep = cms.bool(False),
  appendToDataLabel = cms.string('')
)
