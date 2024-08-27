import FWCore.ParameterSet.Config as cms

def OtherThingAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('OtherThingAnalyzer',
    thingWasDropped = cms.untracked.bool(False),
    other = cms.untracked.InputTag('OtherThing', 'testUserTag'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
