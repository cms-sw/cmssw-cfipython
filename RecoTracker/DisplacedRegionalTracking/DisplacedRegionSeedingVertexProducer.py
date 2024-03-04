import FWCore.ParameterSet.Config as cms

def DisplacedRegionSeedingVertexProducer(**kwargs):
  mod = cms.EDProducer('DisplacedRegionSeedingVertexProducer',
    rParam = cms.double(1),
    minRadius = cms.double(-1),
    nearThreshold = cms.double(9999),
    farThreshold = cms.double(-1),
    discriminatorCut = cms.double(-1),
    input_names = cms.vstring(
      'phi_0',
      'phi_1'
    ),
    output_names = cms.vstring('model_5/activation_10/Softmax'),
    nThreads = cms.untracked.uint32(1),
    graph_path = cms.FileInPath('RecoTracker/DisplacedRegionalTracking/data/FullData_Phi-64-128-256_16-32-64_F-128-64-32_Model.pb'),
    beamSpot = cms.InputTag('offlineBeamSpot'),
    trackClusters = cms.InputTag('generalV0Candidates', 'Kshort'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
