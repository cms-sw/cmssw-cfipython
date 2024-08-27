import FWCore.ParameterSet.Config as cms

def AdaptorConfig(**kwargs):
  mod = cms.Service('AdaptorConfig',
    enable = cms.optional.untracked.bool,
    stats = cms.optional.untracked.bool,
    cacheHint = cms.optional.untracked.string,
    readHint = cms.optional.untracked.string,
    tempDir = cms.optional.untracked.string,
    tempMinFree = cms.optional.untracked.double,
    native = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
