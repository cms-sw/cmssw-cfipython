import FWCore.ParameterSet.Config as cms

def SiteLocalConfigService(**kwargs):
  mod = cms.Service('SiteLocalConfigService',
    siteLocalConfigFileUrl = cms.untracked.string(''),
    overrideSourceCacheTempDir = cms.optional.untracked.string,
    overrideSourceCacheMinFree = cms.optional.untracked.double,
    overrideSourceCacheHintDir = cms.optional.untracked.string,
    overrideSourceCloneCacheHintDir = cms.optional.untracked.string,
    overrideSourceReadHint = cms.optional.untracked.string,
    overrideSourceNativeProtocols = cms.optional.untracked.vstring,
    overrideSourceTTreeCacheSize = cms.optional.untracked.uint32,
    overrideSourceTimeout = cms.optional.untracked.uint32,
    debugLevel = cms.optional.untracked.uint32,
    overridePrefetching = cms.optional.untracked.bool,
    overrideStatisticsDestination = cms.optional.untracked.string,
    overrideStatisticsInfo = cms.optional.untracked.vstring,
    overrideUseLocalConnectString = cms.optional.untracked.bool,
    overrideLocalConnectPrefix = cms.optional.untracked.string,
    overrideLocalConnectSuffix = cms.optional.untracked.string
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
