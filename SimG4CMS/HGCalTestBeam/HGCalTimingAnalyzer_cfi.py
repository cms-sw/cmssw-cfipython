import FWCore.ParameterSet.Config as cms

HGCalTimingAnalyzer = cms.EDAnalyzer('HGCalTimingAnalyzer',
  DetectorEE = cms.string('HGCalEESensitive'),
  DetectorBeam = cms.string('HcalTB06BeamDetector'),
  GroupHits = cms.bool(False),
  TimeUnit = cms.double(0.001),
  IDBeams = cms.vint32(
    1001,
    1002,
    1003,
    1004,
    1005
  ),
  DoTree = cms.untracked.bool(True),
  GeneratorSrc = cms.InputTag('generatorSmeared'),
  CaloHitSrcEE = cms.string('HGCHitsEE'),
  CaloHitSrcBeam = cms.string('HcalTB06BeamHits')
)
