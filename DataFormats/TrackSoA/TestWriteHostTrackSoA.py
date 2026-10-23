import FWCore.ParameterSet.Config as cms

def TestWriteHostTrackSoA(*args, **kwargs):
  mod = cms.EDProducer('TestWriteHostTrackSoA',
    trackSize = cms.uint32(1000),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
