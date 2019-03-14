import FWCore.ParameterSet.Config as cms

hltCSCOverlapFilter = cms.EDFilter('HLTCSCOverlapFilter',
  saveTags = cms.bool(True),
  input = cms.InputTag('hltCsc2DRecHits'),
  minHits = cms.uint32(4),
  xWindow = cms.double(1000),
  yWindow = cms.double(1000),
  ring1 = cms.bool(True),
  ring2 = cms.bool(False),
  fillHists = cms.bool(False)
)
