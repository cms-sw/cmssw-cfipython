import FWCore.ParameterSet.Config as cms

def TestWriteVectorDetId(*args, **kwargs):
  mod = cms.EDProducer('TestWriteVectorDetId',
    testValue = cms.required.uint32,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
