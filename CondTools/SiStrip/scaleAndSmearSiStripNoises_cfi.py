import FWCore.ParameterSet.Config as cms

scaleAndSmearSiStripNoises = cms.EDAnalyzer('SiStripNoisesFromDBMiscalibrator',
  params = cms.VPSet(
    cms.PSet()
  ),
  printDebug = cms.untracked.uint32(1),
  fillDefaults = cms.untracked.bool(False),
  saveMaps = cms.untracked.bool(True),
  mightGet = cms.optional.untracked.vstring
)
