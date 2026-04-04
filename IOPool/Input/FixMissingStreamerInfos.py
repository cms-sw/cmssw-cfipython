import FWCore.ParameterSet.Config as cms

def FixMissingStreamerInfos(*args, **kwargs):
  mod = cms.Service('FixMissingStreamerInfos',
    fileInPath = cms.required.untracked.FileInPath
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
