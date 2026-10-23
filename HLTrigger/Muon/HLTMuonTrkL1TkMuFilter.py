import FWCore.ParameterSet.Config as cms

def HLTMuonTrkL1TkMuFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTMuonTrkL1TkMuFilter',
    saveTags = cms.bool(True),
    inputMuonCollection = cms.InputTag(''),
    inputCandCollection = cms.InputTag(''),
    l1GTAlgoBlockTag = cms.InputTag(''),
    l1GTAlgoNames = cms.vstring(),
    minTrkHits = cms.int32(-1),
    minMuonHits = cms.int32(-1),
    minMuonStations = cms.int32(-1),
    maxNormalizedChi2 = cms.double(1e+99),
    trkMuonId = cms.uint32(0),
    minPt = cms.double(24),
    minN = cms.uint32(1),
    maxAbsEta = cms.double(1e+99),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
