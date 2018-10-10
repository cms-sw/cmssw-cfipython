import FWCore.ParameterSet.Config as cms

hltPixlMBFilt = cms.EDFilter('HLTPixlMBFilt',
  saveTags = cms.bool(True),
  pixlTag = cms.InputTag('hltPixelCands'),
  MinPt = cms.double(0),
  MinTrks = cms.uint32(2),
  MinSep = cms.double(1)
)
