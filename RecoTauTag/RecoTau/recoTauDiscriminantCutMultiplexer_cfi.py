import FWCore.ParameterSet.Config as cms

recoTauDiscriminantCutMultiplexer = cms.EDProducer('RecoTauDiscriminantCutMultiplexer',
  toMultiplex = cms.InputTag('fixme'),
  PFTauProducer = cms.InputTag('fixme'),
  verbosity = cms.int32(0),
  inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
  loadMVAfromDB = cms.bool(True),
  Prediscriminants = cms.PSet(
    BooleanOperator = cms.string('and'),
    decayMode = cms.PSet(
      cut = cms.double(0),
      Producer = cms.InputTag('fixme')
    )
  ),
  mvaOutput_normalization = cms.string(''),
  key = cms.InputTag('fixme')
)
