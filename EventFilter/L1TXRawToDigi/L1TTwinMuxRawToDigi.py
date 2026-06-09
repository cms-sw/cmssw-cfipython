import FWCore.ParameterSet.Config as cms

def L1TTwinMuxRawToDigi(*args, **kwargs):
  mod = cms.EDProducer('L1TTwinMuxRawToDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
