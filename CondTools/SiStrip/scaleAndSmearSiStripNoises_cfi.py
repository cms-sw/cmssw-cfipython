import FWCore.ParameterSet.Config as cms

scaleAndSmearSiStripNoises = cms.EDAnalyzer('SiStripNoisesFromDBMiscalibrator',
  params = cms.VPSet(
    cms.PSet()
  ),
  fillDefaults = cms.untracked.bool(False),
  saveMaps = cms.untracked.bool(True)
)
