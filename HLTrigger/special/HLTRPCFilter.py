import FWCore.ParameterSet.Config as cms

def HLTRPCFilter(**kwargs):
  mod = cms.EDFilter('HLTRPCFilter',
    rpcRecHits = cms.InputTag('hltRpcRecHits'),
    rpcDTPoints = cms.InputTag('rpcPointProducer', 'RPCDTExtrapolatedPoints'),
    rpcCSCPoints = cms.InputTag('rpcPointProducer', 'RPCCSCExtrapolatedPoints'),
    rangestrips = cms.untracked.double(4),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
