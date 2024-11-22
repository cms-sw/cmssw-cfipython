import FWCore.ParameterSet.Config as cms

def timestudy_ExternalWorkSleepingProducer(*args, **kwargs):
  mod = cms.EDProducer('timestudy::ExternalWorkSleepingProducer',
    ivalue = cms.required.int32,
    serviceInitTimes = cms.required.vdouble,
    serviceWorkTimes = cms.required.vdouble,
    serviceFinishTimes = cms.required.vdouble,
    consumes = cms.VInputTag(),
    eventTimes = cms.required.vdouble,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
