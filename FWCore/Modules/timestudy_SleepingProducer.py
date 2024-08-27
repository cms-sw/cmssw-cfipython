import FWCore.ParameterSet.Config as cms

def timestudy_SleepingProducer(**kwargs):
  mod = cms.EDProducer('timestudy::SleepingProducer',
    ivalue = cms.required.int32,
    consumes = cms.VInputTag(),
    eventTimes = cms.required.vdouble,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
