import FWCore.ParameterSet.Config as cms

def RamdiskMonitor(**kwargs):
  mod = cms.EDProducer('RamdiskMonitor',
    streamLabels = cms.required.untracked.vstring,
    runNumber = cms.required.untracked.uint32,
    runInputDir = cms.required.untracked.string,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
