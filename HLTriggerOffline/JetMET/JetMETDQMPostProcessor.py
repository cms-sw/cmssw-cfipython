import FWCore.ParameterSet.Config as cms

def JetMETDQMPostProcessor(**kwargs):
  mod = cms.EDProducer('JetMETDQMPostProcessor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
