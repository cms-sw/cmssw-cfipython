import FWCore.ParameterSet.Config as cms

def ESTestESProductResolverProviderJ(**kwargs):
  mod = cms.ESProducer('ESTestESProductResolverProviderJ',
    expectedCacheIds = cms.untracked.vuint32(),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
