import FWCore.ParameterSet.Config as cms

def HLTRPCTrigNoSyncFilter(**kwargs):
  mod = cms.EDFilter('HLTRPCTrigNoSyncFilter',
    saveTags = cms.bool(True),
    GMTInputTag = cms.InputTag('hltGtDigis'),
    rpcRecHits = cms.InputTag('hltRpcRecHits'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
