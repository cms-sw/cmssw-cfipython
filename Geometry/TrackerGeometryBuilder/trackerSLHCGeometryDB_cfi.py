import FWCore.ParameterSet.Config as cms

trackerSLHCGeometryDB = cms.ESProducer('TrackerDigiGeometryESModule',
  appendToDataLabel = cms.string(''),
  fromDDD = cms.bool(False),
  applyAlignment = cms.bool(True),
  alignmentsLabel = cms.string(''),
  trackerGeometryConstants = cms.PSet(
    upgradeGeometry = cms.bool(True),
    ROWS_PER_ROC = cms.int32(80),
    COLS_PER_ROC = cms.int32(52),
    BIG_PIX_PER_ROC_X = cms.int32(0),
    BIG_PIX_PER_ROC_Y = cms.int32(0),
    ROCS_X = cms.int32(2),
    ROCS_Y = cms.int32(8)
  )
)
