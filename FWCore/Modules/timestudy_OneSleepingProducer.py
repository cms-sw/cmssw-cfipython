import FWCore.ParameterSet.Config as cms

def timestudy_OneSleepingProducer(*args, **kwargs):
  mod = cms.EDProducer('timestudy::OneSleepingProducer',
    ivalue = cms.required.int32,
    resource = cms.string(''),
    consumes = cms.VInputTag(),
    eventTimes = cms.required.vdouble,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
