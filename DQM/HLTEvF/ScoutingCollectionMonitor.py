import FWCore.ParameterSet.Config as cms

def ScoutingCollectionMonitor(*args, **kwargs):
  mod = cms.EDProducer('ScoutingCollectionMonitor',
    onlyScouting = cms.bool(False),
    electrons = cms.InputTag('hltScoutingEgammaPacker'),
    muons = cms.InputTag('hltScoutingMuonPackerNoVtx'),
    muonsVtx = cms.InputTag('hltScoutingMuonPackerVtx'),
    pfcands = cms.InputTag('hltScoutingPFPacker'),
    photons = cms.InputTag('hltScoutingEgammaPacker'),
    pfjets = cms.InputTag('hltScoutingPFPacker'),
    tracks = cms.InputTag('hltScoutingTrackPacker'),
    displacedVertices = cms.InputTag('hltScoutingMuonPackerVtx', 'displacedVtx'),
    displacedVerticesNoVtx = cms.InputTag('hltScoutingMuonPackerNoVtx', 'displacedVtx'),
    primaryVertices = cms.InputTag('hltScoutingPrimaryVertexPacker', 'primaryVtx'),
    pfMetPt = cms.InputTag('hltScoutingPFPacker', 'pfMetPt'),
    pfMetPhi = cms.InputTag('hltScoutingPFPacker', 'pfMetPhi'),
    rho = cms.InputTag('hltScoutingPFPacker', 'rho'),
    onlineMetaDataDigis = cms.InputTag('onlineMetaDataDigis'),
    pfRecHitsEB = cms.InputTag('hltScoutingRecHitPacker', 'EB'),
    pfRecHitsEE = cms.InputTag('hltScoutingRecHitPacker', 'EE'),
    pfRecHitsHBHE = cms.InputTag('hltScoutingRecHitPacker', 'HBHE'),
    pfCleanedRecHitsEB = cms.InputTag('hltScoutingRecHitPacker', 'EBCleaned'),
    pfCleanedRecHitsEE = cms.InputTag('hltScoutingRecHitPacker', 'EECleaned'),
    topfoldername = cms.string('HLT/ScoutingOffline/Miscellaneous'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
