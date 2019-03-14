import FWCore.ParameterSet.Config as cms

hltPixlMBForAlignmentFilter = cms.EDFilter('HLTPixlMBForAlignmentFilter',
  saveTags = cms.bool(True),
  pixlTag = cms.InputTag('hltPixelCands'),
  MinPt = cms.double(5),
  MinTrks = cms.uint32(2),
  MinSep = cms.double(1),
  MinIsol = cms.double(0.05)
)
