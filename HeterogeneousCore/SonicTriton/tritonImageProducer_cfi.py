import FWCore.ParameterSet.Config as cms

tritonImageProducer = cms.EDProducer('TritonImageProducer',
  Client = cms.PSet(
    mode = cms.string('PseudoAsync'),
    allowedTries = cms.untracked.uint32(0),
    modelName = cms.required.string,
    modelVersion = cms.string(''),
    modelConfigPath = cms.required.FileInPath,
    preferredServer = cms.untracked.string(''),
    timeout = cms.required.untracked.uint32,
    verbose = cms.untracked.bool(False),
    useSharedMemory = cms.untracked.bool(True),
    outputs = cms.untracked.vstring()
  ),
  batchSize = cms.int32(1),
  topN = cms.uint32(5),
  imageList = cms.required.FileInPath,
  mightGet = cms.optional.untracked.vstring
)
