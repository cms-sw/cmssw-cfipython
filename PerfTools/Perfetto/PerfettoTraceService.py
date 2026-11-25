import FWCore.ParameterSet.Config as cms

def PerfettoTraceService(*args, **kwargs):
  mod = cms.Service('PerfettoTraceService',
    enabled = cms.untracked.bool(True),
    fileName = cms.untracked.string('cmsrun.pftrace'),
    bufferSizeKB = cms.untracked.uint32(262144),
    shmemSizeKB = cms.untracked.uint32(65536),
    maxEvents = cms.untracked.uint32(0),
    traceFunctions = cms.untracked.bool(False),
    traceAllocations = cms.untracked.bool(False),
    traceGpuKernels = cms.untracked.bool(False),
    traceGpuCopies = cms.untracked.bool(False),
    traceGpuMemory = cms.untracked.bool(False),
    traceGpuModules = cms.untracked.bool(True),
    tracePower = cms.untracked.bool(False),
    powerPeriodMs = cms.untracked.uint32(1000),
    traceModules = cms.untracked.vstring()
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
