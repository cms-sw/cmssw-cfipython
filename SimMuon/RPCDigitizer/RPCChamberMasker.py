import FWCore.ParameterSet.Config as cms

def RPCChamberMasker(*args, **kwargs):
  mod = cms.EDProducer('RPCChamberMasker',
    digiTag = cms.InputTag('preRPCDigis'),
    descopeRE31 = cms.bool(False),
    descopeRE41 = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
