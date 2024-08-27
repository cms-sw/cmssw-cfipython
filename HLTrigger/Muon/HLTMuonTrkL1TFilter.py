import FWCore.ParameterSet.Config as cms

def HLTMuonTrkL1TFilter(**kwargs):
  mod = cms.EDFilter('HLTMuonTrkL1TFilter',
    saveTags = cms.bool(True),
    inputMuonCollection = cms.InputTag(''),
    inputCandCollection = cms.InputTag(''),
    previousCandTag = cms.InputTag(''),
    minTrkHits = cms.int32(-1),
    minMuonHits = cms.int32(-1),
    minMuonStations = cms.int32(-1),
    maxNormalizedChi2 = cms.double(1e+99),
    allowedTypeMask = cms.uint32(255),
    requiredTypeMask = cms.uint32(0),
    trkMuonId = cms.uint32(0),
    minPt = cms.double(24),
    minN = cms.uint32(1),
    maxAbsEta = cms.double(1e+99),
    L1MatchingdR = cms.double(0.3),
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
