import FWCore.ParameterSet.Config as cms

tritonGraphFilter = cms.EDFilter('TritonGraphFilter',
  Client = cms.PSet(
    mode = cms.string('PseudoAsync'),
    allowedTries = cms.untracked.uint32(0),
    verbose = cms.untracked.bool(False),
    modelName = cms.required.string,
    modelVersion = cms.string(''),
    modelConfigPath = cms.required.FileInPath,
    preferredServer = cms.untracked.string(''),
    timeout = cms.required.untracked.uint32,
    useSharedMemory = cms.untracked.bool(True),
    compression = cms.untracked.string(''),
    outputs = cms.untracked.vstring()
  ),
  nodeMin = cms.uint32(100),
  nodeMax = cms.uint32(4000),
  edgeMin = cms.uint32(8000),
  edgeMax = cms.uint32(15000),
  brief = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
