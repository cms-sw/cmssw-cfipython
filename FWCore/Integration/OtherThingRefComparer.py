import FWCore.ParameterSet.Config as cms

def OtherThingRefComparer(**kwargs):
  mod = cms.EDAnalyzer('OtherThingRefComparer',
    first = cms.untracked.InputTag('OtherThing', 'testUserTag'),
    second = cms.untracked.InputTag('OtherThing', 'testUserTag'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
