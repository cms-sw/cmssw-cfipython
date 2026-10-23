import FWCore.ParameterSet.Config as cms

def IntVectorProducer(*args, **kwargs):
  mod = cms.EDProducer('IntVectorProducer',
    ivalue = cms.int32(0),
    count = cms.int32(0),
    delta = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
