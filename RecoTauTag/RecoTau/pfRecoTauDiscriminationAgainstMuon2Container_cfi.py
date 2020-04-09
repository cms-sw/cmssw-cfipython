import FWCore.ParameterSet.Config as cms

pfRecoTauDiscriminationAgainstMuon2Container = cms.EDProducer('PFRecoTauDiscriminationAgainstMuon2Container',
  maskHitsRPC = cms.vint32(
    0,
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
      cut = cms.double(0.5),
      Producer = cms.InputTag('pfRecoTauDiscriminationByLeadingTrackFinding')
    )
  ),
  maskHitsDT = cms.vint32(
    0,
    0,
    0,
    0
  ),
  dRmuonMatch = cms.double(0.3),
  srcMuons = cms.InputTag('muons'),
  IDWPdefinitions = cms.VPSet(
    cms.PSet(
      HoPMin = cms.double(0.2),
      IDname = cms.string('pfRecoTauDiscriminationAgainstMuon2Container'),
      discriminatorOption = cms.string('loose'),
      doCaloMuonVeto = cms.bool(False),
      maxNumberOfHitsLast2Stations = cms.int32(0),
      maxNumberOfMatches = cms.int32(0)
    )
  ),
  mightGet = cms.optional.untracked.vstring
)
