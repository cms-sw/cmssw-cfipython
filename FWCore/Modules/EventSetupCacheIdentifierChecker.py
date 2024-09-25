import FWCore.ParameterSet.Config as cms

def EventSetupCacheIdentifierChecker(*args, **kwargs):
  mod = cms.EDAnalyzer('EventSetupCacheIdentifierChecker',
    allowAnyLabel_ = cms.optional.untracked.vuint32,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
