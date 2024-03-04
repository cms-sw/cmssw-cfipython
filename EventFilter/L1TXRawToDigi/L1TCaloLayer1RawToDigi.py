import FWCore.ParameterSet.Config as cms

def L1TCaloLayer1RawToDigi(**kwargs):
  mod = cms.EDProducer('L1TCaloLayer1RawToDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
