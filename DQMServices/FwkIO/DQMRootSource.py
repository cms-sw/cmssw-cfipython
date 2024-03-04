import FWCore.ParameterSet.Config as cms

def DQMRootSource(**kwargs):
  mod = cms.Source('DQMRootSource',
    fileNames = cms.required.untracked.vstring,
    filterOnRun = cms.untracked.uint32(0),
    reScope = cms.untracked.string('JOB'),
    skipBadFiles = cms.untracked.bool(False),
    overrideCatalog = cms.untracked.string(''),
    lumisToProcess = cms.untracked.VLuminosityBlockRange()
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
