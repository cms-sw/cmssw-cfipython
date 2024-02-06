import FWCore.ParameterSet.Config as cms

hgcalWaferStudy = cms.EDAnalyzer('HGCalWaferStudy',
  detectorNames = cms.vstring(
    'HGCalEESensitive',
    'HGCalHESiliconSensitive'
  ),
  caloHitSources = cms.vstring(
    'HGCHitsEE',
    'HGCHitsHEfront'
  ),
  digiSources = cms.VInputTag(
    'simHGCalUnsuppressedDigis:EE',
    'simHGCalUnsuppressedDigis:HEfront'
  ),
  verbosity = cms.untracked.int32(0),
  nBinHit = cms.untracked.int32(600),
  nBinDig = cms.untracked.int32(600),
  xyMinHit = cms.untracked.double(-3000),
  xyMaxHit = cms.untracked.double(3000),
  xyMinDig = cms.untracked.double(-300),
  xyMaxDig = cms.untracked.double(300),
  ifNose = cms.untracked.bool(False),
  layerMaxSim = cms.untracked.vint32(
    28,
    24
  ),
  layerMaxDig = cms.untracked.vint32(
    28,
    24
  ),
  layerMinSim = cms.untracked.vint32(
    1,
    1
  ),
  layerMinDig = cms.untracked.vint32(
    1,
    1
  ),
  mightGet = cms.optional.untracked.vstring
)
