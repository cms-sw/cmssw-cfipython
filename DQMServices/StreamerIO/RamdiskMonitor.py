import FWCore.ParameterSet.Config as cms

def RamdiskMonitor(*args, **kwargs):
  mod = cms.EDProducer('RamdiskMonitor',
    streamLabels = cms.required.untracked.vstring,
    runNumber = cms.required.untracked.uint32,
    runInputDir = cms.required.untracked.string,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
