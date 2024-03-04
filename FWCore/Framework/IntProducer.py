import FWCore.ParameterSet.Config as cms

def IntProducer(**kwargs):
  mod = cms.EDProducer('IntProducer',
    ivalue = cms.required.int32,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
