import FWCore.ParameterSet.Config as cms

def DependencyGraph(**kwargs):
  mod = cms.Service('DependencyGraph',
    fileName = cms.untracked.string('dependency.dot'),
    highlightModules = cms.untracked.vstring(),
    showPathDependencies = cms.untracked.bool(True)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
