import FWCore.ParameterSet.Config as cms

def UniqPtrIntVectorProducer(**kwargs):
  mod = cms.EDProducer('UniqPtrIntVectorProducer',
    ivalue = cms.int32(0),
    count = cms.int32(0),
    delta = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
