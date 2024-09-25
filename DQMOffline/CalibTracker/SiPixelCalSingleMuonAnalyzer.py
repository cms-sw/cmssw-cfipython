import FWCore.ParameterSet.Config as cms

def SiPixelCalSingleMuonAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('SiPixelCalSingleMuonAnalyzer',
    clusterCollection = cms.InputTag('ALCARECOSiPixelCalSingleMuonTight'),
    nearByClusterCollection = cms.InputTag('closebyPixelClusters'),
    trajectoryInput = cms.InputTag('refittedTracks'),
    muonTracks = cms.InputTag('ALCARECOSiPixelCalSingleMuonTight'),
    distToTrack = cms.InputTag('trackDistances'),
    dqmPath = cms.string('SiPixelCalSingleMuonTight'),
    skimmedGeometryPath = cms.string('SLHCUpgradeSimulations/Geometry/data/PhaseI/PixelSkimmedGeometry_phase1.txt'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
