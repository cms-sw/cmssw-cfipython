import FWCore.ParameterSet.Config as cms

patTauDiscriminantCutMultiplexer = cms.EDProducer('PATTauDiscriminantCutMultiplexer',
  toMultiplex = cms.InputTag('fixme'),
  verbosity = cms.int32(0),
  inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
  loadMVAfromDB = cms.bool(True),
  Prediscriminants = cms.PSet(
    BooleanOperator = cms.string('and'),
    decayMode = cms.PSet()
  ),
  mvaOutput_normalization = cms.string(''),
  key = cms.InputTag('fixme'),
  PATTauProducer = cms.InputTag('fixme')
)
