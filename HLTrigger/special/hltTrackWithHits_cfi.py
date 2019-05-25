import FWCore.ParameterSet.Config as cms

hltTrackWithHits = cms.EDFilter('HLTTrackWithHits',
  saveTags = cms.bool(True),
  src = cms.InputTag(''),
  MinN = cms.int32(0),
  MaxN = cms.int32(99999),
  MinBPX = cms.int32(0),
  MinFPX = cms.int32(0),
  MinPXL = cms.int32(0),
  MinPT = cms.double(0)
)
