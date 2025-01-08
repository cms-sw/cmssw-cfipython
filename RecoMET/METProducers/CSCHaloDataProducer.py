import FWCore.ParameterSet.Config as cms

def CSCHaloDataProducer(*args, **kwargs):
  mod = cms.EDProducer('CSCHaloDataProducer',
    L1MuGMTReadoutLabel = cms.InputTag('gtDigis'),
    HLTResultLabel = cms.InputTag('TriggerResults', '', 'HLT'),
    HLTBitLabel = cms.VInputTag(
      'HLT_CSCBeamHalo',
      'HLT_CSCBeamHaloOverlapRing1',
      'HLT_CSCBeamHaloOverlapRing2',
      'HLT_CSCBeamHaloRing2or3'
    ),
    CSCRecHitLabel = cms.InputTag('csc2DRecHits'),
    HBHErhLabel = cms.InputTag('hbhereco'),
    ECALBrhLabel = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
    ECALErhLabel = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
    CSCSegmentLabel = cms.InputTag('cscSegments'),
    CosmicMuonLabel = cms.InputTag('muonsFromCosmics'),
    MuonLabel = cms.InputTag('muons'),
    SALabel = cms.InputTag('standAloneMuons'),
    ALCTDigiLabel = cms.InputTag('muonCSCDigis', 'MuonCSCALCTDigi'),
    MatchParameters = cms.PSet(
      DTsegments = cms.InputTag('dt4DSegments'),
      CSCsegments = cms.InputTag('cscSegments'),
      DTradius = cms.double(0.01),
      TightMatchDT = cms.bool(False),
      TightMatchCSC = cms.bool(False),
      RPChits = cms.InputTag('rpcRecHits')
    ),
    DetaParam = cms.double(0.1),
    DphiParam = cms.double(1),
    InnerRMinParam = cms.double(0),
    InnerRMaxParam = cms.double(99999),
    OuterRMinParam = cms.double(0),
    OuterRMaxParam = cms.double(99999),
    NormChi2Param = cms.double(8),
    MaxSegmentRDiff = cms.double(10),
    MaxSegmentPhiDiff = cms.double(0.1),
    MaxSegmentTheta = cms.double(0.7),
    MaxDtMuonSegment = cms.double(-10),
    MaxFreeInverseBeta = cms.double(0),
    ExpectedBX = cms.int32(6),
    RecHitTime0 = cms.double(0),
    RecHitTimeWindow = cms.double(25),
    MinOuterMomentumTheta = cms.double(0.1),
    MaxOuterMomentumTheta = cms.double(3),
    MatchingDPhiThreshold = cms.double(0.18),
    MatchingDEtaThreshold = cms.double(0.4),
    MatchingDWireThreshold = cms.int32(5),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
