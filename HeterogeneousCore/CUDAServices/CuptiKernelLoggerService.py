import FWCore.ParameterSet.Config as cms

def CuptiKernelLoggerService(*args, **kwargs):
  mod = cms.Service('CuptiKernelLoggerService',
    kernelLog = cms.untracked.string('kernels.txt'),
    libraryLog = cms.untracked.string('libraries.txt')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
