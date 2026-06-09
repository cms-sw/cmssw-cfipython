import FWCore.ParameterSet.Config as cms

def IntOneSharedProducer(*args, **kwargs):
  mod = cms.EDProducer('IntOneSharedProducer',
    ivalue = cms.required.int32,
    resourceNames = cms.untracked.vstring(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
