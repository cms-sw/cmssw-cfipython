import FWCore.ParameterSet.Config as cms

def FixMissingStreamerInfos(**kwargs):
  mod = cms.Service('FixMissingStreamerInfos',
    fileInPath = cms.required.untracked.FileInPath
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
