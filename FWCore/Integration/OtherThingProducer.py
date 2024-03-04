import FWCore.ParameterSet.Config as cms

def OtherThingProducer(**kwargs):
  mod = cms.EDProducer('OtherThingProducer',
    thingTag = cms.InputTag('Thing'),
    useRefs = cms.untracked.bool(True),
    transient = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
