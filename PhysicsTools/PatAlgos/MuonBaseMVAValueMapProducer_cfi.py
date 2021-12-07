import FWCore.ParameterSet.Config as cms

MuonBaseMVAValueMapProducer = cms.EDProducer('MuonBaseMVAValueMapProducer',
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
  batch_eval = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
