import FWCore.ParameterSet.Config as cms

def SiStripApproximatedClustersDump(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripApproximatedClustersDump',
    approxSiStripClustersTag = cms.InputTag('SiStripClusters2ApproxClusters'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
