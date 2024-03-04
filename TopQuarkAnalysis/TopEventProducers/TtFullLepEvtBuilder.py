import FWCore.ParameterSet.Config as cms

def TtFullLepEvtBuilder(**kwargs):
  mod = cms.EDProducer('TtFullLepEvtBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
