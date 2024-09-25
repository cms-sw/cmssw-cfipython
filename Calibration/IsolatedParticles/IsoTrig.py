import FWCore.ParameterSet.Config as cms

def IsoTrig(*args, **kwargs):
  mod = cms.EDAnalyzer('IsoTrig',
    Triggers = cms.untracked.vstring('HLT_IsoTrackHB'),
    pixCandTag = cms.untracked.InputTag(' '),
    l1CandTag = cms.untracked.InputTag('hltL1sV0SingleJet60'),
    l2CandTag = cms.untracked.InputTag('isolEcalPixelTrackProd'),
    doL2L3 = cms.untracked.bool(False),
    doTimingTree = cms.untracked.bool(False),
    doMipCutTree = cms.untracked.bool(False),
    doTrkResTree = cms.untracked.bool(True),
    doChgIsolTree = cms.untracked.bool(False),
    doStudyIsol = cms.untracked.bool(False),
    verbosity = cms.untracked.int32(0),
    processName = cms.untracked.string('HLT'),
    trackQuality = cms.untracked.string('highPurity'),
    minTrackPt = cms.untracked.double(10),
    maxDxyPV = cms.untracked.double(0.02),
    maxDzPV = cms.untracked.double(0.02),
    maxChi2 = cms.untracked.double(5),
    maxDpOverP = cms.untracked.double(0.1),
    minOuterHit = cms.untracked.int32(4),
    minLayerCrossed = cms.untracked.int32(8),
    maxInMiss = cms.untracked.int32(0),
    maxOutMiss = cms.untracked.int32(0),
    isolationL1 = cms.untracked.double(1),
    coneRadius = cms.untracked.double(34.98),
    coneRadiusMIP = cms.untracked.double(14),
    coneRadiusNeut1 = cms.untracked.double(21),
    coneRadiusNeut2 = cms.untracked.double(29),
    cutMIP = cms.untracked.double(1),
    chargeIsolation = cms.untracked.double(2),
    neutralIsolation = cms.untracked.double(2),
    minRun = cms.untracked.int32(190456),
    maxRun = cms.untracked.int32(203002),
    pixelTracksSources = cms.untracked.VInputTag(
      'hltHITPixelTracksHB',
      'hltHITPixelTracksHE'
    ),
    pixelIsolationConeSizeAtEC = cms.untracked.vdouble(
      35,
      40,
      45,
      50,
      55,
      60,
      63.9,
      70
    ),
    minPTrackValue = cms.untracked.double(0),
    vertexCutSeed = cms.untracked.double(101),
    vertexCutIsol = cms.untracked.double(101),
    tauUnbiasCone = cms.untracked.double(1.2),
    prelimCone = cms.untracked.double(1),
    stageL1Trigger = cms.uint32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
