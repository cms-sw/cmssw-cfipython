import FWCore.ParameterSet.Config as cms

def DependencyGraph(*args, **kwargs):
  mod = cms.Service('DependencyGraph',
    fileName = cms.untracked.string('dependency.dot'),
    highlightModules = cms.untracked.vstring(),
    showPathDependencies = cms.untracked.bool(True)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
