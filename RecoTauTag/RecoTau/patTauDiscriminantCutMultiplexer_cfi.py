import FWCore.ParameterSet.Config as cms

patTauDiscriminantCutMultiplexer = cms.EDProducer('PATTauDiscriminantCutMultiplexer',
  toMultiplex = cms.InputTag('fixme'),
  verbosity = cms.int32(0),
  mapping = cms.VPSet(
    cms.PSet(
      category = cms.uint32(0),
      cut = cms.double(0.5)
    ),
    cms.PSet(
      category = cms.uint32(1),
      cut = cms.double(0.2)
    )
  ),
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
  key = cms.InputTag('fixme'),
  mightGet = cms.optional.untracked.vstring
)
