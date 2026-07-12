import FWCore.ParameterSet.Config as cms

def TruthLogicalGraphHitIndexProducer(*args, **kwargs):
  mod = cms.EDProducer('TruthLogicalGraphHitIndexProducer',
    src = cms.InputTag('truthLogicalGraphProducer'),
    rawSrc = cms.InputTag('truthGraphProducer'),
    recHitMap = cms.InputTag('detIdToRecHitMapProducer'),
    subdetectors = cms.vstring(
      'HGCalCalo',
      'Tracker',
      'MTD',
      'Muon'
    ),
    simHitCollections = cms.VInputTag(
      'g4SimHits:HGCHitsEE',
      'g4SimHits:HGCHitsHEfront',
      'g4SimHits:HGCHitsHEback'
    ),
    trackerSimHitCollections = cms.VInputTag(
      'g4SimHits:TrackerHitsPixelBarrelLowTof',
      'g4SimHits:TrackerHitsPixelBarrelHighTof',
      'g4SimHits:TrackerHitsPixelEndcapLowTof',
      'g4SimHits:TrackerHitsPixelEndcapHighTof',
      'g4SimHits:TrackerHitsTIBLowTof',
      'g4SimHits:TrackerHitsTIBHighTof',
      'g4SimHits:TrackerHitsTIDLowTof',
      'g4SimHits:TrackerHitsTIDHighTof',
      'g4SimHits:TrackerHitsTOBLowTof',
      'g4SimHits:TrackerHitsTOBHighTof',
      'g4SimHits:TrackerHitsTECLowTof',
      'g4SimHits:TrackerHitsTECHighTof'
    ),
    muonSimHitCollections = cms.VInputTag(
      'g4SimHits:MuonDTHits',
      'g4SimHits:MuonCSCHits',
      'g4SimHits:MuonRPCHits',
      'g4SimHits:MuonGEMHits',
      'g4SimHits:MuonME0Hits'
    ),
    doHGCalRelabelling = cms.bool(True),
    mtdSimLayerClusters = cms.InputTag('mix', 'MergedMtdTruthLC'),
    mtdRecoClusterAssociation = cms.InputTag('mtdRecoClusterToSimLayerClusterAssociation'),
    mtdBarrelClusters = cms.InputTag('mtdClusters', 'FTLBarrel'),
    mtdEndcapClusters = cms.InputTag('mtdClusters', 'FTLEndcap'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
