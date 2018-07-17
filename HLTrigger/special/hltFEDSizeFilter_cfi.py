import FWCore.ParameterSet.Config as cms

hltFEDSizeFilter = cms.EDFilter('HLTFEDSizeFilter',
  saveTags = cms.bool(True),
  rawData = cms.InputTag('source'),
  threshold = cms.uint32(0),
  firstFED = cms.uint32(0),
  lastFED = cms.uint32(39),
  requireAllFEDs = cms.bool(False)
)
