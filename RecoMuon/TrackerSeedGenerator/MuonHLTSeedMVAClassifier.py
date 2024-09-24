import FWCore.ParameterSet.Config as cms

def MuonHLTSeedMVAClassifier(*args, **kwargs):
  mod = cms.EDProducer('MuonHLTSeedMVAClassifier',
    src = cms.InputTag('hltIter2IterL3MuonPixelSeeds'),
    L1Muon = cms.InputTag('hltGtStage2Digis', 'Muon'),
    L2Muon = cms.InputTag('hltL2MuonCandidates'),
    rejectAll = cms.bool(False),
    isFromL1 = cms.bool(False),
    mvaFileB = cms.FileInPath('RecoMuon/TrackerSeedGenerator/data/xgb_Run3_Iter2FromL1Seeds_barrel.xml'),
    mvaFileE = cms.FileInPath('RecoMuon/TrackerSeedGenerator/data/xgb_Run3_Iter2FromL1Seeds_endcap.xml'),
    mvaScaleMeanB = cms.vdouble(
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ),
    mvaScaleStdB = cms.vdouble(
      1,
      1,
      1,
      1,
      1,
      1,
      1,
      1
    ),
    mvaScaleMeanE = cms.vdouble(
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ),
    mvaScaleStdE = cms.vdouble(
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
