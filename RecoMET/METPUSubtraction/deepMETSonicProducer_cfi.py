import FWCore.ParameterSet.Config as cms

deepMETSonicProducer = cms.EDProducer('DeepMETSonicProducer',
  Client = cms.PSet(
    mode = cms.string('PseudoAsync'),
    allowedTries = cms.untracked.uint32(0),
    verbose = cms.untracked.bool(False),
    modelName = cms.required.string,
    modelVersion = cms.string(''),
    modelConfigPath = cms.required.FileInPath,
    preferredServer = cms.untracked.string(''),
    timeout = cms.required.untracked.uint32,
    timeoutUnit = cms.untracked.string('seconds'),
    useSharedMemory = cms.untracked.bool(True),
    compression = cms.untracked.string(''),
    outputs = cms.untracked.vstring()
  ),
  pf_src = cms.InputTag('packedPFCandidates'),
  ignore_leptons = cms.bool(False),
  norm_factor = cms.double(50),
  max_n_pf = cms.uint32(4500),
  mightGet = cms.optional.untracked.vstring
)
