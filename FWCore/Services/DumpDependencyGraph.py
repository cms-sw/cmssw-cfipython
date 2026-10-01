import FWCore.ParameterSet.Config as cms

def DumpDependencyGraph(*args, **kwargs):
  mod = cms.Service('DumpDependencyGraph',
    fileName = cms.untracked.string('dependency_graph.json')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
