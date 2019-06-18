import FWCore.ParameterSet.Config as cms

scaleAndSmearSiStripGains = cms.EDAnalyzer('SiStripChannelGainFromDBMiscalibrator',
  params = cms.VPSet(
    cms.PSet()
  ),
  record = cms.untracked.string('SiStripApvGainRcd'),
  gainType = cms.untracked.uint32(1),
  saveMaps = cms.untracked.bool(True),
  mightGet = cms.optional.untracked.vstring
)
