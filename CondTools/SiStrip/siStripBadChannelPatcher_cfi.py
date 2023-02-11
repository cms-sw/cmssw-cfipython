import FWCore.ParameterSet.Config as cms

siStripBadChannelPatcher = cms.EDAnalyzer('SiStripBadChannelPatcher',
  Record = cms.string('SiStripBadStrip'),
  printDebug = cms.bool(False),
  detIdsToExclude = cms.vuint32(),
  detIdsToInclude = cms.vuint32(),
  FEDsToExclude = cms.vuint32(),
  FEDsToInclude = cms.vuint32(),
  mightGet = cms.optional.untracked.vstring
)
