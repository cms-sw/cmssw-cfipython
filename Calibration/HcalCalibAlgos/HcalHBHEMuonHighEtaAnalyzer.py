import FWCore.ParameterSet.Config as cms

def HcalHBHEMuonHighEtaAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HcalHBHEMuonHighEtaAnalyzer',
    labelEBRecHit = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
    labelEERecHit = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
    labelHBHERecHit = cms.InputTag('hbhereco'),
    labelVertex = cms.string('offlinePrimaryVertices'),
    labelMuon = cms.string('muons'),
    labelTrack = cms.string('generalTracks'),
    etaMin = cms.double(2),
    emaxNearPThreshold = cms.double(10),
    analyzeMuon = cms.bool(True),
    unCorrect = cms.bool(True),
    collapseDepth = cms.bool(False),
    isItPlan1 = cms.bool(False),
    getCharge = cms.bool(True),
    useRaw = cms.int32(0),
    verbosity = cms.int32(0),
    fileInCorr = cms.untracked.string(''),
    trackQuality = cms.untracked.string('highPurity'),
    minTrackPt = cms.untracked.double(1),
    maxDxyPV = cms.untracked.double(0.02),
    maxDzPV = cms.untracked.double(100),
    maxChi2 = cms.untracked.double(5),
    maxDpOverP = cms.untracked.double(0.1),
    ignoreHECorr = cms.untracked.bool(False),
    isItPreRecHit = cms.untracked.bool(False),
    writeRespCorr = cms.untracked.bool(False),
    maxDepth = cms.untracked.int32(7),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
