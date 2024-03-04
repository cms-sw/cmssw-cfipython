import FWCore.ParameterSet.Config as cms

def ElectronSeedProducer(**kwargs):
  mod = cms.EDProducer('ElectronSeedProducer',
    initialSeedsVector = cms.VInputTag(),
    useRecoVertex = cms.bool(False),
    vertices = cms.InputTag('offlinePrimaryVerticesWithBS'),
    beamSpot = cms.InputTag('offlineBeamSpot'),
    dynamicPhiRoad = cms.bool(True),
    SCEtCut = cms.double(0),
    applyHOverECut = cms.bool(True),
    hOverEConeSize = cms.double(0.15),
    maxHOverEBarrel = cms.double(0.15),
    maxHOverEEndcaps = cms.double(0.15),
    hbheRecHits = cms.InputTag('hbhereco'),
    recHitEThresholdHB = cms.vdouble(
      0,
      0,
      0,
      0
    ),
    recHitEThresholdHE = cms.vdouble(
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ),
    maxHcalRecHitSeverity = cms.int32(999999),
    usePFThresholdsFromDB = cms.bool(False),
    allowHGCal = cms.bool(False),
    HGCalConfig = cms.PSet(
      HGCEEInput = cms.InputTag('HGCalRecHit', 'HGCEERecHits'),
      HGCFHInput = cms.InputTag('HGCalRecHit', 'HGCHEFRecHits'),
      HGCBHInput = cms.InputTag('HGCalRecHit', 'HGCHEBRecHits')
    ),
    nSigmasDeltaZ1 = cms.double(5),
    deltaZ1WithVertex = cms.double(25),
    z2MaxB = cms.double(0.09),
    r2MaxF = cms.double(0.15),
    rMaxI = cms.double(0.2),
    LowPtThreshold = cms.double(5),
    HighPtThreshold = cms.double(35),
    SizeWindowENeg = cms.double(0.675),
    DeltaPhi1Low = cms.double(0.23),
    DeltaPhi1High = cms.double(0.08),
    DeltaPhi2B = cms.double(0.008),
    DeltaPhi2F = cms.double(0.012),
    ePhiMin1 = cms.double(-0.125),
    ePhiMax1 = cms.double(0.075),
    PhiMax2B = cms.double(0.002),
    PhiMax2F = cms.double(0.003),
    barrelSuperClusters = cms.InputTag('particleFlowSuperClusterECAL', 'particleFlowSuperClusterECALBarrel'),
    endcapSuperClusters = cms.InputTag('particleFlowSuperClusterECAL', 'particleFlowSuperClusterECALEndcapWithPreshower'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
