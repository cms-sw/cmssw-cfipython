import FWCore.ParameterSet.Config as cms

def RPCandIRPCDigiProducer(**kwargs):
  mod = cms.EDProducer('RPCandIRPCDigiProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
