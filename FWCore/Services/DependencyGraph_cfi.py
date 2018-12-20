import FWCore.ParameterSet.Config as cms

DependencyGraph = cms.Service('DependencyGraph',
  fileName = cms.untracked.string('dependency.gv'),
  highlightModules = cms.untracked.vstring(),
  showPathDependencies = cms.untracked.bool(True)
)
