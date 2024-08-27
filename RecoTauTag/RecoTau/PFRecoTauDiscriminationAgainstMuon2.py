import FWCore.ParameterSet.Config as cms

def PFRecoTauDiscriminationAgainstMuon2(**kwargs):
  mod = cms.EDProducer('PFRecoTauDiscriminationAgainstMuon2',
    maskHitsRPC = cms.vint32(
      0,
      0,
      0,
      0
    ),
    maxNumberOfHitsLast2Stations = cms.int32(0),
    maskMatchesRPC = cms.vint32(
      0,
      0,
      0,
      0
    ),
    maskMatchesCSC = cms.vint32(
      1,
      0,
      0,
      0
    ),
    maskHitsCSC = cms.vint32(
      0,
      0,
      0,
      0
    ),
    PFTauProducer = cms.InputTag('pfRecoTauProducer'),
    verbosity = cms.int32(0),
    maskMatchesDT = cms.vint32(
      0,
      0,
      0,
      0
    ),
    minPtMatchedMuon = cms.double(5),
    dRmuonMatchLimitedToJetArea = cms.bool(False),
    Prediscriminants = cms.PSet(
      BooleanOperator = cms.string('and'),
      leadTrack = cms.PSet(
        cut = cms.required.double,
        Producer = cms.required.InputTag
      )
    ),
    maskHitsDT = cms.vint32(
      0,
      0,
      0,
      0
    ),
    HoPMin = cms.double(0.2),
    maxNumberOfMatches = cms.int32(0),
    discriminatorOption = cms.string('loose'),
    dRmuonMatch = cms.double(0.3),
    srcMuons = cms.InputTag('muons'),
    doCaloMuonVeto = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
