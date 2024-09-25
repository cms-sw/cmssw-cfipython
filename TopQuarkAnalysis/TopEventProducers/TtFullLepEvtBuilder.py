import FWCore.ParameterSet.Config as cms

def TtFullLepEvtBuilder(*args, **kwargs):
  mod = cms.EDProducer('TtFullLepEvtBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
