import FWCore.ParameterSet.Config as cms

def TruthLogicalGraphHitIndexProducer(*args, **kwargs):
  mod = cms.EDProducer('TruthLogicalGraphHitIndexProducer',
    src = cms.InputTag('truthLogicalGraphProducer'),
    rawSrc = cms.InputTag('truthGraphProducer'),
    recHitMap = cms.InputTag('detIdToRecHitMapProducer'),
    subdetectors = cms.vstring(
      'Calo',
      'Tracker',
      'MTD',
      'Muon'
    ),
    simHitCollections = cms.VInputTag(
      'g4SimHits:HGCHitsEE',
      'g4SimHits:HGCHitsHEfront',
      'g4SimHits:HGCHitsHEback',
      'g4SimHits:EcalHitsEB',
      'g4SimHits:HcalHits'
    ),
    trackerDigiSimLinks = cms.VInputTag(
      'simSiPixelDigis:Pixel',
      'simSiPixelDigis:Tracker'
    ),
    muonSimHitCollections = cms.VInputTag(
      'g4SimHits:MuonDTHits',
      'g4SimHits:MuonCSCHits',
      'g4SimHits:MuonRPCHits',
      'g4SimHits:MuonGEMHits',
      'g4SimHits:MuonME0Hits'
    ),
    doHcalRelabelling = cms.bool(True),
    sharedSubgraphStore = cms.bool(True),
    mtdSimLayerClusters = cms.InputTag('mix', 'MergedMtdTruthLC'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
