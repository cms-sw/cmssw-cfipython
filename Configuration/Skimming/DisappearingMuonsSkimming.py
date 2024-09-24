import FWCore.ParameterSet.Config as cms

def DisappearingMuonsSkimming(**kwargs):
  mod = cms.EDFilter('DisappearingMuonsSkimming',
    recoMuons = cms.InputTag('muons'),
    tracks = cms.InputTag('generalTracks'),
    StandaloneTracks = cms.InputTag('standAloneMuons'),
    primaryVertices = cms.InputTag('offlinePrimaryVertices'),
    EERecHits = cms.InputTag('reducedEcalRecHitsEE'),
    EBRecHits = cms.InputTag('reducedEcalRecHitsEB'),
    TriggerResultsTag = cms.InputTag('TriggerResults', '', 'HLT'),
    muonPathsToPass = cms.vstring(
      'HLT_IsoMu24_v',
      'HLT_IsoMu27_v'
    ),
    minMuPt = cms.double(26),
    maxMuEta = cms.double(2.4),
    minTrackEta = cms.double(0),
    maxTrackEta = cms.double(2.4),
    minTrackPt = cms.double(20),
    maxTransDCA = cms.double(0.005),
    maxLongDCA = cms.double(0.05),
    maxVtxChi = cms.double(3),
    minInvMass = cms.double(50),
    maxInvMass = cms.double(150),
    trackIsoConesize = cms.double(0.3),
    trackIsoInnerCone = cms.double(0.01),
    ecalIsoConesize = cms.double(0.4),
    minEcalHitE = cms.double(0.3),
    maxTrackIso = cms.double(0.05),
    maxEcalIso = cms.double(10),
    minSigInvMass = cms.double(76),
    maxSigInvMass = cms.double(106),
    minStandaloneDr = cms.double(1),
    maxStandaloneDE = cms.double(-0.5),
    keepOffPeak = cms.bool(True),
    keepSameSign = cms.bool(True),
    keepTotalRegion = cms.bool(True),
    keepPartialRegion = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod