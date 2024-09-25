import FWCore.ParameterSet.Config as cms

def TritonService(*args, **kwargs):
  mod = cms.Service('TritonService',
    verbose = cms.untracked.bool(False),
    servers = cms.untracked.VPSet(
    ),
    fallback = cms.PSet(
      enable = cms.untracked.bool(False),
      debug = cms.untracked.bool(False),
      verbose = cms.untracked.bool(False),
      container = cms.untracked.string('apptainer'),
      device = cms.untracked.string('auto'),
      retries = cms.untracked.int32(-1),
      wait = cms.untracked.int32(-1),
      instanceBaseName = cms.untracked.string('triton_server_instance'),
      instanceName = cms.untracked.string(''),
      tempDir = cms.untracked.string(''),
      imageName = cms.untracked.string(''),
      sandboxName = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
