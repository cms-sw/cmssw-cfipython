import FWCore.ParameterSet.Config as cms

def TtFullHadEvtBuilder(**kwargs):
  mod = cms.EDProducer('TtFullHadEvtBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
