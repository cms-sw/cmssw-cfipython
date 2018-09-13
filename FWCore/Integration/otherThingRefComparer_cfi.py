import FWCore.ParameterSet.Config as cms

otherThingRefComparer = cms.EDAnalyzer('OtherThingRefComparer',
  first = cms.untracked.InputTag('OtherThing', 'testUserTag'),
  second = cms.untracked.InputTag('OtherThing', 'testUserTag')
)
