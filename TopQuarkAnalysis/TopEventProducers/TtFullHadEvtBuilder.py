import FWCore.ParameterSet.Config as cms

def TtFullHadEvtBuilder(*args, **kwargs):
  mod = cms.EDProducer('TtFullHadEvtBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
