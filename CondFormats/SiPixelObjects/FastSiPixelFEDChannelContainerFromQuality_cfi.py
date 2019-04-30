import FWCore.ParameterSet.Config as cms

FastSiPixelFEDChannelContainerFromQuality = cms.EDAnalyzer('FastSiPixelFEDChannelContainerFromQuality',
  printDebug = cms.untracked.bool(False),
  removeEmptyPayloads = cms.untracked.bool(False),
  record = cms.string('SiPixelStatusScenariosRcd'),
  condDBQuality = cms.string('frontier://FrontierPrep/CMS_CONDITIONS'),
  qualityTagName = cms.string('SiPixelQualityOffline_2017_threshold1percent_stuckTBM'),
  condDBCabling = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
  cablingMapTagName = cms.string('SiPixelFedCablingMap_v1'),
  startIOV = cms.uint64(1310841198608821),
  endIOV = cms.uint64(1312696624480350),
  output = cms.string('summary.txt'),
  connect = cms.string(''),
  DBParameters = cms.PSet(
    authenticationPath = cms.untracked.string(''),
    authenticationSystem = cms.untracked.int32(0),
    security = cms.untracked.string(''),
    messageLevel = cms.untracked.int32(0)
  )
)
