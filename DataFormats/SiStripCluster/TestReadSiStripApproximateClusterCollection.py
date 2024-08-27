import FWCore.ParameterSet.Config as cms

def TestReadSiStripApproximateClusterCollection(**kwargs):
  mod = cms.EDAnalyzer('TestReadSiStripApproximateClusterCollection',
    expectedIntegralValues = cms.required.vuint32,
    collectionTag = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
