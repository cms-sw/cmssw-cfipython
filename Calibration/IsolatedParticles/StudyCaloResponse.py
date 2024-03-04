import FWCore.ParameterSet.Config as cms

def StudyCaloResponse(**kwargs):
  mod = cms.EDAnalyzer('StudyCaloResponse',
    particleSource = cms.InputTag('genParticles'),
    verbosity = cms.untracked.int32(0),
    triggers = cms.untracked.vstring(),
    newNames = cms.untracked.vstring(
      'HLT',
      'PixelTracks_Multiplicity',
      'HLT_Physics_',
      'HLT_JetE',
      'HLT_ZeroBias'
    ),
    labelMuon = cms.untracked.InputTag('muons', '', 'RECO'),
    labelTrack = cms.untracked.InputTag('generalTracks', '', 'RECO'),
    trackQuality = cms.untracked.string('highPurity'),
    minTrackPt = cms.untracked.double(1),
    maxDxyPV = cms.untracked.double(0.02),
    maxDzPV = cms.untracked.double(0.02),
    maxChi2 = cms.untracked.double(5),
    maxDpOverP = cms.untracked.double(0.1),
    minOuterHit = cms.untracked.int32(4),
    minLayerCrossed = cms.untracked.int32(8),
    maxInMiss = cms.untracked.int32(0),
    maxOutMiss = cms.untracked.int32(0),
    minTrackP = cms.untracked.double(1),
    maxTrackEta = cms.untracked.double(2.6),
    timeMinCutECAL = cms.untracked.double(-500),
    timeMaxCutECAL = cms.untracked.double(500),
    timeMinCutHCAL = cms.untracked.double(-500),
    timeMaxCutHCAL = cms.untracked.double(500),
    thresholdEB = cms.untracked.double(0.03),
    thresholdEE = cms.untracked.double(0.15),
    thresholdHB = cms.untracked.double(0.7),
    thresholdHE = cms.untracked.double(0.8),
    isItAOD = cms.untracked.bool(False),
    vetoTrigger = cms.untracked.bool(False),
    doTree = cms.untracked.bool(False),
    vetoMuon = cms.untracked.bool(True),
    cutMuon = cms.untracked.double(0.1),
    vetoEcal = cms.untracked.bool(False),
    cutEcal = cms.untracked.double(2),
    cutRatio = cms.untracked.double(0.9),
    puWeights = cms.untracked.vdouble(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
