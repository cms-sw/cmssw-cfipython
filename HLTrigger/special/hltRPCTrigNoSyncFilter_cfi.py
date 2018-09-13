import FWCore.ParameterSet.Config as cms

hltRPCTrigNoSyncFilter = cms.EDFilter('HLTRPCTrigNoSyncFilter',
  saveTags = cms.bool(False),
  GMTInputTag = cms.InputTag('hltGtDigis'),
  rpcRecHits = cms.InputTag('hltRpcRecHits')
)
