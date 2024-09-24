import FWCore.ParameterSet.Config as cms

def Tracer(*args, **kwargs):
  mod = cms.Service('Tracer',
    indention = cms.untracked.string('++'),
    dumpContextForLabels = cms.untracked.vstring(),
    dumpNonModuleContext = cms.untracked.bool(False),
    dumpPathsAndConsumes = cms.untracked.bool(False),
    printTimestamps = cms.untracked.bool(False),
    dumpEventSetupInfo = cms.untracked.bool(False),
    useMessageLogger = cms.untracked.bool(True),
    fileName = cms.untracked.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod