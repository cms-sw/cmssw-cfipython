import FWCore.ParameterSet.Config as cms

def IntOneSharedProducer(**kwargs):
  mod = cms.EDProducer('IntOneSharedProducer',
    ivalue = cms.required.int32,
    resourceNames = cms.untracked.vstring(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
