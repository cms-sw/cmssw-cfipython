import FWCore.ParameterSet.Config as cms

def timestudy_ExternalWorkSleepingProducer(**kwargs):
  mod = cms.EDProducer('timestudy::ExternalWorkSleepingProducer',
    ivalue = cms.required.int32,
    serviceInitTimes = cms.required.vdouble,
    serviceWorkTimes = cms.required.vdouble,
    serviceFinishTimes = cms.required.vdouble,
    consumes = cms.VInputTag(),
    eventTimes = cms.required.vdouble,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
