import FWCore.ParameterSet.Config as cms

def HLTDiMuonGlbTrkFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTDiMuonGlbTrkFilter',
    saveTags = cms.bool(True),
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
    maxEtaMuon = cms.double(1e+99),
    maxYDimuon = cms.double(1e+99),
    minMass = cms.double(1),
    maxMass = cms.double(1e+99),
    ChargeOpt = cms.int32(0),
    maxDCAMuMu = cms.double(1e+99),
    maxdEtaMuMu = cms.double(1e+99),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
