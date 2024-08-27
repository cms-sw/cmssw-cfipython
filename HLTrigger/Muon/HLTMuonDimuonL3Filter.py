import FWCore.ParameterSet.Config as cms

def HLTMuonDimuonL3Filter(**kwargs):
  mod = cms.EDFilter('HLTMuonDimuonL3Filter',
    saveTags = cms.bool(True),
    BeamSpotTag = cms.InputTag('hltOfflineBeamSpot'),
    CandTag = cms.InputTag('hltL3MuonCandidates'),
    PreviousCandTag = cms.InputTag(''),
    L1CandTag = cms.InputTag(''),
    inputMuonCollection = cms.InputTag(''),
    PreviousCandIsL2 = cms.bool(True),
    FastAccept = cms.bool(False),
    MinN = cms.int32(1),
    MaxEta = cms.double(2.5),
    MinNhits = cms.int32(0),
    MaxDr = cms.double(2),
    MaxDz = cms.double(9999),
    ChargeOpt = cms.int32(0),
    MinPtPair = cms.vdouble(0),
    MaxPtPair = cms.vdouble(1e+125),
    MinPtMax = cms.vdouble(3),
    MinPtMin = cms.vdouble(3),
    MaxPtMin = cms.vdouble(1e+125),
    MinInvMass = cms.vdouble(2.8),
    MaxInvMass = cms.vdouble(3.4),
    MinDiMuonDeltaR = cms.double(-1),
    MinAcop = cms.double(-1),
    MaxAcop = cms.double(3.15),
    MinPtBalance = cms.double(-1),
    MaxPtBalance = cms.double(999999),
    NSigmaPt = cms.double(0),
    MaxDCAMuMu = cms.double(99999.9),
    MaxRapidityPair = cms.double(999999),
    CutCowboys = cms.bool(False),
    InputLinks = cms.InputTag(''),
    L1MatchingdR = cms.double(0.3),
    MatchToPreviousCand = cms.bool(True),
    useSimpleGeometry = cms.bool(True),
    useStation2 = cms.bool(True),
    fallbackToME1 = cms.bool(False),
    cosmicPropagationHypothesis = cms.bool(False),
    useMB2InOverlap = cms.bool(False),
    useTrack = cms.string('tracker'),
    useState = cms.string('atVertex'),
    propagatorAlong = cms.ESInputTag('', 'hltESPSteppingHelixPropagatorAlong'),
    propagatorAny = cms.ESInputTag('', 'SteppingHelixPropagatorAny'),
    propagatorOpposite = cms.ESInputTag('', 'hltESPSteppingHelixPropagatorOpposite'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
