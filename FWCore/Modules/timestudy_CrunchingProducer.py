import FWCore.ParameterSet.Config as cms

def timestudy_CrunchingProducer(*args, **kwargs):
  mod = cms.EDProducer('timestudy::CrunchingProducer',
    ivalue = cms.required.int32,
    consumes = cms.VInputTag(),
    eventTimes = cms.required.vdouble,
    useCacheID = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
