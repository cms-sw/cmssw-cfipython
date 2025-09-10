import FWCore.ParameterSet.Config as cms

def TestWriteHostHitSoA(*args, **kwargs):
  mod = cms.EDProducer('TestWriteHostHitSoA',
    hitSize = cms.uint32(1000),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
