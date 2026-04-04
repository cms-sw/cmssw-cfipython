import FWCore.ParameterSet.Config as cms

def L1TCaloLayer1RawToDigi(*args, **kwargs):
  mod = cms.EDProducer('L1TCaloLayer1RawToDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
