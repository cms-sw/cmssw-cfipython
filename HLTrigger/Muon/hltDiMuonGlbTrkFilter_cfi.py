import FWCore.ParameterSet.Config as cms

hltDiMuonGlbTrkFilter = cms.EDFilter('HLTDiMuonGlbTrkFilter',
  inputMuonCollection = cms.InputTag(''),
  inputCandCollection = cms.InputTag(''),
  minTrkHits = cms.int32(-1),
  minMuonHits = cms.int32(-1),
  maxNormalizedChi2 = cms.double(1e+99),
  minDR = cms.double(0.1),
  allowedTypeMask = cms.uint32(255),
  requiredTypeMask = cms.uint32(0),
  trkMuonId = cms.uint32(0),
  minPtMuon1 = cms.double(17),
  minPtMuon2 = cms.double(8),
  minMass = cms.double(1),
  saveTags = cms.bool(True)
)
