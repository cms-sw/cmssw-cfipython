import FWCore.ParameterSet.Config as cms

def OtherThingAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('OtherThingAnalyzer',
    thingWasDropped = cms.untracked.bool(False),
    other = cms.untracked.InputTag('OtherThing', 'testUserTag'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
