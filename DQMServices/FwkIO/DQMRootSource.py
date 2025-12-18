import FWCore.ParameterSet.Config as cms

def DQMRootSource(*args, **kwargs):
  mod = cms.Source('DQMRootSource',
    fileNames = cms.required.untracked.vstring,
    filterOnRun = cms.untracked.uint32(0),
    reScope = cms.untracked.string('JOB'),
    skipBadFiles = cms.untracked.bool(False),
    overrideCatalog = cms.untracked.string(''),
    lumisToProcess = cms.untracked.VLuminosityBlockRange()
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
