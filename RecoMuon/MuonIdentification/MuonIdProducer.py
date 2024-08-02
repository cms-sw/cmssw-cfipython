import FWCore.ParameterSet.Config as cms

def MuonIdProducer(**kwargs):
  mod = cms.EDProducer('MuonIdProducer',
    arbitrateTrackerMuons = cms.bool(False),
    storeCrossedHcalRecHits = cms.bool(False),
    fillShowerDigis = cms.bool(False),
    selectHighPurity = cms.bool(False),
    pvInputTag = cms.InputTag(''),
    TrackAssociatorParameters = cms.PSet(
      GEMSegmentCollectionLabel = cms.InputTag('gemSegments'),
      ME0SegmentCollectionLabel = cms.InputTag('me0Segments'),
      useGEM = cms.bool(False),
      useME0 = cms.bool(False),
      preselectMuonTracks = cms.bool(False),
      RPCHitCollectionLabel = cms.InputTag('rpcRecHits'),
      GEMHitCollectionLabel = cms.InputTag('gemRecHits'),
      ME0HitCollectionLabel = cms.InputTag('me0RecHits')
    ),
    JetExtractorPSet = cms.PSet(
      TrackAssociatorParameters = cms.PSet(
        GEMSegmentCollectionLabel = cms.InputTag('gemSegments'),
        ME0SegmentCollectionLabel = cms.InputTag('me0Segments'),
        useGEM = cms.bool(False),
        useME0 = cms.bool(False),
        preselectMuonTracks = cms.bool(False),
        RPCHitCollectionLabel = cms.InputTag('rpcRecHits'),
        GEMHitCollectionLabel = cms.InputTag('gemRecHits'),
        ME0HitCollectionLabel = cms.InputTag('me0RecHits')
      )
    ),
    CaloExtractorPSet = cms.PSet(
      TrackAssociatorParameters = cms.PSet(
        GEMSegmentCollectionLabel = cms.InputTag('gemSegments'),
        ME0SegmentCollectionLabel = cms.InputTag('me0Segments'),
        useGEM = cms.bool(False),
        useME0 = cms.bool(False),
        preselectMuonTracks = cms.bool(False),
        RPCHitCollectionLabel = cms.InputTag('rpcRecHits'),
        GEMHitCollectionLabel = cms.InputTag('gemRecHits'),
        ME0HitCollectionLabel = cms.InputTag('me0RecHits')
      ),
      UseEcalRecHitsFlag = cms.bool(False),
      UseHcalRecHitsFlag = cms.bool(False),
      UseHORecHitsFlag = cms.bool(False),
      EcalRecHitThresh = cms.bool(False),
      HcalCutsFromDB = cms.bool(False),
      MaxSeverityHB = cms.int32(9),
      MaxSeverityHE = cms.int32(9)
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
