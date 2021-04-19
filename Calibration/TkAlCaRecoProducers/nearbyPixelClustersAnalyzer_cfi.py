import FWCore.ParameterSet.Config as cms

nearbyPixelClustersAnalyzer = cms.EDAnalyzer('NearbyPixelClustersAnalyzer',
  clusterCollection = cms.InputTag('ALCARECOSiPixelCalSingleMuonTight'),
  nearByClusterCollection = cms.InputTag('closebyPixelClusters'),
  trajectoryInput = cms.InputTag('refittedTracks'),
  muonTracks = cms.InputTag('ALCARECOSiPixelCalSingleMuonTight'),
  distToTrack = cms.InputTag('trackDistances'),
  skimmedGeometryPath = cms.string('SLHCUpgradeSimulations/Geometry/data/PhaseI/PixelSkimmedGeometry_phase1.txt'),
  mightGet = cms.optional.untracked.vstring
)
