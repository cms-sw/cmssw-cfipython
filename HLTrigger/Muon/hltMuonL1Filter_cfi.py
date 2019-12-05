import FWCore.ParameterSet.Config as cms

hltMuonL1Filter = cms.EDFilter('HLTMuonL1Filter',
  CandTag = cms.InputTag('hltL1extraParticles'),
  PreviousCandTag = cms.InputTag(''),
  MaxEta = cms.double(2.5),
  MinPt = cms.double(0),
  MinN = cms.int32(1),
  ExcludeSingleSegmentCSC = cms.bool(False),
  CSCTFtag = cms.InputTag('csctfDigis'),
  saveTags = cms.bool(False),
  SelectQualities = cms.vint32()
)
