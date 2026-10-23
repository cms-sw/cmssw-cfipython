import FWCore.ParameterSet.Config as cms

def SiteLocalConfigServiceTester(*args, **kwargs):
  mod = cms.EDAnalyzer('SiteLocalConfigServiceTester',
    sourceCacheHint = cms.required.untracked.string,
    sourceReadHint = cms.required.untracked.string,
    sourceTempDir = cms.required.untracked.string,
    sourceTTreeCacheSize = cms.required.untracked.uint32,
    sourceNativeProtocols = cms.required.untracked.vstring,
    sourceValuesSet = cms.untracked.bool(True),
    expectedUseLocalConnectString = cms.required.untracked.bool,
    expectedLocalConnectPrefix = cms.required.untracked.string,
    expectedLocalConnectSuffix = cms.required.untracked.string,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
