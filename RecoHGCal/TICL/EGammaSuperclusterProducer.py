import FWCore.ParameterSet.Config as cms

def EGammaSuperclusterProducer(**kwargs):
  mod = cms.EDProducer('EGammaSuperclusterProducer',
    ticlSuperClusters = cms.InputTag('ticlTracksterLinksSuperclusteringDNN'),
    ticlTrackstersEM = cms.InputTag('ticlTrackstersCLUE3DHigh'),
    layerClusters = cms.InputTag('hgcalMergeLayerClusters'),
    superclusterEtThreshold = cms.double(4),
    enableRegression = cms.bool(True),
    regressionModelPath = cms.FileInPath('RecoHGCal/TICL/data/superclustering/regression_v1.onnx'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
