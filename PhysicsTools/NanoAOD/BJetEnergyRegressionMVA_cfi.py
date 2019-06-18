import FWCore.ParameterSet.Config as cms

BJetEnergyRegressionMVA = cms.EDProducer('BJetEnergyRegressionMVA',
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
  pvsrc = cms.required.InputTag,
  svsrc = cms.required.InputTag,
  rhosrc = cms.required.InputTag,
  mightGet = cms.optional.untracked.vstring
)
