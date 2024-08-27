import FWCore.ParameterSet.Config as cms

def L1TTwinMuxRawToDigi(**kwargs):
  mod = cms.EDProducer('L1TTwinMuxRawToDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
