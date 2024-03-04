import FWCore.ParameterSet.Config as cms

def EventSetupCacheIdentifierChecker(**kwargs):
  mod = cms.EDAnalyzer('EventSetupCacheIdentifierChecker',
    allowAnyLabel_ = cms.optional.untracked.vuint32,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
