import FWCore.ParameterSet.Config as cms

SiStripDB2Tree = cms.EDAnalyzer('SiStripDB2Tree',
  StripQualityLabel = cms.string('MergedBadComponent'),
  isMC = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring
)
