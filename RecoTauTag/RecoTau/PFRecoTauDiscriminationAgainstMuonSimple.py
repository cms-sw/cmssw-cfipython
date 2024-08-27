import FWCore.ParameterSet.Config as cms

def PFRecoTauDiscriminationAgainstMuonSimple(**kwargs):
  mod = cms.EDProducer('PFRecoTauDiscriminationAgainstMuonSimple',
    PFTauProducer = cms.InputTag('pfRecoTauProducer'),
    Prediscriminants = cms.PSet(
      BooleanOperator = cms.string('and'),
      leadTrack = cms.PSet(
        cut = cms.required.double,
        Producer = cms.required.InputTag
      )
    ),
    IDWPdefinitions = cms.VPSet(
      cms.PSet(
        HoPMin = cms.double(0.2),
        IDname = cms.string('ByLooseMuonRejectionSimple'),
        doCaloMuonVeto = cms.bool(True),
        maxNumberOfHitsLast2Stations = cms.int32(-1),
        maxNumberOfMatches = cms.int32(1),
        maxNumberOfRPCMuons = cms.int32(-1),
        maxNumberOfSTAMuons = cms.int32(-1)
      )
    ),
    IDdefinitions = cms.VPSet(
    ),
    srcPatMuons = cms.InputTag('slimmedMuons'),
    dRmuonMatch = cms.double(0.3),
    dRmuonMatchLimitedToJetArea = cms.bool(False),
    minPtMatchedMuon = cms.double(5),
    maskMatchesDT = cms.vint32(
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
    maskMatchesRPC = cms.vint32(
      0,
      0,
      0,
      0
    ),
    maskHitsDT = cms.vint32(
      0,
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
    maskHitsRPC = cms.vint32(
      0,
      0,
      0,
      0
    ),
    verbosity = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
