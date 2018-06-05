import FWCore.ParameterSet.Config as cms

otherThingAnalyzer = cms.EDAnalyzer('OtherThingAnalyzer',
  thingWasDropped = cms.untracked.bool(False),
  other = cms.untracked.InputTag('OtherThing', 'testUserTag')
)
