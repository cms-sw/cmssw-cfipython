import FWCore.ParameterSet.Config as cms

hgcalRecHitStudyEE = cms.EDAnalyzer('HGCalRecHitStudy',
  detectorName = cms.string('HGCalEESensitive'),
  source = cms.InputTag('HGCalRecHit', 'HGCEERecHits'),
  ifNose = cms.untracked.bool(False),
  ifLayer = cms.untracked.bool(False),
  verbosity = cms.untracked.int32(0),
  nBinR = cms.untracked.int32(300),
  nBinZ = cms.untracked.int32(300),
  nBinEta = cms.untracked.int32(200),
  layers = cms.untracked.int32(28),
  rMin = cms.untracked.double(0),
  rMax = cms.untracked.double(300),
  zMin = cms.untracked.double(300),
  zMax = cms.untracked.double(600),
  etaMin = cms.untracked.double(1),
  etaMax = cms.untracked.double(3),
  mightGet = cms.optional.untracked.vstring
)
