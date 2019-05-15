import FWCore.ParameterSet.Config as cms

thingAnalyzer = cms.EDAnalyzer('edmtest::ThingAnalyzer',
  beginRun = cms.untracked.InputTag('thing', 'beginRun'),
  beginLumi = cms.untracked.InputTag('thing', 'beginLumi'),
  event = cms.untracked.InputTag('thing'),
  endLumi = cms.untracked.InputTag('thing', 'endLumi'),
  endRun = cms.untracked.InputTag('thing', 'endRun')
)
