import FWCore.ParameterSet.Config as cms

def SiStripApprox2Clusters(**kwargs):
  mod = cms.EDProducer('SiStripApprox2Clusters',
    inputApproxClusters = cms.InputTag('siStripClusters'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
