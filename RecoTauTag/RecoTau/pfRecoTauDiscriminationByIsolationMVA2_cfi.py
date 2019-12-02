import FWCore.ParameterSet.Config as cms

pfRecoTauDiscriminationByIsolationMVA2 = cms.EDProducer('PFRecoTauDiscriminationByIsolationMVA2',
  mvaName = cms.required.string,
  loadMVAfromDB = cms.required.bool,
  inputFileName = cms.optional.FileInPath,
  mvaOpt = cms.required.string,
  srcTauTransverseImpactParameters = cms.required.InputTag,
  srcChargedIsoPtSum = cms.required.InputTag,
  srcNeutralIsoPtSum = cms.required.InputTag,
  srcPUcorrPtSum = cms.required.InputTag,
  verbosity = cms.int32(0),
  PFTauProducer = cms.InputTag('fixme'),
  Prediscriminants = cms.PSet(
    BooleanOperator = cms.string('AND'),
    leadTrack = cms.PSet(
      cut = cms.double(0),
      Producer = cms.InputTag('fixme')
    ),
    decayMode = cms.PSet(
      cut = cms.double(0),
      Producer = cms.InputTag('fixme')
    )
  ),
  mightGet = cms.optional.untracked.vstring
)
