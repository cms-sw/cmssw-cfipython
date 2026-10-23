import FWCore.ParameterSet.Config as cms

def TtSemiLepEvtBuilder(*args, **kwargs):
  mod = cms.EDProducer('TtSemiLepEvtBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
