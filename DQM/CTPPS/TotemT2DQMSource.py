import FWCore.ParameterSet.Config as cms

def TotemT2DQMSource(**kwargs):
  mod = cms.EDProducer('TotemT2DQMSource',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
