import FWCore.ParameterSet.Config as cms

tritonGraphProducer = cms.EDProducer('TritonGraphProducer',
  Client = cms.PSet(
    mode = cms.string('PseudoAsync'),
    allowedTries = cms.untracked.uint32(0),
    modelName = cms.required.string,
    modelVersion = cms.int32(-1),
    batchSize = cms.required.untracked.uint32,
    address = cms.required.untracked.string,
    port = cms.required.untracked.uint32,
    timeout = cms.required.untracked.uint32,
    verbose = cms.untracked.bool(False)
  ),
  mightGet = cms.optional.untracked.vstring
)
