import FWCore.ParameterSet.Config as cms

hltMuonTrkFilter = cms.EDFilter('HLTMuonTrkFilter',
  saveTags = cms.bool(False),
  inputMuonCollection = cms.InputTag(''),
  inputCandCollection = cms.InputTag(''),
  minTrkHits = cms.int32(-1),
  minMuonHits = cms.int32(-1),
  minMuonStations = cms.int32(-1),
  maxNormalizedChi2 = cms.double(1e+99),
  allowedTypeMask = cms.uint32(255),
  requiredTypeMask = cms.uint32(0),
  trkMuonId = cms.uint32(0),
  minPt = cms.double(24)
)
