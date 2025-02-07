import FWCore.ParameterSet.Config as cms

def timestudy_SleepingProducer(*args, **kwargs):
  mod = cms.EDProducer('timestudy::SleepingProducer',
    ivalue = cms.required.int32,
    consumes = cms.VInputTag(),
    eventTimes = cms.required.vdouble,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
