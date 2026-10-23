import FWCore.ParameterSet.Config as cms

def L1TBMTFConverter(*args, **kwargs):
  mod = cms.EDProducer('L1TBMTFConverter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
