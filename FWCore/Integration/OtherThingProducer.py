import FWCore.ParameterSet.Config as cms

def OtherThingProducer(*args, **kwargs):
  mod = cms.EDProducer('OtherThingProducer',
    thingTag = cms.InputTag('Thing'),
    useRefs = cms.untracked.bool(True),
    transient = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
