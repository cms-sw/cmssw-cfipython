import FWCore.ParameterSet.Config as cms

def TestAlpakaGlobalProducerMoveToDeviceCache_alpaka(*args, **kwargs):
  mod = cms.EDProducer('TestAlpakaGlobalProducerMoveToDeviceCache@alpaka',
    source = cms.InputTag(''),
    x = cms.int32(0),
    y = cms.int32(1),
    z = cms.int32(2),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
