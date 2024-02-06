import FWCore.ParameterSet.Config as cms

HGCalTBAnalyzer = cms.EDAnalyzer('HGCalTBAnalyzer',
  detectorEE = cms.string('HGCalEESensitive'),
  useEE = cms.bool(True),
  zFrontEE = cms.double(0),
  caloHitSrcEE = cms.string('HGCHitsEE'),
  digiSrcEE = cms.InputTag('hgcalDigis', 'EE'),
  recHitSrcEE = cms.InputTag('HGCalRecHit', 'HGCEERecHits'),
  detectorFH = cms.string('HGCalHESiliconSensitive'),
  useFH = cms.bool(False),
  zFrontFH = cms.double(0),
  caloHitSrcFH = cms.string('HGCHitsHEfront'),
  digiSrcFH = cms.InputTag('hgcalDigis', 'HEfront'),
  recHitSrcFH = cms.InputTag('HGCalRecHit', 'HGCHEFRecHits'),
  detectorBH = cms.string('AHCal'),
  useBH = cms.bool(False),
  zFrontBH = cms.double(0),
  caloHitSrcBH = cms.string('HcalHits'),
  digiSrcBH = cms.InputTag('hgcalDigis', 'HEback'),
  recHitSrcBH = cms.InputTag('HGCalRecHit', 'HGCHEBRecHits'),
  detectorBeam = cms.string('HcalTB06BeamDetector'),
  useBeam = cms.bool(False),
  caloHitSrcBeam = cms.string('HcalTB06BeamHits'),
  idBeams = cms.vint32(
    1000,
    1001,
    1002,
    1003,
    1004,
    1005,
    1006,
    1007,
    1008,
    1011,
    1012,
    1013,
    1014,
    2001,
    2002,
    2003,
    2004,
    2005
  ),
  generatorSrc = cms.InputTag('generatorSmeared'),
  passiveEE = cms.InputTag('g4SimHits', 'HGCalEEPassiveHits'),
  passiveFH = cms.InputTag('g4SimHits', 'HGCalHEPassiveHits'),
  passiveBH = cms.InputTag('g4SimHits', 'HGCalAHPassiveHits'),
  passiveCMSE = cms.InputTag('g4SimHits', 'CMSEPassiveHits'),
  passiveBeam = cms.InputTag('g4SimHits', 'HGCalBeamPassiveHits'),
  doSimHits = cms.bool(True),
  doDigis = cms.bool(True),
  doRecHits = cms.bool(True),
  sampleIndex = cms.int32(0),
  doTree = cms.bool(True),
  doTreeCell = cms.bool(True),
  doPassive = cms.bool(False),
  doPassiveEE = cms.bool(False),
  doPassiveHE = cms.bool(False),
  doPassiveBH = cms.bool(False),
  addP = cms.bool(False),
  doBeam = cms.bool(False),
  gev2mip200 = cms.untracked.double(5.7e-05),
  gev2mip300 = cms.untracked.double(8.55e-05),
  stoc_smear_time_200 = cms.untracked.double(10.24),
  stoc_smear_time_300 = cms.untracked.double(15.5),
  maxDepth = cms.untracked.int32(12),
  deltaX = cms.untracked.double(30),
  deltaY = cms.untracked.double(30),
  deltaZ = cms.untracked.double(81),
  zFirst = cms.untracked.double(17.6),
  mightGet = cms.optional.untracked.vstring
)
