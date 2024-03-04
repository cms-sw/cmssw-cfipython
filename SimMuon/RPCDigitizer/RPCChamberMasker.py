import FWCore.ParameterSet.Config as cms

def RPCChamberMasker(**kwargs):
  mod = cms.EDProducer('RPCChamberMasker',
    digiTag = cms.InputTag('preRPCDigis'),
    descopeRE31 = cms.bool(False),
    descopeRE41 = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
