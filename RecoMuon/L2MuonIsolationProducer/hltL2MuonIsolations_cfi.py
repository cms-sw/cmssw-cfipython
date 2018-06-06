import FWCore.ParameterSet.Config as cms

hltL2MuonIsolations = cms.EDProducer('L2MuonIsolationProducer',
  StandAloneCollectionLabel = cms.InputTag('hltL2MuonCandidates'),
  ExtractorPSet = cms.PSet(
    DR_Veto_H = cms.double(0.1),
    Vertex_Constraint_Z = cms.bool(False),
    Threshold_H = cms.double(0.5),
    ComponentName = cms.string('CaloExtractor'),
    Threshold_E = cms.double(0.2),
    DR_Max = cms.double(1),
    DR_Veto_E = cms.double(0.07),
    Weight_E = cms.double(1.5),
    Vertex_Constraint_XY = cms.bool(False),
    DepositLabel = cms.untracked.string('EcalPlusHcal'),
    CaloTowerCollectionLabel = cms.InputTag('towerMaker'),
    Weight_H = cms.double(1)
  ),
  IsolatorPSet = cms.PSet(
    ConeSizesRel = cms.vdouble(0.3),
    EffAreaSFEndcap = cms.double(1),
    CutAbsoluteIso = cms.bool(True),
    AndOrCuts = cms.bool(True),
    RhoSrc = cms.InputTag('hltKT6CaloJetsForMuons', 'rho'),
    ConeSizes = cms.vdouble(0.3),
    ComponentName = cms.string('CutsIsolatorWithCorrection'),
    ReturnRelativeSum = cms.bool(False),
    RhoScaleBarrel = cms.double(1),
    EffAreaSFBarrel = cms.double(1),
    CutRelativeIso = cms.bool(False),
    EtaBounds = cms.vdouble(2.411),
    Thresholds = cms.vdouble(99999999),
    ReturnAbsoluteSum = cms.bool(True),
    EtaBoundsRel = cms.vdouble(2.411),
    ThresholdsRel = cms.vdouble(99999999),
    RhoScaleEndcap = cms.double(1),
    RhoMax = cms.double(99999999),
    UseRhoCorrection = cms.bool(True)
  ),
  WriteIsolatorFloat = cms.bool(False)
)
