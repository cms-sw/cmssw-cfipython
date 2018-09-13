import FWCore.ParameterSet.Config as cms

saver = cms.EDAnalyzer('DQMFileSaverPB',
  fakeFilterUnitMode = cms.untracked.bool(False),
  streamLabel = cms.untracked.string('streamDQMHistograms'),
  tag = cms.untracked.string('UNKNOWN'),
  producer = cms.untracked.string('DQM'),
  referenceHandling = cms.untracked.string('all'),
  referenceRequireStatus = cms.untracked.int32(100),
  path = cms.untracked.string('./')
)
