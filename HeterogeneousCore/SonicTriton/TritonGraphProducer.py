import FWCore.ParameterSet.Config as cms

def TritonGraphProducer(*args, **kwargs):
  mod = cms.EDProducer('TritonGraphProducer',
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
    nodeMin = cms.uint32(100),
    nodeMax = cms.uint32(4000),
    edgeMin = cms.uint32(8000),
    edgeMax = cms.uint32(15000),
    brief = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
