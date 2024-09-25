import FWCore.ParameterSet.Config as cms

def GEMEfficiencyAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('GEMEfficiencyAnalyzer',
    ohStatusTag = cms.untracked.InputTag('muonGEMDigis', 'OHStatus'),
    vfatStatusTag = cms.untracked.InputTag('muonGEMDigis', 'VFATStatus'),
    monitorGE11 = cms.untracked.bool(True),
    monitorGE21 = cms.untracked.bool(False),
    monitorGE0 = cms.untracked.bool(False),
    maskChamberWithError = cms.untracked.bool(False),
    logCategory = cms.untracked.string('GEMEfficiencyAnalyzer'),
    recHitTag = cms.untracked.InputTag('gemRecHits'),
    muonTag = cms.untracked.InputTag('muons'),
    modeDev = cms.untracked.bool(False),
    muonTrackType = cms.untracked.string('OuterTrack'),
    muonName = cms.untracked.string('STA Muon'),
    folder = cms.untracked.string('GEM/Efficiency/muonSTA'),
    scenario = cms.untracked.string('pp'),
    startingStateType = cms.untracked.string('OutermostMeasurementState'),
    muonSegmentMatchDRCut = cms.untracked.double(5),
    muonPtMinCutGE0 = cms.untracked.double(20),
    muonPtMinCutGE11 = cms.untracked.double(20),
    muonPtMinCutGE21 = cms.untracked.double(20),
    muonEtaMinCutGE11 = cms.untracked.double(1.5),
    muonEtaMaxCutGE11 = cms.untracked.double(2.2),
    muonEtaMinCutGE21 = cms.untracked.double(1.5),
    muonEtaMaxCutGE21 = cms.untracked.double(2.5),
    muonEtaMinCutGE0 = cms.untracked.double(2),
    muonEtaMaxCutGE0 = cms.untracked.double(3),
    propagationErrorRCut = cms.untracked.double(0.5),
    propagationErrorPhiCut = cms.untracked.double(0.2),
    boundsErrorScale = cms.untracked.double(-2),
    matchingMetric = cms.untracked.string('DeltaPhi'),
    matchingCut = cms.untracked.double(0.2),
    muonPtBins = cms.untracked.vdouble(
      0,
      5,
      10,
      20,
      30,
      40,
      50,
      60,
      70,
      80,
      90,
      100,
      110
    ),
    muonEtaNbinsGE11 = cms.untracked.int32(9),
    muonEtaLowGE11 = cms.untracked.double(1.4),
    muonEtaUpGE11 = cms.untracked.double(2.3),
    muonEtaNbinsGE21 = cms.untracked.int32(12),
    muonEtaLowGE21 = cms.untracked.double(1.4),
    muonEtaUpGE21 = cms.untracked.double(2.6),
    muonEtaNbinsGE0 = cms.untracked.int32(12),
    muonEtaLowGE0 = cms.untracked.double(1.9),
    muonEtaUpGE0 = cms.untracked.double(3.1),
    muonSubdetForGE0 = cms.untracked.vint32(),
    muonSubdetForGE11 = cms.untracked.vint32(),
    muonSubdetForGE21 = cms.untracked.vint32(),
    cscForGE11 = cms.untracked.vint32(
      1,
      2
    ),
    cscForGE21 = cms.untracked.vint32(),
    cscForGE0 = cms.untracked.vint32(),
    ServiceParameters = cms.PSet(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
