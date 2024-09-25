import FWCore.ParameterSet.Config as cms

def RPCDataCertification(*args, **kwargs):
  mod = cms.EDProducer('RPCDataCertification',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
