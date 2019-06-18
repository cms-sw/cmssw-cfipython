import FWCore.ParameterSet.Config as cms

EleBaseMVAValueMapProducer = cms.EDProducer('EleBaseMVAValueMapProducer',
  src = cms.required.InputTag,
  variablesOrder = cms.required.vstring,
  name = cms.required.string,
  isClassifier = cms.required.bool,
  variables = cms.PSet(),
  weightFile = cms.required.FileInPath,
  backend = cms.string('TMVA'),
  inputTensorName = cms.string(''),
  outputTensorName = cms.string(''),
  outputNames = cms.vstring(),
  outputFormulas = cms.vstring(),
  nThreads = cms.uint32(1),
  singleThreadPool = cms.string('no_threads'),
  mightGet = cms.optional.untracked.vstring
)
