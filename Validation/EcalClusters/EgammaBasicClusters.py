import FWCore.ParameterSet.Config as cms

def EgammaBasicClusters(*args, **kwargs):
  mod = cms.EDProducer('EgammaBasicClusters',
    barrelBasicClusterCollection = cms.InputTag('hybridSuperClusters', 'hybridBarrelBasicClusters'),
    enableEndcaps = cms.bool(True),
    endcapBasicClusterCollection = cms.InputTag('multi5x5SuperClusters', 'multi5x5EndcapBasicClusters'),
    hist_bins_Size = cms.int32(20),
    hist_min_Size = cms.double(0),
    hist_max_Size = cms.double(20),
    hist_bins_Phi = cms.int32(181),
    hist_min_Phi = cms.double(-3.14159),
    hist_max_Phi = cms.double(3.14159),
    hist_bins_Eta = cms.int32(91),
    hist_min_Eta = cms.double(-2.5),
    hist_max_Eta = cms.double(2.5),
    hist_bins_ET = cms.int32(200),
    hist_min_ET = cms.double(0),
    hist_max_ET = cms.double(200),
    hist_bins_NumRecHits = cms.int32(50),
    hist_min_NumRecHits = cms.double(0),
    hist_max_NumRecHits = cms.double(50),
    hist_bins_R = cms.int32(55),
    hist_min_R = cms.double(0),
    hist_max_R = cms.double(175),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
