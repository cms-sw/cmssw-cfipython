import FWCore.ParameterSet.Config as cms

tritonGraphProducer = cms.EDProducer('TritonGraphProducer',
  Client = cms.PSet(
    mode = cms.string('PseudoAsync'),
    allowedTries = cms.untracked.uint32(0),
    modelName = cms.required.string,
    modelVersion = cms.string(''),
    modelConfigPath = cms.required.FileInPath,
    preferredServer = cms.untracked.string(''),
    timeout = cms.required.untracked.uint32,
    verbose = cms.untracked.bool(False),
    outputs = cms.untracked.vstring()
  ),
  nodeMin = cms.uint32(100),
  nodeMax = cms.uint32(4000),
  edgeMin = cms.uint32(8000),
  edgeMax = cms.uint32(15000),
  mightGet = cms.optional.untracked.vstring
)
