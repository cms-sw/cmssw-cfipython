import FWCore.ParameterSet.Config as cms

siStripGainPayloadCopyAndExclude = cms.EDAnalyzer('SiStripGainPayloadCopyAndExclude',
  excludedModules = cms.untracked.vuint32(),
  record = cms.untracked.string('SiStripApvGainRcd'),
  gainType = cms.untracked.uint32(1),
  reverseSelection = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring
)
