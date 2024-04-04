import FWCore.ParameterSet.Config as cms

MuonBaseMVAValueMapProducer = cms.EDProducer('MuonBaseMVAValueMapProducer',
  src = cms.required.InputTag,
  name = cms.required.string,
  weightFile = cms.required.FileInPath,
  batch_eval = cms.bool(False),
  variables = cms.required.VPSet,
  backend = cms.string('TMVA'),
  isClassifier = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)
