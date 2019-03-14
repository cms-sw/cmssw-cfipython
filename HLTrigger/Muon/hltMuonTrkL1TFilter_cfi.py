import FWCore.ParameterSet.Config as cms

hltMuonTrkL1TFilter = cms.EDFilter('HLTMuonTrkL1TFilter',
  saveTags = cms.bool(True),
  inputMuonCollection = cms.InputTag(''),
  inputCandCollection = cms.InputTag(''),
  previousCandTag = cms.InputTag(''),
  minTrkHits = cms.int32(-1),
  minMuonHits = cms.int32(-1),
  minMuonStations = cms.int32(-1),
  maxNormalizedChi2 = cms.double(1e+99),
  allowedTypeMask = cms.uint32(255),
  requiredTypeMask = cms.uint32(0),
  trkMuonId = cms.uint32(0),
  minPt = cms.double(24),
  minN = cms.uint32(1),
  maxAbsEta = cms.double(1e+99)
)
