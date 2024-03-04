import FWCore.ParameterSet.Config as cms

def TestWriteVectorDetId(**kwargs):
  mod = cms.EDProducer('TestWriteVectorDetId',
    testValue = cms.required.uint32,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
