import FWCore.ParameterSet.Config as cms

def HLTRPCTrigNoSyncFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTRPCTrigNoSyncFilter',
    saveTags = cms.bool(True),
    GMTInputTag = cms.InputTag('hltGtDigis'),
    rpcRecHits = cms.InputTag('hltRpcRecHits'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
