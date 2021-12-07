import FWCore.ParameterSet.Config as cms

TritonService = cms.Service('TritonService',
  verbose = cms.untracked.bool(False),
  servers = cms.untracked.VPSet(
  ),
  fallback = cms.PSet(
    enable = cms.untracked.bool(False),
    debug = cms.untracked.bool(False),
    verbose = cms.untracked.bool(False),
    useDocker = cms.untracked.bool(False),
    useGPU = cms.untracked.bool(False),
    retries = cms.untracked.int32(-1),
    wait = cms.untracked.int32(-1),
    instanceBaseName = cms.untracked.string('triton_server_instance'),
    instanceName = cms.untracked.string(''),
    tempDir = cms.untracked.string(''),
    imageName = cms.untracked.string(''),
    sandboxName = cms.untracked.string('')
  )
)
