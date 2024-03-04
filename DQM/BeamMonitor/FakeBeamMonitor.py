import FWCore.ParameterSet.Config as cms

def FakeBeamMonitor(**kwargs):
  mod = cms.EDProducer('FakeBeamMonitor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
