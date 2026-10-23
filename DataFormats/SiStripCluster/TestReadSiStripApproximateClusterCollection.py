import FWCore.ParameterSet.Config as cms

def TestReadSiStripApproximateClusterCollection(*args, **kwargs):
  mod = cms.EDAnalyzer('TestReadSiStripApproximateClusterCollection',
    expectedIntegralValues = cms.required.vuint32,
    collectionTag = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
