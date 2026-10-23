import FWCore.ParameterSet.Config as cms

def OtherThingRefComparer(*args, **kwargs):
  mod = cms.EDAnalyzer('OtherThingRefComparer',
    first = cms.untracked.InputTag('OtherThing', 'testUserTag'),
    second = cms.untracked.InputTag('OtherThing', 'testUserTag'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
