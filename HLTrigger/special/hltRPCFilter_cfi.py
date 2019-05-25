import FWCore.ParameterSet.Config as cms

hltRPCFilter = cms.EDFilter('HLTRPCFilter',
  rpcRecHits = cms.InputTag('hltRpcRecHits'),
  rpcDTPoints = cms.InputTag('rpcPointProducer', 'RPCDTExtrapolatedPoints'),
  rpcCSCPoints = cms.InputTag('rpcPointProducer', 'RPCCSCExtrapolatedPoints'),
  rangestrips = cms.untracked.double(4)
)
