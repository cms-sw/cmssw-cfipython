import FWCore.ParameterSet.Config as cms

Tracer = cms.Service('Tracer',
  indention = cms.untracked.string('++'),
  dumpContextForLabels = cms.untracked.vstring(),
  dumpNonModuleContext = cms.untracked.bool(False),
  dumpPathsAndConsumes = cms.untracked.bool(False),
  printTimestamps = cms.untracked.bool(False)
)
