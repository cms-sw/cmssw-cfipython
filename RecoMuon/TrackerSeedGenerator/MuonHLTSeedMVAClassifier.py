import FWCore.ParameterSet.Config as cms

def MuonHLTSeedMVAClassifier(**kwargs):
  mod = cms.EDProducer('MuonHLTSeedMVAClassifier',
    src = cms.InputTag('hltIter2IterL3MuonPixelSeeds'),
    L1Muon = cms.InputTag('hltGtStage2Digis', 'Muon'),
    L2Muon = cms.InputTag('hltL2MuonCandidates'),
    rejectAll = cms.bool(False),
    isFromL1 = cms.bool(False),
    mvaFileBL1 = cms.FileInPath('RecoMuon/TrackerSeedGenerator/data/xgb_Run3_Iter2FromL1Seeds_barrel.xml'),
    mvaFileEL1 = cms.FileInPath('RecoMuon/TrackerSeedGenerator/data/xgb_Run3_Iter2FromL1Seeds_endcap.xml'),
    mvaFileBL2 = cms.FileInPath('RecoMuon/TrackerSeedGenerator/data/xgb_Run3_Iter2Seeds_barrel.xml'),
    mvaFileEL2 = cms.FileInPath('RecoMuon/TrackerSeedGenerator/data/xgb_Run3_Iter2Seeds_endcap.xml'),
    mvaScaleMeanBL1 = cms.vdouble(
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ),
    mvaScaleStdBL1 = cms.vdouble(
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1
    ),
    mvaScaleMeanEL1 = cms.vdouble(
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ),
    mvaScaleStdEL1 = cms.vdouble(
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1
    ),
    mvaScaleMeanBL2 = cms.vdouble(
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ),
    mvaScaleStdBL2 = cms.vdouble(
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1
    ),
    mvaScaleMeanEL2 = cms.vdouble(
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ),
    mvaScaleStdEL2 = cms.vdouble(
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1
    ),
    doSort = cms.bool(False),
    nSeedsMaxB = cms.int32(1000000),
    nSeedsMaxE = cms.int32(1000000),
    etaEdge = cms.double(1.2),
    mvaCutB = cms.double(-1),
    mvaCutE = cms.double(-1),
    minL1Qual = cms.int32(7),
    baseScore = cms.double(0.5),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
