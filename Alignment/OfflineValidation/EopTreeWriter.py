import FWCore.ParameterSet.Config as cms

def EopTreeWriter(**kwargs):
  mod = cms.EDAnalyzer('EopTreeWriter',
    src = cms.InputTag('generalTracks'),
    TrackAssociatorParameters = cms.PSet(
      accountForTrajectoryChangeCalo = cms.bool(False),
      propagateAllDirections = cms.bool(True),
      truthMatch = cms.bool(False),
      useCalo = cms.bool(False),
      useEcal = cms.bool(True),
      useGEM = cms.bool(False),
      useHO = cms.bool(True),
      useHcal = cms.bool(True),
      useME0 = cms.bool(False),
      useMuon = cms.bool(True),
      usePreshower = cms.bool(False),
      preselectMuonTracks = cms.bool(False),
      dREcal = cms.double(9999),
      dREcalPreselection = cms.double(0.05),
      dRHcal = cms.double(9999),
      dRHcalPreselection = cms.double(0.2),
      dRMuon = cms.double(9999),
      dRMuonPreselection = cms.double(0.2),
      dRPreshowerPreselection = cms.double(0.2),
      muonMaxDistanceSigmaX = cms.double(0),
      muonMaxDistanceSigmaY = cms.double(0),
      muonMaxDistanceX = cms.double(5),
      muonMaxDistanceY = cms.double(5),
      trajectoryUncertaintyTolerance = cms.double(-1),
      CSCSegmentCollectionLabel = cms.InputTag('cscSegments'),
      CaloTowerCollectionLabel = cms.InputTag('towerMaker'),
      DTRecSegment4DCollectionLabel = cms.InputTag('dt4DSegments'),
      EBRecHitCollectionLabel = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
      EERecHitCollectionLabel = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
      GEMSegmentCollectionLabel = cms.InputTag('gemSegments'),
      HBHERecHitCollectionLabel = cms.InputTag('hbreco'),
      HORecHitCollectionLabel = cms.InputTag('horeco'),
      ME0SegmentCollectionLabel = cms.InputTag('me0Segments'),
      RPCHitCollectionLabel = cms.InputTag('rpcRecHits'),
      GEMHitCollectionLabel = cms.InputTag('gemRecHits'),
      ME0HitCollectionLabel = cms.InputTag('me0RecHits')
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod