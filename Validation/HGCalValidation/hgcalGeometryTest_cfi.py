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
  Verbosity = cms.untracked.int32(0)
)
