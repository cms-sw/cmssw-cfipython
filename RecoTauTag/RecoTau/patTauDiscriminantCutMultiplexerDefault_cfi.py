import FWCore.ParameterSet.Config as cms

patTauDiscriminantCutMultiplexerDefault = cms.EDProducer('PATTauDiscriminantCutMultiplexer',
  toMultiplex = cms.InputTag('fixme'),
  verbosity = cms.int32(0),
  mapping = cms.VPSet(
    cms.PSet(
      category = cms.uint32(0),
      cut = cms.string('fixme')
    )
  ),
  rawValues = cms.vstring('discriminator'),
  workingPoints = cms.vdouble(0),
  inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
  loadMVAfromDB = cms.bool(True),
  PATTauProducer = cms.InputTag('fixme'),
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
  mvaOutput_normalization = cms.string(''),
  mightGet = cms.optional.untracked.vstring
)
