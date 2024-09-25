import FWCore.ParameterSet.Config as cms

def FakeBeamMonitor(*args, **kwargs):
  mod = cms.EDProducer('FakeBeamMonitor',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
