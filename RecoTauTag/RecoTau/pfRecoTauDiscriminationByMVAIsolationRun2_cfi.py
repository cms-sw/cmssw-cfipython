import FWCore.ParameterSet.Config as cms

pfRecoTauDiscriminationByMVAIsolationRun2 = cms.EDProducer('PFRecoTauDiscriminationByMVAIsolationRun2',
  mvaName = cms.string('tauIdMVAnewDMwLT'),
  loadMVAfromDB = cms.bool(True),
  inputFileName = cms.optional.FileInPath,
  mvaOpt = cms.string('newDMwLT'),
  srcTauTransverseImpactParameters = cms.InputTag(''),
  srcBasicTauDiscriminators = cms.InputTag('hpsPFTauBasicDiscriminators'),
  inputIDNameSuffix = cms.string(''),
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
