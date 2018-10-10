import FWCore.ParameterSet.Config as cms

rpcChamberMasker = cms.EDProducer('RPCChamberMasker',
  digiTag = cms.InputTag('preRPCDigis'),
  descopeRE31 = cms.bool(False),
  descopeRE41 = cms.bool(False)
)
