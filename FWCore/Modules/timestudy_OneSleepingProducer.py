import FWCore.ParameterSet.Config as cms

def timestudy_OneSleepingProducer(**kwargs):
  mod = cms.EDProducer('timestudy::OneSleepingProducer',
    ivalue = cms.required.int32,
    resource = cms.string(''),
    consumes = cms.VInputTag(),
    eventTimes = cms.required.vdouble,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
