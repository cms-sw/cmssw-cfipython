import FWCore.ParameterSet.Config as cms

def CentralityProducer(**kwargs):
  mod = cms.EDProducer('CentralityProducer',
    produceHFhits = cms.bool(True),
    produceHFtowers = cms.bool(True),
    produceEcalhits = cms.bool(True),
    produceZDChits = cms.bool(True),
    produceETmidRapidity = cms.bool(True),
    producePixelhits = cms.bool(True),
    produceTracks = cms.bool(True),
    producePixelTracks = cms.bool(True),
    producePF = cms.bool(True),
    reUseCentrality = cms.bool(False),
    srcHFhits = cms.InputTag('hfreco'),
    srcTowers = cms.InputTag('towerMaker'),
    srcEBhits = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
    srcEEhits = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
    srcZDChits = cms.InputTag('zdcreco'),
    srcPixelhits = cms.InputTag('siPixelRecHits'),
    srcTracks = cms.InputTag('hiGeneralTracks'),
    srcVertex = cms.InputTag('hiSelectedVertex'),
    srcReUse = cms.InputTag('hiCentrality'),
    srcPixelTracks = cms.InputTag('hiPixel3PrimTracks'),
    srcPF = cms.InputTag('particleFlow'),
    doPixelCut = cms.bool(True),
    useQuality = cms.bool(True),
    trackQuality = cms.string('highPurity'),
    trackEtaCut = cms.double(2),
    trackPtCut = cms.double(1),
    hfEtaCut = cms.double(4),
    midRapidityRange = cms.double(1),
    lowGainZDC = cms.bool(True),
    isPhase2 = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
