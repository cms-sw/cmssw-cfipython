import FWCore.ParameterSet.Config as cms

def SiStripApproximatedClustersDump(**kwargs):
  mod = cms.EDAnalyzer('SiStripApproximatedClustersDump',
    approxSiStripClustersTag = cms.InputTag('SiStripClusters2ApproxClusters'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
