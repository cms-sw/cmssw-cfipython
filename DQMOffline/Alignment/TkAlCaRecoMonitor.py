import FWCore.ParameterSet.Config as cms

def TkAlCaRecoMonitor(*args, **kwargs):
  mod = cms.EDProducer('TkAlCaRecoMonitor',
    TrackProducer = cms.InputTag('generalTracks'),
    ReferenceTrackProducer = cms.InputTag('generalTrakcs'),
    CaloJetCollection = cms.InputTag('ak4CaloJets'),
    AlgoName = cms.string('testTkAlCaReco'),
    FolderName = cms.string('TkAlCaRecoMonitor'),
    daughterMass = cms.double(0.1056583755),
    maxJetPt = cms.double(10),
    fillInvariantMass = cms.bool(False),
    runsOnReco = cms.bool(False),
    useSignedR = cms.bool(False),
    fillRawIdMap = cms.bool(False),
    MassBin = cms.uint32(100),
    MassMin = cms.double(0),
    MassMax = cms.double(100),
    TrackPtBin = cms.uint32(110),
    TrackPtMin = cms.double(0),
    TrackPtMax = cms.double(110),
    TrackCurvatureBin = cms.uint32(2000),
    TrackCurvatureMin = cms.double(-0.01),
    TrackCurvatureMax = cms.double(0.01),
    SumChargeBin = cms.uint32(11),
    SumChargeMin = cms.double(-5.5),
    SumChargeMax = cms.double(5.5),
    JetPtBin = cms.uint32(100),
    JetPtMin = cms.double(0),
    JetPtMax = cms.double(50),
    MinJetDeltaRBin = cms.uint32(100),
    MinJetDeltaRMin = cms.double(0),
    MinJetDeltaRMax = cms.double(10),
    MinTrackDeltaRBin = cms.uint32(100),
    MinTrackDeltaRMin = cms.double(0),
    MinTrackDeltaRMax = cms.double(3.2),
    TrackEfficiencyBin = cms.uint32(102),
    TrackEfficiencyMin = cms.double(-0.01),
    TrackEfficiencyMax = cms.double(1.01),
    HitMapsZBin = cms.uint32(300),
    HitMapZMax = cms.double(300),
    HitMapsRBin = cms.uint32(120),
    HitMapRMax = cms.double(120),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
