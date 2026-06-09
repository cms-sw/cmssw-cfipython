import FWCore.ParameterSet.Config as cms

def ESTestESProductResolverProviderJ(*args, **kwargs):
  mod = cms.ESProducer('ESTestESProductResolverProviderJ',
    expectedCacheIds = cms.untracked.vuint32(),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
