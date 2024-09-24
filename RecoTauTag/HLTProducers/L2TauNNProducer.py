import FWCore.ParameterSet.Config as cms

def L2TauNNProducer(*args, **kwargs):
  mod = cms.EDProducer('L2TauNNProducer',
    debugLevel = cms.int32(0),
    L1Taus = cms.VPSet(
      cms.PSet(
        L1CollectionName = cms.string('DoubleTau'),
        L1TauTrigger = cms.InputTag('hltL1sDoubleTauBigOR')
      )
    ),
    hbheInput = cms.InputTag('hltHbhereco'),
    hoInput = cms.InputTag('hltHoreco'),
    ebInput = cms.InputTag('hltEcalRecHit', 'EcalRecHitsEB'),
    eeInput = cms.InputTag('hltEcalRecHit', 'EcalRecHitsEE'),
    pataVertices = cms.InputTag('hltPixelVerticesSoA'),
    pataTracks = cms.InputTag('hltPixelTracksSoA'),
    BeamSpot = cms.InputTag('hltOnlineBeamSpot'),
    maxVtx = cms.uint32(100),
    fractionSumPt2 = cms.double(0.3),
    minSumPt2 = cms.double(0),
    track_pt_min = cms.double(1),
    track_pt_max = cms.double(10),
    track_chi2_max = cms.double(99999),
    graphPath = cms.string('RecoTauTag/TrainingFiles/data/L2TauNNTag/L2TauTag_Run3v1.pb'),
    normalizationDict = cms.string('RecoTauTag/TrainingFiles/data/L2TauNNTag/NormalizationDict.json'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
