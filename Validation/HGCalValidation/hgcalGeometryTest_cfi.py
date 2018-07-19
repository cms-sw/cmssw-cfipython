import FWCore.ParameterSet.Config as cms

hgcalGeometryTest = cms.EDAnalyzer('HGCGeometryTest',
  DetectorNames = cms.vstring(
    'HGCalEESensitive',
    'HGCalHESiliconSensitive',
    'HGCalHEScintillatorSensitive'
  ),
  CaloHitSources = cms.vstring(
    'HGCHitsEE',
    'HGCHitsHEfront',
    'HGCHitsHEback'
  ),
  RMin = cms.untracked.double(0),
  RMax = cms.untracked.double(3000),
  ZMin = cms.untracked.double(3000),
  ZMax = cms.untracked.double(6000),
  NBinR = cms.untracked.int32(300),
  NBinZ = cms.untracked.int32(300),
  Verbosity = cms.untracked.int32(0),
  IfNose = cms.untracked.bool(False)
)
