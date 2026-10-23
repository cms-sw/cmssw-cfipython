import FWCore.ParameterSet.Config as cms

def HGCALGPUvsCPUComparisonHists(*args, **kwargs):
  mod = cms.EDProducer('HGCALGPUvsCPUComparisonHists',
    monitoredLayerClusters = cms.InputTag('hltMergeLayerClusters'),
    referenceLayerClusters = cms.InputTag('hltMergeLayerClustersSerialSync'),
    topFolderName = cms.string('HLT/HeterogeneousComparisons/HGCalMonitoring'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
