import FWCore.ParameterSet.Config as cms

def DQMRootSource(*args, **kwargs):
  mod = cms.Source('DQMRootSource',
    fileNames = cms.required.untracked.vstring,
    overrideCatalog = cms.untracked.string(''),
    filterOnRun = cms.untracked.uint32(0),
    reScope = cms.untracked.string('JOB'),
    skipBadFiles = cms.untracked.bool(False),
    lumisToProcess = cms.untracked.VLuminosityBlockRange()
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
