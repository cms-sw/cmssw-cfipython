import FWCore.ParameterSet.Config as cms

def TestPortableProducerCPU(**kwargs):
  mod = cms.EDProducer('TestPortableProducerCPU',
    size = cms.required.int32,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
