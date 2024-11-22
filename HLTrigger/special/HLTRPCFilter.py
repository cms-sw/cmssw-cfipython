import FWCore.ParameterSet.Config as cms

def HLTRPCFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTRPCFilter',
    rpcRecHits = cms.InputTag('hltRpcRecHits'),
    rpcDTPoints = cms.InputTag('rpcPointProducer', 'RPCDTExtrapolatedPoints'),
    rpcCSCPoints = cms.InputTag('rpcPointProducer', 'RPCCSCExtrapolatedPoints'),
    rangestrips = cms.untracked.double(4),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
