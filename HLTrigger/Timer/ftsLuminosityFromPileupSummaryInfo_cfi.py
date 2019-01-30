import FWCore.ParameterSet.Config as cms

ftsLuminosityFromPileupSummaryInfo = cms.EDAnalyzer('FTSLuminosityFromPileupSummaryInfo',
  source = cms.InputTag('addPileupInfo'),
  name = cms.string('pileup'),
  title = cms.string('in-time pileup'),
  label = cms.string('in-time pileup'),
  range = cms.double(40),
  resolution = cms.double(1)
)
