import FWCore.ParameterSet.Config as cms

def AdaptorConfig(*args, **kwargs):
  mod = cms.Service('AdaptorConfig',
    enable = cms.untracked.bool(True),
    stats = cms.untracked.bool(True),
    cacheHint = cms.untracked.string('auto-detect'),
    readHint = cms.untracked.string('auto-detect'),
    tempDir = cms.untracked.string('.:$TMPDIR'),
    tempMinFree = cms.untracked.double(4),
    native = cms.untracked.vstring(),
    storageProxies = cms.untracked.VPSet(
      template = cms.PSetTemplate()
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
